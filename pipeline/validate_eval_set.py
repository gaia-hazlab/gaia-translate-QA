#!/usr/bin/env python3
"""
validate_eval_set.py — Validate the v3 eval-set QAs.

Checks
------
- Schema conformance per QA (required fields, enum values, ID pattern).
- All card IDs referenced in expected_output resolve to defined v3 cards.
- Stratification: per-discipline coverage, query-type distribution,
  difficulty distribution against the targets in docs/eval_qa_schema.md.
- Status integrity (no duplicates; status promotion rules).

Usage
-----
    python pipeline/validate_eval_set.py                 # validate seed set + write eval_dataset_v3.json
    python pipeline/validate_eval_set.py --json          # JSON output
    python pipeline/validate_eval_set.py --strict        # fail on stratification warnings

Exit codes
----------
    0 — all checks passed
    1 — errors detected (or warnings under --strict)
    2 — usage error

Stdlib only (plus PyYAML for the co-retrieval index lookup).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field, asdict
from itertools import combinations
from pathlib import Path
from typing import List, Set, Dict, Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ============================================================================
# CONSTANTS
# ============================================================================

VALID_DISCIPLINES = {
    "hydrology", "seismology", "geotechnical_engineering", "geomorphology",
    "atmospheric_sciences", "ecology", "agricultural_sciences",
    "near_surface_geophysics", "cross_cutting",
}

VALID_QUERY_TYPES = {
    "paper-interpretation", "integration", "vocabulary-disambiguation",
    "refusal-test", "joint-observation",
}

VALID_DOCUMENT_TYPES = {"pdf", "url", "html_text", "none"}

VALID_REFUSAL_TYPES = {
    "forced-analogy", "vocabulary-collision", "different-regime",
    "missing-causality", "outside-grounded-knowledge",
    "fabrication-prevention", "surface-power-law-collision",
}

VALID_STATUSES = {"draft", "reviewed", "approved", "deprecated"}

# v3.1 new enums
VALID_TRANSLATION_TASK_TYPES = {
    "concept-mapping", "method-translation", "sensor-data-equivalence",
    "data-availability-assessment", "terminology-bridging",
    "limitation-translation", "parameter-threshold-equivalence",
}

VALID_TIERS = {"bronze", "silver", "gold"}

VALID_FAILURE_MODES = {
    "hallucinated-analogue", "concept-confusion", "domain-ignorance",
    "implausible-calibration", "missing-constraint", "false-equivalence",
    "terminology-failure",
}

ID_PATTERN = re.compile(r"^(QA-EVAL|QA-CAL|QA-HELDOUT)-\d{3,}$")
CARD_ID_PATTERN = re.compile(r"^(CC|MC|PD|TC)-[A-Za-z0-9_-]+$")

# Stratification targets (from docs/eval_qa_schema.md, Section 4)
TARGETS_FULL_SET = {
    "total": 300,
    "by_discipline_single": {
        "hydrology": 25, "seismology": 25, "geotechnical_engineering": 25,
        "geomorphology": 25, "atmospheric_sciences": 25, "ecology": 25,
        "agricultural_sciences": 25, "near_surface_geophysics": 25,
    },
    "by_cross_discipline_span": {2: 70, 3: 20, 4: 10},
    "by_query_type": {
        "paper-interpretation": 120,
        "integration": 75,
        "vocabulary-disambiguation": 45,
        "refusal-test": 30,
        "joint-observation": 30,
    },
    "by_difficulty": {1: 30, 2: 60, 3: 120, 4: 60, 5: 30},
    # v3.1 dimension targets (mirror pipeline/generate_eval_dataset.py TARGETS and
    # docs/eval_dimensions_framework.md §2-4).
    "by_tier": {"bronze": 150, "silver": 120, "gold": 30},
    "by_translation_task_type": {
        "concept-mapping": 80, "method-translation": 70,
        "sensor-data-equivalence": 50, "data-availability-assessment": 30,
        "terminology-bridging": 50, "limitation-translation": 50,
        "parameter-threshold-equivalence": 35,
    },
    "by_failure_mode_tested": {
        "missing-constraint": 60, "domain-ignorance": 55,
        "concept-confusion": 50, "false-equivalence": 50,
        "implausible-calibration": 40, "terminology-failure": 40,
        "hallucinated-analogue": 30,
    },
    "by_compound_coupling": {
        "hydrology-seismology": 30,
        "geotechnical_engineering-seismology": 25,
        "geomorphology-seismology": 20,
        "atmospheric_sciences-hydrology": 25,
        "ecology-hydrology": 20,
        "agricultural_sciences-hydrology": 20,
        "geomorphology-hydrology": 25,
        "atmospheric_sciences-geomorphology": 15,
        "geotechnical_engineering-hydrology": 20,
    },
    "single_discipline_target": 90,
    "tolerance_per_discipline": 5,
    "tolerance_per_query_type_pct": 0.05,
    "tolerance_per_difficulty": 15,
    "tolerance_per_tier": 15,
    "tolerance_per_task_type": 10,
    "tolerance_per_failure_mode": 10,
    "tolerance_per_coupling": 5,
}


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class ValidationIssue:
    severity: str       # 'error' or 'warning'
    rule: str
    qa_id: str
    message: str

    def to_dict(self):
        return asdict(self)


@dataclass
class ValidationReport:
    issues: List[ValidationIssue] = field(default_factory=list)
    qa_count: int = 0
    stats: Dict = field(default_factory=dict)

    def add(self, severity: str, rule: str, qa_id: str, message: str):
        self.issues.append(ValidationIssue(severity, rule, qa_id, message))

    @property
    def errors(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == "warning"]


# ============================================================================
# HELPERS
# ============================================================================

def collect_defined_card_ids(corpus_root: Path) -> Set[str]:
    """Walk skills/long_form/*/concept_cards.md (etc) for `## CC-/MC-/PD-/TC-` headers."""
    card_id_pattern = re.compile(r"^##\s+((?:CC|MC|PD|TC)-[A-Za-z0-9_-]+?):", re.MULTILINE)
    ids: Set[str] = set()
    long_form = corpus_root / "skills" / "long_form"
    for disc_dir in long_form.iterdir():
        if not disc_dir.is_dir() or disc_dir.name == "v2_legacy":
            continue
        for f in disc_dir.glob("*.md"):
            text = f.read_text(encoding="utf-8")
            for m in card_id_pattern.finditer(text):
                ids.add(m.group(1))
    return ids


# ============================================================================
# PER-QA SCHEMA VALIDATION
# ============================================================================

def validate_qa(qa: Dict, defined_card_ids: Set[str], report: ValidationReport) -> None:
    """Validate a single QA dict against the v3 schema."""
    qa_id = qa.get("id", "<no-id>")

    # ID format
    if not ID_PATTERN.match(qa_id):
        report.add("error", "id-format", qa_id,
                   f"id '{qa_id}' does not match QA-EVAL-### / QA-CAL-### / QA-HELDOUT-### pattern.")

    # schema_version
    if qa.get("schema_version") != "v3":
        report.add("error", "schema-version", qa_id,
                   f"schema_version must be 'v3', got {qa.get('schema_version')!r}.")

    # primary_disciplines
    pdsc = qa.get("primary_disciplines", [])
    if not isinstance(pdsc, list) or not pdsc:
        report.add("error", "primary-disciplines", qa_id,
                   "primary_disciplines must be a non-empty list.")
    else:
        if not 1 <= len(pdsc) <= 4:
            report.add("error", "primary-disciplines", qa_id,
                       f"primary_disciplines must have 1-4 entries; got {len(pdsc)}.")
        for d in pdsc:
            if d not in VALID_DISCIPLINES:
                report.add("error", "primary-disciplines", qa_id,
                           f"primary_disciplines contains unknown discipline '{d}'.")

    # query_type
    qt = qa.get("query_type")
    if qt not in VALID_QUERY_TYPES:
        report.add("error", "query-type", qa_id,
                   f"query_type '{qt}' must be one of {VALID_QUERY_TYPES}.")

    # translation_task_types (v3.1)
    ttt = qa.get("translation_task_types", [])
    if not isinstance(ttt, list) or not ttt:
        report.add("error", "translation-task-types", qa_id,
                   "translation_task_types must be a non-empty list (1-3 entries).")
    elif not 1 <= len(ttt) <= 3:
        report.add("error", "translation-task-types", qa_id,
                   f"translation_task_types must have 1-3 entries; got {len(ttt)}.")
    else:
        for t in ttt:
            if t not in VALID_TRANSLATION_TASK_TYPES:
                report.add("error", "translation-task-types", qa_id,
                           f"unknown translation task type '{t}'; must be one of {sorted(VALID_TRANSLATION_TASK_TYPES)}.")

    # tier (v3.1)
    tier = qa.get("tier")
    if tier not in VALID_TIERS:
        report.add("error", "tier", qa_id,
                   f"tier '{tier}' must be one of {VALID_TIERS}.")

    # compound_coupling (v3.1) — list of "disc-disc" pairs, alphabetized within each pair.
    # For an N-discipline QA, the list must contain exactly C(N,2) canonical pairs
    # covering every pair of primary_disciplines (empty for single-discipline QAs).
    cc = qa.get("compound_coupling", [])
    parsed_pairs: Set[tuple] = set()
    coupling_valid = True
    if not isinstance(cc, list):
        report.add("error", "compound-coupling", qa_id,
                   "compound_coupling must be a list (empty for single-disc QAs).")
        coupling_valid = False
    else:
        for pair in cc:
            if not isinstance(pair, str) or "-" not in pair:
                report.add("error", "compound-coupling", qa_id,
                           f"compound_coupling entry '{pair}' must be 'discipline-discipline' format.")
                coupling_valid = False
                continue
            # Split into the longest left-side discipline name that exists in VALID_DISCIPLINES,
            # because discipline names themselves may contain underscores (not hyphens), so
            # splitting on the first hyphen correctly separates the two discipline names.
            parts = pair.split("-", 1)
            if len(parts) != 2:
                report.add("error", "compound-coupling", qa_id,
                           f"compound_coupling entry '{pair}' has unexpected format.")
                coupling_valid = False
                continue
            d1, d2 = parts[0], parts[1]
            if d1 not in VALID_DISCIPLINES or d2 not in VALID_DISCIPLINES:
                report.add("error", "compound-coupling", qa_id,
                           f"compound_coupling '{pair}' references unknown discipline(s).")
                coupling_valid = False
                continue
            if d1 >= d2:
                report.add("error", "compound-coupling-order", qa_id,
                           f"compound_coupling '{pair}' is not alphabetized within pair "
                           f"(canonical: '{min(d1,d2)}-{max(d1,d2)}').")
                coupling_valid = False
                continue
            parsed_pairs.add((d1, d2))

    # Coverage check: parsed pairs must equal the C(N,2) pairs of primary_disciplines.
    if coupling_valid and isinstance(pdsc, list) and pdsc:
        valid_disc_in_pdsc = [d for d in pdsc if d in VALID_DISCIPLINES]
        expected_pairs = {
            (a, b) for a, b in (
                tuple(sorted([d1, d2])) for d1, d2 in combinations(valid_disc_in_pdsc, 2)
            )
        }
        if expected_pairs != parsed_pairs:
            missing = expected_pairs - parsed_pairs
            extra = parsed_pairs - expected_pairs
            details = []
            if missing:
                details.append("missing " + ", ".join(f"'{a}-{b}'" for a, b in sorted(missing)))
            if extra:
                details.append("unexpected " + ", ".join(f"'{a}-{b}'" for a, b in sorted(extra)))
            report.add("error", "compound-coupling-coverage", qa_id,
                       f"compound_coupling must contain exactly the C(N,2) canonical pairs of "
                       f"primary_disciplines ({len(expected_pairs)} for {len(valid_disc_in_pdsc)} "
                       f"disciplines); " + "; ".join(details) + ".")

    # difficulty
    diff = qa.get("difficulty")
    if not isinstance(diff, int) or not 1 <= diff <= 5:
        report.add("error", "difficulty", qa_id,
                   f"difficulty must be int 1-5; got {diff!r}.")

    # prompt
    prompt = qa.get("prompt", "")
    if not isinstance(prompt, str) or len(prompt.strip()) < 10:
        report.add("error", "prompt", qa_id,
                   "prompt must be a string of at least 10 characters.")

    # input_document
    doc = qa.get("input_document", {})
    if not isinstance(doc, dict):
        report.add("error", "input-document", qa_id, "input_document must be a dict.")
    else:
        dt = doc.get("type")
        if dt not in VALID_DOCUMENT_TYPES:
            report.add("error", "input-document", qa_id,
                       f"input_document.type '{dt}' must be one of {VALID_DOCUMENT_TYPES}.")

    # expected_output
    exp = qa.get("expected_output", {})
    if not isinstance(exp, dict):
        report.add("error", "expected-output", qa_id, "expected_output must be a dict.")
    else:
        # Card-ID references resolve
        for fld in ("concept_matches", "method_matches", "phenomenon_matches", "translation_matches"):
            for cid in exp.get(fld, []):
                if not isinstance(cid, str):
                    report.add("error", "expected-output", qa_id,
                               f"{fld} contains non-string: {cid!r}.")
                    continue
                if not CARD_ID_PATTERN.match(cid):
                    report.add("error", "card-id-format", qa_id,
                               f"{fld}: '{cid}' is not a valid card ID format.")
                elif cid not in defined_card_ids:
                    report.add("error", "card-id-unresolved", qa_id,
                               f"{fld}: '{cid}' is not defined in the v3 corpus.")

        # Refusals enum values
        for r in exp.get("refusals_or_caveats_expected", []):
            if r not in VALID_REFUSAL_TYPES:
                report.add("error", "refusal-type", qa_id,
                           f"refusals_or_caveats_expected '{r}' must be one of {VALID_REFUSAL_TYPES}.")

        # failure_modes_tested (v3.1) — required, 1-4 entries
        fm = exp.get("failure_modes_tested", [])
        if not isinstance(fm, list) or not fm:
            report.add("error", "failure-modes", qa_id,
                       "expected_output.failure_modes_tested must be a non-empty list (1-4 entries).")
        else:
            if len(fm) > 4:
                report.add("error", "failure-modes-count", qa_id,
                           f"failure_modes_tested has {len(fm)} entries; must be 1-4.")
            for f in fm:
                if f not in VALID_FAILURE_MODES:
                    report.add("error", "failure-modes", qa_id,
                               f"unknown failure mode '{f}'; must be one of {sorted(VALID_FAILURE_MODES)}.")

        # Themes: 3-6 specific themes recommended
        themes = exp.get("user_specific_response_themes", [])
        if not isinstance(themes, list):
            report.add("error", "themes", qa_id,
                       "user_specific_response_themes must be a list.")
        elif len(themes) < 2:
            report.add("warning", "themes-count", qa_id,
                       f"only {len(themes)} response themes; recommend 3-6.")
        elif len(themes) > 8:
            report.add("warning", "themes-count", qa_id,
                       f"{len(themes)} response themes; consider trimming to 3-6.")

        # Refusal-test QAs must have refusals_expected
        if qt == "refusal-test" and not exp.get("refusals_or_caveats_expected"):
            report.add("error", "refusal-test-mismatch", qa_id,
                       "query_type=refusal-test but refusals_or_caveats_expected is empty.")

        # Vocabulary-disambiguation QAs must have vocab_collisions
        if qt == "vocabulary-disambiguation" and not exp.get("vocabulary_collisions_flagged"):
            report.add("warning", "vocab-disambig-mismatch", qa_id,
                       "query_type=vocabulary-disambiguation but vocabulary_collisions_flagged is empty.")

    # status
    status = qa.get("status")
    if status not in VALID_STATUSES:
        report.add("error", "status", qa_id,
                   f"status '{status}' must be one of {VALID_STATUSES}.")
    elif status == "approved":
        qn = qa.get("quality_notes", {})
        if not qn.get("last_reviewed_by"):
            report.add("warning", "approval-review", qa_id,
                       "status=approved but quality_notes.last_reviewed_by is empty.")

    # quality_notes
    qn = qa.get("quality_notes", {})
    if not isinstance(qn, dict) or not qn.get("author"):
        report.add("error", "quality-notes", qa_id,
                   "quality_notes.author is required.")


# ============================================================================
# CROSS-QA INTEGRITY
# ============================================================================

def check_duplicates(qas: List[Dict], report: ValidationReport) -> None:
    ids = [qa.get("id", "") for qa in qas]
    seen: Counter = Counter(ids)
    for qa_id, count in seen.items():
        if count > 1:
            report.add("error", "duplicate-id", qa_id, f"id appears {count} times.")


# ============================================================================
# STRATIFICATION
# ============================================================================

def compute_stats(qas: List[Dict]) -> Dict:
    by_query_type = Counter(qa["query_type"] for qa in qas)
    by_difficulty = Counter(qa["difficulty"] for qa in qas)
    by_status = Counter(qa["status"] for qa in qas)

    # By primary discipline (each QA counted once per discipline)
    by_discipline = Counter()
    for qa in qas:
        for d in qa["primary_disciplines"]:
            by_discipline[d] += 1

    # Cross-discipline span
    by_span = Counter(len(qa["primary_disciplines"]) for qa in qas)

    # v3.1: tier
    by_tier = Counter(qa.get("tier", "unknown") for qa in qas)

    # v3.1: translation task types (each QA contributes to multiple)
    by_task_type = Counter()
    for qa in qas:
        for t in qa.get("translation_task_types", []):
            by_task_type[t] += 1

    # v3.1: compound coupling (each QA contributes to multiple if multi-coupling)
    by_coupling = Counter()
    for qa in qas:
        for c in qa.get("compound_coupling", []):
            by_coupling[c] += 1
    # Track count of single-discipline QAs (no coupling)
    single_disc_count = sum(1 for qa in qas if not qa.get("compound_coupling"))

    # v3.1: failure modes (each QA contributes to multiple)
    by_failure_mode = Counter()
    for qa in qas:
        for f in qa.get("expected_output", {}).get("failure_modes_tested", []):
            by_failure_mode[f] += 1

    # Note: int keys are preserved here so check_stratification() can look up
    # targets by their native int keys (difficulty, span). json.dump auto-stringifies
    # int dict keys when serializing the canonical JSON.
    return {
        "total": len(qas),
        "by_query_type": dict(by_query_type),
        "by_difficulty": dict(by_difficulty),
        "by_discipline": dict(by_discipline),
        "by_span": dict(by_span),
        "by_status": dict(by_status),
        # v3.1 additions
        "by_tier": dict(by_tier),
        "by_translation_task_type": dict(by_task_type),
        "by_compound_coupling": dict(by_coupling),
        "single_discipline_count": single_disc_count,
        "by_failure_mode_tested": dict(by_failure_mode),
    }


def check_stratification(stats: Dict, full_set: bool, report: ValidationReport) -> None:
    """
    Check stratification against targets. For seed sets (full_set=False), only
    report warnings; for full set (full_set=True), warnings become errors.
    """
    severity = "error" if full_set else "warning"

    if full_set:
        total = stats["total"]
        if abs(total - TARGETS_FULL_SET["total"]) > 20:
            report.add(severity, "stratification-total", "",
                       f"total QAs {total}; target {TARGETS_FULL_SET['total']}.")

    # By discipline (single-disc only; cross-disc tracked separately)
    targets = TARGETS_FULL_SET["by_discipline_single"]
    tolerance = TARGETS_FULL_SET["tolerance_per_discipline"]
    for disc, target in targets.items():
        actual = stats["by_discipline"].get(disc, 0)
        if full_set and abs(actual - target) > tolerance:
            report.add(severity, "stratification-discipline", "",
                       f"{disc}: {actual} QAs; target {target} ± {tolerance}.")

    # By query type
    targets_qt = TARGETS_FULL_SET["by_query_type"]
    if full_set:
        for qt, target in targets_qt.items():
            actual = stats["by_query_type"].get(qt, 0)
            tolerance_qt = int(TARGETS_FULL_SET["total"] * TARGETS_FULL_SET["tolerance_per_query_type_pct"])
            if abs(actual - target) > tolerance_qt:
                report.add(severity, "stratification-query-type", "",
                           f"{qt}: {actual} QAs; target {target} ± {tolerance_qt}.")

    # By difficulty
    targets_diff = TARGETS_FULL_SET["by_difficulty"]
    tolerance_diff = TARGETS_FULL_SET["tolerance_per_difficulty"]
    if full_set:
        for d, target in targets_diff.items():
            actual = stats["by_difficulty"].get(d, 0)
            if abs(actual - target) > tolerance_diff:
                report.add(severity, "stratification-difficulty", "",
                           f"difficulty {d}: {actual} QAs; target {target} ± {tolerance_diff}.")

    # v3.1 stratification: tier, translation task type, failure mode, compound coupling
    if full_set:
        for tier, target in TARGETS_FULL_SET["by_tier"].items():
            actual = stats.get("by_tier", {}).get(tier, 0)
            tol = TARGETS_FULL_SET["tolerance_per_tier"]
            if abs(actual - target) > tol:
                report.add(severity, "stratification-tier", "",
                           f"tier {tier}: {actual} QAs; target {target} ± {tol}.")

        for tt, target in TARGETS_FULL_SET["by_translation_task_type"].items():
            actual = stats.get("by_translation_task_type", {}).get(tt, 0)
            tol = TARGETS_FULL_SET["tolerance_per_task_type"]
            if abs(actual - target) > tol:
                report.add(severity, "stratification-task-type", "",
                           f"task type {tt}: {actual} QAs; target {target} ± {tol}.")

        for fm, target in TARGETS_FULL_SET["by_failure_mode_tested"].items():
            actual = stats.get("by_failure_mode_tested", {}).get(fm, 0)
            tol = TARGETS_FULL_SET["tolerance_per_failure_mode"]
            if abs(actual - target) > tol:
                report.add(severity, "stratification-failure-mode", "",
                           f"failure mode {fm}: {actual} QAs; target {target} ± {tol}.")

        for coupling, target in TARGETS_FULL_SET["by_compound_coupling"].items():
            actual = stats.get("by_compound_coupling", {}).get(coupling, 0)
            tol = TARGETS_FULL_SET["tolerance_per_coupling"]
            if abs(actual - target) > tol:
                report.add(severity, "stratification-coupling", "",
                           f"coupling {coupling}: {actual} QAs; target {target} ± {tol}.")

        single_actual = stats.get("single_discipline_count", 0)
        single_target = TARGETS_FULL_SET["single_discipline_target"]
        if abs(single_actual - single_target) > TARGETS_FULL_SET["tolerance_per_difficulty"]:
            report.add(severity, "stratification-single-discipline", "",
                       f"single-discipline QAs: {single_actual}; target {single_target} ± "
                       f"{TARGETS_FULL_SET['tolerance_per_difficulty']}.")


# ============================================================================
# REPORTING
# ============================================================================

def is_tty() -> bool:
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def color(text: str, code: str) -> str:
    if not is_tty():
        return text
    return f"\033[{code}m{text}\033[0m"


def print_text_report(report: ValidationReport, stats: Dict) -> None:
    if not report.issues:
        print(color("✓", "32") + f"  Eval set validates clean — {report.qa_count} QAs, 0 errors, 0 warnings.")
    else:
        # Group by qa_id
        by_id: Dict[str, List[ValidationIssue]] = {}
        for issue in report.issues:
            by_id.setdefault(issue.qa_id, []).append(issue)
        for qa_id in sorted(by_id):
            label = qa_id or "(set-wide)"
            print(color(label, "36"))
            for issue in by_id[qa_id]:
                sev_color = "31" if issue.severity == "error" else "33"
                sev_label = color(issue.severity.upper().ljust(7), sev_color)
                print(f"  {sev_label} {issue.rule:30s} {issue.message}")

    err = len(report.errors)
    warn = len(report.warnings)
    print()
    print(f"Summary: {report.qa_count} QAs, "
          f"{color(str(err), '31')} errors, {color(str(warn), '33')} warnings.")
    print()
    print("Stats:")
    print(f"  By query type:        {stats['by_query_type']}")
    print(f"  By difficulty:        {stats['by_difficulty']}")
    print(f"  By tier:              {stats.get('by_tier', {})}")
    print(f"  By discipline:        {stats['by_discipline']}")
    print(f"  By disc-span:         {stats['by_span']}")
    print(f"  By status:            {stats['by_status']}")
    print(f"  By task type:         {stats.get('by_translation_task_type', {})}")
    print(f"  Single-disc count:    {stats.get('single_discipline_count', 0)}")
    print(f"  By coupling:          {stats.get('by_compound_coupling', {})}")
    print(f"  By failure mode:      {stats.get('by_failure_mode_tested', {})}")


def print_json_report(report: ValidationReport, stats: Dict) -> None:
    out = {
        "summary": {
            "qa_count": report.qa_count,
            "errors": len(report.errors),
            "warnings": len(report.warnings),
        },
        "stats": stats,
        "issues": [i.to_dict() for i in report.issues],
    }
    print(json.dumps(out, indent=2))


# ============================================================================
# MAIN
# ============================================================================

def load_qas(corpus_root: Path) -> List[Dict]:
    """Load the seed QA set from pipeline/seed_qa_dataset.py."""
    # Use importlib to avoid having pipeline/ on PYTHONPATH
    import importlib.util
    p = corpus_root / "pipeline" / "seed_qa_dataset.py"
    spec = importlib.util.spec_from_file_location("seed_qa_dataset", str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SEED_QAS


def write_canonical_json(qas: List[Dict], stats: Dict, out_path: Path) -> None:
    from datetime import datetime, timezone
    out = {
        "schema_version": "v3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stats": stats,
        "qas": qas,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the v3 eval-set QAs.")
    parser.add_argument(
        "--full-set",
        action="store_true",
        help="Apply full-set stratification targets (~300 QAs). Default is seed-set mode (relaxed).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero if any warnings are present.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output (for CI).",
    )
    parser.add_argument(
        "--write",
        type=Path,
        default=Path("eval_dataset/eval_dataset_v3.json"),
        help="Write the canonical JSON eval set to this path (relative to corpus root). "
             "Pass --no-write to skip.",
    )
    parser.add_argument("--no-write", action="store_true", help="Skip writing the JSON file.")
    parser.add_argument(
        "--corpus-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Root of the gaia-translate-QA repository.",
    )
    args = parser.parse_args(argv)

    corpus_root: Path = args.corpus_root
    if not (corpus_root / "skills" / "long_form").is_dir():
        print(f"ERROR: corpus root '{corpus_root}' missing skills/long_form.", file=sys.stderr)
        return 2

    # Load defined card IDs
    defined_card_ids = collect_defined_card_ids(corpus_root)
    if not defined_card_ids:
        print("WARNING: no card IDs found in corpus.", file=sys.stderr)

    # Load seed QAs
    try:
        qas = load_qas(corpus_root)
    except Exception as e:
        print(f"ERROR loading seed QAs: {e}", file=sys.stderr)
        return 2

    report = ValidationReport()
    report.qa_count = len(qas)

    # Per-QA validation
    for qa in qas:
        validate_qa(qa, defined_card_ids, report)

    # Cross-QA integrity
    check_duplicates(qas, report)

    # Stratification
    stats = compute_stats(qas)
    report.stats = stats
    check_stratification(stats, full_set=args.full_set, report=report)

    # Write canonical JSON if requested
    if not args.no_write:
        write_canonical_json(qas, stats, corpus_root / args.write)

    # Output
    if args.json:
        print_json_report(report, stats)
    else:
        print_text_report(report, stats)

    if report.errors:
        return 1
    if args.strict and report.warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
