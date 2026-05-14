# Eval QA schema — v3

**Status**: v0.1, drafted as the Phase 6 deliverable. Subject to a small revision after the first batch of QAs is reviewed.

**Companion to**: `docs/phase4_output_schema.md` (the chatbot's output schema). Where the Phase 4 schema defines what the chatbot *produces*, this QA schema defines what we *expect* the chatbot to produce for a given input.

---

## 1. Why this exists

Phase 6 of the roadmap expands the eval set from 60 QAs (v2) to ~300 (v3). The schema below is the contract between:

- **QA authors** (Marine, collaborators, Claude-drafted-then-edited)
- **the Phase 4 tool** (Derek's chatbot — produces structured CC/MC/PD/TC output)
- **the reviewer scoring app** (the Streamlit Phase 7c app, eventually; the xlsx in v1)
- **the aggregator** (per-section IRR analysis; the Phase 8 methodology paper)

A QA written against this schema is automatically (a) consumable by the chatbot as input, (b) scoreable per-section by reviewers against the rubric, (c) aggregable for IRR + revision-priority ranking.

---

## 2. Schema (Pydantic v2 canonical)

```python
from __future__ import annotations
from enum import Enum
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


# ============================================================================
# Enums — these must match the Phase 4 output schema enums.
# ============================================================================

class Discipline(str, Enum):
    hydrology = "hydrology"
    seismology = "seismology"
    geotechnical_engineering = "geotechnical_engineering"
    geomorphology = "geomorphology"
    atmospheric_sciences = "atmospheric_sciences"
    ecology = "ecology"
    agricultural_sciences = "agricultural_sciences"
    near_surface_geophysics = "near_surface_geophysics"
    cross_cutting = "cross_cutting"


class QueryType(str, Enum):
    paper_interpretation = "paper-interpretation"
    integration = "integration"
    vocabulary_disambiguation = "vocabulary-disambiguation"
    refusal_test = "refusal-test"
    joint_observation = "joint-observation"


class DocumentType(str, Enum):
    pdf = "pdf"
    url = "url"
    html_text = "html_text"
    none = "none"


class RefusalType(str, Enum):
    """Mirrors agent_playbook.md refusal patterns."""
    forced_analogy = "forced-analogy"
    vocabulary_collision = "vocabulary-collision"
    different_regime = "different-regime"
    missing_causality = "missing-causality"
    outside_grounded_knowledge = "outside-grounded-knowledge"
    fabrication_prevention = "fabrication-prevention"
    surface_power_law_collision = "surface-power-law-collision"


class QAStatus(str, Enum):
    draft = "draft"             # initial; not yet reviewed
    reviewed = "reviewed"        # someone has scored it acceptable
    approved = "approved"        # ready for production eval
    deprecated = "deprecated"    # remove from production but keep for history


# ============================================================================
# Sub-objects
# ============================================================================

class QADocument(BaseModel):
    """Document context the chatbot will receive alongside the prompt."""
    type: DocumentType
    source: Optional[str] = Field(
        None,
        description="File path for PDF, URL for url, 'inline' for html_text, None for type=none."
    )
    title: Optional[str] = None
    notes: Optional[str] = Field(
        None,
        description="Context for QA authors; not shown to the chatbot. E.g., 'real paper from a UW seismology PhD candidate.'"
    )


class ExpectedOutput(BaseModel):
    """The gold-standard structure of what the chatbot should produce."""

    concept_matches: List[str] = Field(
        default_factory=list,
        description=(
            "List of CC-* card IDs the chatbot should identify as relevant. "
            "Order is by expected relevance (most relevant first)."
        )
    )
    method_matches: List[str] = Field(default_factory=list)
    phenomenon_matches: List[str] = Field(default_factory=list)
    translation_matches: List[str] = Field(default_factory=list)

    vocabulary_collisions_flagged: List[str] = Field(
        default_factory=list,
        description=(
            "Terms from agent_playbook.md vocabulary table that the chatbot should disambiguate. "
            "Empty if no polysemous term appears in the prompt."
        )
    )
    refusals_or_caveats_expected: List[RefusalType] = Field(
        default_factory=list,
        description=(
            "Refusal patterns the chatbot should invoke. Empty for queries that don't trigger any. "
            "A 'refusal-test' QA must have at least one entry here."
        )
    )

    user_specific_response_themes: List[str] = Field(
        default_factory=list,
        description=(
            "Bullet list of key ideas the chatbot's user_specific_response should hit. "
            "Used by reviewers to score completeness without prescribing exact wording. "
            "Typically 3–6 themes per QA."
        )
    )

    must_not_say: List[str] = Field(
        default_factory=list,
        description=(
            "Phrases or claims that would be hard-fails (e.g., 'fabricated citation', "
            "'forced equivalence between Gutenberg-Richter and Hack's law'). "
            "Used by reviewers to score citation-discipline and refusal-correctness."
        )
    )


class QualityNotes(BaseModel):
    """Curation metadata for QA authors and reviewers."""

    author: str = Field(..., description="QA author. E.g., 'Marine', 'Claude+Marine-edit', 'Derek'.")
    source_question: Optional[str] = Field(
        None,
        description="If the QA was drawn from a real research conversation or paper, attribute it here."
    )
    review_notes: Optional[str] = None
    last_reviewed_date: Optional[str] = None
    last_reviewed_by: Optional[str] = None


# ============================================================================
# Top-level QA
# ============================================================================

class EvalQA(BaseModel):
    """One eval-set question with its expected structured response."""

    # --- Identifier ---
    id: str = Field(
        ...,
        pattern=r"^(QA-EVAL|QA-CAL|QA-HELDOUT)-\d{3,}$",
        description="QA-EVAL-### for production, QA-CAL-### for calibration round, QA-HELDOUT-### for post-revision held-out set."
    )
    schema_version: Literal["v3"] = "v3"

    # --- Classification ---
    primary_disciplines: List[Discipline] = Field(
        ...,
        min_length=1,
        max_length=4,
        description="Disciplines the QA touches. 1 for single-discipline QAs; 2-4 for cross-discipline."
    )
    query_type: QueryType
    difficulty: int = Field(
        ...,
        ge=1, le=5,
        description="1=trivial, 3=median graduate-student question, 5=research-frontier integration."
    )

    # --- Inputs to the chatbot ---
    prompt: str = Field(..., min_length=10)
    input_document: QADocument

    # --- Expected output ---
    expected_output: ExpectedOutput

    # --- Curation metadata ---
    status: QAStatus = QAStatus.draft
    quality_notes: QualityNotes

    class Config:
        extra = "forbid"
```

---

## 3. Per-section scoring map

Each section of the chatbot's response is scored against the corresponding `expected_output` field, then mapped to one or more rubric criteria from `eval_platform/`.

| Chatbot section (Phase 4 output) | Expected-output field | Rubric criteria scored |
|---|---|---|
| `concept_matches` | `concept_matches` | Technical accuracy, Citation discipline, Vocabulary precision |
| `method_matches` | `method_matches` | Technical accuracy, Citation discipline |
| `phenomenon_matches` | `phenomenon_matches` | Technical accuracy, Citation discipline |
| `translation_matches` | `translation_matches` | Cross-discipline integration (the criterion this section is for) |
| `vocabulary_collisions_flagged` | `vocabulary_collisions_flagged` | Vocabulary precision |
| `refusals_or_caveats` | `refusals_or_caveats_expected` | Refusal correctness |
| `user_specific_response` | `user_specific_response_themes`, `must_not_say` | Completeness, Presentation, Overall usefulness |

Scoring rules:

- **Recall on card matches**: of the expected card IDs in `expected_output.X_matches`, what fraction did the chatbot include? Score on Technical accuracy.
- **Precision on card matches**: of the cards the chatbot included, what fraction are reasonable (per the reviewer's judgment, *not* requiring exact match to the expected list)? Score on Technical accuracy.
- **Theme coverage**: of `user_specific_response_themes`, what fraction did the chatbot's response cover? Score on Completeness.
- **`must_not_say` violation**: any violation is an automatic 1 on the relevant criterion (Citation discipline for fabricated citations; Refusal correctness for forced analogies).

The reviewer-facing spreadsheet from Phase 7 prefills the expected output as a checklist; reviewers tick which expected items the chatbot got right and which it got wrong.

---

## 4. Stratification targets

The full Phase 6 eval set (~300 QAs) should approximately match these distributions. The validator (`pipeline/validate_eval_set.py`) checks against these.

### Per-discipline coverage (single-discipline QAs)

| Discipline | Target count |
|---|---|
| Hydrology | 25 |
| Seismology | 25 |
| Geotechnical engineering | 25 |
| Geomorphology | 25 |
| Atmospheric sciences | 25 |
| Ecology | 25 |
| Agricultural sciences | 25 |
| Near-surface geophysics | 25 |
| (subtotal, single-discipline) | **200** |

Tolerance: ±5 per discipline.

### Cross-discipline coverage

| Discipline span | Target count |
|---|---|
| 2-discipline | 70 |
| 3-discipline | 20 |
| 4+ discipline | 10 |
| (subtotal, cross-discipline) | **100** |

Tolerance: ±10 across the cross-discipline subset.

### Query-type distribution

| Query type | Target % | Target count |
|---|---|---|
| paper-interpretation | 40% | 120 |
| integration | 25% | 75 |
| vocabulary-disambiguation | 15% | 45 |
| refusal-test | 10% | 30 |
| joint-observation | 10% | 30 |

Tolerance: ±5% per category.

### Difficulty distribution

| Difficulty | Target count |
|---|---|
| 1 (trivial) | 30 |
| 2 (easy) | 60 |
| 3 (median) | 120 |
| 4 (hard) | 60 |
| 5 (frontier) | 30 |

Tolerance: ±15 per level.

### Author mix

| Author | Target count |
|---|---|
| Hand-drafted by Marine + Denolle Group + collaborators | 120 (40%) |
| LLM-drafted then human-edited | 180 (60%) |

This mix is what the methodology paper will report.

---

## 5. Calibration sub-set

20 QAs (a stratified subset of the 300) form the **calibration round** that establishes inter-rater reliability before the full eval. The 20 are chosen to span:

- All 9 disciplines (≥ 2 per discipline).
- All 5 query types.
- A range of difficulties (mostly 3, plus 5× difficulty 2 and 5× difficulty 4).
- The 3 already-authored calibration QAs (QA-CAL-01/02/03 from `eval_platform/calibration_qas/`) automatically qualify.

The `--calibration` flag in `pipeline/validate_eval_set.py` picks a candidate calibration set from the full v3 eval JSON.

---

## 6. Held-out subset for Phase 8 re-evaluation

50 QAs (also a stratified subset of the 300) are reserved for **post-revision held-out evaluation** in Phase 8. They are *not* shown to reviewers during the Phase 7 evaluation rounds. Marine + 2 trusted collaborators score these against the revised chatbot to measure whether card revisions improved performance.

The `--heldout` flag in `pipeline/validate_eval_set.py` flags candidates.

---

## 7. JSON output format

The canonical eval set is one JSON file with a flat array of `EvalQA` objects:

```json
{
  "schema_version": "v3",
  "generated_at": "2026-...",
  "stats": {
    "total_qas": 300,
    "by_discipline": {...},
    "by_query_type": {...},
    "by_difficulty": {...}
  },
  "qas": [
    { "id": "QA-EVAL-001", "schema_version": "v3", ... },
    { "id": "QA-EVAL-002", "schema_version": "v3", ... },
    ...
  ]
}
```

File path: `eval_dataset/eval_dataset_v3.json`.

---

## 8. Reviewer-facing xlsx output

`pipeline/build_review_spreadsheet.py` reads `eval_dataset_v3.json` and produces `eval_dataset/gaia_translator_eval_review_v3.xlsx`. The xlsx has columns:

- Identifier and classification (id, disciplines, query_type, difficulty, status)
- Input (prompt, input_document.type, input_document.source, input_document.title)
- Expected output as separate columns: concept_matches, method_matches, etc. (comma-separated IDs)
- Themes and must-not-say (newline-separated)
- Reviewer columns (empty, to be filled): per-section scores, comments, overall, confidence, time

This xlsx is what gets imported into the Streamlit reviewer app (Phase 7c) or used as the v1 paper-Sheets review surface (Phase 7a).

---

## 9. Open decisions

1. **Should `expected_output.X_matches` be a strict subset or a soft target?** Recommendation: soft. Reviewers score recall *and* precision; the chatbot is allowed to add relevant cards we didn't anticipate. The expected list is "what we expect at minimum."

2. **Should `must_not_say` accept regex patterns or plain strings?** Recommendation: plain strings for v3.0; revisit if regex flexibility is needed.

3. **What's the canonical form of cross-discipline disciplines in `primary_disciplines`?** Recommendation: keep them as flat lists of disciplines (no ordering preference for multi-discipline QAs).

4. **Should `quality_notes.source_question` be required for hand-drafted QAs?** Recommendation: strongly encouraged but not required. Provenance is useful for the methodology paper but not always available.

---

## 10. Versioning

- v3.0: the schema in this document.
- Breaking changes bump major. Additive changes bump minor.
- The eval set's `schema_version` field must equal the schema-version of the validator used to ingest it.

When schema v4 is needed (presumably after Phase 7 feedback), document the migration explicitly: which fields changed, how existing QAs are upgraded.

---

## 11. Implementation files

| File | Purpose |
|---|---|
| `docs/eval_qa_schema.md` | This document. |
| `docs/eval_qa_design.md` | Guidelines for QA authors. |
| `pipeline/seed_qa_dataset.py` | Hand-curated anchor QAs in v3 format. |
| `pipeline/validate_eval_set.py` | Schema + stratification validator. |
| `pipeline/build_review_spreadsheet.py` | JSON → reviewer xlsx. |
| `pipeline/generate_eval_dataset.py` | LLM-drafter skeleton (Anthropic SDK). |
| `eval_dataset/eval_dataset_v3.json` | The canonical eval set. |
| `eval_dataset/gaia_translator_eval_review_v3.xlsx` | Reviewer surface. |
