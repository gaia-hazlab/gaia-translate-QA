# Eval dimensions framework — v3 (post-prior-art-revision)

**Status**: v3.1. Supersedes the dimensional sketches in the initial `docs/eval_qa_schema.md` and `docs/eval_qa_design.md` by adding four new dimensions derived from a review of prior art (EarthSE arXiv:2505.17139, K2 arXiv:2306.05064, HydroLLM-Benchmark 2025). See `docs/prior_art/` for the underlying analyses.

## What changed and why

The initial Phase 6 framework tracked two QA classification dimensions: `query_type` (5 values: paper-interpretation / integration / vocab-disambiguation / refusal-test / joint-observation) and `difficulty` (numeric 1–5). Prior-art analysis identified four additional dimensions that are **load-bearing for the publishable methodology paper** and that the initial framework either missed or under-specified:

1. **Translation task types** (7-item taxonomy of cognitive translation operations).
2. **Tier** (Bronze / Silver / Gold — task-complexity-anchored).
3. **Compound coupling** (which discipline pair the translation crosses).
4. **Failure modes tested** (7-item taxonomy of *where* the chatbot is expected to fail).

The dominant payoff is #4: the publishable contribution per the prior-art review is *not* "augmented model beats base model" (predictable) — it's "**augmentation targets these specific failure modes (+23%) but not these others (+1%), revealing the mechanism by which domain calibration helps**." That analysis requires the failure-mode dimension on every QA, computed at design time, so the eval set explicitly probes each failure mode with calibrated coverage.

## Dimension 1: Translation task types

**What it is.** A taxonomy of the *cognitive operations* the chatbot performs when translating across disciplines. Adapted from the prior-art recommendation in `docs/prior_art/benchmark_design_lessons_from_prior_art.md`, §1.

**The 7 task types.**

| Task type | Definition | Example |
|---|---|---|
| **concept-mapping** | Given a concept in discipline A, find/define its functional analogue in B. | "What's the seismic analogue of 'aquifer drawdown'?" |
| **method-translation** | Given a method in A, describe how to operationalize the equivalent method in B. | "How would you do 'moment tensor inversion' on hydrology data?" |
| **sensor-data-equivalence** | Given a sensor or dataset in A, name the equivalent instrument or data source in B. | "What does a piezometer measure that's analogous to a seismometer's observable?" |
| **data-availability-assessment** | Given a question that arises in A, what datasets in B are accessible and operationally usable? | "I want to study induced seismicity; what hydrology datasets should I look for?" |
| **terminology-bridging** | Translate jargon from A into plain-language and the appropriate jargon in B. | "When a seismologist says 'noise,' what does an ecologist mean by it?" |
| **limitation-translation** | Given a known limitation of a method in A, what's the analogous limitation when the method is used in B? | "Vs30 has known limitations in linear-elastic site response — what limitations apply in the nonlinear (geotech) regime?" |
| **parameter-threshold-equivalence** | Given a parameter or threshold in A, what's the equivalent calibration/value in B? | "Earthquake stress drops are 1–10 MPa; what's the analogous magnitude scale in pore-pressure-driven failures?" |

**Why it's separate from `query_type`.** Query type describes the *interaction shape* (does the user ask for paper interpretation? a refusal? a joint-observation strategy?). Translation task type describes the *cognitive operation* the chatbot must perform. They're orthogonal: a single paper-interpretation QA can involve concept-mapping AND method-translation AND limitation-translation in its expected response. A single integration QA might be purely concept-mapping.

**Field**: `translation_task_types: List[str]`, 1–3 entries from the 7-item taxonomy. List is ordered by primary→secondary.

## Dimension 2: Tier (Bronze / Silver / Gold)

**What it is.** Three-level tier structure adapted from EarthSE's Iron/Silver/Gold framing. Anchored to *task complexity and required reasoning depth*, not just numeric difficulty.

**The 3 tiers.**

| Tier | Description | Typical numeric difficulty | Source-corpus notes |
|---|---|---|---|
| **bronze** | Simple within-discipline or simple-pair translations. Tests basic competence. | 1–2 | Textbook content; well-established review articles. |
| **silver** | Cross-group translations with modest complexity. Tests specialized knowledge + bridging. | 3–4 | Specialized papers in each subdomain. |
| **gold** | Advanced reasoning, multi-turn translation, novel methodological synthesis. | 4–5 | Top-cited compound-hazard papers showing cross-domain synergy. |

