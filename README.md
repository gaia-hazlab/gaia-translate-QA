# Gaia translator — cross-disciplinary geoscience skill files

Open-source skill files, RAG-friendly knowledge cards, and a Claude-based evaluation pipeline for a multidisciplinary translator agent spanning hydrology, seismology, geomorphology, atmospheric sciences, geotechnical engineering, ecology, agricultural sciences, near-surface geophysics, and the cross-cutting concepts that bridge them.

**What this is for.** Building a research chatbot that helps geoscientists (a) interpret papers outside their primary discipline, (b) discover how their work integrates with adjacent fields, and (c) propose joint-observation strategies — with every answer grounded in cited scientific evidence.

**Maintained by the Denolle Group (Gaia / CRESST)**, University of Washington Earth and Space Sciences.

---

## Repository layout

```
gaia-translator/
├── README.md                        ← you are here
├── LICENSE                          ← MIT for code, CC-BY-4.0 for content
├── CONTRIBUTING.md                  ← how colleagues can add cards
├── .gitignore
│
├── docs/
│   ├── architecture.md              ← the system design (short prompt + RAG corpus)
│   └── card_format_spec.md          ← schema for concept / method / phenomenon / translation cards
│
├── skills/                          ← the agent's grounding knowledge
│   ├── README.md
│   ├── agent_playbook.md            ← how the chatbot should reason (templates, refusal rules)
│   ├── co_retrieval_index.yaml      ← concept → recommended-to-retrieve papers (machine-readable)
│   ├── cross_cutting_concepts.md    ← unifying principles + NAS reports + exemplar synthesis
│   │
│   ├── summaries/                   ← short, system-prompt-grade (200-400 words each)
│   │   └── hydrology.md             ← ✅ demo for v3 card-pattern restructuring
│   │
│   └── long_form/                   ← retrieval corpus (chunked into cards)
│       ├── hydrology/               ← ✅ v3 demo (fully card-structured)
│       │   ├── concept_cards.md
│       │   ├── method_cards.md
│       │   ├── phenomenon_dossiers.md
│       │   └── translation_cards.md
│       │
│       ├── seismology/              ← ✅ v3 done
│       │   ├── concept_cards.md
│       │   ├── method_cards.md
│       │   ├── phenomenon_dossiers.md
│       │   └── translation_cards.md
│       │
│       ├── geotechnical_engineering/ ← ✅ v3 done
│       │   ├── concept_cards.md
│       │   ├── method_cards.md
│       │   ├── phenomenon_dossiers.md
│       │   └── translation_cards.md
│       │
│       └── v2_legacy/               ← awaiting v3 card-pattern restructuring
│           ├── geomorphology.md         (not yet uploaded; awaiting source)
│           ├── atmospheric_sciences.md
│           ├── ecology.md
│           ├── agricultural_sciences.md
│           ├── near_surface_geophysics.md
│           └── geotechnical_engineering.md  (v2 archive; superseded by ../geotechnical_engineering/ v3 cards)
│
├── pipeline/                        ← eval-set generation
│   ├── generate_eval_dataset.py     ← Opus 4.7 drafting + critique pipeline
│   ├── seed_qa_dataset.py           ← 50 hand-drafted QAs (v1)
│   ├── additional_seed_qas.py       ← 10 cross-discipline QAs (v2)
│   └── build_review_spreadsheet.py  ← JSON → reviewer .xlsx
│
└── eval_dataset/
    ├── eval_dataset_v2.json
    └── gaia_translator_eval_review.xlsx
```

## Quickstart for colleagues

```bash
# Clone
git clone <YOUR_GITHUB_URL>/gaia-translator.git
cd gaia-translator

# Set up Python environment (only needed for pipeline / eval regeneration)
python -m venv .venv && source .venv/bin/activate
pip install anthropic openpyxl pyyaml

# Read the eval set (no Python needed — just open the xlsx)
open eval_dataset/gaia_translator_eval_review.xlsx

# Regenerate the eval workbook
cd pipeline
python -c "
import json
from seed_qa_dataset import SEED_QAS
from additional_seed_qas import ADDITIONAL_SEED_QAS
json.dump(SEED_QAS + ADDITIONAL_SEED_QAS, open('../eval_dataset/eval_dataset_v2.json', 'w'), indent=2)
"
python build_review_spreadsheet.py --in ../eval_dataset/eval_dataset_v2.json --out ../eval_dataset/gaia_translator_eval_review.xlsx

# Generate new QAs with Claude (requires API key)
export ANTHROPIC_API_KEY=sk-ant-...
python generate_eval_dataset.py --n 60 --discipline-dir ../skills/long_form --out ../eval_dataset/eval_dataset_llm.json
```

## How to read the skill files

