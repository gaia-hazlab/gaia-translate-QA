# Phase 4 output schema — Gaia translator tool

**Status**: draft v0.1; subject to a single locking round between Derek (tool builder) and the eval-platform owner before Phase 4 inference runs start.

**Why this document exists.** The Phase 4 tool produces structured output that is consumed downstream by the eval platform (Phase 6 onward). The schema is the *contract* between the tool and the eval. Schema drift after the eval has started invalidates the calibration round and forces a re-run, so we lock it now.

This document is intended to be self-contained — a graduate-student software engineer should be able to start building the Phase 4 tool from this spec without needing additional context.

---

## 1. Tool overview

**Phase 4 tool**: a single-shot Python CLI / library that takes a research question (always) plus an optional document (PDF or URL/HTML) and returns a structured translation organized by the four card categories plus a free-form user-specific response.

**Inputs**:

| Field | Required | Type | Notes |
|---|---|---|---|
| `prompt` | Yes | string | The user's research question or translation request. |
| `paper` | Optional | file path | PDF; Claude has native PDF support, no separate extraction needed. |
| `url` | Optional | URL string | Fetched via web tool and passed as HTML/text. |

`paper` and `url` are mutually exclusive; at most one document per inference for v1. Multi-document is a future extension.

**Outputs**: a single JSON document (see Section 2) plus an optional Markdown rendering for human display.

**Architecture (one-line)**: prompt + optional doc → vocabulary disambiguator → skill-loaded Claude inference → structured JSON output → citation-discipline guardrail post-check → logged response.

**Where the tool sits**: it's the working chatbot for Phase 7 expert evaluation. Reviewers will score outputs from this tool against the 8-criterion rubric in `eval_platform/`.

---

## 2. The schema (canonical specification)

Pydantic v2 reference implementation. This is the source-of-truth; the JSON Schema export in Section 8 is generated from this.

