#!/usr/bin/env python3
"""
lint_cards.py — Validate the Gaia translator v3 card corpus.

Checks
------
- Word-count caps per card type (concept/method 450, phenomenon 500, translation 550).
- Required sections per card type.
- 'When you see this in a paper' hook on every concept and method card.
- At least one Cross-discipline equivalent on every concept and method card.
- DOI coverage on anchor citations (with heuristic allow-list for books,
  pre-1970 papers, FAO/USDA/USGS technical reports, proceedings).
- All CC-/MC-/PD-/TC- references in card bodies resolve to defined card IDs.

Usage
-----
    python pipeline/lint_cards.py                         # lint full corpus
    python pipeline/lint_cards.py --card path/to/card.md  # lint one file
    python pipeline/lint_cards.py --strict                # fail on warnings too
    python pipeline/lint_cards.py --json                  # JSON output for CI

Exit codes
----------
    0 — all checks passed (no errors; warnings tolerated unless --strict)
    1 — errors detected (or warnings under --strict)
    2 — usage error / corpus not found

Dependencies
------------
    Standard library only. PyYAML for parsing co_retrieval_index.yaml.

Author: Gaia translator project (Denolle Group, UW ESS).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List, Dict, Set, Optional, Iterable

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ============================================================================
# CONSTANTS
# ============================================================================

# Hard caps per card-type prefix. Targets are softer; warnings only.
WORD_CAPS = {"CC-": 450, "MC-": 450, "PD-": 500, "TC-": 550}
WORD_TARGETS = {"CC-": 280, "MC-": 330, "PD-": 400, "TC-": 450}

# Required sections per card type. Each entry is a LIST of acceptable variant
# names for one required section: the linter accepts ANY of the variants as
# satisfying that requirement. Matching is case-insensitive substring against
# the (parenthetical-stripped) section name found in the card body.
REQUIRED_SECTIONS = {
    "CC": [
        ["Quantity"],
        ["Defining relation", "Defining relations", "Defining structure"],
        ["Typical range", "Typical ranges", "Typical relations"],
        ["Cross-discipline equivalent", "Cross-discipline equivalents"],
        ["When you see this in a paper"],
        ["Anchor citation", "Anchor citations"],
        ["Related card", "Related cards"],
    ],
    "MC": [
        ["What it is"],
        ["What you can retrieve"],
        ["Failure mode", "Failure modes"],
        ["Cross-discipline use", "Cross-discipline uses"],
        ["When you see this in a paper"],
        ["Anchor citation", "Anchor citations"],
        ["Related card", "Related cards"],
    ],
    "PD": [
        ["Setting"],
        ["Mechanism"],
        ["Observables per discipline"],
        ["Open questions"],
        ["Anchor paper", "Anchor papers", "Anchor citation", "Anchor citations"],
        ["Related card", "Related cards"],
    ],
    "TC": [
        ["Shared structure"],
        ["Discipline-specific manifestation", "Discipline-specific manifestations"],
        ["When the analogy holds"],
        ["When the analogy breaks"],
        ["Translator agent move"],
        ["Anchor citation", "Anchor citations"],
        ["Related card", "Related cards"],
    ],
}

# Sections that, on a concept or method card, must additionally be non-trivially
# populated (at least 1 bullet item). For cards where the section name uses a
# variant (e.g., "Cross-discipline equivalents"), the substring match is enough.
NONTRIVIAL_SECTIONS = {
    "CC": ["Cross-discipline equivalent"],
    "MC": ["Cross-discipline use"],
}

# ============================================================================
# PATTERNS
# ============================================================================

# DOI as it appears in cards: "doi:10.xxxx/yyyy"
DOI_PATTERN = re.compile(r"\bdoi:10\.\d{4,9}/\S+", re.IGNORECASE)

# Card-ID references in body text: "CC-foo-bar", "MC-foo", "PD-foo", "TC-NN"
CARD_REF_PATTERN = re.compile(r"\b((?:CC|MC|PD|TC)-[A-Za-z0-9_-]+?)(?=[`\s,.;:)\]]|$)")

# Card header: "## CC-foo-bar: Title"
CARD_HEADER_PATTERN = re.compile(
    r"^##\s+((?:CC|MC|PD|TC)-[A-Za-z0-9_-]+?):\s*(.*?)$",
    re.MULTILINE,
)

# Section header inside a card body: "**Name**:" or "**Name (suffix)**:" or
# "**Name** (suffix):" — must be at the start of a line so we don't match
# bullet-item bold tags like "- **Hydrology**: ..." (which are SUB-headers
# inside the Cross-discipline-equivalents section, not section headers).
SECTION_PATTERN = re.compile(
    r"^\*\*([^*\n]+?)\*\*(?:\s*\([^)]*\))?\s*[:.](?:\s|$)",
    re.MULTILINE,
)

# Bullet line inside a section.
BULLET_PATTERN = re.compile(r"^[-*]\s+", re.MULTILINE)

# Year inside a citation, used for the pre-1970 heuristic.
YEAR_PATTERN = re.compile(r"\((\d{4})\)")

# Frontmatter at top of card files.
FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


# ============================================================================
# DOI-LESS ALLOW-LIST (heuristic)
# ============================================================================

# An anchor citation lacking a DOI is acceptable if it matches any of these
# patterns. Otherwise it generates a warning (not error).
DOI_LESS_PATTERNS = [
    # Books (publishers; italicized title in *Asterisks*; allows optional
    # parenthetical annotations like "(2nd ed.)" between title and publisher,
    # and optional "In *Anothertitle*..." chapter-in-book wrappers).
    re.compile(
        r"\*[^*]+\*"                       # italicized title
        r"(?:\s*\([^)]*\))*"               # zero+ "(2nd ed.)"-style annotations
        r"[.,;]?\s*"                       # optional punctuation + whitespace
        r"(?:\([^)]*\)\s*[.,;]?\s*)*"      # more annotations like "(ed.)"
        r"(?:Wiley(?:-Blackwell)?|Springer(?:\s|\.)|Academic Press|"
        r"Cambridge University Press|Princeton University Press|"
        r"Prentice Hall|Elsevier|McGraw-Hill|CRC Press|Blackwell|"
        r"Oxford University Press|Routledge|"
        r"National Academies Press|Allen & Unwin|"
        r"AGU Water Resources Monograph|SIAM|"
        r"Edward Arnold|Victor Dalmont|Franz Deuticke|"
        r"University Science Books|Spon Press|Blackie|"
        r"U\.S\. Geological Survey)",
        re.IGNORECASE,
    ),
    # Chapter-in-book pattern: "In *Book Title* ..."
    re.compile(
        r"\bIn\s+\*[^*]+\*",
        re.IGNORECASE,
    ),
    # IPCC reports
    re.compile(r"IPCC\s+(?:WG\d\s+)?AR\d", re.IGNORECASE),
    re.compile(r"Climate Change \d{4}:", re.IGNORECASE),
    # PhD dissertations
    re.compile(r"Ph\.?\s*D\.?\s*[Dd]issertation", re.IGNORECASE),
    re.compile(r"[Dd]octoral\s+(?:thesis|dissertation)", re.IGNORECASE),
    # EU / international project deliverables
    re.compile(r"European Commission project", re.IGNORECASE),
    re.compile(r"deliverable\s+D\d", re.IGNORECASE),
    # Pre-1990 ASCE journals (ASCE didn't issue DOIs until ~1990s).
    # Pattern matches a citation with year < 1990 in an ASCE journal.
    re.compile(
        r"\(19[0-8]\d\)\..*?\*"
        r"(?:J\.\s*Soil Mech(?:anics)?\.?\s*(?:and|&)?\s*Found(?:ations)?\.?\s*Div(?:ision)?\.?|"
        r"J\.\s*Geotech\.\s*Eng(?:ineering)?\.?\s*Div(?:ision)?\.?|"
        r"J\.\s*Hydraulic\s*Div(?:ision)?\.?)\s*\(ASCE\)",
        re.IGNORECASE,
    ),
    # Pre-1970 papers (year extraction handled separately)
    # FAO, USDA, EERI, USGS technical reports
    re.compile(r"FAO Irrigation and Drainage Paper \d+", re.IGNORECASE),
    re.compile(r"FAO\b.*?Paper\b", re.IGNORECASE),
    re.compile(r"EERI Monograph", re.IGNORECASE),
    re.compile(r"\bMNO-\d+\b"),
    re.compile(r"UCD/CGM-\d+"),
    re.compile(r"USDA Agriculture Handbook \d+"),
    re.compile(r"USDA Forest Service GTR"),
    re.compile(r"USGS Open-File Report"),
    re.compile(r"USGS Techniques (?:of Water-Resources Investigations|and Methods)"),
    re.compile(r"NCAR Tech\.?\s*Note"),
    re.compile(r"NCAR/TN-\d+"),
    # Proceedings and symposia (no DOI typically)
    re.compile(r"Proceedings of (?:the )?\d+(?:st|nd|rd|th)?\s*(?:ICSMFE|IAHR|Meeting)",
               re.IGNORECASE),
    re.compile(r"Proc\.\s*\d+(?:st|nd|rd|th)?\s*ICSMFE", re.IGNORECASE),
    re.compile(r"Symposia of the Society for Experimental Biology", re.IGNORECASE),
    re.compile(r"Mitteilungen der", re.IGNORECASE),
    # USGS Professional Papers without numeric DOI in the citation but typically
    # have DOIs at pubs.usgs.gov; the heuristic flags the URL form too.
    re.compile(r"USGS Professional Paper", re.IGNORECASE),
    re.compile(r"pubs\.usgs\.gov", re.IGNORECASE),
    # Software manuals, dataset documentation
    re.compile(r"User['']?s? [Mm]anual", re.IGNORECASE),
    re.compile(r"Aarhus Workbench user guide", re.IGNORECASE),
    # Specific old refs known DOI-less
    re.compile(r"Gutenberg,\s*B\.,?\s*&?\s*Richter,\s*C\.\s*F\.\s*\(1944\)"),
    re.compile(r"Aki,\s*K\.\s*\(1965\)\."),
    re.compile(r"Shields,\s*A\.\s*\(1936\)"),
    re.compile(r"Meyer-Peter,\s*E\.,?\s*&?\s*Müller,\s*R\.\s*\(1948\)"),
    re.compile(r"Skempton,\s*A\.\s*W\.\s*\(1948\)"),
    re.compile(r"Casagrande,\s*A\.,?\s*&?\s*Fadum,\s*R\.\s*E\.\s*\(1940\)"),
    re.compile(r"Monteith,\s*J\.\s*L\.\s*\(1965\)\."),
    re.compile(r"Idriss,\s*I\.\s*M\.,?\s*&?\s*Sun,\s*J\.\s*I\.\s*\(1992\)"),
    re.compile(r"Hashash,?\s*Y\.\s*M\.\s*A\.,?\s*et al\.\s*\(2020\)\."),
    re.compile(r"Wischmeier,\s*W\.\s*H\.,?\s*&?\s*Smith,\s*D\.\s*D\.\s*\(1978\)"),
    re.compile(r"Helley,\s*E\.\s*J\.,?\s*&?\s*Smith,\s*W\.\s*\(1971\)"),
    re.compile(r"Soil Survey Staff\.\s*\(\d{4}\)"),
    re.compile(r"Schaefer,\s*G\.\s*L\..*?SCAN\)"),
    re.compile(r"Lindeman,\s*R\.\s*L\.\s*\(1942\)"),
    re.compile(r"MacArthur,\s*R\.\s*H\.,?\s*&?\s*Wilson,\s*E\.\s*O\.\s*\(1967\)"),
    re.compile(r"Sloat,\s*L\."),  # has DOI but format may not detect
    re.compile(r"Reichle.*?DART"),  # not strict; DART is the data assimilation toolkit
    re.compile(r"Nakamura,\s*Y\.\s*\(1989\)"),
    re.compile(r"Schaap,\s*M\.\s*G\..*ROSETTA"),
    re.compile(r"Bishop,\s*A\.\s*W\.\s*\(1959\)\."),
    re.compile(r"Idriss,\s*I\.\s*M\.,?\s*&?\s*Boulanger,\s*R\.\s*W\.\s*\(2008\)"),
    re.compile(r"Boulanger,\s*R\.\s*W\.,?\s*&?\s*Idriss,\s*I\.\s*M\.\s*\(2014\)"),
    re.compile(r"Allen,?\s*R\.\s*G\.,?\s*Pereira,\s*L\.\s*S\..*?FAO Irrigation"),
    re.compile(r"Allen,?\s*R\.\s*G\.,?\s*Walter"),  # ASCE Standardized
]


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class LintIssue:
    severity: str            # 'error' | 'warning'
    rule: str                # rule name
    file: str                # file path relative to repo root
    card_id: str             # offending card ID, or '' for file-level
    message: str             # human-readable message
    line: Optional[int] = None  # optional line number for editor jumps

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class LintReport:
    issues: List[LintIssue] = field(default_factory=list)
    cards_linted: int = 0
    files_linted: int = 0

    def add(self, severity: str, rule: str, file: str, card_id: str,
            message: str, line: Optional[int] = None) -> None:
        self.issues.append(LintIssue(severity, rule, file, card_id, message, line))

    @property
    def errors(self) -> List[LintIssue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> List[LintIssue]:
        return [i for i in self.issues if i.severity == "warning"]


# ============================================================================
# PARSING
# ============================================================================

def split_cards(text: str) -> List[Dict]:
    """
    Split a card file's body into individual card records.

    Returns a list of dicts with keys: card_id, title, body.
    """
    # Strip frontmatter.
    body = FRONTMATTER_PATTERN.sub("", text, count=1)

    cards = []
    matches = list(CARD_HEADER_PATTERN.finditer(body))
    for i, m in enumerate(matches):
        card_id = m.group(1)
        title = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        card_body = body[start:end].strip()
        # Trim trailing '---' separator if present
        card_body = re.sub(r"\n+---\s*$", "", card_body).strip()
        cards.append({
            "card_id": card_id,
            "title": title,
            "body": card_body,
        })
    return cards


def find_sections(card_body: str) -> Dict[str, str]:
    """
    Locate the bold-section markers in a card body and return a dict mapping
    the section name (without parenthetical suffix) to the section text up to
    the next section marker.
    """
    sections: Dict[str, str] = {}
    matches = list(SECTION_PATTERN.finditer(card_body))
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        # Strip parenthetical suffix: "Mechanism (4-step chain)" → "Mechanism"
        clean_name = re.sub(r"\s*\(.*?\)\s*$", "", name).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(card_body)
        section_text = card_body[start:end].strip()
        sections[clean_name] = section_text
    return sections


def count_words(text: str) -> int:
    """Wordcount that matches the verification script we've been running."""
    return len(text.split())


