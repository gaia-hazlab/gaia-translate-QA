# Eval QA design guidelines (v3.1 — post-prior-art-revision)

How to write a good v3 eval QA. Companion to `docs/eval_qa_schema.md` (the formal spec), `docs/eval_dimensions_framework.md` (the new dimensional framework), `docs/prior_art/` (the EarthSE-derived analyses that motivated the revision), and `eval_platform/calibration_qas/calibration_set_v1.md` (3 worked examples).

This document is the operational guide for QA authors — Marine, collaborators, Claude-drafted-then-edited. Read once before writing your first batch; refer back when stuck on a specific QA.

**What changed in v3.1**: Four new dimensions to tag on every QA — `translation_task_types`, `tier`, `compound_coupling`, and `expected_output.failure_modes_tested`. The failure-mode taxonomy is the headline addition; tagging it on every QA at design time is what enables the methodology paper's publishable per-failure-mode analysis.

---

## 1. What makes a good QA, in one sentence

**A real research question a real researcher would ask, with a clearly definable expected response that distinguishes a good chatbot from a fabricating one.**

Three implications:

- **Real research questions, not contrived tests.** "Tell me about X" is a bad QA; "I'm reading a paper on X and don't understand how Y connects to my work on Z" is a good QA.
- **The expected response must be specifiable in advance.** If you can't write `expected_output.user_specific_response_themes` for a question, the question is too vague.
- **The QA should distinguish good from fabricating.** If a hallucinating chatbot could fluently answer in a way that looks plausible to a non-specialist, the QA isn't doing the work. Good QAs surface citation-discipline, vocabulary precision, and refusal-correctness — the failure modes that matter.

---

## 2. The five query types

Each type has a distinct shape. Mixing types within a single QA is fine but the dominant type goes in `query_type`.

### Paper-interpretation (40% of the eval set)

**Shape**: "I just read [paper]. What should I take away?" or "Help me interpret this PDF as a [discipline] researcher."

**Inputs**: prompt + an actual document (PDF or URL). The document context is what makes this query type distinct.

**Expected output**:
- High `concept_matches` count — the chatbot should identify the variables and equations the paper uses.
- High `method_matches` count — the methods the paper relies on.
- 1–3 `phenomenon_matches` — the phenomena the paper studies.
- 1–3 `translation_matches` — cross-discipline bridges the chatbot should surface for the reader.
- `user_specific_response_themes` should match what the reader's discipline would care about, often emphasizing what the paper *doesn't* address.

**Common failure modes**: chatbot summarizes the paper without translating; chatbot misses the cross-discipline bridges; chatbot fabricates references not in the paper.

**Example**: QA-CAL-01 (Nisqually liquefaction; see `eval_platform/calibration_qas/`).

### Integration (25% of the eval set)

**Shape**: "How does my work on X connect to discipline Y?"

**Inputs**: prompt only; the document is `type: none`.

**Expected output**:
- `translation_matches` is the heaviest — the bridges between the two disciplines.
- `concept_matches` from both source and target discipline.
- `user_specific_response_themes` should hit: shared structure, X-side instantiation, Y-side instantiation, when the analogy holds, when it breaks, recommended next step.

**Common failure modes**: chatbot finds surface analogies that don't survive scrutiny (the agent_playbook's refusal patterns target this); chatbot misses real bridges that exist (`TC-01` through `TC-19`).

**Example**: "How does my hydrology work on aquifer depletion connect to seismology?"

### Vocabulary disambiguation (15% of the eval set)

**Shape**: "What does [polysemous term] mean in [discipline]?" or "I'm confused — does X in field A mean the same as X in field B?"

**Inputs**: prompt; document optional.

**Expected output**:
- `vocabulary_collisions_flagged` populated with the term.
- `concept_matches` covering each discipline's meaning.
- `user_specific_response_themes` should distinguish the meanings clearly; may invoke a refusal if the user is asking for a bridge between them.

**Common failure modes**: chatbot picks one meaning without flagging the ambiguity; chatbot conflates the meanings.

