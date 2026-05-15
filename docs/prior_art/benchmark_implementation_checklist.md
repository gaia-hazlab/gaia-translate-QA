# Quick-Start Checklist: Build Your Benchmark in 3 Months

Use this as your project checklist. Check items off as you complete them. Print and pin it.

---

## PHASE 1: DESIGN & SETUP (Target: end of Week 3)

### Task Definition
- [ ] **List 6–10 translation task types** (e.g., Concept Mapping, Method Translation, Sensor Equiv.)
  - Where: Draft Google Doc or Markdown file
  - Format: One-liner + example for each
  - Example: "Concept Mapping: 'Fault rupture velocity (seis) → ?' (hydro) Define functional analogue and justify"
  - Deadline: Week 1 end
  
- [ ] **Get feedback from domain experts** (quick email/chat, 15 min per person)
  - Ask: "Do these task types cover the translation space you care about?"
  - Ask: "Anything missing or redundant?"
  - Deadline: Week 1 end

- [ ] **Refine task definitions based on feedback**
  - Deadline: Week 2 mid

### Rubric Design
- [ ] **Draft a 5–7 point rubric** with explicit scoring criteria
  - Dimensions: Functional Accuracy, Domain Fit, Specificity, Limitation Honesty, Usability, (others?)
  - Each dimension: 0–5 point scale with clear descriptors
  - Where: Create a Google Doc rubric with examples
  - Deadline: Week 2 start
  
- [ ] **Share rubric with 2–3 domain experts for feedback**
  - Ask: "Is this scorable? Do you understand what each point means?"
  - Ask: "Should we weight certain dimensions?"
  - Deadline: Week 2 end

- [ ] **Finalize rubric**
  - Document any disagreements (expert A wanted to weight Accuracy higher; decision: equal weights pending pilot)
  - Deadline: Week 2 end

### Corpus Strategy
- [ ] **Identify candidate papers**
  - Strategy: Search "compound geohazard," "earthquake AND landslide," "seismic AND hydrologic," etc.
  - Target: 30–50 recent papers that naturally involve ≥2 subdomains
  - Tool: Google Scholar, EarthArXiv, AGU GeoRefs, EGU preprints
  - Store as: BibTeX file + folder with PDFs
  - Deadline: Week 2 end

- [ ] **Hand-code 20 papers for natural task-type coverage**
  - For each paper, label: "Concept Mapping? Yes/No. Method Translation? Yes/No..." etc.
  - Find papers that support diversity of task types
  - Use this to refine corpus
  - Deadline: Week 2 end / Week 3 start

- [ ] **Design stratification matrix**
  - Rows: task types; Columns: compound couplings (seismic-hydro, seismic-geo, etc.)
  - Fill with target counts (e.g., 40 Concept Mapping items in seismic-hydro tier)
  - Use this as a guide for item generation
  - Deadline: Week 3 start

### Expert Recruitment
- [ ] **Identify and recruit 3–4 domain experts**
  - Ideal: 1–2 seismologists, 1 hydrologist, 1 climate/atmosphere scientist
  - Ideally with transdisciplinary/compound-hazard experience
  - Contact now with: "We're building a cross-disciplinary translation benchmark for LLMs. We need expert input. ~25–30 hours over 2 months. Can you help?"
  - Deadline: Week 1 end (start now!)

- [ ] **Confirm expert availability and scheduling**
  - Schedule 2-hour training session for Week 4
  - Deadline: Week 2 end

---

## PHASE 2: PILOT & CALIBRATION (Target: end of Week 5)

### Pilot Item Generation
- [ ] **Generate 50–80 pilot items** covering all task types
  - Method: LLM prompt (GPT-4 or Claude) to generate translations given source concept
  - Include justification component (your CoT equivalent)
  - Store as: CSV or JSON with columns: [source_concept, source_domain, target_domain, task_type, translation_prompt, llm_output, justification]
  - Deadline: Week 3 end

- [ ] **Quick expert review of pilot items** (feedback only, not scoring yet)
  - Share 10–15 items with each expert
  - Ask: "Do these items make sense? Are they answerable in your domain? Any nonsense?"
  - Collect feedback informally (email, chat)
  - Deadline: Week 4 start