def extract_card_refs(text: str) -> Set[str]:
    """Find all CC-/MC-/PD-/TC- references in text."""
    refs = set()
    for m in CARD_REF_PATTERN.finditer(text):
        ref = m.group(1).rstrip("-_.")
        refs.add(ref)
    return refs


# ============================================================================
# CHECKS
# ============================================================================

def check_word_count(card: Dict, file_rel: str, report: LintReport) -> None:
    """Word count vs. hard cap."""
    cid = card["card_id"]
    prefix = cid[:3]
    cap = WORD_CAPS.get(prefix, 999)
    target = WORD_TARGETS.get(prefix, 999)
    wc = count_words(card["body"])
    if wc > cap:
        report.add("error", "word-count-cap", file_rel, cid,
                   f"Body is {wc} words; hard cap for {prefix.rstrip('-')} cards is {cap}.")
    elif wc > target * 1.5:
        # Soft warning: more than 50% over target
        report.add("warning", "word-count-target", file_rel, cid,
                   f"Body is {wc} words; target is ~{target}.  Consider trimming.")


def check_required_sections(card: Dict, file_rel: str, report: LintReport) -> None:
    """
    Each card type must contain all its required sections.

    Each requirement is a list of acceptable variant names; the linter accepts
    ANY variant as satisfying the requirement.
    """
    cid = card["card_id"]
    prefix = cid[:2]   # "CC", "MC", "PD", "TC"
    required_groups = REQUIRED_SECTIONS.get(prefix, [])
    sections = find_sections(card["body"])
    section_keys_lower = [k.lower() for k in sections.keys()]

    for variants in required_groups:
        found = False
        for variant in variants:
            v = variant.lower()
            if any(k.startswith(v) or v in k for k in section_keys_lower):
                found = True
                break
        if not found:
            # Report using the canonical (first) variant name
            canonical = variants[0]
            report.add("error", "missing-required-section", file_rel, cid,
                       f"Required section '**{canonical}**' not found "
                       f"(accepted variants: {', '.join(variants)}).")


