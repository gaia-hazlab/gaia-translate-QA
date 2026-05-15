# Benchmark Design Lessons from EarthSE, K2, and Related Work
## What You Should Borrow and Adapt for Your Cross-Disciplinary Translation Benchmark

---

## 1. TASK DEFINITION FRAMEWORK (from EarthSE)

**EarthSE's approach:** They define **11 foundational task types** explicitly before building the dataset. Each paper is analyzed, and the most appropriate task type is assigned.

**Task types they use:**
- Understanding: term explanation, knowledge QA, fact verification
- Reasoning: analysis, relation extraction, calculation
- Research: tool utilization, literature citation, dataset recommendation, experimental design, code generation

**Why this matters for your work:**
EarthSE doesn't just throw diverse questions at papers — they operationalize what "scientific exploration" means as 11 distinct primitives. You should do the same for **cross-disciplinary translation**. 

**Your translation task types should be something like:**

1. **Concept Mapping** — Given a concept in Subdomain A (e.g., "fault rupture propagation" in seismology), define its functional equivalent in Subdomain B (hydrology: what's the analogue?)
2. **Method Translation** — Given a method from A (e.g., "moment tensor inversion"), describe how to operationalize the equivalent in B (hydrogeology: stress inversion from well-test analysis?)
3. **Sensor/Data Equivalence** — Given a sensor from A (seismometer), name and justify the instrument/data source in B (piezometer + water level time series?)
4. **Data Availability Assessment** — Given a problem in A, what datasets are readily available in B to tackle the same question?
5. **Terminology Bridging** — Translate jargon from A into plain-language and domain-specific jargon in B
6. **Limitation Translation** — Given a limitation of a method in A, what's the analogous limitation in B's context?
7. **Parameter/Threshold Equivalence** — If a method in A uses a specific threshold/parameter, what's the equivalent calibration in B?

**Action item:** Define 6–10 translation task types explicitly. Create a one-sentence definition + one worked example for each. This makes task assignment systematic, not intuitive.

---

## 2. MULTI-TIER DIFFICULTY ARCHITECTURE (from EarthSE)

**EarthSE's model:**
- **Earth-Iron:** 4,133 questions, broad coverage, from 100K papers (base corpus)
- **Earth-Silver:** harder, from curated high-impact journal papers (10K papers)
- **Earth-Gold:** advanced, from top 10% most-cited papers (1K papers), multi-turn dialogue format

The tiers serve different purposes:
- Iron = breadth + basic competence
- Silver = depth + specialized knowledge
- Gold = advanced reasoning + scientific discovery

**Why this matters for your work:**
Translation complexity has natural tiers. You can use this structure.

**Your potential tiers:**

1. **Bronze tier (easiest):** Simple within-group translations
   - Example: "You know seismology. A hydrologist uses 'drawdown' to mean water-level response in aquifers. What's the seismic analogue?"
   - Source corpus: introductory-level papers and well-known review articles
   - ~500-1000 items

2. **Silver tier (intermediate):** Cross-group translations with modest complexity
   - Example: "A seismologist measures 'rigidity' using seismic wave velocities. In the context of landslide risk, how would you operationalize an equivalent measure and what data would you use?"
   - Source: specialized papers in each subdomain
   - ~300-500 items

3. **Gold tier (advanced):** Multi-turn dialogue requiring methodological translation + innovation
   - Example: "A method from climate modeling (X) can inform seismic hazard assessment. Outline the method, identify limitations in the seismic context, propose a modification, and assess limitations of that modification."
   - Source: highly-cited papers showing cross-domain synergy
   - ~100-200 items

**Action item:** Decide on your tier structure and the corpus size per tier before annotation starts.

---

## 3. EXPERT VALIDATION WITH EXPLICIT RUBRICS (from EarthSE)

**EarthSE's approach:**
For their open-ended Earth-Gold benchmark, they use **two explicit evaluation criteria:**
1. **Information Density Scoring** — Higher scores for specific analytical methods, datasets, or well-defined events; lower for vague discussion
2. **Methodological Quality Assessment** — Proposed methods scored higher if systematically enumerated and concretely implementable

This is **not** "does it look good?" — it's operationalized scoring.

**Why this matters for your work:**
Translation quality is subjective but not infinitely variable. Experts disagree, but you can bound and measure that disagreement.

**Your rubric might include:**

1. **Accuracy of Functional Analogue** (0–5 points)
   - Does the proposed concept/method/sensor from B actually fulfill the role it plays in A?
   - Example: Is piezometer + water level truly analogous to seismometer for tracking crustal stress?

2. **Specificity and Detail** (0–5 points)
   - Does the translation include concrete parameters, datasets, instruments, or methods?
   - OR is it hand-wavy ("just use similar techniques")?

3. **Domain Appropriateness** (0–5 points)
   - Does the translation respect domain B's constraints, limitations, and typical practices?
   - Would an expert in B actually use this translation, or would they say "you don't understand how we work"?

4. **Honesty about Limitations** (0–5 points)
   - Does the translation acknowledge where the analogue breaks down?
   - Example: "Seismic velocity is analogous to pore-pressure sensitivity, but seismic sensors can't measure pressure directly — you'd infer it."

5. **Accessibility for Non-Expert** (0–5 points)
   - Could someone familiar with A but not B understand and follow this translation?

Total: 0–25 points per item, then normalize.

**Action item:** Draft a 5–7 point rubric. Share with 3–4 domain experts (seismologist, hydrologist, climatologist, geomorphologist) in **advance** of annotation to refine it. This is mandatory—do not skip.

---

## 4. INTER-ANNOTATOR AGREEMENT PROTOCOL (essential, and EarthSE underspecifies this)

**The gap:** EarthSE validates their open-ended dialogues with domain experts but does NOT report Cohen's κ, Fleiss' κ, Krippendorff's α, or any formal agreement statistic. This is a weakness reviewers will notice.

**What you must do:**
1. Have **minimum 2, ideally 3 independent experts** score each item (especially for Bronze tier where disagreement is lower, up to 4 for Gold tier)
2. Report **Krippendorff's α** for each task type (handles ordinal scales, missing data, multiple annotators)
3. Threshold: α ≥ 0.70 for retention in final benchmark; flag items with α = 0.50–0.70 for expert discussion
4. **Document all disputes:** If two experts score an item 5 and 2, report why. This becomes part of your quality narrative.

**Why κ matters:** A benchmark is only as trustworthy as the agreement that produced it. If κ = 0.65, reviewers will treat your benchmark with caution. If κ = 0.78, they'll trust it.

**Action item:** Decide on agreement thresholds NOW. Budget for 3 expert annotators per item, especially Gold tier.

---

## 5. NOVEL EVALUATION METRIC (from EarthSE's Scientific Exploration Score)

**EarthSE's innovation:**
For open-ended dialogues, they can't use accuracy. Instead, they create **Scientific Exploration Score (SES):**

SES = (retention rate) × (diversity)

- **Retention rate (r):** GPT-4 ranks M diverse LLM outputs vs. reference answer. r = (ranking_position - 1) / M. So if the reference is ranked 1st, r = 0 (bad). If it's ranked last, r = 1 (excellent).
- **Diversity (d):** Semantic similarity of all M outputs around their mean. Lower similarity = higher diversity. d = 1 / mean_cosine_similarity.
- **Multiplicative combination:** SES = r × d. Rewards both quality AND divergent thinking.

**Why this matters for your work:**
Translation quality can't be reduced to "right/wrong." You need a metric that captures:
- Whether the translation is actually good (retention)
- Whether the model can propose multiple valid translations (diversity)

**Your metric could be:**

**Translation Adequacy and Diversity Score (TADS):**

TADS = (fidelity × contextual_fit) / (redundancy)

Where:
- **Fidelity (0–1):** Preserves the functional role of the concept in the source domain
- **Contextual fit (0–1):** Respects domain B constraints, practices, and data availability
- **Redundancy penalty:** If M responses are generated, measure semantic diversity; high redundancy lowers the score

Or even simpler, adopt EarthSE's approach wholesale:
- Generate M=3 translations per item
- Human expert ranks them (with tiebreaker by second expert if needed)
- Compute retention and diversity, combine

**Action item:** Decide on your metric before evaluation. Don't wing it.

---

## 6. DATA CLEANING PIPELINE (from EarthSE)

**EarthSE's two-phase approach:**

1. **Phase 1: Rule-based primary cleaning**
   - Formatting issues (missing answer options, wrong reference format)
   - Structural errors (incomplete questions, garbled text)
   - ~5–10% of items typically fail here

2. **Phase 2: Semantic/LLM-based advanced cleaning**
   - Multiple correct answers (ambiguous questions)
   - Factually incorrect generated content (LLM hallucinations)
   - Irrelevant or nonsensical questions
   - Use CoT reasoning as ground truth for error detection

**Then:** Difficulty filtering. Remove questions where LLMs achieve >80% accuracy (too easy). For 60–80% accuracy, have humans decide (value-dependent).

**Why this matters for your work:**
LLM-generated translation items will have errors. You need a systematic way to find them.

**Your pipeline:**

1. **Rule-based (immediate rejection):**
   - Missing required sections (source concept, target domain, rubric-scorable response)
   - Obvious grammar/formatting errors that impede understanding
   - Duplicates or near-duplicates

2. **Expert review (Phase 2):**
   - Expert looks at LLM-generated translation and judges: "Is this a plausible translation that I would teach to someone?"
   - If no → reject
   - If yes → retain for annotation
   - Document rejection reasons (hallucination, domain misunderstanding, implausible)

3. **Difficulty filter (optional):**
   - Run zero-shot base model on bronze tier
   - Remove items where it scores ≥0.85 (ceiling effect)
   - This is less critical for translation (inherently harder) but still useful

**Action item:** Write down your cleaning pipeline rules before generating items. Test on a small pilot set (50 items) first.

---

## 7. TASK SELECTION AND ASSIGNMENT (from EarthSE)

**EarthSE's approach:**
Before generating a question, a small LLM reads the paper and selects the most suitable task type from the 11 predefined types. This **increases relevance** — calculation questions come from papers with numbers, code generation from methods papers, etc.

**Why this matters for your work:**
You don't want random translation prompts. Some compounds (seismic + hydrologic) are naturally rich for translation; others less so.

**Your workflow:**
1. Identify candidate papers that naturally involve multiple subdomains (GAIA compound geohazard papers are perfect)
2. For each paper, **explicitly classify which translation task types it supports**
   - Example: "This paper on earthquake-triggered landslides supports: Concept Mapping (stress transfer), Method Translation (ground motion → slope instability), Limitation Translation (earthquake forecasting limitations → landslide prediction)"
3. Generate the most appropriate translation prompts, not all 6–10 types per paper
4. This ensures high-quality item-to-topic matching

**Action item:** Before annotation, hand-code 20 papers and label which translation task types each naturally supports. Use this to refine your task typology.

---

## 8. CHAIN-OF-THOUGHT AS GROUND TRUTH (from EarthSE)

**EarthSE's insight:**
When they generate QA pairs with GPT-4, they require CoT reasoning: the model must show step-by-step derivation, not just the answer. This CoT becomes the ground truth for later validation.

**Why:** If the CoT is nonsensical, you know the question is bad. If the CoT is sound, you trust the answer even if it's long or complex.

**Your equivalent:**
When you (or an LLM) generate a translation, include a **justification component:**

> Q: "Seismometer → ??? in hydrology for measuring aquifer stress response"
>
> A: **Translation:** Piezometer + water level logger
>
> **Justification:** 
> - Seismometers measure ground acceleration (indirect stress/strain sensing)
> - Piezometers measure pore pressure directly; water level changes indicate aquifer stress response
> - Both provide time-series data of subsurface response to forcing (earthquakes vs. recharge)
> - Limitation: seismic sensors are orders of magnitude more sensitive; piezometer networks are sparser

The justification is what experts will score, not just the one-liner answer.

**Action item:** Structure your benchmark items as `[Question] → [Translation] → [Justification]`. Train expert annotators to score justifications, not bare answers.

---

## 9. OPEN-ENDED DIALOGUE FOR ADVANCED TIER (from EarthSE)

**EarthSE's Earth-Gold design:**
Multi-turn dialogue following a specific pattern:

1. **Turn 1:** "Given existing method M0 in domain A with limitations L0, what's the adapted method in domain B?"
2. **Turn 2:** "Now that you've proposed M1, what are its limitations in the B context (L1)?"
3. Optional Turn 3: "How would you modify M1 to address L1?"

This **mirrors the scientific process** — problem → solution → critique → refinement.

**Why this matters for your work:**
Translation is iterative. A good benchmark should capture that.

**Your dialogue structure might be:**

1. **Turn 1 (Context + Challenge):**
   - "Compound geohazard setting: Earthquakes can trigger landslides. In seismology, you characterize earthquake severity with moment magnitude. In geomorphology, landslide susceptibility is driven by slope stability (friction angle, cohesion). How would you translate 'moment magnitude' into a metric that predicts landslide triggering in your field?"

2. **Turn 2 (Critique):**
   - "Now propose a method combining your translated metric with geomorphic data. What are the limitations of this integrated approach?"

3. **Turn 3 (Refinement, optional):**
   - "How would you modify your approach to account for [specific complexity, e.g., seasonal pore pressure]?"

**Action item:** Design a 2–3 turn dialogue template for Gold tier. Test it on 5–10 expert annotators in a pilot phase.

---

## 10. FAILURE-MODE TAXONOMY (your innovation, not in EarthSE but essential)

**The gap:** EarthSE reports aggregate performance but doesn't systematically categorize where and why models fail.

**You should go further.** After evaluation, classify each failure into categories:

1. **Hallucinated Analogue** — Model invents a sensor/method that doesn't exist
2. **Concept Confusion** — Misunderstands the role of the source concept
3. **Domain Ignorance** — Proposes something standard in the target domain but not actually applicable
4. **Implausible Calibration** — Correct concept but wrong parameters/scale/timescale
5. **Missing Constraint** — Ignores a key limitation of the target domain
6. **False Equivalence** — Oversimplifies a genuinely complex analogy
7. **Terminology Failure** — Uses correct concept but wrong jargon for the target domain

**Why this matters:**
This becomes your **contribution narrative.** Instead of "LLMs score X% on translation," you can say "LLMs excel at identifying functional analogues (77% correct) but struggle with domain-specific constraints (41% correct), particularly in compound systems where feedback loops matter."

**Action item:** After you run a pilot, code 100 responses manually and build a failure taxonomy. Publish this as part of your paper.

---

## 11. EXPERT RECRUITMENT AND TRAINING (implicit in K2, critical for you)

**K2's approach:**
They recruit geoscientists to verify generated Q&A pairs and validate proposed translations. But they don't detail training or disagreement resolution.

**You must be explicit about:**

1. **Expert selection:**
   - You need 3–4 experts across subdomains (1–2 seismologists, 1 hydrologist, 1 climate/atmosphere person, maybe 1 geomorphologist)
   - Each should have 10+ years in their field
   - Ideally, at least one has done transdisciplinary/compound-hazard work

2. **Expert training (critical):**
   - 2–3 hour workshop where you:
     - Explain the translation task definition and rubric
     - Walk through 5–10 worked examples (both good and bad)
     - Discuss what "domain-appropriate" means (not just linguistically correct, but operationally sound)
     - Establish disagreement resolution protocol (e.g., "if 2 of 3 experts score within 2 points, keep the item; otherwise discuss")

3. **Calibration phase:**
   - Have all experts independently score the same 30–50 pilot items
   - Compute κ
   - If κ < 0.65, repeat training or refine rubric
   - If κ > 0.70, proceed to full annotation

**Action item:** Budget for expert time. 3 experts × 2 hours training + 3 experts × ~20 hours annotation (if Bronze tier is 1000 items) = ~70 person-hours. Compensate appropriately.

---

## 12. DATASET SCALE AND STRATIFICATION (from EarthSE + practical advice)

**EarthSE's scale:**
- Earth-Iron: 4,133 items
- Earth-Silver: ~1,500 items  
- Earth-Gold: ~300 multi-turn dialogues

For a geoscience methods paper, you probably don't need EarthSE's scale. Smaller, expert-curated benchmarks are respected in this field.

**Realistic target for you:**
- **Bronze tier:** 300–500 items (covers core translation types, broad coverage)
- **Silver tier:** 150–250 items (specialized, harder)
- **Gold tier:** 50–100 multi-turn dialogues (advanced, time-intensive)

**Why smaller is OK for geoscience:**
- You're not training a model (which needs 10k+ items)
- You're evaluating translation quality, which benefits from **depth over breadth**
- Expert-curated benchmarks (GPQA, MATH, HumanEval in CS) are often 300–2000 items and highly respected

**Stratification (critical):**
Make sure your Bronze tier covers:
- All major translation task types evenly (if you have 7 types, each should be ~40–70 items)
- All major compound-hazard couplings (seismic-hydrologic, seismic-geomorphic, hydrologic-climate, etc.)

Compute a stratification matrix before annotation:

| Task Type | Seismic-Hydro | Seismic-Geo | Hydro-Climate | Hydro-Geo | Total |
|-----------|---------------|-------------|---------------|-----------|-------|
| Concept Mapping | 40 | 40 | 30 | 30 | 140 |
| Method Translation | 35 | 35 | 25 | 25 | 120 |
| Sensor Equiv. | 40 | 35 | 20 | 25 | 120 |
| ... | ... | ... | ... | ... | ... |
| **Total** | **200** | **180** | **150** | **150** | **500** |

This ensures no subdomain or task type is accidentally underrepresented.

**Action item:** Define your target scale and stratification matrix before annotation.

---

## SUMMARY: YOUR BENCHMARK ROADMAP

### Phase 1: Design (2–3 weeks)
- [ ] Define 6–10 translation task types with examples
- [ ] Draft evaluation rubric (5–7 dimensions)
- [ ] Design corpus collection strategy (GAIA papers, other compound-hazard literature)
- [ ] Compute stratification matrix (task types × compound couplings)
- [ ] Recruit 3–4 domain experts
- [ ] Create expert training materials with 10+ worked examples

### Phase 2: Pilot (2–3 weeks)
- [ ] Generate 50–100 items for pilot annotation
- [ ] Run expert training + calibration phase
- [ ] Compute inter-annotator κ; refine rubric if κ < 0.65
- [ ] Test data cleaning pipeline on pilot set
- [ ] Document any task type issues or expert feedback

### Phase 3: Full annotation (4–6 weeks, depending on scale)
- [ ] Generate full Bronze + Silver + Gold corpus
- [ ] Clean and validate with rule-based + expert review
- [ ] Final expert annotation with agreement tracking
- [ ] Compute per-task-type κ and report

### Phase 4: Evaluation + Analysis (2–3 weeks)
- [ ] Run baseline (zero-shot base model, base + skill file, maybe RAG variant)
- [ ] Compute benchmark difficulty distribution
- [ ] Build failure-mode taxonomy from error analysis
- [ ] Write results section + discussion

**Total timeline:** ~3–4 months for a solid, publishable benchmark

---

## SPECIFIC PAPERS TO READ IN FULL

1. **EarthSE (arXiv:2505.17139)** — Read sections 3.1–3.4 on benchmark construction, data cleaning, and validation
2. **K2 (arXiv:2306.05064)** — Read section 3.2 on instruction tuning data design and expert alignment
3. **HydroLLM-Benchmark** (Environmental Data Science, 2025) — Once you can access it, focus on their rubric design for domain-specific QA

---

## RED FLAGS TO AVOID

1. ❌ **Single expert validation** — You need minimum 2, preferably 3, with reported κ
2. ❌ **No rubric, just "does it look good?"** — Operationalize your scoring
3. ❌ **Baseline-free evaluation** — Include zero-shot + at least one augmented variant
4. ❌ **Aggregate metrics only** — Break down by task type and compound coupling; report failure modes
5. ❌ **No difficulty filtering** — Remove ceiling and floor items
6. ❌ **Vague task definitions** — Each task type needs a one-sentence definition + concrete example
7. ❌ **Undersized benchmark for a "short note"** — 300–500 items is fine, but don't claim generalizability on 50
8. ❌ **Dismissing prior art** — Cite EarthSE, K2, HydroLLM, GeoBench explicitly; explain how yours is different (translation focus, not knowledge-QA)

