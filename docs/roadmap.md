# Gaia translator — roadmap

Sorted by priority. Each phase has a goal, the concrete deliverables, the upstream dependencies it unblocks, the success criteria, and a rough effort estimate. Phases are mostly sequential because the corpus, the retrieval layer, the eval set, and the expert platform have hard dependencies in that order; where parallel work is possible it is flagged.

Status as of this document:

- Seismology v3 corpus ✅ (8 / 7 / 5 / 3 cards)
- Geotechnical engineering v3 corpus ✅ (7 / 7 / 4 / 3 cards including the new `TC-12`)
- Hydrology v3 — claimed-complete in README but *files are missing from the workspace*; this is the single largest blocker
- Cross-cutting concepts skill ✅
- Card format spec ✅ (`docs/card_format_spec.md`)
- Agent playbook 🟡 (skeleton + vocab table for hydro / seismo / geotech)
- Co-retrieval index 🟡 (hydro + seismo + geotech)
- Eval set v2 ✅ (60 QAs across 9 disciplines, xlsx + JSON)
- Pipeline 🟡 (only `additional_seed_qas.py` present in workspace; `seed_qa_dataset.py`, `generate_eval_dataset.py`, `build_review_spreadsheet.py` referenced in README but not in workspace)
- RAG retrieval layer 🔲
- Paper corpus 🔲
- Working chatbot 🔲
- Expert evaluation platform 🔲

---

## Phase 1 — Unblock the corpus (critical path; ~2 weeks)

**Goal.** Stop the corpus from referencing files that do not exist. Without this, the retrieval layer cannot index, the chatbot cannot retrieve, and the eval set cannot be re-grounded.

**Why first.** Every v3 card in seismology and geotech points to `CC-hydro-*`, `MC-hydro-*`, `PD-AR-landslide`, `PD-aquifer-depletion`, `PD-induced-seismicity`, and `TC-01` through `TC-06`. The cross-references resolve in the co-retrieval index but the underlying card bodies are absent from the workspace. Until those exist, the chatbot cannot answer any hydrology question and cannot fulfill the seismology↔hydrology and geotech↔hydrology bridges that are already named in the corpus.

**Deliverables.**
1. `skills/long_form/hydrology/concept_cards.md` — populate from the IDs and titles already in the co-retrieval index (9 cards: K, T, S, D, h, p, ET, Q, recharge).
2. `skills/long_form/hydrology/method_cards.md` — 7 cards (NWIS, GRACE, SMAP, COSMOS, eddy covariance, isotopes, MODFLOW/ParFlow/CLM/SWAT).
3. `skills/long_form/hydrology/phenomenon_dossiers.md` — 5 dossiers (AR-landslide, aquifer depletion, induced seismicity, drought, earthquake-hydro coupling).
4. `skills/long_form/hydrology/translation_cards.md` — TC-01 through TC-06, the cross-cutting bridges the rest of the corpus already cites.
5. `skills/summaries/hydrology.md` — ~350-word system-prompt summary.
6. Audit pass: every cross-reference in seismology and geotech resolves to a real card.

**Success criteria.** The cross-reference verification script (the one used in the geotech build) returns zero unresolved references across the full v3 corpus.

**Open question to resolve before starting.** Does the user have hydrology v3 drafts elsewhere (notebook, Overleaf, prior session)? If yes, ingest them rather than re-author. If no, author from the v2 legacy hydrology file (which is also not in the current workspace — we will need it uploaded) and from the dense set of forward references already in the corpus.

**Effort.** 2 weeks if authored from a v2 source; 4 weeks if authored from scratch.

---

## Phase 2 — Finish the discipline corpus (4 disciplines; ~6–8 weeks)

**Goal.** Bring the remaining v2 legacy files up to the v3 card pattern. Same procedure as geotech: read v2, propose inventory, get approval, write cards, update co-retrieval index, playbook, summary, README.

**Ordering inside the phase, by amount-of-corpus-it-unblocks:**