```python
from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


# ============================================================================
# Enums
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
    cross_cutting = "cross_cutting"   # for queries that aren't discipline-specific


class QueryType(str, Enum):
    paper_interpretation = "paper-interpretation"
    integration = "integration"
    vocabulary_disambiguation = "vocabulary-disambiguation"
    refusal_test = "refusal-test"
    joint_observation = "joint-observation"
    other = "other"


class DocumentType(str, Enum):
    pdf = "pdf"
    url = "url"
    html_text = "html_text"
    none = "none"


class Confidence(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class RefusalType(str, Enum):
    forced_analogy = "forced-analogy"
    vocabulary_collision = "vocabulary-collision"
    different_regime = "different-regime"
    missing_causality = "missing-causality"
    outside_grounded_knowledge = "outside-grounded-knowledge"
    fabrication_prevention = "fabrication-prevention"
    surface_power_law_collision = "surface-power-law-collision"
    other = "other"


# ============================================================================
# Sub-objects
# ============================================================================

class InputDocument(BaseModel):
    """Metadata about the document the user supplied (if any)."""
    type: DocumentType
    source: Optional[str] = Field(
        None,
        description="File path for PDF, URL for url, 'inline' for html_text, None for type=none."
    )
    title: Optional[str] = Field(
        None,
        description="Extracted from document content; may be inferred if the document lacks an explicit title."
    )
    extracted_text_summary: Optional[str] = Field(
        None,
        description="1-3 sentence summary of the document content. Useful for eval-set quality control and reviewer spot-checking."
    )
    token_count: Optional[int] = Field(
        None,
        description="Approximate token count of the document as ingested into the inference context."
    )


class CardMatch(BaseModel):
    """A single card that the translator identifies as relevant."""
    card_id: str = Field(
        ...,
        pattern=r"^(CC|MC|PD|TC)-[A-Za-z0-9_-]+$",
        description="Must exist in skills/co_retrieval_index.yaml."
    )
    title: str = Field(..., description="The card's headline title as it appears in the card file.")
    discipline: Discipline
    relevance: str = Field(
        ...,
        max_length=600,
        description="1-3 sentences on how this card connects to the user's query and/or the supplied document."
    )
    confidence: Confidence = Field(
        ...,
        description="How confident is the agent that this card is genuinely relevant? Reviewers can downgrade scoring on low-confidence matches."
    )
    anchor_citations_cited: List[str] = Field(
        default_factory=list,
        description="DOIs (or 'Author Year' for DOI-less works) from this card that the agent specifically referenced in user_specific_response. Empty list if the card was identified as relevant but not directly cited."
    )


class VocabularyCollision(BaseModel):
    """A polysemous term that needed disambiguation in the response."""
    term: str = Field(..., description="The polysemous term, e.g., 'Q' or 'permeability'.")
    interpretations: List[dict] = Field(
        ...,
        description=(
            "List of {discipline, meaning} dicts giving the candidate interpretations. "
            "Pulled from skills/agent_playbook.md vocabulary table."
        )
    )
    chosen_interpretation: Optional[str] = Field(
        None,
        description=(
            "Which interpretation the agent went with, or None if it explicitly refused to choose "
            "(in which case there should be a corresponding entry in refusals_or_caveats)."
        )
    )
    disambiguation_basis: str = Field(
        ...,
        max_length=300,
        description="Why the agent picked this interpretation (or refused). E.g., 'document context indicates seismology'."
    )


class RefusalOrCaveat(BaseModel):
    """An explicit refusal or scientific caveat the agent applied."""
    type: RefusalType
    description: str = Field(
        ...,
        max_length=600,
        description="What the agent refused or caveat-ed and why."
    )
    cards_invoked: List[str] = Field(
        default_factory=list,
        description=(
            "Card IDs whose refusal pattern was applied (e.g., TC-04 for surface power-law collisions). "
            "May reference a section of agent_playbook.md if no specific card applies, in which case "
            "use the string 'agent_playbook.md#section-name'."
        )
    )


class TokenCounts(BaseModel):
    input: int
    output: int
    total: int


# ============================================================================
# Top-level schema
# ============================================================================

class GaiaTranslatorResponse(BaseModel):
    """The single structured output of one Phase 4 inference."""

    # --- Provenance / metadata ---
    schema_version: Literal["1.0"] = "1.0"
    tool_version: str = Field(..., description="Semver of the gaia-translator tool, e.g., '0.1.0'.")
    corpus_version: str = Field(
        ...,
        description="Git SHA of the gaia-translate-QA repo at inference time. Used for reproducibility — a card-revision in the future will produce a different output for the same input."
    )
    model: str = Field(
        ...,
        description="Exact Claude model identifier, e.g., 'claude-opus-4-7'."
    )
    inference_timestamp: datetime
    inference_duration_seconds: float
    token_counts: TokenCounts
    cost_usd: Optional[float] = Field(
        None,
        description="Computed from token_counts and the model's pricing at inference time. Optional but useful for budget tracking."
    )

    # --- Input echo ---
    user_query: str = Field(..., description="The user's prompt, verbatim.")
    input_document: InputDocument

    # --- Routing / classification ---
    primary_disciplines_detected: List[Discipline] = Field(
        ...,
        min_length=1,
        description=(
            "Disciplines the agent identified as primary for this query. "
            "Used by reviewers for assignment routing in the eval platform."
        )
    )
    query_type: QueryType = Field(
        ...,
        description="Which of the four agent-playbook flows (plus 'other') this query falls into."
    )

    # --- The four card-category matches ---
    concept_matches: List[CardMatch] = Field(default_factory=list)
    method_matches: List[CardMatch] = Field(default_factory=list)
    phenomenon_matches: List[CardMatch] = Field(default_factory=list)
    translation_matches: List[CardMatch] = Field(default_factory=list)

    # --- Vocabulary and refusal handling ---
    vocabulary_collisions_flagged: List[VocabularyCollision] = Field(default_factory=list)
    refusals_or_caveats: List[RefusalOrCaveat] = Field(default_factory=list)

    # --- The free-form synthesis ---
    user_specific_response: str = Field(
        ...,
        description=(
            "Markdown-formatted, the direct answer to the user's question. "
            "Must cite only DOIs / works that appear in either the loaded skill context "
            "or the input_document. Citation-discipline guardrail (Section 4) checks this."
        )
    )

    # --- Optional: model self-report ---
    suggested_followup_cards: List[str] = Field(
        default_factory=list,
        description="Card IDs the agent suggests as productive next reading; not necessarily directly relevant to the immediate query."
    )
    suggested_next_step: Optional[str] = Field(
        None,
        max_length=400,
        description=(
            "If the user is researching the topic further, one concrete recommended next action: "
            "a specific paper to read, a dataset to look at, an instrument network to query, "
            "an external collaborator to talk to."
        )
    )

    class Config:
        # Allows extra fields for forward-compatibility but doesn't validate them.
        extra = "allow"
```

---

## 3. Field-by-field semantics

### 3.1 Provenance / metadata

- **`schema_version`**: bump on any breaking change. v1.0 is the target for Phase 4 v0.1.
- **`tool_version`**: Phase 4 tool's own semver. Increments independently of the corpus.
- **`corpus_version`**: git SHA of `gaia-translate-QA` at inference. Required for reproducibility — the eval will be re-run on revised cards in Phase 8, and we need to attribute differences to corpus revisions vs. tool revisions.
- **`model`**: exact model string. If we A/B Opus vs. Sonnet vs. Haiku, this is the discriminator.
- **`token_counts`**: input includes the full skill-loaded context. Useful for monitoring whether skill loading is hitting the model's limits.
- **`cost_usd`**: optional but recommended; auto-compute from token counts using a small pricing table in the tool.

