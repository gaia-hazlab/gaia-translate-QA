# PR Prep — Eval Framework v3.1 (failure-mode + tier dimensions)

This file is scratch documentation for the PR review with GitHub Copilot. It is
safe to delete after the PR is merged. Move/rename freely; nothing else
references it.

---

## 1. Branch

```bash
git checkout -b feat/eval-v3.1-dimensions
```

Rationale: short, semantic, single-feature. Matches the convention of prior
branches in this repo (which were committed directly to `main` — moving forward,
we want PR-reviewed changes from a feature branch).

---

## 2. What changed in one sentence

Adds three new dimensions to the eval framework — **tier** (bronze/silver/gold),
**translation task type** (7-item taxonomy), and **failure mode tested** (7-item
taxonomy) — so the v3.1 eval set can be reported per-failure-mode (the
publishable contribution per the prior-art analyses we just imported).

---

## 3. Commit message (single commit, conventional-commits style)

```
feat(eval): v3.1 dimensions — tier, translation_task_types, failure_modes_tested

Adds three new required dimensions to every eval QA, derived from the prior-art
analyses in docs/prior_art/ (EarthSE, K2, HydroLLM):

  - tier: bronze | silver | gold  (canonical 3-level difficulty)
  - translation_task_types: List of 1-3 from a 7-item taxonomy
      (concept-mapping, method-translation, sensor-data-equivalence,
       data-availability-assessment, terminology-bridging,
       limitation-translation, parameter-threshold-equivalence)
  - expected_output.failure_modes_tested: List of 1-4 from a 7-item taxonomy
      (hallucinated-analogue, concept-confusion, domain-ignorance,
       implausible-calibration, missing-constraint, false-equivalence,
       terminology-failure)
  - compound_coupling: List[str] of alphabetized "disc-disc" pairs

Why: per-failure-mode reporting (augmentation +23% on missing-constraint vs.
+1% on hallucinated-analogue, per EarthSE) is the headline result for any
benchmark paper. The previous schema only had query_type + difficulty, so we
could only report aggregates.

What was touched
  docs/
    eval_qa_schema.md           — Pydantic v2 enums + field definitions
    eval_qa_design.md           — sections 2.5-2.8 explain each new dimension
    eval_dimensions_framework.md (NEW) — stratification targets per dimension
    prior_art/ (NEW)            — 3 markdown analyses driving this design
    roadmap.md, PR_v3.1_dimensions.md — bookkeeping

  pipeline/
    seed_qa_dataset.py          — 21 anchor QAs migrated to v3.1
    validate_eval_set.py        — validation + stats for new fields
    build_review_spreadsheet.py — 4 new columns; SCORE_COLS shifted to 22-30
    generate_eval_dataset.py    — auto_pick_gap() now spans all 6 dimensions;
                                  --coverage and --tier/--task-type/
                                  --failure-mode CLI flags

  eval_dataset/
    eval_dataset_v3.json        — 21 QAs regenerated under v3.1
    gaia_translator_eval_review_v3.xlsx — regenerated reviewer sheet

Validation
  $ python pipeline/validate_eval_set.py
    21 QAs, 0 errors, 0 warnings.
  $ python pipeline/generate_eval_dataset.py --coverage
    Prints gap analysis across all 6 dimensions.
  $ python pipeline/generate_eval_dataset.py --auto --n 5 --dry-run
    Picks 5 most-undercovered combinations without LLM calls.

Out of scope (follow-up PRs)
  - Real LLM drafting to expand the eval set from 21 → 300 QAs
  - Streamlit reviewer app (Phase 7c)
  - Per-failure-mode scoring tab in the xlsx reviewer sheet
```

---

## 4. PR title

```
Eval framework v3.1: tier + failure-mode dimensions for per-mode reporting
```

---

## 5. PR description (paste into the PR body)