**Example**: QA-CAL-02 (seismic Q vs. streamflow Q).

### Refusal-test (10% of the eval set)

**Shape**: a question designed to elicit a refusal — vocabulary collision, forced analogy, fabrication temptation, outside-grounded-knowledge.

**Inputs**: prompt; document optional.

**Expected output**:
- `refusals_or_caveats_expected` populated with the expected refusal type(s).
- `must_not_say` populated with the forbidden response (e.g., "fabricated citation," "asserted equivalence between G-R and flood-frequency power laws").
- `user_specific_response_themes` should explain *why* the refusal applies + offer a constructive alternative.

**Common failure modes**: chatbot answers anyway with fluent-sounding wrongness; chatbot refuses without offering an alternative.

**Example**: QA-CAL-02 has both refusal and vocabulary disambiguation aspects.

### Joint-observation (10% of the eval set)

**Shape**: "Can I jointly observe / invert X (from method A) and Y (from method B)?"

**Inputs**: prompt; document optional.

**Expected output**:
- `method_matches` covering both observational methods.
- `translation_matches` — usually `TC-08` (joint geophysical inversion) or `TC-09` (source identification).
- `user_specific_response_themes` should hit: shared physical model, what each observation constrains, existing joint-inversion frameworks, critical caveats.

**Common failure modes**: chatbot endorses a joint inversion that the physics doesn't actually support; chatbot misses petrophysical coupling constraints.

**Example**: QA-CAL-03 (Central Valley dv/v as hydrology product).

---

## 2.5. Translation task types (NEW in v3.1) — what cognitive operation is the chatbot doing?

Independent of `query_type` (which describes the interaction shape), each QA has 1–3 `translation_task_types` describing the **cognitive operation** the chatbot must perform:

- **concept-mapping** — find the functional analogue of a concept in another discipline.
- **method-translation** — operationalize a method's equivalent in another discipline.
- **sensor-data-equivalence** — name the equivalent instrument or data source.
- **data-availability-assessment** — what datasets in B are accessible for a question from A?
- **terminology-bridging** — translate jargon between disciplines (closely linked to vocabulary-disambiguation query type).
- **limitation-translation** — what's the analogous limitation in B for a method's limitation in A?
- **parameter-threshold-equivalence** — what's the equivalent calibration / parameter / threshold in B?

**Most paper-interpretation QAs** involve 2–3 task types (concept-mapping + method-translation + limitation-translation is a common combo).

**Single-discipline QAs** often have one task type (concept-mapping with no cross-discipline target). A refusal-test on vocabulary collision is purely terminology-bridging.

## 2.6. Tier (NEW in v3.1) — what KIND of cognitive demand?

Bronze / silver / gold, distinct from numeric difficulty:

- **bronze** — simple, within-group or straightforward cross-discipline. The model should mostly get this right. Used to anchor floor performance.
- **silver** — cross-group with modest complexity. The model should get this with effort. Used to differentiate models.
- **gold** — advanced methodological synthesis, often multi-step reasoning. The model should struggle. Used to test ceiling and to surface failure-mode differences.

Approximate mapping: bronze ↔ difficulty 1–2; silver ↔ difficulty 3–4; gold ↔ difficulty 4–5. But difficulty captures within-tier variation: a moderately-hard bronze (difficulty 2) and an easy silver (difficulty 3) are testing different things even though their numeric distance is small.

## 2.7. Compound coupling (NEW in v3.1) — explicit pair tagging

For cross-discipline QAs, the `compound_coupling` field lists discipline-pair couplings the translation crosses, alphabetized within each pair (canonical form). Example: `["geotechnical_engineering-seismology", "hydrology-seismology"]`.

- Single-discipline QAs: empty list `[]`.
- A QA that spans seismology + hydrology + geotech has THREE couplings (each pair counted): `["geotechnical_engineering-hydrology", "geotechnical_engineering-seismology", "hydrology-seismology"]`.

