#!/usr/bin/env python3
"""
generate_eval_dataset.py — LLM-assisted drafter for new v3 QAs.

Goal
----
Get from 21 seed QAs → ~300 production QAs by having Claude draft candidates
that the human then reviews, edits, and commits. The script is the skeleton;
the human curation is the load-bearing part.

Usage
-----
    # Draft N new QAs targeting a specific discipline + query type + difficulty:
    python pipeline/generate_eval_dataset.py \
        --discipline hydrology \
        --query-type integration \
        --difficulty 3 \
        --n 5 \
        --out drafts/qa_drafts_2026-05-14.json

    # Draft a balanced batch that fills the worst gaps in current coverage:
    python pipeline/generate_eval_dataset.py --auto --n 20 --out drafts/

The output is a directory of *candidate* QA JSON files. Each requires human
review before being merged into pipeline/seed_qa_dataset.py and committed.

Workflow
--------
1. Run this script to produce N candidate JSON files.
2. Open each candidate in an editor.
3. Apply the QA quality checklist from docs/eval_qa_design.md, Section 11.
4. Edit aggressively: trim expected_output (LLM tends to over-stuff), recalibrate
   difficulty, sharpen response themes, verify card IDs exist.
5. When ready, append the QA to pipeline/seed_qa_dataset.py with author tag
   "Claude+<your-name>-edit".
6. Run pipeline/validate_eval_set.py to confirm the addition.
7. Run pipeline/build_review_spreadsheet.py to regenerate the reviewer xlsx.

Requirements
------------
- ANTHROPIC_API_KEY environment variable.
- `pip install anthropic` (not done in this skeleton; tested at runtime).

This file is a *skeleton* — it has the structure, prompt-templates, and CLI
plumbing. The actual API call is wrapped in a try/except so the file can be
inspected without invoking inference.

Author: Denolle Group.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import textwrap
import uuid
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


# ============================================================================
# CONFIG
# ============================================================================

DEFAULT_MODEL = "claude-opus-4-7"
DEFAULT_MAX_TOKENS = 4096

VALID_DISCIPLINES = [
    "hydrology", "seismology", "geotechnical_engineering", "geomorphology",
    "atmospheric_sciences", "ecology", "agricultural_sciences",
    "near_surface_geophysics",
]
VALID_QUERY_TYPES = [
    "paper-interpretation", "integration", "vocabulary-disambiguation",
    "refusal-test", "joint-observation",
]


# ============================================================================
# PROMPT TEMPLATES
# ============================================================================

SYSTEM_PROMPT = """\
You are an expert geoscientist drafting candidate evaluation questions for the
Gaia translator, a research chatbot that helps researchers interpret papers
across geoscience disciplines (hydrology, seismology, geotechnical engineering,
geomorphology, atmospheric sciences, ecology, agricultural sciences,
near-surface geophysics).

Your job: produce ONE candidate evaluation QA that follows the v3 schema
specified in docs/eval_qa_schema.md. The QA will be reviewed and edited by a
human (Marine Denolle, ESS UW) before being added to the production eval set.

CRITICAL RULES:

1. Phrase the prompt as a REAL research question a real researcher would ask.
   "Tell me about X" is bad; "I'm reading paper Y as a discipline Z researcher
   and don't understand how W connects to my work" is good.

2. The expected_output.user_specific_response_themes must be 3-6 SPECIFIC
   themes (e.g., "Explains why dv/v cannot replace wells in the Central Valley"
   not "Discusses dv/v limitations").

3. Card IDs in concept_matches / method_matches / phenomenon_matches /
   translation_matches must be REAL, EXISTING v3 cards from this corpus.
   The corpus is loaded into your context. Do NOT invent card IDs.

4. For refusal-test queries, populate refusals_or_caveats_expected with the
   correct refusal pattern and populate must_not_say with phrases the chatbot
   must avoid.

5. Difficulty calibration:
   - 1: trivial textbook lookup
   - 2: easy single-discipline
   - 3: median graduate-student question (most QAs should be 3)
   - 4: hard cross-discipline with real failure modes
   - 5: research frontier