```markdown
## Summary

Extends the eval schema with three new dimensions so the v3.1 eval set can be
reported **per-failure-mode**, which is the headline contribution per the
prior-art analyses now in `docs/prior_art/`.

### New required fields on every QA
| Field | Cardinality | Values |
|---|---|---|
| `tier` | exactly 1 | `bronze`, `silver`, `gold` |
| `translation_task_types` | 1–3 | 7-item taxonomy (see `docs/eval_qa_schema.md` §2.5) |
| `compound_coupling` | 0–N | alphabetized `"discA-discB"` pairs |
| `expected_output.failure_modes_tested` | 1–4 | 7-item taxonomy (see schema §2.7) |

### Why now
The two earlier dimensions (`query_type`, `difficulty`) only let us report
aggregate accuracy. Prior-art benchmarks (EarthSE, K2, HydroLLM) show **the
useful signal is per-failure-mode**: e.g. augmentation gives +23% on
`missing-constraint` but only +1% on `hallucinated-analogue`. To produce that
analysis we need each QA to declare which failure modes it probes.

## Files touched

- **Schema and design** — `docs/eval_qa_schema.md`,
  `docs/eval_qa_design.md`, new `docs/eval_dimensions_framework.md`.
- **Pipeline** — `pipeline/{seed_qa_dataset,validate_eval_set,build_review_spreadsheet,generate_eval_dataset}.py`.
- **Data artifacts** — regenerated `eval_dataset/eval_dataset_v3.json` and
  `eval_dataset/gaia_translator_eval_review_v3.xlsx` (binary diff).
- **Prior-art docs (new)** — 3 analyses in `docs/prior_art/` and the synthesis
  in `docs/eval_dimensions_framework.md`.

## Specific reviewer questions for Copilot

1. **`pipeline/generate_eval_dataset.py` — `auto_pick_gap()`**
   Six-dimension gap picker with two self-consistency nudges (tier ↔ difficulty
   range, refusal-test ↔ failure-mode subset). Are the nudges defensible? Any
   edge case where they oscillate or pick an inconsistent set?

2. **`pipeline/build_review_spreadsheet.py`** — `SCORE_COLS` shifted from
   `range(18,26)` to `range(22,30)`, `MEAN_COL` from 26 to 30, and Progress-tab
   formulas now reference `AJ/AD/AI/AH` instead of `AF/Z/AE/AD`. Spot-check
   that every reference moved consistently.

3. **`pipeline/validate_eval_set.py` — `validate_qa()`** — does the
   `compound_coupling` alphabetization check correctly handle 3-discipline QAs
   (which produce C(3,2)=3 pairs)?

4. **`docs/eval_qa_schema.md`** — Pydantic `min_length`/`max_length` constraints
   on the new list fields look right? `failure_modes_tested` is 1–4, not 1–3
   like task types — intentional (some QAs probe more failure modes than they
   exercise translation tasks).

## Testing

```bash
# All three should pass cleanly
python pipeline/validate_eval_set.py
python pipeline/generate_eval_dataset.py --coverage
python pipeline/generate_eval_dataset.py --auto --n 5 --dry-run
python pipeline/build_review_spreadsheet.py
```

## Out of scope (separate follow-up PRs)

- **Real LLM drafting** to fill the 21 → 300 gap. This PR ships the
  *infrastructure*; the drafter itself runs locally with a user-provided
  `ANTHROPIC_API_KEY`. See `docs/PR_v3.1_dimensions.md` §6 for the exact
  command.
- Streamlit reviewer scoring app (Phase 7c).
- Per-failure-mode pivot tab in the reviewer xlsx.
```

---

## 6. Real LLM drafting — exact local command

The sandbox running this session has no `ANTHROPIC_API_KEY`, so the drafter
**must be run locally**. From the repo root:

```bash
# 1. Confirm key is set in your shell
export ANTHROPIC_API_KEY="sk-ant-..."

# 2. Sanity check coverage gaps
python pipeline/generate_eval_dataset.py --coverage

# 3. Dry-run to preview what will be drafted (no tokens spent)
python pipeline/generate_eval_dataset.py --auto --n 10 --dry-run

# 4. For real — drafts to /drafts/ (NOT to eval_dataset_v3.json directly;
#    drafts go through human review before merging into the canonical set)
python pipeline/generate_eval_dataset.py --auto --n 10

# 5. Review the drafts in /drafts/
ls -la drafts/
```

The drafter writes one JSON file per QA into `/drafts/`. Marine should
manually inspect each draft, edit as needed, then move into
`pipeline/seed_qa_dataset.py` (or a successor `corpus_qa_dataset.py`).

### Token cost estimate
- Each QA → ~3k input tokens (corpus context) + ~1k output tokens
- 10 QAs ≈ 30k input + 10k output tokens
- At `claude-opus-4-6` rates: roughly $0.50 – $0.80 total

---

## 7. After merge

Update `docs/roadmap.md` Phase 6 row from "in progress" to
"complete (schema), in progress (drafting)" — but only after the first
follow-up PR that fills the drafting gap.