- [ ] **Fix obvious issues in pilot set**
  - Remove hallucinated sensors/methods
  - Fix garbled prompts
  - Add clarity where experts said "I don't understand what you're asking"
  - Deadline: Week 4 start

### Expert Training & Calibration
- [ ] **Hold 2-hour expert training session**
  - Cover: task definitions, rubric explanation, 10+ worked examples (good + bad)
  - Goal: shared understanding of "what makes a translation good"
  - Record if possible (some experts may want to review)
  - Deadline: Week 4

- [ ] **Give experts pilot items to score independently**
  - All 3 experts score the same 50 items (or stratified sample of 30–40)
  - Deadline: Week 4 end

- [ ] **Compute inter-annotator agreement (Krippendorff's α)**
  - Tool: Use Python `krippendorff` library or R `irr` package
  - Report per-dimension and overall
  - Deadline: Week 4 end / Week 5 start

- [ ] **Evaluate agreement**
  - If α ≥ 0.70: proceed to full annotation ✓
  - If α = 0.60–0.70: hold debrief with experts, refine rubric, re-calibrate on 20 new items
  - If α < 0.60: stop, revisit rubric and task definitions
  - Deadline: Week 5 start

- [ ] **Document calibration results**
  - Report: α per task type, per compound coupling
  - Document any systematic disagreements (e.g., "Experts disagreed most on Limitation Honesty dimension")
  - Deadline: Week 5

---

## PHASE 3: FULL CORPUS GENERATION & ANNOTATION (Target: end of Week 10)

### Generate Full Benchmark
- [ ] **Generate Bronze tier items** (300–500 items)
  - Follow stratification matrix
  - Use same LLM + prompt as pilot
  - Include task-type selection logic (if possible)
  - Deadline: Week 6

- [ ] **Generate Silver tier items** (150–250 items, harder)
  - Same process; source from more specialized papers
  - Deadline: Week 7

- [ ] **Generate Gold tier items** (50–100 multi-turn dialogues)
  - Structure: 2–3 turn format with methodology → limitation → refinement
  - More labor-intensive
  - Deadline: Week 8

- [ ] **Run rule-based cleaning on all items**
  - Check: complete components (prompt, translation, justification)?
  - Check: no obvious formatting errors?
  - Remove/fix ~5–15% of items
  - Deadline: Week 8 end

### Expert Validation & Annotation
- [ ] **Expert review phase** (semantic/domain validation)
  - Each expert reviews ~30–50% of items (distribute to balance workload)
  - Flag: hallucinated concepts, implausible translations, nonsensical prompts
  - Remove flagged items or fix and re-review
  - Deadline: Week 9

- [ ] **Final expert annotation**
  - Each expert scores items assigned to them using rubric
  - For Bronze/Silver: each item scored by 2–3 experts (divide work)
  - For Gold: each item scored by 3 experts (harder items need agreement)
  - Use standardized scoresheet (Google Form or Qualtrics)
  - Deadline: Week 10

- [ ] **Collect all scores and compute final agreement**
  - Krippendorff's α overall and per task type
  - Report and document
  - Deadline: Week 10 end

---

## PHASE 4: EVALUATION & ANALYSIS (Target: end of Week 12)

### Run Baselines
- [ ] **Baseline 1: Zero-shot base model**
  - Prompt: "Given [source concept in source domain], propose the equivalent in [target domain]. Justify."
  - Model: GPT-4, Claude, or open-source (your choice)
  - Score on each dimension using rubric
  - Deadline: Week 10 end

- [ ] **Baseline 2: Base model + your skill file**
  - Same prompt, but augment with domain knowledge (your skill file or context window)
  - Compare to Baseline 1
  - Deadline: Week 11 start

- [ ] **Optional Baseline 3: Retrieval-augmented baseline**
  - Augment prompt with relevant papers/examples from corpus
  - Shows whether in-context learning helps
  - Deadline: Week 11 (optional, time-permitting)

### Failure Analysis
- [ ] **Manually classify 100–150 model errors**
  - Use your failure taxonomy: Hallucinated Analogue, Concept Confusion, Domain Ignorance, etc.
  - Create error distribution table
  - Deadline: Week 11

- [ ] **Build failure-mode narrative**
  - Example: "Models achieve 72% on Concept Mapping but only 41% on Limitation Honesty, suggesting they struggle to predict failure modes in new domains."
  - This is your key insight for the paper
  - Deadline: Week 11 end

### Final Documentation
- [ ] **Create benchmark metadata**
  - Total items per tier
  - Inter-annotator agreement statistics
  - Stratification coverage (check matrix)
  - Task-type distribution
  - Compound-coupling distribution
  - Deadline: Week 11 end

- [ ] **Write benchmark description (for paper)**
  - ~2 pages: task definition, corpus, annotation protocol, agreement results
  - Deadline: Week 12

- [ ] **Prepare benchmark for release**
  - Create CSV/JSON format with: [ID, source_concept, source_domain, target_domain, task_type, translation_prompt, reference_translation, reference_justification, expert_scores_dim1, expert_scores_dim2, ..., gold_label]
  - De-identify if needed
  - Create README with: usage instructions, scoring rubric, citation info
  - Upload to Zenodo (get DOI)
  - Deadline: Week 12

---

## QUICK WINS YOU CAN START THIS WEEK

### Week 1 only (2–3 hours)
- [ ] Draft task-type definitions (Google Doc)
- [ ] Make list of potential domain experts
- [ ] Start corpus paper search (aim for 30 by end of week)

### Week 2 only (3–4 hours)
- [ ] Rubric draft with 5–6 dimensions
- [ ] Send rubric + task definitions to 2 experts for gut-check feedback
- [ ] Finish corpus hand-coding on 20 papers

### Do NOT wait for
- [ ] Full corpus to start pilot (generate 50 items and start scoring with experts NOW)
- [ ] Perfect agreement (α = 0.70 is good enough; refine in full annotation phase)
- [ ] Baseline results to write paper (you know what you're doing conceptually)

---

## RESOURCE BUDGET

### Time
- Your time: ~40–50 hours (generation, prompt engineering, cleanup)
- Expert time: ~70 person-hours (training 6 hrs, annotation 20–25 hrs per expert × 3)
- Total: ~120–150 person-hours

### Money (if paying experts)
- Assume $50–75/hour for domain expert consulting
- 70 person-hours × $60/hr = $4,200
- Budget: $4,000–5,000 (depends on institution, expert seniority)

### Tools (mostly free)
- LLM API: GPT-4 or Claude (if you have institutional access, $0; otherwise ~$50–100)
- Annotation: Google Forms (free) or Qualtrics (if your institution has it)
- Analysis: Python (numpy, scipy, krippendorff package) — all free
- Storage: Zenodo (free) or your institution's repository

---

## RED FLAGS TO CATCH EARLY

### Week 3
- [ ] Do task types make sense to experts? If >1 expert says "unclear," refine

### Week 4
- [ ] Is κ < 0.65 after calibration? STOP. Don't proceed to full annotation. Revisit rubric.

### Week 8
- [ ] Are you generating 15%+ hallucinated items? Refine your LLM prompt.

### Week 10
- [ ] Are experts flagging systematic issues (e.g., "all Limitation Honesty items are bad")? Fix and re-generate that subset.

---

## SUCCESS CRITERIA (by end of Week 12)

You've succeeded if:
- ✓ You have 450–500 Bronze items with α ≥ 0.70
- ✓ You have 150–250 Silver items with α ≥ 0.70
- ✓ You have 50–100 Gold items with α ≥ 0.65 (higher bar OK for small set)
- ✓ You have 3 baselines with comparable results
- ✓ You have a failure taxonomy with ≥5 distinct categories
- ✓ Benchmark is on Zenodo with DOI
- ✓ You can write the methods section (§3 of your paper) from this

---

## NEXT STEPS (Week 1 ACTION ITEMS)

1. **Today:** Draft task-type definitions (email to me for feedback if helpful)
2. **Tomorrow:** Reach out to 3–4 domain experts with recruitment email
3. **This week:** Finish corpus search and hand-code 20 papers
4. **Week 1 end:** Schedule expert training session for Week 4

Then come back with a status update and let's refine as you go.
