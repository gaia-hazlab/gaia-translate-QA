# Eval platform — architecture note for generalization

The Gaia translator eval is the first instance of a general pattern: **domain-expert evaluation of LLM-agent outputs against a multi-criterion rubric, calibrated for inter-rater reliability, designed to feed back into the underlying skill files.** This note documents the design choices that keep the platform generalizable to subsequent exercises (coding agents, document-review agents, research-assistant agents) and lays out the path from v1 (Sheets) to a citable benchmark / possible OA tool.

## The generic data model

The atomic unit of evaluation is a **(question, agent_output, retrieved_context, gold_reference?, scores, comments, attribution)** record. Concretely, every row across every eval exercise has this shape:

```json
{
  "exercise_id": "gaia-translator-v1",
  "qa_id": "QA-CAL-01",
  "domain": "seismology+geotech",
  "subdomain": "liquefaction",
  "query_type": "paper-interpretation",
  "difficulty": 3,
  "question": "...",
  "agent_output": "...",
  "retrieved_context": ["CC-geotech-CSR-CRR", "..."],
  "gold_reference": "..." | null,
  "scores": {
    "technical_accuracy": 5,
    "citation_discipline": 5,
    "vocabulary_precision": 5,
    "cross_discipline_integration": 5,
    "refusal_correctness": null,    // N/A when not a refusal QA
    "completeness": 4,
    "presentation": 4,
    "overall_usefulness": 5
  },
  "comments": {
    "technical_accuracy": "...",
    "...": "..."
  },
  "skill_file_to_revise": ["CC-geotech-Vs30", "TC-12"],
  "confidence_in_score": 5,
  "time_to_score_minutes": 8,
  "flag_for_discussion": false,
  "reviewer_id": "ORCID:0000-...",
  "reviewer_discipline_primary": "seismology",
  "exercise_round": "calibration" | "production" | "held_out",
  "timestamp": "2026-..."
}
```

This schema is intentionally generic. To run a coding-agent eval against the same platform, the only changes are:

- `domain`: from "seismology" to e.g. "python", "rust", "embedded", "ML-infrastructure"
- `subdomain`: from "liquefaction" to e.g. "concurrency", "memory-safety"
- `query_type`: from "paper-interpretation" to e.g. "bug-fix", "refactor", "explain-this-stack-trace"
- Some `scores` criteria are swapped — e.g., replace `cross_discipline_integration` with `api_correctness` or `security_awareness`. The rest (technical accuracy, citation/source discipline, completeness, presentation, overall usefulness) carry over.
- `skill_file_to_revise` points at the coding agent's skill files instead.

Everything else — the calibration-round-first workflow, the per-reviewer xlsx, the master tracker, the Krippendorff's α computation, the low-score-→-revision feedback loop — is unchanged.

## Versioning and reproducibility

For the eval set to be citable, the version of *everything* must be recorded:

- `exercise_id` includes a version tag (e.g., `gaia-translator-v1`).
- Each reviewer's xlsx exports to a JSON record stamped with: scoring date, agent version, retrieval-stack version, card-corpus version (git commit SHA).
- The aggregated JSON dataset is published with: exercise id, rubric version, calibration α, reviewer count, attribution list (per consent).

The output is a Croissant-style (or Datasheets-for-Datasets-style) artifact suitable for Zenodo or HuggingFace Datasets release. A second-generation eval against an improved agent produces a v2 dataset that is comparable to v1 within the same rubric and reviewer pool.

## Path to a citable benchmark

v1 (Sheets + Form, this build) is enough to produce a defensible Phase-7 deliverable. To turn it into a citable benchmark:

1. **Open the calibration set.** Three calibration QAs publicly released; useful as a teaching artifact and as a quick sanity check for anyone replicating.
2. **Release the rubric definitions** under CC-BY-4.0. The 8-criterion definitions with scale anchors are themselves a contribution worth citing.
3. **Release the aggregated dataset** (scores + comments + retrieval context + gold references), reviewer-anonymized at the row level but with reviewer pool documented in aggregate (N=18, disciplines covered, mean experience). Per the consent form, reviewers opt in to identity-attached or aggregated-only release.
4. **Document the methodology** in a methods paper. Reasonable venues: a *Scientific Data* descriptor paper (focused on the dataset); an *EMNLP / NAACL / NeurIPS Datasets & Benchmarks* paper (focused on the methodology and the model evaluation); a *Reviews of Geophysics* piece (focused on the cross-discipline science).

## Path beyond v1

The v1 platform (manual Sheets + Form) is intentionally lightweight. The next milestone is a web app — Streamlit or Gradio with ORCID OAuth — that gives reviewers a clean per-QA scoring UI and the PI a live IRR / progress dashboard. This is Phase 7c in `docs/roadmap.md`. Beyond that, any productization, infrastructure-hosting, or integration with model-training pipelines is out of scope for the public design described in this document.

## Things we are deliberately *not* doing in v1

To keep v1 shippable and the meeting runnable:

- No automated answer generation (the chatbot is not yet built; for v1, "agent_output" is filled by Claude Opus with the cards in-context, simulating retrieval).
- No live-dashboard UI for reviewers; they live in their personal xlsx.
- No automatic IRR computation in-spreadsheet; the PI runs a Python script after the calibration round.
- No reviewer-to-reviewer chat or comment threading; flagged QAs are discussed in the next group meeting, not asynchronously.
- No automated card-revision recommender; the "skill_file_to_revise" column is human-flagged, and the PI manually ranks revision priorities for now.

Each of these is a Phase-B candidate to build *after* v1 has produced enough signal to know what's worth automating.