6. Output is JSON conforming exactly to the schema. NO commentary, NO
   surrounding prose. Just the JSON object.
"""

USER_PROMPT_TEMPLATE = """\
Generate ONE candidate v3 eval QA with these constraints:

- Primary discipline(s): {disciplines}
- Query type: {query_type}
- Difficulty: {difficulty}
- ID: {qa_id}

The QA should explore one of the cross-discipline frontiers actively studied
in the GAIA HazLab agenda or in standard geoscience research practice.
Prefer real-paper anchoring when possible (e.g., reference a real publication
the researcher might be reading).

Output a single JSON object with this exact shape:

```json
{{
  "id": "{qa_id}",
  "schema_version": "v3",
  "primary_disciplines": [...],
  "query_type": "{query_type}",
  "difficulty": {difficulty},
  "prompt": "...",
  "input_document": {{
    "type": "none",
    "source": null,
    "title": null,
    "notes": "LLM draft; review before approval"
  }},
  "expected_output": {{
    "concept_matches": ["CC-..."],
    "method_matches": ["MC-..."],
    "phenomenon_matches": ["PD-..."],
    "translation_matches": ["TC-..."],
    "vocabulary_collisions_flagged": [],
    "refusals_or_caveats_expected": [],
    "user_specific_response_themes": [
      "Theme 1: ...",
      "Theme 2: ...",
      "Theme 3: ..."
    ],
    "must_not_say": []
  }},
  "status": "draft",
  "quality_notes": {{
    "author": "Claude-drafted",
    "source_question": null,
    "review_notes": null,
    "last_reviewed_date": null,
    "last_reviewed_by": null
  }}
}}
```

Remember: card IDs must reference REAL cards in the loaded corpus. Use only
3-6 specific themes. If your query_type is refusal-test, populate
refusals_or_caveats_expected and must_not_say. Output JSON only.
"""


# ============================================================================
# CORPUS LOADING
# ============================================================================

def load_corpus_as_context(corpus_root: Path) -> str:
    """
    Build the system-prompt-grade context: discipline summaries +
    agent playbook + cross-cutting concepts + co-retrieval index.

    Returns a single string of ~10k-15k tokens for the model to consume
    as in-context grounding.
    """
    parts = []

    # Summaries
    summaries_dir = corpus_root / "skills" / "summaries"
    for sf in sorted(summaries_dir.glob("*.md")):
        parts.append(f"\n\n=== DISCIPLINE SUMMARY: {sf.stem} ===\n")
        parts.append(sf.read_text(encoding="utf-8"))

    # Agent playbook
    parts.append("\n\n=== AGENT PLAYBOOK (refusal patterns, vocabulary table) ===\n")
    parts.append((corpus_root / "skills" / "agent_playbook.md").read_text(encoding="utf-8"))

    # Cross-cutting concepts
    parts.append("\n\n=== CROSS-CUTTING CONCEPTS ===\n")
    parts.append((corpus_root / "skills" / "cross_cutting_concepts.md").read_text(encoding="utf-8"))

    # Co-retrieval index (compressed)
    parts.append("\n\n=== CO-RETRIEVAL INDEX (card titles) ===\n")
    parts.append((corpus_root / "skills" / "co_retrieval_index.yaml").read_text(encoding="utf-8"))

    return "\n".join(parts)


def load_corpus_long_form(corpus_root: Path) -> str:
    """
    Build the LONG-form context: all long-form cards across all disciplines.

    This is ~70k tokens. Use this only when you need the agent to ground in
    specific card content for a high-quality draft.
    """
    parts = []
    long_form = corpus_root / "skills" / "long_form"
    for disc_dir in sorted(long_form.iterdir()):
        if not disc_dir.is_dir() or disc_dir.name == "v2_legacy":
            continue
        for f in sorted(disc_dir.glob("*.md")):
            parts.append(f"\n\n=== {disc_dir.name.upper()} / {f.name.upper()} ===\n")
            parts.append(f.read_text(encoding="utf-8"))
    return "\n".join(parts)


# ============================================================================
# LLM CALL (skeleton)
# ============================================================================

def draft_one_qa(
    corpus_context: str,
    disciplines: List[str],
    query_type: str,
    difficulty: int,
    qa_id: str,
    long_form_context: Optional[str] = None,
    model: str = DEFAULT_MODEL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> Dict:
    """
    Call Claude to draft one candidate QA.

    Returns the parsed JSON dict. Raises if the API key is missing or
    the response can't be parsed.
    """
    try:
        import anthropic
    except ImportError:
        raise RuntimeError("anthropic package not installed. pip install anthropic")

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY environment variable not set.")

    client = anthropic.Anthropic(api_key=api_key)

    user_prompt = USER_PROMPT_TEMPLATE.format(
        disciplines=disciplines,
        query_type=query_type,
        difficulty=difficulty,
        qa_id=qa_id,
    )

    # Concatenate corpus context as a system-prompt prefix.
    system_with_corpus = SYSTEM_PROMPT + "\n\n" + corpus_context
    if long_form_context:
        system_with_corpus += "\n\n=== LONG-FORM CARD CONTENT ===\n" + long_form_context

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_with_corpus,
        messages=[{"role": "user", "content": user_prompt}],
    )

    # Extract the JSON payload from the response.
    text = response.content[0].text.strip()
    # Strip markdown code fences if present
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
    if text.endswith("```"):
        text = text.rsplit("\n", 1)[0]
    text = text.strip()

    return json.loads(text)


# ============================================================================
# AUTO-PRIORITIZATION
# ============================================================================

def load_existing_qa_ids(corpus_root: Path) -> List[str]:
    """Find the highest QA-EVAL-### ID in use so we don't collide."""
    try:
        sys.path.insert(0, str(corpus_root / "pipeline"))
        from seed_qa_dataset import SEED_QAS
        return [qa["id"] for qa in SEED_QAS]
    except Exception:
        return []