Stratification target: ~20–30 QAs per major coupling (see `docs/eval_dimensions_framework.md` §3). Plus 90 single-discipline QAs.

## 2.8. Failure modes tested (NEW in v3.1) — the headline dimension

Per-QA tagging of which of the 7 failure modes the QA probes. This is the publishable contribution: at analysis time, we compute per-failure-mode accuracy for base model vs. augmented model, showing *where* domain calibration helps and where it doesn't.

The 7 modes:

- **hallucinated-analogue** — chatbot invents a sensor/method/concept that doesn't exist.
- **concept-confusion** — misreads the functional role of the source concept.
- **domain-ignorance** — proposes something standard but not applicable in this context.
- **implausible-calibration** — right concept, wrong parameters/scale/timescale.
- **missing-constraint** — ignores a key target-domain constraint.
- **false-equivalence** — oversimplifies a complex analogy.
- **terminology-failure** — correct concept, wrong target-domain jargon.

**How to tag a QA with failure modes** (1–4 modes per QA, ordered primary→secondary):

- Ask: "If the chatbot were going to *fail* on this question, what category of failure would it be?"
- A refusal-test QA on the Q-Q vocabulary collision probes: hallucinated-analogue (it might invent a paper), false-equivalence (it might assert a relation), terminology-failure (it might pick the wrong meaning).
- A paper-interpretation QA on Boulanger & Idriss probes: missing-constraint (it might miss the Vs1 upper-30-m limitation), implausible-calibration (it might quote wrong CSR values), false-equivalence (it might conflate dv/v with pre-event triggering).
- A vocabulary-disambiguation QA on "permeability" probes: terminology-failure, concept-confusion.

**Don't over-tag**: 1–3 modes is typical. If you tag 5+, you're probably not focusing the test.

**Coverage target**: each failure mode should appear in 30–60 QAs across the full eval set.

## 3. Difficulty calibration

The `difficulty` field is 1–5. Use this rubric:

- **1 — trivial**: a textbook definition or a one-line lookup. Useful for floor-setting; reviewers should give 5 on every criterion.
- **2 — easy**: a single-discipline question that any specialist can answer; tests basic technical accuracy and citation discipline. Reviewers should give 4–5.
- **3 — median**: a typical graduate-student question; the question many real researchers would ask. Most production QAs sit at 3. Reviewers should give 3–4 if the chatbot is good.
- **4 — hard**: cross-discipline integration with multiple bridges and real failure modes; tests cross-discipline integration and refusal correctness. Reviewers should give 2–4 with high spread.
- **5 — frontier**: questions at the active research edge; ambiguous-on-purpose. Tests refusal correctness and honest uncertainty. Reviewers should give a wide range.

Distribution target: 30 / 60 / 120 / 60 / 30 (i.e., median-heavy with informative tails).

---

## 4. Writing the `expected_output` block — practical rules

### `concept_matches`, `method_matches`, `phenomenon_matches`, `translation_matches`

- **List card IDs in order of relevance**, most relevant first.
- For paper-interpretation QAs, aim for 4–8 cards across all four categories.
- For integration QAs, aim for 3–6 with `translation_matches` being the heaviest.
- For vocabulary-disambiguation QAs, aim for 2–4 (just the conflicting cards).
- For refusal-test QAs, aim for 2–4.
- For joint-observation QAs, aim for 4–6 spread across method and translation.
- **Do not over-stuff**. If you list 15 cards as "expected," reviewers will score the chatbot's precision low if it only matches 5 of them; that punishes the chatbot for *your* over-specification.

### `vocabulary_collisions_flagged`

- List terms from the agent_playbook vocabulary table that *appear in the prompt or expected response* and are polysemous.
- Empty for queries that don't touch a polysemous term.
- A vocabulary-disambiguation QA must have at least one entry.

### `refusals_or_caveats_expected`