def check_nontrivial_sections(card: Dict, file_rel: str, report: LintReport) -> None:
    """Some sections must have non-trivial content (≥ 1 bullet item)."""
    cid = card["card_id"]
    prefix = cid[:2]
    must_be_nontrivial = NONTRIVIAL_SECTIONS.get(prefix, [])
    sections = find_sections(card["body"])

    for req in must_be_nontrivial:
        section_text = None
        for k, v in sections.items():
            if k.lower().startswith(req.lower()):
                section_text = v
                break
        if section_text is None:
            continue   # missing-section will catch this elsewhere
        bullet_count = len(BULLET_PATTERN.findall(section_text))
        if bullet_count == 0:
            report.add("error", "empty-cross-discipline", file_rel, cid,
                       f"'**{req}s**' section has no bullet items "
                       "(at least one cross-discipline link required).")


def check_doi_coverage(card: Dict, file_rel: str, report: LintReport) -> None:
    """
    Every anchor citation should have a DOI, unless it matches a DOI-less
    heuristic (book, pre-1970 paper, FAO/USDA/USGS report, proceedings).
    """
    cid = card["card_id"]
    sections = find_sections(card["body"])

    # Find the anchor-citations section (or "Anchor papers" for PD).
    anchor_text = None
    for k, v in sections.items():
        if "anchor" in k.lower():
            anchor_text = v
            break
    if anchor_text is None:
        return  # required-sections check handles absence

    # Split into individual citations (one per bullet typically).
    citation_lines = [
        line.strip().lstrip("-* ").strip()
        for line in anchor_text.splitlines()
        if line.strip().startswith(("-", "*")) and len(line.strip()) > 5
    ]

    if not citation_lines:
        report.add("warning", "no-anchor-citations", file_rel, cid,
                   "Anchor-citations section appears empty (no bullet items found).")
        return

    for cite in citation_lines:
        has_doi = bool(DOI_PATTERN.search(cite))
        if has_doi:
            continue
        # No DOI: check allow-list
        is_allowed = False
        for pat in DOI_LESS_PATTERNS:
            if pat.search(cite):
                is_allowed = True
                break
        # Pre-1970 papers
        if not is_allowed:
            ym = YEAR_PATTERN.search(cite)
            if ym and int(ym.group(1)) < 1970:
                is_allowed = True
        if not is_allowed:
            # Truncate citation for readability
            short = cite if len(cite) < 100 else cite[:97] + "..."
            report.add("warning", "missing-doi", file_rel, cid,
                       f"No DOI on anchor citation: '{short}'")