def next_qa_id(existing: List[str]) -> str:
    """Pick the next QA-EVAL-### that doesn't collide."""
    used = set()
    for x in existing:
        if x.startswith("QA-EVAL-"):
            try:
                used.add(int(x.split("-")[-1]))
            except ValueError:
                pass
    n = 1
    while n in used:
        n += 1
    return f"QA-EVAL-{n:03d}"


def auto_pick_gap(existing_qas: List[Dict]) -> Dict:
    """
    Identify the worst undercoverage in the current eval set vs. targets.
    Returns a dict {"disciplines": [...], "query_type": "...", "difficulty": N}.
    """
    # Targets from docs/eval_qa_schema.md
    target_qt = {
        "paper-interpretation": 120, "integration": 75,
        "vocabulary-disambiguation": 45, "refusal-test": 30,
        "joint-observation": 30,
    }
    target_disc = {d: 25 for d in VALID_DISCIPLINES}
    target_diff = {1: 30, 2: 60, 3: 120, 4: 60, 5: 30}

    actual_qt = Counter(qa["query_type"] for qa in existing_qas)
    actual_disc = Counter()
    for qa in existing_qas:
        for d in qa["primary_disciplines"]:
            actual_disc[d] += 1
    actual_diff = Counter(qa["difficulty"] for qa in existing_qas)

    # Pick query type with highest target-actual ratio
    gap_qt = max(target_qt, key=lambda k: target_qt[k] - actual_qt.get(k, 0))
    gap_disc = max(target_disc, key=lambda k: target_disc[k] - actual_disc.get(k, 0))
    gap_diff = max(target_diff, key=lambda k: target_diff[k] - actual_diff.get(k, 0))

    return {
        "disciplines": [gap_disc],
        "query_type": gap_qt,
        "difficulty": gap_diff,
    }


