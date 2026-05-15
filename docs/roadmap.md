# Gaia translator — roadmap

Sorted by priority. Each phase has a goal, the concrete deliverables, the upstream dependencies it unblocks, the success criteria, and a rough effort estimate. Where parallel work is possible it is flagged.

**Critical-path summary (post-revision)**: Phase 3 linter (3 days) → Phase 4 low-level translator tool (2–3 weeks, Derek) → Phase 6 eval set expansion (4 weeks, partially parallelizable) → Phase 7 expert evaluation (6 weeks staged; v1 platform already built) → Phase 8 iteration + release (4 weeks). Roughly **~6 months elapsed from now to a peer-reviewable published methodology**, with most weeks running concurrent threads (corpus QA + tool dev + reviewer recruitment).

Status as of this document:

- All 9 disciplines v3-complete ✅ (170 cards: hydrology 27, seismology 23, geomorphology 22, atmospheric_sciences 21, ecology 21, geotechnical_engineering 21, near_surface_geophysics 18, agricultural_sciences 17)
- Cross-cutting concepts skill ✅
- Card format spec ✅ with calibrated word-count caps
- Agent playbook ✅ with 8-discipline vocab table (including Agriculture column)
- Co-retrieval index ✅ with 170 entries; zero unresolved references
- 9 system-prompt summaries ✅
- Eval platform v1 ✅ (Sheets template + reviewer instructions docx + meeting agenda + signup form + 3 calibration QAs + architecture note + private STRATEGY.md)
- Eval set v2 ✅ (60 QAs across 9 disciplines, xlsx + JSON)
- Pipeline 🟡 (`additional_seed_qas.py` present; `seed_qa_dataset.py`, `generate_eval_dataset.py`, `build_review_spreadsheet.py` need re-creation as part of Phase 6)
- Card linter ✅ (`pipeline/lint_cards.py`; 0 errors, 3 acceptable warnings)
- **Low-level translator tool** 🔲 (Phase 4, Derek's work, ~2–3 weeks; schema spec at `docs/phase4_output_schema.md`)
- Eval set v3.1 🟡 21 / ~300 seed QAs with full dimensional tagging (translation task types, tier, compound coupling, failure modes); Phase 6 in progress; per-failure-mode analysis is the methodology-paper headline (`docs/eval_dimensions_framework.md`)
- Expert evaluation rounds 🔲 (Phase 7)
- ~~RAG retrieval layer~~ ⏸ deferred to future option
- ~~Paper corpus~~ ⏸ deferred to future option

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

## Phase 3 — Card-spec linter (✅ complete)

**Status.** Complete. Spec calibration was done in Phase 2; the linter `pipeline/lint_cards.py` was built and runs clean on the full 9-discipline corpus.

**What it enforces** (stdlib-only, ~600 lines):

- Word-count caps per card type (concept/method 450, phenomenon 500, translation 550).
- Required sections per card type, with accepted lexical variants (e.g., "Defining relation" / "Defining relations" / "Defining structure"; "Typical ranges" / "Typical relations").
- "When you see this in a paper" hook on every concept and method card.
- At least one bullet item in the Cross-discipline-equivalents section of every concept and method card.
- DOI coverage on anchor citations, with a heuristic allow-list for known DOI-less works (books, IPCC chapters, PhD dissertations, EU project deliverables, pre-1990 ASCE journal articles, FAO and USDA technical reports, USGS Professional Papers, software manuals, proceedings, and specific pre-1970 papers).
- Cross-reference resolution: every `CC-/MC-/PD-/TC-` reference in any card body resolves to a defined card in the corpus.

**Final state on the corpus**:

- 170 cards in 32 files linted.
- **0 errors.**
- **3 acceptable warnings**: CC-seismo-Vs word-count (429 / cap 450; intentionally information-dense after the TC-12 revision), Mudd et al. (2014) missing DOI (the published version is 2016 with `doi:10.5194/esurf-4-655-2016`; year fix and DOI add recommended), and Zhan (2020) ARES DAS review missing DOI (verify `doi:10.1146/annurev-earth-053018-065033` and add).

**Usage**:

```bash
python pipeline/lint_cards.py                          # full corpus
python pipeline/lint_cards.py --card path/to/file.md   # single file
python pipeline/lint_cards.py --strict                 # fail on warnings (for CI)
python pipeline/lint_cards.py --json                   # JSON output (for CI)
```

Exit codes follow standard convention (0 clean, 1 errors, 2 usage error). The linter is ready for CI integration.

---

## Phase 4 (revised) — Low-level translator tool (~2–3 weeks)

**This is the working chatbot.** No retrieval layer, no curated paper corpus, no vector store. The user supplies the document context (paper to interpret); the system supplies the framework (cards as Claude Skills or system-prompt context). Stuffs the entire corpus into the context budget — fits comfortably for Opus 4-class models at ~75k tokens of card content out of 200k context.

**Owner**: Derek (student) leads.

**Goal.** A single-shot Python tool that takes a research question (always) plus an optional document (PDF or URL/HTML) and returns a structured translation organized by the four card categories plus whatever the user is specifically asking.

**Inputs**:
- `prompt` (required): the user's research question or translation request.
- `paper` (optional): a PDF file (Claude has native PDF support).
- `url` (optional): a URL to a paper or article (HTML fetched via `web_fetch` and passed as text).
- Mutually exclusive: either `paper` or `url` or neither, not both. (Multi-document support is a future extension.)

**Output** (JSON + Markdown rendering):

```json
{
  "user_query": "...",
  "input_document": {"type": "pdf|url|none", "source": "...", "title": "..."},
  "primary_disciplines_detected": ["seismology", "geotechnical_engineering"],
  "concept_matches": [
    {"card_id": "CC-seismo-Vs", "title": "...", "relevance": "...", "anchor_citations": [...]}
  ],
  "method_matches":      [{"card_id": "MC-...", ...}],
  "phenomenon_matches":  [{"card_id": "PD-...", ...}],
  "translation_matches": [{"card_id": "TC-...", ...}],
  "vocabulary_collisions_flagged": [...],
  "refusals_or_caveats": [...],
  "user_specific_response": "Direct answer to the user's question: ..."
}
```

**Deliverables.**

1. **Document ingestion**. PDF support (Claude native). URL/HTML support via `mcp__workspace__web_fetch` or equivalent + html-to-text extraction.
2. **Skill-based context loading**. Discipline summaries (~10k tokens) + agent playbook (~3k) + cross-cutting concepts (~3k) always loaded. Long-form cards (~70k for the full corpus) loaded either entirely-on for Opus, or selectively via Claude Skills based on which disciplines the query/document touches.
3. **Vocabulary disambiguator**. Pre-process the query against the playbook's vocab table; insert a clarification turn when a polysemous term is ambiguous.
4. **Structured-output inference**. System prompt instructs the model to organize its response by card category, with each match including the card ID, title, and a brief relevance statement. The user-specific response section is the free-form synthesis the user actually asked for.
5. **Citation-discipline guardrail**. Post-hoc verification that every cited DOI or paper appears in either (a) the loaded skill context (the cards themselves carry their anchor citations), or (b) the user-supplied document. Flag any out-of-context citation as a potential fabrication for human review.
6. **CLI and a Gradio demo**. `gaia translate "..."  [--paper file.pdf | --url https://...]` for local use; Gradio web demo (Hugging Face Spaces hosting) embeddable in `gaia-hazlab.github.io`.
7. **Logging**. JSON log of every inference for downstream evaluation; format matches the eval scoring app's expected schema in `eval_platform/`.

**Success criteria.** End-to-end demo on the existing 60 QAs returns structured responses with: zero fabricated DOIs (verified by the citation guardrail), correctly-identified primary disciplines (>= 85% accuracy on a 30-QA spot check), and category-organized output that maps cleanly into the eval scoring spreadsheet.

**Effort.** ~2 weeks for the core tool; +0.5 week for the Gradio demo; +0.5 week for citation guardrail and logging. Total ~2–3 weeks.

**Dependency.** Phase 3 (linter complete is helpful but not strictly required; a clean corpus is required, which Phases 1–2 already deliver).

**Coordination with the eval side.** The output JSON schema must be locked between Derek and the eval-platform owner *before* the tool starts generating answers for scoring. **The draft is in `docs/phase4_output_schema.md`** (Pydantic v2 + worked examples on the three calibration QAs + per-section scoring map + 8 open decisions for the lock meeting). Schema drift after the eval has started invalidates the calibration round.

**What's intentionally NOT in this phase.**
- No curated paper corpus (deferred to "Future option" below).
- No autonomous paper retrieval (deferred).
- No vector DB / embeddings / FAISS / Qdrant (deferred).
- No multi-document QA (single-document only).
- No multi-turn conversation memory (added in optional Phase 5 if needed).

---

## Phase 5 (optional / deferred to post-evaluation) — Multi-turn orchestration

**Goal.** Convert the single-shot Phase 4 tool into a conversational agent with session memory and the four explicit user flows from `agent_playbook.md` (paper interpretation, integration, vocabulary disambiguation, joint observation).

**Why optional.** A useful research tool can ship without this. The four flows are useful prompts; making them explicit modes is helpful only if the single-shot interface proves friction-laden in user testing. Promote to active phase only if Phase 7 expert feedback calls for it.

**Effort.** ~2 weeks if/when activated. Builds on Phase 4 without modification — the orchestration layer is pure Python around the single-shot core.

---

## Future option — Full RAG with curated paper corpus (deferred indefinitely)

**Not on the critical path.** Reactivate only if a downstream need surfaces:

- **Autonomous paper recommendation**: "What three papers should I read on X?" without the user providing the source material.
- **Productization for non-researcher users**: a startup-track product targeting users who don't want to upload papers themselves.
- **Embedding-aware RLHF/DPO study**: a controlled comparison of retrieval-conditioned vs. skill-conditioned generation as a research question in its own right.
- **Coverage beyond the user's library**: cases where the relevant anchor papers are not in the user's hand and the agent must surface them.

**If reactivated, scope** (≈ 4 weeks):

- Card chunker: JSONL with `id`, `discipline`, `card_type`, `title`, `body`, `cross_references`, `cited_dois` per card.
- Embedding pipeline: voyage-3 or text-embedding-3-large; one embedding per card.
- Hybrid retriever: dense + BM25 + structured co-retrieval (`always_retrieve_with`); FAISS-on-disk to start.
- Anchor paper corpus: ~100 papers from the cards' anchor-citation lists; PDF + extracted text + chunked embeddings; respect publisher licenses.
- Replace skill-loaded context in the Phase 4 tool with retrieval-conditioned context; everything downstream of context assembly stays the same.

This is a real architectural upgrade and worth tracking, but it is *not* what the GAIA HazLab agenda needs in the next year.

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

**Effort.** ~4 weeks; can run in parallel with the second half of Phase 4 once the tool's output schema is locked.

**Dependency.** Phase 4 (the low-level translator tool — so the chatbot can generate the structured answers being scored). The structured output schema is the contract between Phase 4 and Phase 6 / 7.

**Reuse.** `pipeline/seed_qa_dataset.py` (21 seed QAs as anchors), `pipeline/generate_eval_dataset.py` (LLM-assisted drafter, gap-prioritized auto mode), `pipeline/validate_eval_set.py` (schema + stratification checks), and `pipeline/build_review_spreadsheet.py` (JSON → reviewer xlsx) are all built. The structured-output format simplifies QA design: each QA produces an expected CC/MC/PD/TC match set plus an expected user-specific response section, making per-section scoring tractable.

**Phase 6 kickoff status (May 2026)**: schema spec (`docs/eval_qa_schema.md`), design guidelines (`docs/eval_qa_design.md`), 21 seed QAs covering all 9 disciplines and all 5 query types, full Python pipeline (validate + build + draft), canonical `eval_dataset/eval_dataset_v3.json`, and reviewer `eval_dataset/gaia_translator_eval_review_v3.xlsx` (50 formulas, 0 errors). Remaining work: author ~280 more QAs in the same format (workflow: LLM-draft auto-prioritized to fill gaps → human edit → append to seed dataset → re-validate → re-build xlsx).

**Adaptation for the structured output**. The 8-criterion rubric in `eval_platform/` applies per-section as well as overall:
- Technical accuracy, citation discipline, vocabulary precision are scored on each card-category section.
- Cross-discipline integration is scored on the translation-card section specifically.
- Refusal correctness is scored on the refusals-or-caveats section.
- Completeness and presentation are scored on the overall response.
- Overall usefulness is the holistic judgment.

This per-section scoring is cleaner than scoring a single free-form answer and should improve reviewer IRR.

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

Post-revision roadmap is ~18 weeks of focused effort (was ~30 in the RAG-included version). Confirmed assignments and rough resourcing:

- **PI (Marine)** at ~10% time for scientific direction, expert recruitment, meeting facilitation, and final-quality review of card revisions.
- **Derek (student)** owns Phase 4: low-level translator tool, structured-output design, citation guardrail, CLI + Gradio demo. ~2–3 weeks of focused work + ongoing maintenance.
- **Eval-platform owner** (TBD — postdoc, grad student, or part-time engineer hire): Phase 3 linter (small), Phase 6 eval-set expansion (substantial), Phase 7c Streamlit reviewer app (substantial), aggregation and IRR analysis.
- **Domain-expert reviewers**: 15–25 across the 9 disciplines, recruited from UW colleagues, AGU networks, and the GAIA HazLab collaborator pool. Time commitment 5–8 hours each over six weeks.

The remaining open staffing question is whether the eval-platform owner is one focused person for ~3 months or split across multiple part-time hires.

Honoraria budget for reviewers: 15–25 × $250 ≈ $4–6k. API spend for chatbot inference + eval generation (now lower since no embedding indexing): ~$2–4k. Total cash budget on top of personnel: ~$8–10k.

This effort dovetails with the NSF IDSS proposal preparation: the Gaia translator is a candidate Category I or II IDSS deliverable, and the eval set is itself a national-scale data product. The `nsf-idss-proposal-preparer` skill can frame this directly.

### IP and licensing

Already established: code MIT, content CC-BY-4.0. Reviewer scores require a consent form; aggregate release should be the default, with opt-in for individual attribution.

### Publication strategy

Three publication outputs are likely:

1. **Methodology paper** (Phase 8) — the eval set + scoring methodology + chatbot architecture.
2. **Discipline-bridge papers** — short, focused papers showing the cross-discipline translation working for specific cases (Nisqually liquefaction digital twin; Cascadia hazard cascade; aquifer depletion + subsidence + induced seismicity).
3. **Open dataset paper** — Scientific Data or Earth System Science Data, releasing the eval set as a citable artifact.

### Risk register

- ~~**Hydrology cards never materialize.**~~ Resolved in Phase 1.
- **Expert recruitment under-delivers.** Mitigation: start recruitment now (parallel with Phase 4 development); offer co-authorship and a streamlined first review (3 calibration QAs to validate engagement).
- **LLM cost.** Generating 300 QAs + 25 inference runs per QA × per reviewer + the eval scoring rounds. With the simplified Phase 4 (no embedding indexing, no paper-corpus ingestion), per-inference token budget is ~80k input + ~10k output = ~$1.50 per Opus inference. 300 QAs × 5 inferences/QA × $1.50 ≈ $2,250 for full eval set generation. Plus calibration and revision rounds. Budget ~$3–5k total.
- **Citation fabrication.** The single most dangerous failure mode for a research-context chatbot. Phase 4's citation-discipline guardrail (every cited DOI must appear in either the loaded skill context or the user-supplied document) must be evaluated explicitly in Phase 7. The simpler skill-loaded architecture makes verification cleaner than a retrieval-based system would.
- **Skill-loading token budget.** Stuffing the full 9-discipline corpus into context is ~75k tokens, comfortable for Opus but tight for Sonnet/Haiku. Mitigation: implement selective skill loading via Claude Skills if benchmarking shows the always-on approach is too expensive at scale.
- **Single-document limitation.** Phase 4 takes one paper at a time. For multi-paper meta-analysis questions, the tool will need extending. This is a real limitation but matches the dominant user workflow (interpret *this* paper) and is acceptable for v1.

---

## Decision points

Phases 1 and 2 are complete; corpus is 9-discipline-v3 and the eval platform v1 is built. The remaining open decisions:

1. **Phase 4 output schema.** Lock between Derek and the eval-platform owner before any Phase 4 inference runs. The structured-output JSON (`concept_matches`, `method_matches`, `phenomenon_matches`, `translation_matches`, `vocabulary_collisions`, `refusals_or_caveats`, `user_specific_response`) is the contract between the tool and the eval. Schedule a 30-minute sync in week 1.
2. **Eval-platform staffing.** Phase 3 (linter, 3 days), Phase 6 (eval-set expansion, 4 weeks), Phase 7c (Streamlit reviewer app, 3 weeks) need an owner. Postdoc, grad student, external engineer for the app portion, or some split?
3. **Skill-loading strategy in Phase 4.** Full-corpus always-on (simplest, ~75k tokens, fits Opus comfortably) vs. Claude-Skills-based selective loading (more efficient, requires a small dispatch layer). My recommendation: start with full-corpus always-on for the first 60 QAs; benchmark and switch to selective loading only if latency or cost demand it.
4. **Funding gate.** Reviewer honoraria (~$5k) and API spend (~$3k) — confirmed against an existing grant, or does Phase 7 wait for additional support?
5. **Publication venue.** AGU Advances vs. Reviews of Geophysics vs. Eos vs. *Scientific Data* descriptor for the eval dataset. Affects Phase 8 rigor target on the held-out re-evaluation.
6. **Public Gradio demo timing.** Embed in gaia-hazlab.github.io showcase immediately upon Phase 4 completion, or hold until after the Phase 7 calibration round so external visitors see a verified-quality tool? My recommendation: hold for ~6–8 weeks until calibration is clean, then publish with a "v1, open for feedback" framing.
7. **Reactivating the deferred RAG layer.** Not on the critical path. Revisit only if (a) Phase 7 feedback specifically calls for autonomous paper recommendation, (b) productization plans firm up, or (c) a research question explicitly needs retrieval-conditioned generation as a controlled variable.