### 3.2 Input echo

- **`user_query`**: verbatim user prompt. Don't pre-process; the disambiguator's output should be reflected in `vocabulary_collisions_flagged`, not in the echoed query.
- **`input_document`**: even when `type == none`, populate this with `type="none"` and `source=None`; downstream consumers expect the field to always exist.
- **`extracted_text_summary`**: write 1–3 sentences. Used by eval reviewers to spot-check that the document was correctly ingested; also indexed by the eval-platform progress tracker.

### 3.3 Routing / classification

- **`primary_disciplines_detected`**: ≥1 discipline; cap at 4. The eval-platform owner will use this to route the QA to the appropriate reviewer pool.
- **`query_type`**: one of the four agent-playbook flows or "other". Used in eval to verify that the eval set has reasonable distribution across query types (Phase 6 target: ~40% paper-interpretation, ~25% integration, ~15% vocabulary, ~10% refusal-test, ~10% joint-observation).

### 3.4 The four card-category matches

These are the core of the structured output. Each list is *ordered by the agent's judgment of relevance*, most relevant first.

**Match rules** (the agent's contract):

- A card appears in `concept_matches` if it's a `CC-*` card. Same for MC, PD, TC.
- Cards that are loaded into context but *not used* in the response should not appear here. Only cards the agent considered actively relevant.
- An agent should typically return 2–8 matches per category for a paper-interpretation query; fewer for narrow queries; possibly zero for some categories (e.g., a vocabulary-disambiguation query might have no PD matches).
- Hard cap: 20 matches per category. If the agent thinks more than 20 cards are relevant, it's not differentiating enough; the post-check will warn.

**Per-match required fields**:

- `card_id`: must validate against `skills/co_retrieval_index.yaml`. Validation rule: lookup must succeed.
- `title`: copy the title from the card file. Validation rule: title must match the card's actual `## CC-...: Title` heading (allow slight rewording, but they should be substantially the same).
- `discipline`: pulled from the card's frontmatter.
- `relevance`: 1–3 sentences specific to *this query / document*. Generic "this card is about X" is not sufficient. Reviewers will downgrade scoring for unspecific relevance statements.
- `confidence`: high / medium / low. Medium is the default; high is reserved for cards the agent is very confident apply; low signals "this card seemed plausible but I'm not certain". Reviewers can use confidence to interpret scoring.
- `anchor_citations_cited`: the DOIs from this card's `Anchor citations` section that the agent specifically pulled into `user_specific_response`. Empty list is fine — sometimes a card is referenced but the agent doesn't directly cite the anchor paper.

### 3.5 Vocabulary collisions

Populate this list when the user's query (or the document) contains a term flagged in `skills/agent_playbook.md`'s vocabulary table. For each collision:

- List all the candidate interpretations from the playbook.
- State which one the agent picked.
- Briefly justify the choice (document context, user discipline, query phrasing).

If the agent cannot reliably pick, set `chosen_interpretation = None` and *also* create a matching entry in `refusals_or_caveats` with `type = vocabulary-collision`.

### 3.6 Refusals and caveats

The agent's explicit "I won't make this claim" or "with this caveat" actions. Each entry maps a refusal pattern from `agent_playbook.md` Section "Refusal patterns" to the specific instance.

Common types:

- **`forced-analogy`**: refused to assert cross-discipline equivalence based on verbal similarity (e.g., Gutenberg-Richter vs. flood-frequency power laws). Almost always invokes `TC-04`.
- **`vocabulary-collision`**: paired with a `VocabularyCollision` entry where the agent declined to pick.
- **`different-regime`**: refused to apply an equation outside its regime (e.g., Darcy's law in karst flow).
- **`missing-causality`**: noted correlation without endorsing the proposed causal mechanism.
- **`outside-grounded-knowledge`**: the question requires information not present in the loaded skill context or the user-supplied document; agent acknowledges and suggests escalation.
- **`fabrication-prevention`**: the agent caught itself almost making up a citation or fact and refused; rare but worth logging.
- **`surface-power-law-collision`**: specifically the G-R vs. landslide-size vs. flood-frequency vs. Hack's-law refusal pattern.

### 3.7 User-specific response

The free-form Markdown synthesis. This is the section reviewers will read most carefully.

**Style guidance** (the agent should follow this in its system prompt):

- Direct, technical, citation-anchored. Audience: geoscience researchers.
- Lead with the answer; details follow.
- Cite using `[Author, Year](doi:...)` style inline.
- *Only cite DOIs that appear in either*:
  - (a) the loaded skill context (the card bodies and their anchor citations), or
  - (b) the input document.
- Cross-reference the card-category match lists by `card_id` when relevant: "(see `CC-seismo-Vs`)".

**Length**: typically 300–800 words for a paper-interpretation query; 200–500 for a vocabulary-disambiguation query.

### 3.8 Optional model self-report

- **`suggested_followup_cards`**: cards the agent suggests as next reading. Distinct from the four match lists — these are *recommendations* rather than *uses*.
- **`suggested_next_step`**: a concrete action (a specific paper, dataset, instrument network, collaborator). Reviewers value this; it's the "what should I do with this answer" handoff.

---

## 4. Validation rules and the citation-discipline guardrail

These are post-inference checks applied by the tool before returning a response. Failures are logged and surfaced in the response (under a `_validation` field if it's present); reviewers can choose to score normally or flag.

### 4.1 Schema-level

1. All required fields present.
2. `primary_disciplines_detected` is non-empty and a subset of the `Discipline` enum.
3. Every `card_id` in any match list exists in `skills/co_retrieval_index.yaml`.
4. Every `card_id` in `refusals_or_caveats[].cards_invoked` either exists in the index or starts with `agent_playbook.md#`.
5. `vocabulary_collisions_flagged[].chosen_interpretation = None` implies a matching `refusals_or_caveats` entry with `type = vocabulary-collision`.

### 4.2 Citation-discipline guardrail

The single most important post-inference check.

**Procedure**:

1. Extract every DOI (regex: `10\.\d{4,9}/[-._;()/:A-Za-z0-9]+`) from `user_specific_response`.
2. For each extracted DOI:
   - Look it up in the union of:
     - All anchor citations in the loaded skill context (all card bodies).
     - All DOIs present in the input document (if any).
   - If the DOI is found in either context: ✅ valid citation.
   - If not found: 🚨 potential fabrication.
3. Also extract `Author Year` style citations (for DOI-less works) and apply the same check using lightweight string matching against the same union.
4. If any potential-fabrication citation is detected, the tool appends a `_validation` field to the response:

   ```json
   "_validation": {
     "status": "warning",
     "fabrication_candidates": [
       {"citation": "10.xxxx/yyyy", "extracted_from": "user_specific_response", "found_in_context": false}
     ]
   }
   ```

5. The tool does *not* automatically reject the response — fabrication candidates are flagged for human review. Reviewers in the eval will lower Citation-discipline scoring accordingly.

### 4.3 Internal-consistency checks

6. Cards listed in `anchor_citations_cited` should have those DOIs present in the actual card file. Validation script: parse the card file's `Anchor citations` section, compare.
7. `query_type` should be plausibly consistent with `vocabulary_collisions_flagged` and `refusals_or_caveats` (e.g., a `refusal-test` query type should have at least one entry in `refusals_or_caveats`).
8. Card-match count caps (≤ 20 per category) enforced.

### 4.4 Token-budget sanity

9. `token_counts.input + output` should match (within ~5%) the model's reported usage. Validation against the model's `usage` object.

---

## 5. Three worked examples

These mirror the three calibration QAs in `eval_platform/calibration_qas/calibration_set_v1.md`. Use these as the golden test cases for the tool's first end-to-end validation.

### 5.1 QA-CAL-01 — clearly good (paper interpretation)

**Input**:
```python
prompt = ("I just read Boulanger & Idriss (2014) on CPT and SPT liquefaction-"
          "triggering procedures. I'm a seismologist working on the Nisqually "
          "basin and I want to understand how this connects to my work on Vs30 "
          "and ambient-noise dv/v. What should I take away?")
paper = None   # Or could supply the PDF; either works
```

**Expected output** (illustrative, abbreviated):
```json
{
  "schema_version": "1.0",
  "tool_version": "0.1.0",
  "corpus_version": "fb0cfd2",
  "model": "claude-opus-4-7",
  "inference_timestamp": "2026-06-15T14:23:11Z",
  "inference_duration_seconds": 12.4,
  "token_counts": {"input": 78240, "output": 1840, "total": 80080},
  "cost_usd": 1.42,

  "user_query": "I just read Boulanger & Idriss (2014)...",
  "input_document": {"type": "none", "source": null, "title": null, "extracted_text_summary": null, "token_count": null},

  "primary_disciplines_detected": ["geotechnical_engineering", "seismology"],
  "query_type": "integration",

  "concept_matches": [
    {
      "card_id": "CC-geotech-CSR-CRR",
      "title": "Cyclic stress ratio CSR and cyclic resistance ratio CRR",
      "discipline": "geotechnical_engineering",
      "relevance": "Boulanger & Idriss (2014) defines the operational CSR/CRR framework. CSR includes a_max from the user's seismology work; CRR is computed from in-situ tests (SPT, CPT) or Vs1.",
      "confidence": "high",
      "anchor_citations_cited": ["10.1061/JSFEAQ.0001662"]
    },
    {
      "card_id": "CC-seismo-Vs",
      "title": "Shear-wave velocity Vs and Vs30",
      "discipline": "seismology",
      "relevance": "Vs1 from MASW or seismic CPT feeds the Vs-based CRR curve (Andrus-Stokoe 2000); this is the user's direct entry point.",
      "confidence": "high",
      "anchor_citations_cited": ["10.1061/(ASCE)1090-0241(2000)126:11(1015)"]
    },
    {
      "card_id": "CC-geotech-G-Gmax",
      "title": "Modulus reduction G/Gmax and damping ratio ξ(γ)",
      "discipline": "geotechnical_engineering",
      "relevance": "Transient G/Gmax reduction explains coseismic dv/v signals; the bridge to the user's ambient-noise work.",
      "confidence": "medium",
      "anchor_citations_cited": []
    }
  ],

  "method_matches": [
    {
      "card_id": "MC-geotech-CPT",
      "title": "Cone Penetration Test and seismic CPT",
      "discipline": "geotechnical_engineering",
      "relevance": "Seismic CPT directly produces Vs1 alongside CPT q_c; the operational measurement underlying the framework.",
      "confidence": "high",
      "anchor_citations_cited": []
    },
    {
      "card_id": "MC-seismo-MASW",
      "title": "Multichannel analysis of surface waves",
      "discipline": "seismology",
      "relevance": "MASW Vs profile vs. seismic CPT Vs profile is the depth-regime question the user should ask for Nisqually.",
      "confidence": "high",
      "anchor_citations_cited": []
    },
    {
      "card_id": "MC-geotech-GMPE",
      "title": "Ground motion prediction equations",
      "discipline": "geotechnical_engineering",
      "relevance": "a_max input to CSR comes from NGA-West2 / NGA-Sub; the user's seismicity model feeds this directly.",
      "confidence": "high",
      "anchor_citations_cited": ["10.1193/070113EQS184M"]
    }
  ],

  "phenomenon_matches": [
    {
      "card_id": "PD-liquefaction",
      "title": "Earthquake-induced liquefaction",
      "discipline": "seismology",
      "relevance": "Nisqually 2001 is the canonical PNW case; the digital-twin anchor.",
      "confidence": "high",
      "anchor_citations_cited": []
    },
    {
      "card_id": "PD-site-response",
      "title": "Nonlinear site response and basin effects",
      "discipline": "geotechnical_engineering",
      "relevance": "Basin amplification needs Vs profile beyond the upper 30 m; relevant to the user's ambient-noise tomography work.",
      "confidence": "medium",
      "anchor_citations_cited": []
    }
  ],

  "translation_matches": [
    {
      "card_id": "TC-10",
      "title": "Linear seismology ↔ nonlinear geotechnical site response",
      "discipline": "geotechnical_engineering",
      "relevance": "The user's ambient-noise dv/v lives in the linear-elastic regime; CSR/CRR is the nonlinear engineering counterpart. TC-10 is the bridge.",
      "confidence": "high",
      "anchor_citations_cited": []
    },
    {
      "card_id": "TC-12",
      "title": "Vs across depth regimes — geotech borehole, NSG/MASW, seismic tomography",
      "discipline": "geotechnical_engineering",
      "relevance": "Vs at 0-30 m (CPT-Vs) vs. 5-50 m (MASW) vs. 0.1-10 km (ambient-noise tomography) is THE Nisqually integration problem; TC-12 frames it directly.",
      "confidence": "high",
      "anchor_citations_cited": ["10.1785/0120030105", "10.1126/science.1108339"]
    },
    {
      "card_id": "TC-02",
      "title": "Effective stress unifies hydrology, geotechnical engineering, and seismology",
      "discipline": "hydrology",
      "relevance": "Underlies liquefaction (σ' → 0 mechanism); the deep bridge underneath the CSR/CRR framework.",
      "confidence": "medium",
      "anchor_citations_cited": []
    }
  ],

  "vocabulary_collisions_flagged": [],

  "refusals_or_caveats": [],

  "user_specific_response": "**Three direct connections from Boulanger & Idriss (2014) back to your seismology work**:\n\n1. **Your a_max feeds CSR directly**. CSR = 0.65 (a_max/g)(σ_v0/σ'_v0) r_d (see `CC-geotech-CSR-CRR`). The peak ground acceleration comes from NGA-West2 or NGA-Sub GMPEs ([Boore et al. 2014](https://doi.org/10.1193/070113EQS184M)), which your seismicity model and ground-motion simulations parameterize. The link is mechanical: better seismology → better CSR.\n\n2. **Vs1 → CRR via Andrus–Stokoe (2000)** ([doi:10.1061/(ASCE)1090-0241(2000)126:11(1015)](...)). The Vs-based triggering curve uses your `CC-seismo-Vs` but only in the upper 30 m (`CC-geotech-Vs30` regime in `TC-12`). For Nisqually, your basin Vs profiles from MASW and ambient-noise tomography give different shallow Vs than the borehole control, and the Vs-based curve is sensitive to which you trust.\n\n3. **dv/v is a coseismic/postseismic monitor, not a pre-event triggering indicator**. dv/v decreases of 10⁻⁴ to 10⁻³ are routinely observed after strong shaking, partly reflecting transient G/Gmax reduction (`CC-geotech-G-Gmax`, `TC-10`). Useful for tracking post-event recovery of site stiffness; not predictive of CRR at a never-tested site.\n\n**Recommended next step**: a joint inversion combining MASW (`MC-seismo-MASW`), ambient-noise tomography (`MC-seismo-ambient-noise`), and CPT-Vs (`MC-geotech-CPT`) into one profile resolving the 50 m – 1 km 'missing middle' (`TC-12`). Boulanger–Idriss CSR/CRR uses only the upper-30 m portion; basin amplification (`PD-site-response`) needs the full profile.",

  "suggested_followup_cards": ["TC-08", "PD-megathrust"],
  "suggested_next_step": "Read Boulanger & Idriss (2014) Section 4 on Vs-based triggering; then propose a single seismic CPT (SCPT) location in the Nisqually basin to anchor the depth-regime joint inversion."
}
```

### 5.2 QA-CAL-02 — clearly bad (vocabulary collision; refusal expected)

**Input**:
```python
prompt = ("Can seismic attenuation Q tell me about streamflow Q in a watershed? "
          "They have the same symbol, so there should be some kind of relation "
          "I can exploit. What papers explore this?")
paper = None
```

**Expected output** (the tool *must* refuse):

```json
{
  "primary_disciplines_detected": ["seismology", "hydrology"],
  "query_type": "vocabulary-disambiguation",
  "concept_matches": [
    {
      "card_id": "CC-seismo-Q",
      "title": "Seismic attenuation Q",
      "discipline": "seismology",
      "relevance": "Dimensionless attenuation parameter; entirely different physics from streamflow.",
      "confidence": "high",
      "anchor_citations_cited": []
    },
    {
      "card_id": "CC-hydro-Q",
      "title": "Streamflow Q and baseflow",
      "discipline": "hydrology",
      "relevance": "Volumetric discharge [m³/s]; entirely different physics from seismic attenuation.",
      "confidence": "high",
      "anchor_citations_cited": []
    }
  ],
  "method_matches": [],
  "phenomenon_matches": [],
  "translation_matches": [],
  "vocabulary_collisions_flagged": [
    {
      "term": "Q",
      "interpretations": [
        {"discipline": "seismology", "meaning": "Quality factor for seismic attenuation, dimensionless"},
        {"discipline": "hydrology", "meaning": "Streamflow, volumetric discharge [m³/s]"}
      ],
      "chosen_interpretation": null,
      "disambiguation_basis": "User explicitly asks about the connection between the two — the agent must refuse rather than choose."
    }
  ],
  "refusals_or_caveats": [
    {
      "type": "vocabulary-collision",
      "description": "Seismic Q and streamflow Q share a symbol, not physics. No causal or methodological relation exists. The agent refuses to assert a relation.",
      "cards_invoked": ["CC-seismo-Q", "CC-hydro-Q", "agent_playbook.md#refusal-patterns"]
    },
    {
      "type": "fabrication-prevention",
      "description": "User asks for 'papers that explore this'. No such papers exist in the loaded context; the agent refuses to invent citations.",
      "cards_invoked": ["agent_playbook.md#citation-discipline"]
    }
  ],
  "user_specific_response": "The two Q's share a symbol but not physics, and there is no mechanistic relation between them.\n\n- **Seismic Q** (`CC-seismo-Q`) is the dimensionless quality factor for seismic attenuation: 1/Q ∝ energy dissipated per cycle. Defined for P-waves (Qp), S-waves (Qs), as intrinsic vs. scattering. Typical crustal Qs is 50–300.\n- **Streamflow Q** (`CC-hydro-Q`) is the volumetric water discharge through a stream cross-section, with units of m³/s, computed at gauging stations from stage and a rating curve.\n\nThese are different physical quantities measured by different instruments, with different units, on different timescales. No causal or methodological relation exists — and importantly, no paper genuinely 'exploits' a connection between them, despite occasional speculation in seminars.\n\nIf you have an underlying physical question that prompted this — for example, 'can ambient seismic noise tell me anything about a watershed' — the productive answer is `TC-03` (dv/v as a hydrology proxy via storage and pore-pressure changes), which is a real bridge through `CC-seismo-dvv` and `CC-hydro-S`. That is mechanistically grounded in poroelasticity; the Q-Q symbol coincidence is not.",
  "suggested_followup_cards": ["TC-03", "CC-seismo-dvv", "CC-hydro-S"],
  "suggested_next_step": "If you're interested in any genuine seismology↔hydrology bridge, start with `TC-03` and Clements & Denolle (2018) for the dv/v ↔ groundwater storage example."
}
```

### 5.3 QA-CAL-03 — contested (no document; complex multi-discipline integration)

**Input**:
```python
prompt = ("Can I replace groundwater-monitoring well networks in California with "
          "ambient seismic noise dv/v? I'm building a proposal to deploy dense "
          "seismic arrays in the Central Valley and I want to claim dv/v as a "
          "hydrology product.")
paper = None
```

**Expected output** (illustrative, abbreviated — full version generated by the tool):

```json
{
  "primary_disciplines_detected": ["seismology", "hydrology"],
  "query_type": "joint-observation",
  "concept_matches": [
    {"card_id": "CC-seismo-dvv", "title": "...", "discipline": "seismology", "relevance": "...", "confidence": "high", "anchor_citations_cited": ["10.1029/2018GL077706", "10.1038/s41598-017-14468-9"]},
    {"card_id": "CC-hydro-S", "title": "...", "discipline": "hydrology", "relevance": "...", "confidence": "high", "anchor_citations_cited": []},
    {"card_id": "CC-hydro-h", "title": "...", "discipline": "hydrology", "relevance": "...", "confidence": "medium", "anchor_citations_cited": []}
  ],
  "method_matches": [
    {"card_id": "MC-seismo-ambient-noise", "title": "...", "discipline": "seismology", "relevance": "...", "confidence": "high", "anchor_citations_cited": ["10.1029/2006GL027797"]},
    {"card_id": "MC-hydro-NWIS", "title": "...", "discipline": "hydrology", "relevance": "...", "confidence": "high", "anchor_citations_cited": []}
  ],
  "phenomenon_matches": [
    {"card_id": "PD-aquifer-depletion", "title": "...", "discipline": "hydrology", "relevance": "Central Valley canonical case.", "confidence": "high", "anchor_citations_cited": []}
  ],
  "translation_matches": [
    {"card_id": "TC-03", "title": "Ambient seismic noise as hydrology proxy (dv/v)", "discipline": "seismology", "relevance": "The bridge the user is invoking; this card spells out exactly what dv/v can and cannot recover.", "confidence": "high", "anchor_citations_cited": []}
  ],
  "vocabulary_collisions_flagged": [],
  "refusals_or_caveats": [
    {
      "type": "different-regime",
      "description": "dv/v at typical 0.5-5 Hz bands integrates over tens of meters and recovers a *relative* signal; it cannot replace point-source aquifer-head measurements at known wellhead depths without site-specific calibration.",
      "cards_invoked": ["TC-03"]
    }
  ],
  "user_specific_response": "Short version: **dv/v complements well networks but cannot replace them at the Central Valley scale you're proposing.** Three reasons, with citations to ground them...\n\n[full markdown response, ~600 words, citing Sens-Schönfelder & Wegler 2006 / Clements & Denolle 2018 / Lecocq et al. 2017 / Hillers et al. 2015 — all of which appear in the loaded context]"
}
```

---

## 6. Open decisions

These need to be resolved between Derek and the eval-platform owner before locking the schema:

1. **Confidence levels — discrete or continuous?** Spec currently uses `high / medium / low` (Confidence enum). Alternative: 0–100 numeric confidence. Recommendation: discrete is more eval-friendly and less prone to model over-confidence; numerical values can always be added later without breaking the schema. ✅ Lock as discrete.

2. **Multi-document support — explicit no for v1?** Spec currently allows at most one `paper` or `url` per inference. Future extension for v2 should be backward-compatible (add a `documents: List[InputDocument]` alongside or in place of `input_document`). Recommendation: v1 single-document only.

3. **Streaming vs. blocking inference**. Spec doesn't specify. For the eval-batch use case (Phase 6 / 7), blocking is simpler. For the Gradio demo, streaming is the better UX. Recommendation: implement blocking first; add streaming as a wrapper in the Gradio adapter only.

4. **Card-match cap — 20 per category?** Hard cap. If the agent is identifying > 20 cards as relevant to a single query, it's probably under-differentiating. Some `paper-interpretation` queries on rich papers might legitimately approach this; we can revisit if needed.

5. **`anchor_citations_cited` tracking — required or optional?** Spec marks as required (default empty list). Tracking which specific DOIs the agent pulls from each card is what makes the citation-discipline guardrail tractable. Recommendation: keep required.

6. **`cost_usd` — required or optional?** Currently optional. Useful for budget tracking but not for evaluation. Recommendation: optional, but the tool should compute and populate it whenever possible.

7. **Logging — file-per-inference or single append-only log?** Operational concern. Recommendation: file-per-inference (`logs/<inference_uuid>.json`) for ease of debugging; an aggregator script combines them for batch analysis.

8. **Markdown rendering — included in the JSON or generated by a separate renderer?** Recommendation: keep the JSON pure; a separate `render_markdown.py` (or Jinja template) produces human-readable output. This separates the canonical data from the presentation.

---

## 7. Coordination with the eval platform

The Phase 4 output JSON maps directly to the columns in `eval_platform/templates/scoring_template.xlsx`. Mapping:

| Schema field | Spreadsheet column | Per-section scoring? |
|---|---|---|
| `user_query` | `Question` | — |
| `input_document.extracted_text_summary` | `Cited_Context` (prepended) | — |
| `primary_disciplines_detected` | `Discipline` | — |
| `query_type` | `Query type` | — |
| `concept_matches` | inline in `Model_Answer` + S1/S2/S3 per-section | yes |
| `method_matches` | inline in `Model_Answer` + S1/S2/S3 per-section | yes |
| `phenomenon_matches` | inline in `Model_Answer` + S1/S2/S3 per-section | yes |
| `translation_matches` | inline in `Model_Answer` + S4 (cross-discipline integration) | yes |
| `vocabulary_collisions_flagged` | inline in `Model_Answer` + S3 (vocabulary precision) | yes |
| `refusals_or_caveats` | inline in `Model_Answer` + S5 (refusal correctness) | yes |
| `user_specific_response` | inline in `Model_Answer` + S6/S7/S8 (completeness, presentation, overall) | yes |
| `_validation.fabrication_candidates` | Reviewer flag + S2 (citation discipline) | yes |
| `suggested_next_step` | inline in `Model_Answer` | — |
| `corpus_version`, `tool_version`, `model` | Provenance metadata (hidden columns in the spreadsheet) | — |

Per-section scoring means: the 8 criteria can be scored *on each card-category section as well as overall*. This is a refinement of the v1 rubric and likely improves IRR. Document the rubric expansion in `eval_platform/STRATEGY.md` (private) before the calibration round.

**A small QA-generator change**: the Phase 6 eval-set v3 generator should produce QAs in a format that matches this schema's input contract — `prompt` plus optional `paper` / `url`. The expected-answer specification should reference the structured output, e.g., "expected concept_matches include CC-seismo-Vs and CC-geotech-CSR-CRR."

---

## 8. JSON Schema export (auto-generated from Pydantic)

For interop with non-Python consumers, the Pydantic model in Section 2 generates a JSON Schema document. Derek should produce this as a build artifact:

```python
from gaia_translator.schema import GaiaTranslatorResponse
import json

with open("docs/phase4_output_schema.json", "w") as f:
    json.dump(GaiaTranslatorResponse.model_json_schema(), f, indent=2)
```

Commit this JSON Schema artifact to the repo so external consumers (the Streamlit reviewer app in Phase 7c, any future tools, the methodology paper's supplementary materials) can validate without depending on Python.

---

## 9. Versioning policy

- **Schema version 1.0** for the v1 lock (this document).
- Breaking changes (renaming fields, changing required-ness, changing enum values) → bump major version.
- Additive changes (new optional fields, new enum values added to existing fields) → bump minor version.
- The Phase 4 tool's `schema_version` field reports which schema version its output conforms to. Downstream consumers (eval scoring app, aggregator, eventual paper-companion replication) validate against this.

The eval batch in Phase 6 / 7 will be locked to schema_version 1.0. Schema bumps mid-evaluation invalidate the calibration; if a change is needed, re-run the calibration on a 20-QA subset before proceeding.

---

## 10. Build sequence for Derek (suggested order)

1. **Day 1**: implement the Pydantic schema (Section 2). Validate with synthetic JSON examples.
2. **Day 2–3**: skill-loading. Stuff the full corpus into the system prompt; verify token counts and successful Opus inference on the three calibration QAs.
3. **Day 4–6**: structured-output prompting. Write the system prompt that produces JSON conforming to the schema. Iterate on the three calibration QAs until the output matches the expected structure.
4. **Day 7–8**: PDF and URL ingestion. Test with 5 representative PNW papers.
5. **Day 9–10**: vocabulary disambiguator (pre-inference) and citation-discipline guardrail (post-inference).
6. **Day 11–12**: CLI wrapper (`gaia translate ...`).
7. **Day 13–14**: Gradio demo. Embeddable in `gaia-hazlab.github.io` once stable.

Total: ~3 weeks at sustainable pace, including testing and writing the README for the tool. Less if you can hammer through.

---

**Next step after lock**: Marine + Derek + eval-platform owner do a 30-min sync to:
1. Read this document together.
2. Resolve the 8 open decisions in Section 6.
3. Tag the schema as v1.0 in git (`git tag schema-v1.0`).
4. Update the eval-platform's scoring spreadsheet to surface per-section scoring as described in Section 7.

After that, Derek starts coding.