# ============================================================================
# CLI
# ============================================================================

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Draft new v3 eval QAs via Claude.")
    parser.add_argument("--discipline", help="Primary discipline. Required unless --auto.")
    parser.add_argument("--query-type", choices=VALID_QUERY_TYPES,
                        help="Query type. Required unless --auto.")
    parser.add_argument("--difficulty", type=int, choices=[1, 2, 3, 4, 5],
                        help="Difficulty. Required unless --auto.")
    parser.add_argument("--auto", action="store_true",
                        help="Auto-select discipline/type/difficulty by gap analysis.")
    parser.add_argument("--n", type=int, default=1, help="Number of QAs to draft.")
    parser.add_argument("--out", type=Path, default=Path("drafts/"),
                        help="Output directory or single JSON file.")
    parser.add_argument("--with-long-form", action="store_true",
                        help="Include all 170 long-form cards in context (~70k tokens; slower; better quality).")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what we'd ask Claude without making the API call.")
    parser.add_argument(
        "--corpus-root", type=Path,
        default=Path(__file__).resolve().parent.parent,
    )
    args = parser.parse_args(argv)

    if not args.auto and not (args.discipline and args.query_type and args.difficulty):
        print("ERROR: specify --discipline, --query-type, --difficulty, or use --auto.",
              file=sys.stderr)
        return 2

    corpus_context = load_corpus_as_context(args.corpus_root)
    long_form_context = load_corpus_long_form(args.corpus_root) if args.with_long_form else None
    existing_ids = load_existing_qa_ids(args.corpus_root)
    existing_qas = []
    if args.auto:
        # Load existing for gap analysis
        try:
            sys.path.insert(0, str(args.corpus_root / "pipeline"))
            from seed_qa_dataset import SEED_QAS
            existing_qas = SEED_QAS
        except Exception:
            print("WARNING: could not load existing QAs for auto mode; falling back to random.",
                  file=sys.stderr)

    out_dir = args.out
    if not out_dir.is_absolute():
        out_dir = args.corpus_root / out_dir
    if str(out_dir).endswith(".json"):
        out_file = out_dir
        out_dir = out_file.parent
    else:
        out_file = None
    out_dir.mkdir(parents=True, exist_ok=True)

    drafted = []
    for i in range(args.n):
        if args.auto:
            choice = auto_pick_gap(existing_qas + drafted)
            disciplines = choice["disciplines"]
            query_type = choice["query_type"]
            difficulty = choice["difficulty"]
        else:
            disciplines = [args.discipline]
            query_type = args.query_type
            difficulty = args.difficulty

        qa_id = next_qa_id(existing_ids + [qa["id"] for qa in drafted])

        if args.dry_run:
            print(f"[DRY RUN] Would draft: {qa_id} "
                  f"({disciplines}, {query_type}, difficulty={difficulty})")
            drafted.append({"id": qa_id, "primary_disciplines": disciplines,
                            "query_type": query_type, "difficulty": difficulty})
            continue

        print(f"Drafting {qa_id} ({disciplines}, {query_type}, diff={difficulty})...")
        try:
            qa = draft_one_qa(
                corpus_context=corpus_context,
                disciplines=disciplines,
                query_type=query_type,
                difficulty=difficulty,
                qa_id=qa_id,
                long_form_context=long_form_context,
                model=args.model,
            )
        except Exception as e:
            print(f"  ERROR drafting {qa_id}: {e}", file=sys.stderr)
            continue

        # Write to per-file or aggregate
        if out_file:
            existing = []
            if out_file.exists():
                with out_file.open() as f:
                    existing = json.load(f)
            existing.append(qa)
            with out_file.open("w") as f:
                json.dump(existing, f, indent=2)
        else:
            single_path = out_dir / f"{qa_id}.json"
            with single_path.open("w") as f:
                json.dump(qa, f, indent=2)

        drafted.append(qa)

    print(f"\nDrafted {len(drafted)} QAs to {out_file or out_dir}.")
    if not args.dry_run:
        print("\nNext steps:")
        print("  1. Open each draft and review against docs/eval_qa_design.md, Section 11.")
        print("  2. Edit aggressively (trim expected_output, recalibrate difficulty).")
        print("  3. When ready, append to pipeline/seed_qa_dataset.py (author='Claude+<your-name>-edit').")
        print("  4. Run: python pipeline/validate_eval_set.py")
        print("  5. Run: python pipeline/build_review_spreadsheet.py")

    return 0


if __name__ == "__main__":
    sys.exit(main())