- Empty for most QAs.
- A refusal-test QA must have at least one entry.
- For forced-analogy refusals, use `forced-analogy` + the specific subtype if applicable (`surface-power-law-collision` for G-R vs. flood-frequency).
- For "outside grounded knowledge" — use sparingly; only for QAs that genuinely require admitting the chatbot can't answer.

### `user_specific_response_themes`

- **The most important field for scoring.** Reviewers use this to score Completeness.
- **3–6 themes per QA**. Each theme is one sentence; the chatbot's response should hit each.
- **Be specific**: "explains why dv/v cannot replace wells in the Central Valley" not "discusses dv/v limitations."
- **Cover the question, not the topic**. If the prompt asks "should I deploy seismic arrays in the Central Valley?", a theme should be "answers the should-I question," not "explains seismic arrays."

### `must_not_say`

- **Phrases that would be hard-fails.** Examples:
  - "Smith et al. 2019 in *Journal of Hydrological Geophysics*" (a fabricated citation)
  - "Stream power and stress drop are mathematically equivalent" (a forced analogy)
  - "ARs are entirely driven by Pacific Decadal Oscillation" (a wrong attribution)
- 0–3 entries typical. Refusal-test QAs often have 2–3.
- **Do not list correct claims** — `must_not_say` is for the wrong-or-forbidden, not the alternatives.

---

## 5. Author-mix policy

The methodology paper (Phase 8) will report what fraction of the eval set was hand-drafted vs. LLM-drafted-then-edited. The target mix is ~40% hand, ~60% LLM+edit. Why both:

- **Hand-drafted** QAs preserve authentic researcher framings — questions from real conversations and papers Marine sees in her own work and at GAIA HazLab meetings.
- **LLM-drafted-then-edited** QAs scale the corpus without producing 300 questions that all sound like Marine wrote them. The LLM-drafter (`pipeline/generate_eval_dataset.py`) takes a discipline + query type + difficulty target and produces a candidate; the human edits before approval.

In `quality_notes.author`, attribute clearly:

- `"Marine"` — Marine wrote this.
- `"Claude+Marine-edit"` — Claude drafted, Marine reviewed and edited.
- `"Derek+Marine-review"` — Derek wrote, Marine reviewed.
- `"Collaborator: Jane Doe (UW ESS PhD)"` — external collaborator wrote it.

---

## 6. Quality bar — when is a QA ready to mark `approved`?

A QA goes from `draft` → `reviewed` → `approved` (or `deprecated`) through the curation workflow. The bar to mark a QA `approved`:

- [ ] Schema-validates against `EvalQA` Pydantic model.
- [ ] Prompt is a real research question (not a contrived test).
- [ ] `expected_output.user_specific_response_themes` has 3–6 specific themes.
- [ ] All card IDs in `*_matches` resolve to defined v3 cards (the validator checks).
- [ ] Difficulty rating has been calibrated against the rubric in Section 3.
- [ ] If a document is provided (`input_document.type != "none"`), it's accessible and renders correctly.
- [ ] At least one human (not the original author) has reviewed it.
- [ ] No QA-CAL- or QA-HELDOUT- ID overlap with the calibration / held-out subsets.

The validator (`pipeline/validate_eval_set.py`) checks the first three programmatically; the rest are human judgments tracked in `quality_notes`.

---

## 7. Common pitfalls (avoid these)

- **Over-specifying the expected output**. Listing 15 cards as `expected concept_matches` punishes the chatbot for under-specifying. Be realistic.
- **Themes that are about the topic, not the question**. "Discusses dv/v" is bad; "Explains why dv/v alone can't replace a well network in the Central Valley" is good.
- **QAs that confuse the chatbot's role with a textbook**. The chatbot translates between disciplines and helps researchers integrate. It is *not* a substitute for reading the paper. Don't ask "summarize this paper" — ask "what should I as a [discipline] researcher take from this paper?"
- **Difficulty inflation**. Most QAs are difficulty 3, not 5. If you find yourself rating most of your draft QAs 4–5, your bar is wrong; recalibrate against the median graduate student.
- **Forgetting refusal QAs**. The refusal-test category is small (10%) but the most important for the methodology paper's contribution. Don't skip it.
- **Citations in `must_not_say` without justification**. If you list a citation as forbidden, explain why in `quality_notes.review_notes` (so a future reviewer understands).