def check_when_you_see_hook(card: Dict, file_rel: str, report: LintReport) -> None:
    """Concept and method cards must include the 'When you see this in a paper' hook."""
    cid = card["card_id"]
    if not cid.startswith(("CC-", "MC-")):
        return
    sections = find_sections(card["body"])
    found = any("when you see this in a paper" in k.lower() for k in sections.keys())
    if not found:
        report.add("error", "missing-when-you-see-hook", file_rel, cid,
                   "Missing '**When you see this in a paper**' hook.")


def check_card_id_matches_file_discipline(
    card: Dict, file_rel: str, file_discipline: Optional[str],
    report: LintReport
) -> None:
    """
    Optional sanity check: a CC-seismo-* card should live in seismology/.
    Skip translation cards (TC) — they can live in any discipline's file.
    """
    cid = card["card_id"]
    if cid.startswith("TC-") or file_discipline is None:
        return
    # CC-, MC-, PD- have a discipline prefix in the ID format CC-<disc>-rest.
    # Some PDs don't (PD-<short> only). Normalize for comparison.
    parts = cid.split("-", 2)
    if len(parts) < 2:
        return
    disc_token = parts[1]
    # Mapping: seismo→seismology, hydro→hydrology, geotech→geotechnical_engineering, etc.
    disc_aliases = {
        "seismo": "seismology",
        "hydro": "hydrology",
        "geotech": "geotechnical_engineering",
        "geomorph": "geomorphology",
        "atm": "atmospheric_sciences",
        "eco": "ecology",
        "ag": "agricultural_sciences",
        "nsg": "near_surface_geophysics",
    }
    expected = disc_aliases.get(disc_token)
    if expected and expected != file_discipline:
        # PD-<short> form has no discipline prefix; skip
        if not cid.startswith("PD-"):
            report.add("warning", "discipline-mismatch", file_rel, cid,
                       f"Card ID suggests discipline '{expected}' but file is in '{file_discipline}'.")