**Stratification target across the full 300-QA eval set**: roughly 50% bronze + 40% silver + 10% gold (parallel to EarthSE's 4133 : ~1500 : ~300 ratio for breadth-vs-depth).

**Why it's separate from `difficulty`.** Difficulty captures fine-grained variation within a tier (a moderately-hard bronze QA vs. an easy silver one). Tier captures the *kind* of cognitive demand. A bronze QA at difficulty 2 and a gold QA at difficulty 2 are testing different things — the bronze is testing basic competence; the gold is testing novel methodological synthesis with low complexity. Reviewers will score bronze and gold against the same rubric but with different expectations.

**Field**: `tier: Literal["bronze", "silver", "gold"]`.

## Dimension 3: Compound coupling

**What it is.** Explicit pairing of disciplines that the translation crosses. For single-discipline QAs, this is empty. For cross-discipline QAs, it's an ordered or unordered list of pairs (we use unordered for stratification).

**Format**: alphabetized within each pair so `"hydrology-seismology"` ≡ `"seismology-hydrology"` — canonical form is the alphabetized one. Example list (3-discipline QA spanning hydrology + seismology + geotechnical engineering): `["geotechnical_engineering-hydrology", "geotechnical_engineering-seismology", "hydrology-seismology"]`.

**Why it matters.** The publishable analysis the prior-art review recommends is "where is translation hardest, by coupling": e.g., seismic→hydrology might score 78%, seismic→atmosphere only 61%, suggesting timescale-mismatch is the dominant gap for atmospheric translations. This requires explicit coupling tagging on every cross-discipline QA.

**Stratification target** (recommended; matches the matrix in `docs/prior_art/benchmark_design_lessons_from_prior_art.md` §12):

| Coupling (canonical, alphabetized) | Target QA count |
|---|---|
| hydrology-seismology | 30 |
| geotechnical_engineering-seismology | 25 |
| geomorphology-seismology | 20 |
| atmospheric_sciences-hydrology | 25 |
| ecology-hydrology | 20 |
| agricultural_sciences-hydrology | 20 |
| geomorphology-hydrology | 25 |
| atmospheric_sciences-geomorphology | 15 |
| geotechnical_engineering-hydrology | 20 |
| (three-way couplings) | 10 |
| Single-discipline (no coupling) | 90 |
| **Total** | **300** |

Tolerance: ±5 per coupling.

**Field**: `compound_coupling: List[str]`. Empty list `[]` for single-discipline QAs.

## Dimension 4: Failure modes tested

**The headline new dimension.** Adapted from `docs/prior_art/REVISED_novelty_assessment_earthse_context.md` and `benchmark_design_lessons_from_prior_art.md` §10.

**What it is.** For each QA, identify which categorical failure modes the chatbot's response is being tested against. This is *what's being probed*, not *what reviewers score* — though the two are closely linked. At evaluation time, reviewers can score per-failure-mode (did the chatbot avoid this specific failure?). At dataset-level analysis, we can compute per-failure-mode accuracy across the eval set, which is the headline result.

**The 7 failure modes.**

| Failure mode | Definition | When to tag a QA with this |
|---|---|---|
| **hallucinated-analogue** | Chatbot invents a sensor/method/concept that doesn't exist (the canonical "fabrication" failure). | The QA's correct response requires NOT inventing something plausible-sounding. |
| **concept-confusion** | Chatbot misunderstands the role/function of the source concept (treats noise as signal-class-collision, treats stress drop as fault property). | The source concept has a specific functional role that's easy to misread. |
| **domain-ignorance** | Chatbot proposes something standard in the target domain but not actually applicable in this context. | The target-discipline-side answer needs domain-specific qualifications. |
| **implausible-calibration** | Right concept, wrong parameters / scale / timescale. | Numerical answer or quantitative comparison required. |
| **missing-constraint** | Chatbot ignores a key limitation or constraint of the target domain. | The right answer requires acknowledging a hard practical constraint. |
| **false-equivalence** | Chatbot oversimplifies a genuinely complex analogy or asserts equivalence where it doesn't hold. | The right answer requires a "*when the analogy holds / when it breaks*" structure. |
| **terminology-failure** | Correct concept but wrong jargon for the target domain. | Vocabulary collision or domain-specific terminology test. |

**Field**: `expected_output.failure_modes_tested: List[str]`, 1–4 entries. Most QAs probe 1–3 modes.

**Use in scoring** (per `eval_platform/` rubric mapping):

| Rubric criterion (existing) | Failure mode it most directly tests |
|---|---|
| S1 Technical accuracy | concept-confusion, implausible-calibration |
| S2 Citation discipline | hallucinated-analogue |
| S3 Vocabulary precision | terminology-failure |
| S4 Cross-discipline integration | false-equivalence, missing-constraint |
| S5 Refusal correctness | hallucinated-analogue, false-equivalence |
| S6 Completeness | domain-ignorance, missing-constraint |

This map lets us back out per-failure-mode performance from the per-criterion scores in the existing rubric, without having to invent a separate scoring instrument.

## The publishable analysis this dimensional framework unlocks

With the dimensions above on every QA, the methodology paper (Phase 8) can report:

1. **Overall accuracy** by tier (Bronze 72%, Silver 54%, Gold 38%) — shows the difficulty-stratified picture.
2. **Per-failure-mode performance** for base model and for skill-loaded augmented model (the headline):

   | Failure mode | Base model | Augmented | Δ |
   |---|---|---|---|
   | hallucinated-analogue | 40% | 42% | **+2%** ← augmentation doesn't fix |
   | missing-constraint | 45% | 68% | **+23%** ← augmentation works |
   | concept-confusion | 50% | 65% | +15% |
   | implausible-calibration | 38% | 59% | +21% |
   | false-equivalence | 52% | 68% | +16% |
   | terminology-failure | 60% | 75% | +15% |
   | domain-ignorance | 42% | 71% | **+29%** ← augmentation works hard |

   This is the publishable contribution: augmentation targets *constraint awareness* effectively but does *not* fix *fabrication*.

3. **Per-coupling performance**: seismic-hydro 78% vs. seismic-atm 61% reveals where translation is structurally hardest.

4. **Per-translation-task-type performance**: e.g., concept-mapping 70% vs. limitation-translation 42% reveals which cognitive operations are limiting.

5. **Per-tier × per-failure-mode matrix**: e.g., hallucinated-analogue is more common at the Bronze tier where the model "knows it should answer something" and less common at Gold where it might refuse more.

Together these are the **failure-mode taxonomy story** that makes the methodology paper publishable per the prior-art review.

## Connection to the existing per-section scoring

The existing 8-criterion rubric in `eval_platform/` is preserved. The new dimensions don't replace it; they *augment* it with additional metadata that lets us aggregate the per-section scores into per-failure-mode and per-task-type breakdowns.

Reviewers don't need to change how they score. The chatbot's output still goes through the rubric. What changes is the *aggregation*: instead of just averaging Technical Accuracy across all QAs, we can also break it down by failure-mode-tested, by tier, by coupling.

## Coverage targets summary (300-QA full set)

To make the analysis above statistically meaningful, the stratification matrix is:

- **Tier**: 150 bronze / 120 silver / 30 gold
- **Translation task types**: 50–60 QAs per task type (with overlap since each QA can have 1–3)
- **Compound coupling**: as in the table above
- **Failure modes**: 30–60 QAs per failure mode (with overlap; each QA tests 1–4)
- **Existing dimensions** (query_type, difficulty, discipline): as in `docs/eval_qa_schema.md` §4

A QA covers multiple cells: e.g., a single silver-tier concept-mapping QA on seismic-hydro coupling testing the missing-constraint and hallucinated-analogue failure modes contributes to four cells of the stratification, which means we don't need 300 × (4 + 7 + 7 + 10) cells of data — each QA earns multiple "ticks."

## Migration of the existing 21 seed QAs

All 21 seed QAs in `pipeline/seed_qa_dataset.py` need to have the four new fields added. This is done explicitly per-QA (no automated migration); each QA is hand-labeled with its translation task types, tier, compound coupling, and probed failure modes. The seed set is small enough (21) that this is half a day of work.

## Open questions for the lock-meeting

1. Should `compound_coupling` capture *ordered* pairs (e.g., `"seismology→hydrology"` directionality matters for translation direction) or *unordered*? **Resolved: unordered, alphabetized canonical form** (`"hydrology-seismology"`). The v3.1 schema and validator both enforce this — every QA must list its C(N,2) pairs in alphabetized form. Directionality can be revisited in a future schema version (v3.2+) if per-direction asymmetry turns out to be a useful analysis cut; for now `query_type` + `translation_task_types` carry the directional information.
2. Should the failure-mode list be considered exhaustive, or should we accommodate new modes as the eval reveals them? Recommendation: lock v3.1 with the 7 listed, then update to v3.2 if Phase 7 reveals a new pattern.
3. For the gold tier, do we adopt the EarthSE multi-turn-dialogue format (Turn 1 = problem, Turn 2 = critique, Turn 3 = refinement)? Recommendation: yes, but only after the single-shot Phase 4 tool is stable; multi-turn is a Phase 5-and-onward extension.

## Action items

1. ✅ Save prior art docs to `docs/prior_art/`.
2. ✅ Write this framework doc.
3. **Update `docs/eval_qa_schema.md`** to add the four new fields to the Pydantic schema, validation rules, and stratification targets.
4. **Update `docs/eval_qa_design.md`** to incorporate the failure-mode taxonomy and translation task types into the QA-author guide.
5. **Migrate the 21 seed QAs** in `pipeline/seed_qa_dataset.py` to include the new fields.
6. **Update `pipeline/validate_eval_set.py`** to validate the new fields and check the new stratification matrices.
7. **Update `pipeline/build_review_spreadsheet.py`** to surface the new dimensions as columns.
8. **Regenerate `eval_dataset/eval_dataset_v3.json` and the reviewer xlsx.**
9. **Update `README.md` and `docs/roadmap.md`** to reflect the failure-mode framing.

This update is happening before any further QA authoring proceeds, so that the full ~300-QA eval set is structured from the beginning around the failure-mode analysis that the methodology paper will report.