---

## 8. The "starting from a paper" workflow

Most paper-interpretation QAs start from a paper you've actually read. Workflow:

1. Pick a paper that you'd give to a colleague from a different discipline.
2. Note: which cards in our v3 corpus would the agent need to retrieve to make sense of it?
3. Frame the prompt as if a researcher in your discipline is reading it: "I'm a [discipline] researcher; I just read [author year]. What should I take away?"
4. Write the expected output: which cards (3–8 total), what cross-discipline integration is missed by the paper, what's the most-useful next step.
5. Difficulty: typically 3 (median) for an average paper; bump to 4 if the paper itself is complex or unusually cross-disciplinary.

Use real papers wherever possible. Real prompts → real expected outputs → meaningful evaluations.

---

## 9. The LLM-drafter workflow

When using `pipeline/generate_eval_dataset.py`:

1. Specify the constraints: discipline (or cross-discipline), query type, difficulty.
2. The script invokes Claude with the corpus loaded + a system prompt asking for a candidate QA in the v3 schema.
3. Review the output: does the prompt sound like a real researcher? Is `expected_output` specific enough? Are the cards correctly identified?
4. Edit aggressively. The LLM tends to over-stuff `expected_output` and over-rate `difficulty`. Trim and recalibrate.
5. Mark `author: "Claude+<your-name>-edit"` to attribute correctly.

About 1 in 3 LLM drafts will be acceptable with minimal edits; the others need more work or should be discarded.

---

## 10. Reviewing existing v2 QAs for migration

The 60 v2 QAs in `eval_dataset_v2.json` (and `pipeline/additional_seed_qas.py`) have a different schema. Migration:

1. v2's `question` → v3's `prompt`.
2. v2's `golden_answer` (a free-form paragraph) → v3's `user_specific_response_themes` (a 3–6-bullet decomposition).
3. v2's `key_references` → cross-check against the v3 corpus; identify which cards the references appear in.
4. v2's `type` (e.g., "concept_translation", "phenomenon_multi_lens") → v3's `query_type` (closest match).
5. v2's `difficulty` string → v3's integer 1–5.

Migration is iterative. Don't migrate all 60 in one pass; pick the strongest 20–30 and do them carefully.

---

## 11. Quick checklist for the QA author (v3.1)

Before saving a new QA:

- [ ] `id` follows pattern `QA-EVAL-###` (or `QA-CAL-###` for calibration, `QA-HELDOUT-###` for held-out).
- [ ] `primary_disciplines` is correct (1 for single-disc, 2+ for cross-disc).
- [ ] `query_type` matches the QA's interaction shape.
- [ ] **`translation_task_types`** lists 1–3 cognitive translation operations (NEW v3.1).
- [ ] **`tier`** is `bronze` / `silver` / `gold` (NEW v3.1; aligned with difficulty).
- [ ] **`compound_coupling`** lists discipline pairs in alphabetical-within-pair canonical form (NEW v3.1; empty for single-disc QAs).
- [ ] `difficulty` is calibrated to the rubric in Section 3.
- [ ] `prompt` reads like a real researcher's question.
- [ ] `input_document` is `type: none` unless you have a real document to attach.
- [ ] `expected_output.*_matches` lists real, defined v3 card IDs in order of relevance.
- [ ] `expected_output.user_specific_response_themes` has 3–6 specific themes.
- [ ] `expected_output.must_not_say` populated for refusal-test QAs; empty otherwise.
- [ ] **`expected_output.failure_modes_tested`** lists 1–4 failure modes this QA probes (NEW v3.1; the headline field — see Section 2.8).
- [ ] `quality_notes.author` attributes correctly.
- [ ] `status` set to `draft` (the validator will not let `approved` slip through without review).