def check_cross_references(
    corpus_root: Path, defined_ids: Set[str],
    forward_pending: Set[str], report: LintReport
) -> None:
    """File-wide: every CC-/MC-/PD-/TC- reference in any card body resolves."""
    for f in iter_card_files(corpus_root):
        rel = str(f.relative_to(corpus_root.parent))
        text = f.read_text(encoding="utf-8")
        for card in split_cards(text):
            cid = card["card_id"]
            refs = extract_card_refs(card["body"])
            for ref in refs:
                if ref == cid:
                    continue
                if ref in defined_ids or ref in forward_pending:
                    continue
                report.add("error", "unresolved-card-ref", rel, cid,
                           f"References {ref}, which is not defined in the corpus.")


# ============================================================================
# FILE / CORPUS ITERATION
# ============================================================================

def iter_card_files(corpus_root: Path) -> Iterable[Path]:
    """Yield each card file in the v3 corpus (excludes v2_legacy)."""
    long_form = corpus_root / "skills" / "long_form"
    for disc_dir in sorted(long_form.iterdir()):
        if not disc_dir.is_dir() or disc_dir.name == "v2_legacy":
            continue
        for fname in ("concept_cards.md", "method_cards.md",
                      "phenomenon_dossiers.md", "translation_cards.md"):
            p = disc_dir / fname
            if p.exists():
                yield p