The skill files come in two flavors. Pick the right one for the right purpose.

### Summaries (`skills/summaries/`)
Short documents (~200-400 words) suitable for **system-prompt inclusion every turn**. They describe what the discipline does, name its core variables, and surface the most important cross-discipline hooks. They do **not** contain enough detail to ground a research-quality answer; they exist so the agent always has discipline awareness.

### Long-form cards (`skills/long_form/<discipline>/`)
Detailed knowledge cards intended to live in a **RAG retrieval corpus**, chunked at the card level. Four card types:

- **Concept cards** — one per major variable or governing equation. Definition, units, typical numerical ranges, cross-discipline equivalents, anchor citations.
- **Method cards** — one per measurement technique, instrument, or dataset. What it measures, resolution, failure modes, cross-discipline reuse.
- **Phenomenon dossiers** — one per major phenomenon (AR-driven landslide, drought, induced seismicity, etc.). Mechanism, observables per discipline, open questions, recommended-to-retrieve anchor papers.
- **Translation cards** — one per cross-discipline bridge. Shared equation or concept, manifestation in each discipline, when the analogy holds, when it breaks.

See `docs/card_format_spec.md` for the formal spec.

### Cross-cutting concepts (`skills/cross_cutting_concepts.md`)
Unifying principles (effective stress, diffusion, power laws, ambient field exploitation, critical zone, digital twins) and four anchor NAS reports. Read this when no single discipline file has the bridge you need.

### Agent playbook (`skills/agent_playbook.md`)
The meta-procedure: how the chatbot should structure its reasoning for paper interpretation, integration suggestions, and disambiguation queries. Refusal patterns for forced analogies live here.

## Current status (v3)

| Component | Status |
|---|---|
| Eval set (60 QAs, 9 disciplines, xlsx + JSON) | ✅ complete |
| Pipeline (drafting + critique) | ✅ complete |
| Cross-cutting concepts skill | ✅ complete |
| Card format spec (`docs/card_format_spec.md`) | ✅ **v3 complete** |
| Hydrology — long-form card pattern | ✅ **v3 complete** (9 concept / 7 method / 5 phenomenon / 6 translation cards including TC-01 through TC-06) |
| Hydrology — short summary | ✅ complete |
| Seismology — long-form card pattern | ✅ **v3 complete** |
| Seismology — short summary | ✅ complete |
| Geotechnical engineering — long-form card pattern | ✅ **v3 complete** (7 concept / 7 method / 4 phenomenon / 3 translation cards including TC-10, TC-11, TC-12) |
| Geotechnical engineering — short summary | ✅ complete |
| Other 5 disciplines (geomorphology, atmospheric sciences, ecology, agricultural sciences, near-surface geophysics) — long-form card pattern | 🟡 v2 legacy; awaiting v3 restructuring |
| Other 5 disciplines — short summaries | 🟡 not yet written |
| Agent playbook | 🟢 vocab table covers hydro + seismo + geotech; needs extension as remaining disciplines land |
| Co-retrieval index | 🟢 hydrology + seismology + geotechnical_engineering entries; remaining disciplines to follow |
| RAG retrieval layer | 🔲 not yet built |
| Paper corpus | 🔲 not yet built |

## Roadmap

See `docs/roadmap.md` for the prioritized plan from here to a full-blown eval set with expert engagement. Phase 1 (unblocking hydrology) is the critical path; phases 2–8 cover the remaining discipline corpora, the RAG retrieval layer, the eval-set expansion, the expert review platform, and public release.

## Evaluation platform

See `eval_platform/` for the v1 expert-evaluation platform (Sheets + Form-based; generalizable to coding-agent evals and future LLM/MoE work). Contents include the kickoff meeting agenda, the reviewer instructions doc, the per-reviewer scoring spreadsheet template, the signup-form question set, and three calibration QAs. `eval_platform/README.md` is the entry point.

## How to contribute

See `CONTRIBUTING.md`. The short version: pick a discipline, follow the card format spec, file a PR with new cards or revisions. Each card should be ≤200 words, self-contained, and cite at least one anchor paper with DOI.

## License

- **Code** (pipeline, scripts): MIT License.
- **Content** (skill files, cards, eval dataset): CC-BY-4.0.

See `LICENSE` for full text.

## Acknowledgements

This work is part of the Gaia / Agentic Earth initiative at the University of Washington, supported by NSF (EAR-2346079) and related awards. The eval set and skill files were drafted with Claude Opus 4.7 and curated by the Denolle Group.

## Citation

If you use this repository in published work, please cite as:

> Denolle, M., et al. (2026). Gaia translator: cross-disciplinary geoscience skill files and evaluation set. *GitHub repository*. https://github.com/<YOUR_GITHUB_URL>/gaia-translator