1. **Geomorphology** (highest leverage). Already has named forward references in the co-retrieval index: `CC-geomorph-D`, `CC-geomorph-streampower`, `CC-geomorph-flood-frequency`, `CC-geomorph-landslide-size`. Bridges hydrology (sediment transport, Hack's law, flood frequency), seismology (earthquake-triggered landslides, fault scarps), and geotechnical engineering (`TC-11` natural hillslope FS). Estimated 8 concept / 7 method / 5 phenomenon / 2 translation cards.
2. **Atmospheric sciences** (high leverage). Forward references `MC-atm-ERA5`; AR-driven landslide phenomenon already split across disciplines. Bridges hydrology (P, ET, AR), seismology (microseism, infrasound), ecology (GPP forcing), agriculture (drought, irrigation demand). Estimated 8 / 7 / 5 / 1–2 cards.
3. **Ecology** (medium leverage). Forward references `CC-eco-GPP`, `CC-eco-IHA`, `CC-eco-plant-water-source`. Bridges hydrology (ET, root water uptake), atmospheric (carbon flux), geomorph (root cohesion in landslides). Estimated 6 / 5 / 4 / 1 cards.
4. **Agricultural sciences** (lower standalone leverage but tied to subsidence). Forward reference `CC-ag-ET0`. Bridges hydrology (irrigation, aquifer depletion), geotech (subsidence-consolidation), ecology (GPP, crop water use). Estimated 5 / 4 / 3 / 1 cards.
5. **Near-surface geophysics** (referenced by `MC-nsg-ERT` and `TC-08`). Bridges seismology (joint inversion), hydrology (hydrogeophysics), geotech (Vs profiles, site response). Estimated 6 / 6 / 3 / 1 cards.

**Deliverables (per discipline).** Four card files + summary + co-retrieval entries + playbook vocab additions + README status update. Same shape as the geotech delivery.

**Success criteria.** All 9 disciplines have v3 corpora; co-retrieval index has full discipline coverage; cross-reference verification returns zero unresolved.

**Effort.** ~1.5 weeks per discipline using the geotech delivery as the template, so ~7–8 weeks total. Two disciplines can run in parallel if a collaborator (e.g., postdoc, grad student) takes one stream.

**Risk.** Quality drift. The seismology and geotech cards set a fairly rigorous standard (full DOIs, explicit failure modes, named phenomena with anchor papers); ecology and agricultural science have larger and more dispersed primary literatures, and we should expect more time per card.

---

## Phase 3 — Card format spec calibration and quality audit (~1 week)

**Goal.** Reconcile the `≤200 words` aspiration in the spec with the actual reference standard (seismology + geotech cards run 260–470 words). Decide which is canonical and bring everything into line.

**Why now.** Three discipline corpora are about to be authored. Setting the bar once, before the bulk of authoring, avoids inconsistent density across the corpus.

**Deliverables.**
1. Decide canonical word-count target. Recommendation: ~250 words for concept and method, ~350 for phenomenon, ~400 for translation. Update `docs/card_format_spec.md`.
2. Run a uniformity audit across seismology + geotech + the new hydrology cards. Flag outliers (TC-12 at 468 words, CC-seismo-Vs at 430 words — both probably justified, but the audit should explicitly bless them).
3. Add a card linter script (`pipeline/lint_cards.py`) that checks: word count, required sections, DOI coverage, presence of cross-discipline equivalents, presence of "when you see this in a paper" hook. Run in CI eventually.

**Success criteria.** Linter passes on the full v3 corpus.

**Effort.** ~1 week including the linter.

---

## Phase 4 — RAG retrieval layer (~3–4 weeks)

**Goal.** Build the retrieval system the cards were designed for. The cards are useless until something can fetch them in response to a user query.

**Deliverables.**
1. **Card chunker.** One chunk per card (the corpus is already chunked at the card level by design). Output: JSONL with `id`, `discipline`, `card_type`, `title`, `body`, `cross_references`, `cited_dois`.
2. **Embedding pipeline.** Embed each card with a single model — recommend `voyage-3` or `text-embedding-3-large` (OpenAI) initially; later evaluate Cohere, BGE, or a fine-tuned encoder.
3. **Retriever.** Hybrid search: dense (embeddings) + sparse (BM25) + structured (co-retrieval index for guaranteed co-retrieval of `always_retrieve_with` cards). Output top-k cards plus their guaranteed co-retrieval expansions.
4. **Query classifier.** A small Claude call (Haiku) that tags each query with one of the four agent-playbook flows (interpret-paper / integration / vocabulary / joint-observation) and identifies candidate discipline(s) for routing.
5. **Vocabulary disambiguator.** A pre-retrieval pass that checks the playbook's vocabulary table and inserts a clarification turn when needed.
6. **System-prompt assembly.** Inject the appropriate summary cards + the agent playbook + the retrieved long-form cards.

**Architecture choice.** Start with FAISS-on-disk + a thin Python wrapper. Migrate to Qdrant or Weaviate only when latency or scale demands it. Cards fit comfortably in a single in-memory index.

**Success criteria.** Top-3 retrieval contains the correct anchor card for ≥80% of the 60-QA eval set; top-10 contains it for ≥95%. This is a precondition for evaluating the chatbot.

**Effort.** ~3 weeks for a working system; another week for tuning and evaluation.

**Dependency.** Phases 1–3 (corpus must be complete and consistent).

---

## Phase 5 — Paper corpus and inference loop (~3 weeks)

**Owner**: Derek (student) is leading the chatbot inference-loop build as a separate workstream that runs in parallel with Phases 6–7 of the eval-side roadmap. Coordination with the eval platform happens through the shared data schema in `eval_platform/` (the chatbot logs retrieval sets and responses in the format the scoring app expects) and through periodic sync on what the cards/playbook need to surface for the agent.

**Goal.** Wire the retrieval layer to Claude inference, so the chatbot can actually answer a query. Add a small corpus of anchor papers (PDFs / text) so the chatbot can quote primary sources beyond the cards.

**Deliverables.**
1. **Anchor paper corpus.** Pull the ~100 anchor papers already cited in the cards. Store as `corpus/papers/<doi-slug>.pdf` + extracted text + chunked embeddings. Respect publisher licenses — use open-access where available; for paywalled, store metadata + DOI and rely on the card summary plus a `read more` link.
2. **Inference loop.** Python module (`gaia_translator/agent.py`) that takes a user query, runs disambiguation → retrieval → system-prompt assembly → Claude inference → response. Logs the retrieval set, the prompt, and the response in JSON in the format consumed by the eval scoring app.
3. **Refusal & citation discipline.** Implement the refusal patterns from `agent_playbook.md` as response-time guardrails (e.g., regex / Claude self-check that flags any citation not in the retrieved context).
4. **Conversation memory.** Maintain disambiguation state and prior turn context across a multi-turn session; persist as JSON.
5. **CLI and minimal web demo.** A `gaia` CLI for local use; a **Gradio** chat demo for sharing externally (eventually embeddable in the gaia-hazlab.github.io showcase). Gradio (not Streamlit) for the public chat demo: `gr.ChatInterface` is best-in-class for streaming chat UIs and Hugging Face Spaces is the natural home. (Reviewer scoring app uses Streamlit — different role; see Phase 7c.)

**Success criteria.** End-to-end demo on the existing 60 QAs returns plausible, cited answers with no fabricated DOIs.

**Effort.** ~3 weeks for the inference loop and the demo; another 1–2 weeks for the paper corpus.

**Dependency.** Phase 4 (retrieval layer). The chatbot work can run in parallel with Phases 6–7 as long as the data schema is stable.

**Hidden cost.** Cleaning paper PDFs and extracting clean text is always slower than expected. Budget 1 week for the paper corpus alone.

**Coordination with the eval side.** The chatbot's output format (question, retrieved cards, model answer, retrieval log) maps directly to the scoring spreadsheet's columns. Lock this schema between Derek and the eval-platform owner before the chatbot generates the first batch of answers to score — schema drift here invalidates the eval set.

---

## Phase 6 — Eval set expansion and gold-standard answers (~4 weeks)

**Goal.** Grow the 60-QA seed set to ~300 QAs balanced by discipline and query type, and hand-curate gold-standard answers for at least the cross-discipline subset.

**Deliverables.**
1. **Eval set v3** — target 300 QAs.
   - Per-discipline coverage: ~25 QAs each × 9 disciplines = 225 single-discipline QAs.
   - Cross-discipline QAs: ~75 spanning pairs and triples (these are the most informative for translator-agent evaluation).
   - Query-type stratification: paper-interpretation (40%), integration (25%), vocabulary-disambiguation (15%), refusal-tests (10%), joint-observation (10%).
   - Author mix: 60% LLM-drafted then human-edited, 40% hand-drafted from real research questions the Denolle Group and collaborators encounter.
2. **Gold-standard answers** for ~100 QAs (the cross-discipline subset + the refusal tests). These are the anchor truth against which the chatbot will be scored.
3. **Scoring rubric.** Eight-criterion grading scale matching the `pre-submission-reviewer` skill structure: novelty/relevance, technical accuracy, citation discipline, vocabulary precision, cross-discipline integration, refusal correctness (where applicable), presentation, and an overall.
4. **Rubric calibration set.** 20 QAs scored by the user, the postdoc team, and 2 external collaborators to establish inter-rater reliability before the full evaluation begins.

**Success criteria.** Krippendorff's α ≥ 0.7 across the calibration set; QA distribution is approximately balanced; gold-standard answers are reviewed by the user.

**Effort.** ~4 weeks.

**Dependency.** Phases 4–5 (so the chatbot can generate the answers being scored).

**Reuse.** `additional_seed_qas.py` and `seed_qa_dataset.py` (once recovered or rewritten) become the v3 generators.

---

## Phase 7 — Expert evaluation platform (~6 weeks staged)

**Note**: the v1 platform (Sheets + Form) is now built under `eval_platform/`. The deliverables described below are the v1 → v3 evolution from that starting point.



**Goal.** Engage 15–25 domain experts across the 9 disciplines to score chatbot answers against the rubric, with inter-rater reliability tracking, attribution, and a low-friction interface.

**Why staged.** Start with the lowest-effort interface that gets reviewers reviewing; escalate only if the data demands it. Each stage is a real release that we can stop at if it's sufficient.

**Stage 7a — Spreadsheet pilot (1 week).** Extend the existing `gaia_translator_eval_review.xlsx` with reviewer columns (`reviewer_id`, `score_*`, `comments`, `flagged_for_discussion`). Distribute to 3–5 trusted internal reviewers. Lessons learned about rubric ambiguity and friction feed the next stage. Decision gate: is a spreadsheet sufficient or do we need a real app?

**Stage 7b — Google Form + auto-populated Sheet (2 weeks).** Wrap each QA in a Google Form so reviewers don't have to navigate a spreadsheet. Auto-populate from the JSON eval set. Pros: zero infrastructure, easy auth via Google. Cons: limited UX, no in-line citation checking. Sufficient for 10–15 reviewers and a few-hundred-QA set.

**Stage 7c — Streamlit reviewer scoring app (3 weeks).** When the spreadsheet/form workflow hits friction, build a custom interface in Streamlit. Streamlit (not Gradio) for this role: the scoring task is multi-page tabular workflow with sidebar progress, persistent per-user state, OIDC auth, and a PI-facing IRR dashboard — every one of which is Streamlit's strength. Gradio is the right tool for a separate public chatbot demo (see note in Phase 5), but it is not built for multi-page reviewer-labeling workflows.

Feature checklist for v7c:
- **Auth**: ORCID OAuth (researcher identity + attribution) via `streamlit-authenticator` or `st.experimental_user` with an OIDC provider; fallback to email allowlist for the first cohort.
- **Per-reviewer assignment**: discipline-aware QA routing; reviewers see only their assigned set; no peer-visibility during independent scoring.
- **In-line citation checking**: clickable DOI links; "is the cited source actually in the retrieved context?" indicator computed against the chatbot's retrieval log.
- **Live IRR dashboard** (PI view): running Krippendorff's α per criterion, broken out by discipline pair; flag-for-discussion queue with comment threading.
- **Reviewer dashboards**: personal progress, mean scoring time, completion percent, any rubric-required comments still missing.
- **Persistence**: read/write to the same Google Sheets backend as Stage 7b via `st.connection("gsheets")`, OR migrate to SQLite/Postgres if scale demands. Migrating from Sheets→DB is a Phase 7d decision, not a 7c blocker.
- **Export**: one-click JSON dump of the full eval dataset for downstream analysis (RLHF/DPO/Datasheets paper).
- **Hosting**: Streamlit Community Cloud (free; supports private apps with GitHub auth); upgrade to UW research-computing if institutional data-residency rules require it.

Code layout suggestion: a separate repo `gaia-eval-app` (or a `streamlit_app/` directory in `gaia-translate-QA`) imports the v1 data schema from `eval_platform/` so the rubric definitions, calibration QAs, and JSON schema stay single-sourced.

**Stage 7d — Calibration + expansion rounds.** Two calibration rounds (20 QAs each) to align reviewers, then full evaluation. Pair every QA with ≥2 reviewers; ≥3 for cross-discipline.

**Recruitment** (in parallel from Phase 7a onward). Target 2–3 reviewers per discipline, prefer mid-career researchers with cross-discipline experience. UW colleagues, AGU contacts, NSF program managers' networks. Offer co-authorship on the methodology paper (Phase 8) and a small honorarium ($200–500) if grant funds allow.

**Success criteria.** ≥150 QAs scored by ≥2 reviewers each; Krippendorff's α ≥ 0.7 across all reviewers; reviewer attrition < 30%.

**Effort.** ~6 weeks total, but heavily parallelizable with Phases 6 and 8.

**Dependency.** Phase 6 (rubric, gold standard, eval set).

---

## Phase 8 — Iteration and public release (~4 weeks)

**Goal.** Close the loop: use expert scores to identify chatbot failure modes, iterate the cards/playbook/retrieval, re-score on a held-out subset, and publish.

**Deliverables.**
1. **Failure-mode analysis** of the expert scores: which discipline pairs underperform, which query types, which refusal patterns the chatbot misses.
2. **Card and playbook revisions** targeting the lowest-scoring categories.
3. **Held-out re-evaluation** on a 50-QA test set the experts haven't seen, scored on the same rubric. Demonstrates whether revisions actually improved the chatbot.
4. **Methodology paper.** Target venue: AGU *AGU Advances* (cross-discipline), *Eos* (community-facing), or *Reviews of Geophysics*. Open-data ethics: release the eval set under CC-BY-4.0 (already noted in `LICENSE`); release reviewer scores in aggregated form with consent.
5. **Public corpus release.** Tag v3.0 in git; publish to Zenodo with DOI; announce on AGU listservs, CSDMS, EarthCube, NAIRR-aligned communities.

**Success criteria.** ≥75% of categories show improvement on held-out re-evaluation; methodology paper submitted; Zenodo DOI minted.

**Effort.** ~4 weeks.

---

## Cross-cutting concerns (apply across all phases)

### Funding and team

The full roadmap is ~30 weeks of focused effort. Confirmed assignments and rough resourcing:

- **PI (Marine)** at ~10% time for scientific direction, card authoring quality control, expert recruitment, and meeting facilitation.
- **Derek (student)** owns Phase 5: chatbot inference loop, paper corpus, Gradio public chat demo. Runs in parallel with Phases 6–7 once the v3 corpus and retrieval layer (Phase 4) are in place.
- **Eval-platform owner** (TBD — postdoc, grad student, or part-time engineer hire): card authoring for the remaining 5 disciplines (Phase 2), retrieval layer (Phase 4), eval-set expansion (Phase 6), Streamlit reviewer app (Phase 7c), aggregation and IRR analysis.
- **Domain-expert reviewers**: 15–25 across the 9 disciplines, recruited from UW colleagues, AGU networks, and the GAIA HazLab collaborator pool. Time commitment 5–8 hours each over six weeks.

The remaining open staffing question is whether the eval-platform owner is one full-time person for 6 months, two grad students at half-time, or split across a postdoc plus a ~6-week external software-engineer engagement for the Streamlit app specifically.

Honoraria budget for reviewers: 15–25 × $250 ≈ $4–6k. API spend for chatbot inference + eval generation: ~$2–5k. Total cash budget on top of personnel: ~$10k.

This effort dovetails with the NSF IDSS proposal preparation: the Gaia translator is a candidate Category I or II IDSS deliverable, and the eval set is itself a national-scale data product. The `nsf-idss-proposal-preparer` skill can frame this directly.

### IP and licensing

Already established: code MIT, content CC-BY-4.0. Reviewer scores require a consent form; aggregate release should be the default, with opt-in for individual attribution.

### Publication strategy

Three publication outputs are likely:

1. **Methodology paper** (Phase 8) — the eval set + scoring methodology + chatbot architecture.
2. **Discipline-bridge papers** — short, focused papers showing the cross-discipline translation working for specific cases (Nisqually liquefaction digital twin; Cascadia hazard cascade; aquifer depletion + subsidence + induced seismicity).
3. **Open dataset paper** — Scientific Data or Earth System Science Data, releasing the eval set as a citable artifact.

### Risk register

- **Hydrology cards never materialize.** Blocks everything downstream. Mitigation: schedule Phase 1 as the first hard deliverable, with a backup plan to author from scratch using the v2 legacy hydrology file if the v3 drafts are not found.
- **Expert recruitment under-delivers.** Mitigation: start recruitment in Phase 6, well before the platform is live; offer co-authorship and a streamlined first review (5 QAs to validate engagement).
- **LLM cost.** Generating 300 QAs + scoring + the chatbot itself costs real money. Budget ~$2,000–$5,000 in API spend for the full roadmap; verify against awarded grants.
- **Citation fabrication.** The single most dangerous failure mode for a research-context chatbot. Phase 5's citation-discipline guardrail must be evaluated explicitly in Phase 7.

---

## Decision points

Phases 1 and 2 are now scoped and underway; the remaining open decisions:

1. **Eval-platform staffing.** Phase 2 (cards for 5 remaining disciplines), Phase 4 (retrieval), Phase 6 (eval-set expansion), and Phase 7 (Streamlit reviewer app) need an owner. Postdoc, grad student, external engineer for the app portion, or some split?
2. **Schema lock between Derek and the eval platform.** The chatbot's response-and-retrieval-log JSON must match the scoring spreadsheet's columns. Schedule a 30-minute sync between Derek and the eval-platform owner before Phase 5 work starts producing artifacts.
3. **Funding gate.** Reviewer honoraria (~$5k) and API spend (~$3k) — confirmed against an existing grant, or does Phase 7 wait for additional support?
4. **Publication venue.** AGU Advances vs. Reviews of Geophysics vs. Eos — affects Phase 8 framing and rigor target on the held-out re-evaluation. Possibly also a separate *Scientific Data* descriptor paper for the open eval dataset.
5. **Public chatbot demo timing.** Phase 5 delivers a Gradio demo; do we embed it in the gaia-hazlab.github.io showcase immediately, or hold until the v3 corpus covers all 9 disciplines so a public-facing demo doesn't disappoint on out-of-corpus questions?