def collect_defined_ids(corpus_root: Path) -> Set[str]:
    """Pre-scan: collect every defined card ID in the v3 corpus."""
    ids = set()
    for f in iter_card_files(corpus_root):
        text = f.read_text(encoding="utf-8")
        for m in CARD_HEADER_PATTERN.finditer(text):
            ids.add(m.group(1))
    return ids


def collect_forward_pending(corpus_root: Path) -> Set[str]:
    """
    Read skills/co_retrieval_index.yaml and find any card IDs explicitly
    marked as 'to be created' (forward references whose card body is not
    yet authored). These are treated as acceptable references.
    """
    index_path = corpus_root / "skills" / "co_retrieval_index.yaml"
    pending: Set[str] = set()
    if not index_path.exists():
        return pending
    with index_path.open() as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError:
            return pending
    # Walk the structure looking for "# to be created" comments — handled via
    # explicit annotation. For now we expect zero pending after 9-discipline
    # completion. Leave hook in for forward-compatibility.
    return pending


def get_file_discipline(file_path: Path) -> Optional[str]:
    """Infer discipline from path: skills/long_form/<discipline>/*.md."""
    parts = file_path.parts
    if "long_form" in parts:
        idx = parts.index("long_form")
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return None


# ============================================================================
# REPORTING
# ============================================================================

def is_tty() -> bool:
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def color(text: str, code: str) -> str:
    if not is_tty():
        return text
    return f"\033[{code}m{text}\033[0m"


def print_text_report(report: LintReport) -> None:
    err_count = len(report.errors)
    warn_count = len(report.warnings)

    if not report.issues:
        print(color("✓", "32") + f"  Linter clean — {report.cards_linted} cards in "
              f"{report.files_linted} files; 0 errors, 0 warnings.")
        return

    # Group by file for readability
    by_file: Dict[str, List[LintIssue]] = {}
    for issue in report.issues:
        by_file.setdefault(issue.file, []).append(issue)

    for file_path in sorted(by_file):
        print()
        print(color(file_path, "36"))
        for issue in by_file[file_path]:
            sev_color = "31" if issue.severity == "error" else "33"
            sev_label = color(issue.severity.upper().ljust(7), sev_color)
            cid_str = f"[{issue.card_id}]" if issue.card_id else ""
            print(f"  {sev_label} {issue.rule:30s} {cid_str:30s} {issue.message}")

    print()
    print(
        f"Summary: {color(str(err_count), '31')} errors, "
        f"{color(str(warn_count), '33')} warnings "
        f"across {report.cards_linted} cards in {report.files_linted} files."
    )


def print_json_report(report: LintReport) -> None:
    out = {
        "summary": {
            "errors": len(report.errors),
            "warnings": len(report.warnings),
            "cards_linted": report.cards_linted,
            "files_linted": report.files_linted,
        },
        "issues": [i.to_dict() for i in report.issues],
    }
    print(json.dumps(out, indent=2))


# ============================================================================
# MAIN
# ============================================================================

def lint_file(path: Path, corpus_root: Path, report: LintReport,
              skip_xref: bool = False) -> None:
    """Lint a single card file. Cross-reference checks deferred to corpus-level."""
    rel = str(path.relative_to(corpus_root.parent))
    text = path.read_text(encoding="utf-8")
    discipline = get_file_discipline(path)

    cards = split_cards(text)
    if not cards:
        report.add("warning", "no-cards-found", rel, "",
                   "No CC-/MC-/PD-/TC- card headers found in file.")
        report.files_linted += 1
        return

    report.files_linted += 1
    for card in cards:
        report.cards_linted += 1
        check_word_count(card, rel, report)
        check_required_sections(card, rel, report)
        check_nontrivial_sections(card, rel, report)
        check_doi_coverage(card, rel, report)
        check_when_you_see_hook(card, rel, report)
        check_card_id_matches_file_discipline(card, rel, discipline, report)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Lint the Gaia translator v3 card corpus."
    )
    parser.add_argument(
        "--card",
        type=Path,
        help="Lint a single card file (relative or absolute path). Skips cross-ref check.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero if any warnings are present (errors always fail).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output (for CI integration). Default is human-readable.",
    )
    parser.add_argument(
        "--corpus-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Root of the gaia-translate-QA repository. Defaults to script's parent's parent.",
    )
    args = parser.parse_args(argv)

    corpus_root: Path = args.corpus_root
    if not (corpus_root / "skills" / "long_form").is_dir():
        print(f"ERROR: corpus root '{corpus_root}' does not contain skills/long_form.",
              file=sys.stderr)
        return 2

    report = LintReport()

    if args.card:
        # Lint just one file
        card_path = args.card.resolve()
        if not card_path.exists():
            print(f"ERROR: card file '{card_path}' does not exist.", file=sys.stderr)
            return 2
        lint_file(card_path, corpus_root, report, skip_xref=True)
    else:
        # Lint full corpus
        for f in iter_card_files(corpus_root):
            lint_file(f, corpus_root, report)
        # Cross-reference check spans the whole corpus
        defined_ids = collect_defined_ids(corpus_root)
        forward_pending = collect_forward_pending(corpus_root)
        check_cross_references(corpus_root, defined_ids, forward_pending, report)

    if args.json:
        print_json_report(report)
    else:
        print_text_report(report)

    if report.errors:
        return 1
    if args.strict and report.warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
