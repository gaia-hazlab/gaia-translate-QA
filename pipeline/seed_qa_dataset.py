"""
seed_qa_dataset.py — hand-curated v3 anchor QAs for the Gaia translator eval set.

These QAs are the starting point for Phase 6 (eval set expansion from 60 → 300).
Each QA follows the schema in docs/eval_qa_schema.md. The seed set is intentionally
small (~20-25 QAs) but covers all 9 disciplines and all 5 query types — it sets the
density and style bar that LLM-drafted-then-edited QAs (Phase 6 bulk) should match.

Three calibration QAs (QA-CAL-01/02/03) are duplicated here from
eval_platform/calibration_qas/calibration_set_v1.md so the eval set has a single
canonical source.

Usage
-----
    from pipeline.seed_qa_dataset import SEED_QAS
    print(f"{len(SEED_QAS)} seed QAs")

To produce the JSON eval set, run:
    python pipeline/build_review_spreadsheet.py

Author: Denolle Group, UW ESS.
"""

from __future__ import annotations

from typing import List, Dict


# ============================================================================
# CALIBRATION QAS — duplicated from eval_platform/calibration_qas/calibration_set_v1.md
# ============================================================================

CALIBRATION_QAS: List[Dict] = [
    {
        "id": "QA-CAL-001",
        "schema_version": "v3",
        "primary_disciplines": ["seismology", "geotechnical_engineering"],
        "query_type": "integration",
        "difficulty": 3,
        "prompt": (
            "I just read Boulanger & Idriss (2014) on CPT and SPT liquefaction-triggering "
            "procedures. I'm a seismologist working on the Nisqually basin and I want to "
            "understand how this connects to my work on Vs30 and ambient-noise dv/v. What "
            "should I take away?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Calibration set; clearly-good answer is the target.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-geotech-CSR-CRR",
                "CC-seismo-Vs",
                "CC-geotech-G-Gmax",
            ],
            "method_matches": [
                "MC-geotech-CPT",
                "MC-seismo-MASW",
                "MC-geotech-GMPE",
            ],
            "phenomenon_matches": [
                "PD-liquefaction",
                "PD-site-response",
            ],
            "translation_matches": [
                "TC-10",
                "TC-12",
                "TC-02",
            ],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Explains that a_max from NGA-West2 (the user's GMPE work) feeds CSR directly.",
                "Explains the Vs1 → CRR Andrus-Stokoe link in the upper 30 m, citing the depth-regime issue (TC-12).",
                "Distinguishes coseismic dv/v (G/Gmax transient via TC-10) from pre-event triggering.",
                "Proposes joint MASW + ambient-noise tomography + CPT-Vs as the cross-discipline next step.",
                "Cites Boulanger & Idriss correctly without fabricating other references.",
            ],
            "must_not_say": [
                "ambient-noise dv/v can replace CPT for liquefaction triggering",
                "linear-elastic site response captures G/Gmax reduction at strong ground motion",
            ],
        },
        "status": "approved",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real Nisqually digital-twin conversation",
            "review_notes": "Calibration QA; anchor for clearly-good answer scoring.",
            "last_reviewed_date": "2026-05-14",
            "last_reviewed_by": "Marine",
        },
    },
    {
        "id": "QA-CAL-002",
        "schema_version": "v3",
        "primary_disciplines": ["seismology", "hydrology"],
        "query_type": "vocabulary-disambiguation",
        "difficulty": 2,
        "prompt": (
            "Can seismic attenuation Q tell me about streamflow Q in a watershed? "
            "They have the same symbol, so there should be some kind of relation I can "
            "exploit. What papers explore this?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Calibration set; refusal expected.",
        },
        "expected_output": {
            "concept_matches": ["CC-seismo-Q", "CC-hydro-Q"],
            "method_matches": [],
            "phenomenon_matches": [],
            "translation_matches": ["TC-03"],
            "vocabulary_collisions_flagged": ["Q"],
            "refusals_or_caveats_expected": [
                "vocabulary-collision",
                "fabrication-prevention",
            ],
            "user_specific_response_themes": [
                "Refuses to assert a physical relation between seismic Q and streamflow Q.",
                "Defines each Q distinctly with units (dimensionless vs. m³/s).",
                "Refuses to fabricate citations to support a non-existent relation.",
                "Offers a constructive alternative: TC-03 (dv/v as a real hydrology bridge through poroelasticity).",
            ],
            "must_not_say": [
                "the Q-Q theorem",
                "Smith et al. 2019 Journal of Hydrological Geophysics",
                "wetter sediments have higher attenuation, so streamflow Q correlates with seismic Q",
            ],
        },
        "status": "approved",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Synthetic test case for the refusal pattern",
            "review_notes": "Calibration QA; anchor for clearly-bad answer (anything but refusal is wrong).",
            "last_reviewed_date": "2026-05-14",
            "last_reviewed_by": "Marine",
        },
    },
    {
        "id": "QA-CAL-003",
        "schema_version": "v3",
        "primary_disciplines": ["seismology", "hydrology"],
        "query_type": "joint-observation",
        "difficulty": 4,
        "prompt": (
            "Can I replace groundwater-monitoring well networks in California with "
            "ambient seismic noise dv/v? I'm building a proposal to deploy dense "
            "seismic arrays in the Central Valley and I want to claim dv/v as a "
            "hydrology product."
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Calibration set; contested answer expected (reviewer disagreement is the goal).",
        },
        "expected_output": {
            "concept_matches": ["CC-seismo-dvv", "CC-hydro-h", "CC-hydro-S"],
            "method_matches": ["MC-seismo-ambient-noise", "MC-hydro-NWIS"],
            "phenomenon_matches": ["PD-aquifer-depletion"],
            "translation_matches": ["TC-03"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": ["different-regime"],
            "user_specific_response_themes": [
                "Hedges 'replace' to 'complement' — dv/v cannot fully replace wells at Central Valley scale.",
                "Calibration is site-specific: dv/v → hydrologic state requires local petrophysics.",
                "Thermoelastic and source-distribution effects must be separated (Hillers et al. 2015).",
                "Vertical resolution is coarse: dv/v at 0.5–5 Hz integrates over tens of meters.",
                "Concrete recommendation: dense seismic deployment + a strategically retained well subset.",
            ],
            "must_not_say": [
                "dv/v can fully replace groundwater monitoring wells",
            ],
        },
        "status": "approved",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real NSF proposal-shaping conversation",
            "review_notes": "Calibration QA; reviewer disagreement on the 'replace vs. complement' framing is the productive outcome.",
            "last_reviewed_date": "2026-05-14",
            "last_reviewed_by": "Marine",
        },
    },
]


# ============================================================================
# SINGLE-DISCIPLINE PAPER-INTERPRETATION QAs (one per discipline)
# ============================================================================

PAPER_INTERPRETATION_QAS: List[Dict] = [
    {
        "id": "QA-EVAL-001",
        "schema_version": "v3",
        "primary_disciplines": ["hydrology"],
        "query_type": "paper-interpretation",
        "difficulty": 3,
        "prompt": (
            "I just read Famiglietti (2014) 'The global groundwater crisis' in Nature "
            "Climate Change. I'm an atmospheric-sciences PhD candidate. What's the "
            "essential physics and what should I take away for my own work on climate "
            "projections?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": "Famiglietti 2014 (cited but not attached)",
            "notes": "Seed QA; document not attached but readers know the paper.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-hydro-S",
                "CC-hydro-recharge",
                "CC-hydro-h",
            ],
            "method_matches": [
                "MC-hydro-GRACE",
                "MC-hydro-NWIS",
            ],
            "phenomenon_matches": [
                "PD-aquifer-depletion",
                "PD-drought",
            ],
            "translation_matches": [
                "TC-06",
                "TC-18",
            ],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Explains storage anomaly (S × Δh) as the core observable from GRACE.",
                "Distinguishes inelastic storage loss (permanent) from elastic Sₛ.",
                "Connects to atmospheric forcing: precipitation deficits + irrigation demand both modify storage.",
                "Implications for climate projections: groundwater contribution to sea-level rise (Konikow 2011).",
                "Cites Famiglietti and Konikow without fabricating other references.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Atmospheric-sciences PhD candidate's interpretation question",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-002",
        "schema_version": "v3",
        "primary_disciplines": ["seismology"],
        "query_type": "paper-interpretation",
        "difficulty": 3,
        "prompt": (
            "I'm an ecologist who just read Brenguier et al. (2008) 'Postseismic relaxation "
            "along the San Andreas fault at Parkfield from continuous seismological "
            "observations' in Science. I don't know seismology — what's the essential "
            "physics, and is there anything in this paper relevant to ambient-acoustic "
            "monitoring in ecology?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": "Brenguier et al. 2008 (cited but not attached)",
            "notes": "Seed QA; cross-discipline read from ecology side.",
        },
        "expected_output": {
            "concept_matches": ["CC-seismo-dvv", "CC-seismo-noise"],
            "method_matches": ["MC-seismo-ambient-noise"],
            "phenomenon_matches": [],
            "translation_matches": ["TC-03"],
            "vocabulary_collisions_flagged": ["noise"],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Explains dv/v as fractional velocity change from coda-wave interferometry.",
                "Distinguishes 'ambient noise' in seismology (the signal!) from acoustic ambient in ecology (vocabulary collision).",
                "Notes the postseismic-relaxation timescale (months) is a seismology observable, not directly ecological.",
                "Honestly states: minimal direct relevance to ecology bioacoustics; shared signal-processing techniques exist.",
                "Suggests TC-03 if ecologist is interested in the hydrology-seismology bridge.",
            ],
            "must_not_say": [
                "seismic dv/v is the same as bioacoustic ambient monitoring",
            ],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Synthetic cross-discipline read from ecology side",
            "review_notes": "Tests vocabulary-collision flagging on 'noise'.",
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-003",
        "schema_version": "v3",
        "primary_disciplines": ["geotechnical_engineering"],
        "query_type": "paper-interpretation",
        "difficulty": 3,
        "prompt": (
            "I'm a geomorphologist who studies landslides. I just read Iverson (2000) "
            "'Landslide triggering by rain infiltration' WRR. The hydrology and the "
            "geomechanics blur together. Can you separate them for me — what's the "
            "geotech engineering content vs. the hydrology content?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": "Iverson 2000 WRR (cited)",
            "notes": "Cross-discipline interpretation; geomorph reading a geotech-flavored paper.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-geotech-MohrCoulomb",
                "CC-geotech-PorePressure",
                "CC-geotech-FS",
                "CC-hydro-p",
            ],
            "method_matches": [],
            "phenomenon_matches": ["PD-AR-landslide"],
            "translation_matches": ["TC-02", "TC-11"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Geotech content: Mohr-Coulomb failure criterion and transient FS calculation.",
                "Hydrology content: pore-pressure diffusion through the unsaturated zone.",
                "The bridge: TC-02 effective stress; pore pressure modifies σ' and FS.",
                "Geomorphic application: TC-11 — same equation, natural-hillslope boundary conditions.",
                "Cites Iverson 2000 specifically without fabricating others.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Geomorphology PhD student's frequent question",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-004",
        "schema_version": "v3",
        "primary_disciplines": ["geomorphology"],
        "query_type": "paper-interpretation",
        "difficulty": 4,
        "prompt": (
            "I'm a hydrologist reading Roering et al. (1999) 'Evidence for nonlinear, "
            "diffusive sediment transport on hillslopes' WRR. The math looks like the "
            "diffusion equations I use, but the rates are very different. Help me make "
            "the bridge."
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": "Roering et al. 1999 WRR (cited)",
            "notes": "Cross-discipline read; hydrology side reading geomorph.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-geomorph-D",
                "CC-hydro-D",
                "CC-geomorph-erosion-rate",
            ],
            "method_matches": [],
            "phenomenon_matches": [],
            "translation_matches": ["TC-01"],
            "vocabulary_collisions_flagged": ["diffusivity"],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "TC-01 is the bridge: the same diffusion equation governs both.",
                "Hydraulic D (m²/s) vs. hillslope κ (m²/yr) — ~10¹⁰× scale difference.",
                "Linear form breaks at slope angle near angle of repose (Roering nonlinear).",
                "Cosmogenic isotope work anchors the long-term erosion rate (timescale 10³–10⁵ yr).",
                "Honestly states: the equation is the same; the substrate physics and timescales are different.",
            ],
            "must_not_say": [
                "hydraulic and hillslope diffusion have the same diffusivity",
            ],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Hydrology PhD student question",
            "review_notes": "Tests vocabulary-collision flagging on 'diffusivity'.",
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-005",
        "schema_version": "v3",
        "primary_disciplines": ["atmospheric_sciences"],
        "query_type": "paper-interpretation",
        "difficulty": 3,
        "prompt": (
            "I'm a geotechnical engineer who just read Ralph et al. (2019) on the AR Scale. "
            "What are the key atmospheric variables, and which of them matter for dam "
            "and levee safety?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": "Ralph et al. 2019 BAMS",
            "notes": "Cross-discipline read; geotech side reading atmospheric.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-atm-IVT",
                "CC-atm-precip",
                "CC-atm-q",
            ],
            "method_matches": [
                "MC-atm-GPM",
                "MC-atm-ERA5",
            ],
            "phenomenon_matches": [
                "PD-atmospheric-river",
                "PD-dam-levee-safety",
            ],
            "translation_matches": ["TC-15"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Defines IVT (kg/m/s) as the AR-Scale categorization variable.",
                "AR-Scale 1–5 by peak IVT + duration; AR-5 events are the design-storm regime.",
                "Geotech relevance: AR precipitation drives embankment pore-pressure rise.",
                "Climate-change intensification (TC-15) means historical PMP / PMF need revisiting.",
                "Cites Ralph et al. 2019 correctly.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Dam-safety engineer's question",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-006",
        "schema_version": "v3",
        "primary_disciplines": ["ecology"],
        "query_type": "paper-interpretation",
        "difficulty": 4,
        "prompt": (
            "I'm a hydrologist who just read Allen et al. (2010) on global drought-induced "
            "tree mortality (Forest Ecology and Management). The mechanisms section talks "
            "about hydraulic failure and carbon starvation. How does that connect to my "
            "soil-moisture and ET observations?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": "Allen et al. 2010",
            "notes": "Cross-discipline read; hydro side reading ecology.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-eco-GPP",
                "CC-hydro-ET",
                "CC-atm-q",
            ],
            "method_matches": [
                "MC-eco-eddycov",
                "MC-hydro-SMAP",
            ],
            "phenomenon_matches": [
                "PD-forest-mortality",
                "PD-flash-drought",
            ],
            "translation_matches": ["TC-16"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Hydraulic failure: xylem cavitation under sustained low water potential — connects to SMAP root-zone moisture observations.",
                "Carbon starvation: stomatal closure terminates photosynthesis; eddy covariance shows GPP collapse.",
                "TC-16 is the bridge: ET and GPP share stomatal conductance at the leaf.",
                "Soil-moisture observations are the leading indicator if you have the right depth resolution.",
                "Concrete suggestion: pair MC-hydro-SMAP with FLUXNET towers in your study basin.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real conversation with a hydrology postdoc",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-007",
        "schema_version": "v3",
        "primary_disciplines": ["agricultural_sciences"],
        "query_type": "paper-interpretation",
        "difficulty": 3,
        "prompt": (
            "I'm a seismologist who reads about California seasonal-seismicity studies "
            "(Johnson et al. 2017 in Science). I want to understand the agricultural side: "
            "how big is the irrigation withdrawal that's loading the crust, and where does "
            "that water come from?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": "Johnson et al. 2017",
            "notes": "Cross-discipline read; seismology asking the agriculture-side question.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-ag-irrigation-demand",
                "CC-hydro-recharge",
            ],
            "method_matches": [
                "MC-hydro-GRACE",
                "MC-ag-NASS-CDL",
            ],
            "phenomenon_matches": [
                "PD-aquifer-depletion",
                "PD-subsidence-consolidation",
            ],
            "translation_matches": ["TC-18"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "California Central Valley irrigation: ~10–20 km³/yr pumping, exceeds recharge in dry years.",
                "Source: groundwater + surface (State Water Project + Central Valley Project).",
                "Loading mechanism: aquifer mass change directly modulates surface elastic load.",
                "Johnson et al. 2017 documents seasonal seismicity correlating with seasonal storage cycle.",
                "Cites Faunt 2016 for the consolidation/subsidence side.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real GAIA HazLab integration discussion",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-008",
        "schema_version": "v3",
        "primary_disciplines": ["near_surface_geophysics"],
        "query_type": "paper-interpretation",
        "difficulty": 4,
        "prompt": (
            "I'm a hydrology researcher reading Minsley et al. (2021) on the USGS Mississippi "
            "Embayment AEM survey (Scientific Reports). The geophysics methods are unfamiliar. "
            "How do I read a σ map as a hydrologist?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": "Minsley et al. 2021",
            "notes": "Cross-discipline read; hydro side reading NSG.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-nsg-resistivity",
                "CC-nsg-EM-conductivity",
                "CC-hydro-K",
            ],
            "method_matches": [
                "MC-nsg-AEM",
                "MC-nsg-ERT",
            ],
            "phenomenon_matches": [
                "PD-aquifer-architecture",
            ],
            "translation_matches": ["TC-08"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Archie's law is the petrophysical bridge: σ depends on porosity, saturation, fluid conductivity.",
                "Low σ in saline aquifers vs. high σ in clay-bearing aquitards — the architecture distinction.",
                "AEM resolves 100–400 m depth at 50–200 m line spacing — regional scale.",
                "Near-surface (<10 m) resolution is poor; complement with ground ERT or wells.",
                "Honest caveat: σ → K conversion requires petrophysical calibration with local well data.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real cross-discipline question at a CSDMS workshop",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-009",
        "schema_version": "v3",
        "primary_disciplines": ["geomorphology"],
        "query_type": "paper-interpretation",
        "difficulty": 5,
        "prompt": (
            "I'm an atmospheric scientist working on AR climatology. I just read Burtin "
            "et al. (2008) JGR on seismic noise from bedload transport. Walk me through "
            "the physics — what does this tell me about coupling between ARs, river "
            "discharge, and bedload?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": "Burtin et al. 2008",
            "notes": "Cross-discipline read; atmosphere side reading seismology/geomorph cross-pub.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-seismo-noise",
                "CC-geomorph-Qs",
                "CC-geomorph-streampower",
                "CC-hydro-Q",
            ],
            "method_matches": [
                "MC-seismo-broadband",
                "MC-geomorph-sediment-monitoring",
            ],
            "phenomenon_matches": [
                "PD-river-floods",
                "PD-atmospheric-river",
            ],
            "translation_matches": ["TC-14", "TC-15"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Bedload transport produces broadband seismic noise (1–100 Hz) as grains impact bed.",
                "TC-14 is the bridge: passive seismic monitoring of bedload — continuous, non-intrusive.",
                "AR connection: AR-driven storms → high Q → high bedload → high seismic noise. The same atmospheric forcing modulates all three.",
                "TC-15 (Clausius-Clapeyron) intensification means more bedload-driven seismic signal in a warming climate.",
                "Suggests joint AR-precipitation + streamflow + seismic-noise time series at instrumented basins.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Frontier-research question; difficulty 5",
            "review_notes": "Hard QA; reviewer disagreement expected.",
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
]


# ============================================================================
# INTEGRATION QAS — cross-discipline bridge questions
# ============================================================================

INTEGRATION_QAS: List[Dict] = [
    {
        "id": "QA-EVAL-010",
        "schema_version": "v3",
        "primary_disciplines": ["hydrology", "seismology"],
        "query_type": "integration",
        "difficulty": 3,
        "prompt": (
            "I work on aquifer-recharge modeling. How does my work connect to seismology? "
            "Are there real, mechanistic bridges or just statistical correlations?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Standard hydro↔seismo integration question.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-hydro-p",
                "CC-hydro-D",
                "CC-seismo-stress",
            ],
            "method_matches": ["MC-seismo-ambient-noise"],
            "phenomenon_matches": [
                "PD-induced-seismicity",
                "PD-eq-hydro-coupling",
            ],
            "translation_matches": ["TC-02", "TC-03"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "TC-02 effective stress: mechanistic bridge, not statistical.",
                "Hydraulic diffusion D maps to fault-pressure diffusion (PD-induced-seismicity r²/t analysis).",
                "TC-03 dv/v: ambient seismic noise tracks groundwater storage changes.",
                "Two productive next steps: induced-seismicity literature (Ellsworth 2013), dv/v in your basin (Clements & Denolle 2018).",
                "Refuses to assert spurious correlations not grounded in TC-02 / TC-03.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Hydrology PhD student question",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-011",
        "schema_version": "v3",
        "primary_disciplines": ["geomorphology", "ecology", "atmospheric_sciences"],
        "query_type": "integration",
        "difficulty": 4,
        "prompt": (
            "I'm interested in modeling post-fire debris-flow hazard under climate change. "
            "I'd need to integrate atmospheric (precip), ecological (vegetation recovery), "
            "and geomorphic (sediment) processes. What bridges exist between these three?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Three-discipline integration; high cross-discipline scoring potential.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-eco-root-cohesion",
                "CC-atm-precip",
                "CC-geomorph-Qs",
            ],
            "method_matches": [
                "MC-geomorph-debris-flow-modeling",
            ],
            "phenomenon_matches": [
                "PD-post-fire-erosion",
                "PD-debris-flow",
                "PD-fire-recovery",
            ],
            "translation_matches": ["TC-11", "TC-13", "TC-15"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Three coupled mechanisms: root-cohesion decay (eco), runoff intensification (hydro/atm), sediment yield amplification (geomorph).",
                "TC-15: climate-driven precipitation intensification ↔ post-fire erosion window.",
                "TC-11: root-cohesion contribution to natural-hillslope FS.",
                "Cannon et al. 2008 post-fire rainfall thresholds, derived in CA/CO, may not transfer to PNW.",
                "Suggests a coupled modeling stack: NWP precipitation → CLM/ELM vegetation → Landlab/D-Claw sediment.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real research direction at GAIA HazLab",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-012",
        "schema_version": "v3",
        "primary_disciplines": ["geotechnical_engineering", "hydrology", "agricultural_sciences"],
        "query_type": "integration",
        "difficulty": 4,
        "prompt": (
            "I'm proposing a multi-discipline study of California Central Valley land "
            "subsidence. I want to integrate the hydrology (pumping), agriculture (irrigation "
            "demand), and geotechnical engineering (consolidation). How do the three "
            "communities talk to each other, and what bridges are operational?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Real proposal-shaping question.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-ag-irrigation-demand",
                "CC-hydro-recharge",
                "CC-geotech-cv",
                "CC-geotech-MohrCoulomb",
            ],
            "method_matches": [
                "MC-hydro-GRACE",
                "MC-geomorph-InSAR",
            ],
            "phenomenon_matches": [
                "PD-aquifer-depletion",
                "PD-subsidence-consolidation",
            ],
            "translation_matches": ["TC-02", "TC-13", "TC-18"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "TC-02 effective stress is the deep bridge; pumping → reduced p → increased σ' → consolidation.",
                "Operational data: USGS NWIS wells + GRACE TWS + Sentinel-1 InSAR.",
                "Permanent storage loss (inelastic m_v) is the key non-reversible cost.",
                "Faunt 2016 documents 9 m cumulative subsidence; agricultural side is the driver.",
                "Suggests a digital-twin approach pairing hydrology, geotech, and InSAR.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real NSF proposal-shaping conversation",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-013",
        "schema_version": "v3",
        "primary_disciplines": ["seismology", "near_surface_geophysics", "geotechnical_engineering"],
        "query_type": "integration",
        "difficulty": 4,
        "prompt": (
            "I'm a seismologist with regional tomography work in the PNW. How do my Vs models "
            "connect to the geotechnical site characterization that the Cascadia hazard "
            "community needs?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Three-discipline integration around Vs.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-seismo-Vs",
                "CC-geotech-G-Gmax",
            ],
            "method_matches": [
                "MC-seismo-tomography",
                "MC-seismo-MASW",
                "MC-geotech-CPT",
            ],
            "phenomenon_matches": [
                "PD-site-response",
                "PD-liquefaction",
            ],
            "translation_matches": ["TC-12", "TC-10"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "TC-12 is the depth-regime bridge: tomography 0.1-10 km, MASW 5-50 m, borehole 0-30 m.",
                "Vs30 derived from the upper-30-m portion of the seismologist's profile.",
                "TC-10: linear seismology gives the elastic Vs; engineering site response needs G/Gmax nonlinearity.",
                "Joint inversion (TC-08) combining seismology + geotech bridges the 'missing middle' 50 m - 1 km.",
                "Operational next step: MASW or seismic CPT at sites where tomography under-resolves the upper 100 m.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real cross-discipline seismology question",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
]


# ============================================================================
# VOCABULARY-DISAMBIGUATION QAS
# ============================================================================

VOCABULARY_QAS: List[Dict] = [
    {
        "id": "QA-EVAL-014",
        "schema_version": "v3",
        "primary_disciplines": ["hydrology", "geotechnical_engineering"],
        "query_type": "vocabulary-disambiguation",
        "difficulty": 2,
        "prompt": (
            "I'm reading a hydrogeology paper that uses 'permeability' and a geotechnical "
            "paper that uses 'permeability' — they seem to mean the same thing but I'm not "
            "sure. Are they the same?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Vocabulary disambig within geosciences (same physical quantity).",
        },
        "expected_output": {
            "concept_matches": [
                "CC-hydro-K",
                "CC-geotech-cv",
            ],
            "method_matches": [],
            "phenomenon_matches": [],
            "translation_matches": ["TC-01"],
            "vocabulary_collisions_flagged": ["permeability"],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "Yes, intrinsic permeability k [m²] is the same physical quantity in both.",
                "But hydrology often reports hydraulic conductivity K = kρg/μ [m/s]; not the same as k.",
                "Geotechnical c_v = k/(γ_w m_v) — k appears but coupled with mechanical compressibility.",
                "Bridge: TC-01 diffusion equation; same equation, different state variable (head vs. pressure).",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Geomorphology PhD student's question",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-015",
        "schema_version": "v3",
        "primary_disciplines": ["geotechnical_engineering", "seismology"],
        "query_type": "vocabulary-disambiguation",
        "difficulty": 3,
        "prompt": (
            "When my structural-engineering colleagues talk about 'stress,' do they mean "
            "the same thing as my seismologist friend who studies stress drop on faults?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Stress vocabulary disambig — surprisingly subtle.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-geotech-MohrCoulomb",
                "CC-seismo-stress",
            ],
            "method_matches": [],
            "phenomenon_matches": [],
            "translation_matches": ["TC-02"],
            "vocabulary_collisions_flagged": ["stress"],
            "refusals_or_caveats_expected": [],
            "user_specific_response_themes": [
                "The same stress tensor formalism — but conventions differ.",
                "Geotech defaults: total stress σ vs. effective σ' = σ − p (Terzaghi).",
                "Seismology defaults: on a fault, σ_n and τ; stress drop Δσ = τ_initial − τ_final.",
                "Bridge: TC-02 — same Mohr-Coulomb equation on engineered soils and on faults.",
                "Practical implication: ambient-state stress is rarely what either reports.",
            ],
            "must_not_say": [],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real cross-discipline question",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
]


# ============================================================================
# REFUSAL-TEST QAS
# ============================================================================

REFUSAL_QAS: List[Dict] = [
    {
        "id": "QA-EVAL-016",
        "schema_version": "v3",
        "primary_disciplines": ["seismology", "hydrology"],
        "query_type": "refusal-test",
        "difficulty": 4,
        "prompt": (
            "Both earthquake-magnitude distributions and flood-frequency distributions "
            "follow power laws. They must share the same underlying mechanism — what is it? "
            "Can I use Gutenberg-Richter machinery to predict flood return periods directly?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Surface-statistics refusal pattern (TC-04).",
        },
        "expected_output": {
            "concept_matches": [
                "CC-seismo-GR",
                "CC-geomorph-flood-frequency",
            ],
            "method_matches": [],
            "phenomenon_matches": [],
            "translation_matches": ["TC-04"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": [
                "forced-analogy",
                "surface-power-law-collision",
            ],
            "user_specific_response_themes": [
                "Refuses the forced analogy: power laws ≠ shared mechanism.",
                "Gutenberg-Richter from fault-system self-organized criticality.",
                "Flood frequency from extreme-precipitation × hydrologic response.",
                "Statistical machinery (EVT, return periods, completeness) is portable; mechanism is not.",
                "Concretely: use log-Pearson III (USGS Bulletin 17C) for floods, NOT b-value methodology.",
            ],
            "must_not_say": [
                "share the same mechanism",
                "Gutenberg-Richter can predict flood return periods",
                "stress drop and discharge are statistically equivalent",
            ],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Synthetic test case for TC-04 refusal pattern",
            "review_notes": "Targets the canonical surface-power-law-collision refusal.",
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
    {
        "id": "QA-EVAL-017",
        "schema_version": "v3",
        "primary_disciplines": ["ecology", "seismology"],
        "query_type": "refusal-test",
        "difficulty": 3,
        "prompt": (
            "Both ambient seismic noise and soundscape ecology use 'noise' as their data. "
            "What's the connection between seismic noise studies and acoustic biodiversity "
            "monitoring? Are they really the same field?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Vocabulary-collision refusal.",
        },
        "expected_output": {
            "concept_matches": ["CC-seismo-noise"],
            "method_matches": ["MC-eco-PAM", "MC-seismo-ambient-noise"],
            "phenomenon_matches": [],
            "translation_matches": [],
            "vocabulary_collisions_flagged": ["noise"],
            "refusals_or_caveats_expected": [
                "vocabulary-collision",
            ],
            "user_specific_response_themes": [
                "Refuses to equate the two: same word, different physics.",
                "Seismic noise is elastic-wave ground motion (m/s); soundscape is acoustic pressure (Pa).",
                "Shared signal-processing techniques (spectral analysis, ML pickers) — but not shared substrate.",
                "Genuinely different fields, with separate publication and instrumentation communities.",
                "One small connection: marine ocean-bottom seismometers do detect whale calls — but that's incidental, not the basis for unification.",
            ],
            "must_not_say": [
                "seismic noise and soundscape ecology are the same field",
            ],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real conversation at a multidisciplinary workshop",
            "review_notes": None,
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
]


# ============================================================================
# JOINT-OBSERVATION QAS
# ============================================================================

JOINT_OBSERVATION_QAS: List[Dict] = [
    {
        "id": "QA-EVAL-018",
        "schema_version": "v3",
        "primary_disciplines": ["hydrology", "seismology", "near_surface_geophysics"],
        "query_type": "joint-observation",
        "difficulty": 5,
        "prompt": (
            "I want to monitor a small catchment's groundwater state in real time without "
            "relying solely on a sparse well network. What's the best multi-sensor joint-"
            "observation strategy — what do I get from seismic, electrical, and gravity "
            "methods, and how do I fuse them?"
        ),
        "input_document": {
            "type": "none",
            "source": None,
            "title": None,
            "notes": "Real research direction; difficulty 5 frontier.",
        },
        "expected_output": {
            "concept_matches": [
                "CC-hydro-S",
                "CC-hydro-h",
                "CC-nsg-resistivity",
                "CC-nsg-gravity",
                "CC-seismo-dvv",
            ],
            "method_matches": [
                "MC-seismo-ambient-noise",
                "MC-nsg-ERT",
                "MC-nsg-gravity",
                "MC-nsg-joint-inversion",
            ],
            "phenomenon_matches": [
                "PD-aquifer-architecture",
            ],
            "translation_matches": ["TC-03", "TC-08", "TC-19"],
            "vocabulary_collisions_flagged": [],
            "refusals_or_caveats_expected": ["different-regime"],
            "user_specific_response_themes": [
                "Each method captures a different aspect: dv/v → integrated storage/saturation; ERT → spatial distribution; gravity → mass.",
                "TC-08 joint inversion is the operational fusion framework.",
                "Spatial scales mismatched: dv/v ≈ 100m–km; ERT 10–100 m; microgravity 10–100 m. Honest framing.",
                "Calibration: still need a small well network to anchor petrophysics (Archie's law).",
                "Concrete proposal: 3–5 wells + dense seismic array + monthly ERT + microgravity at fixed stations.",
            ],
            "must_not_say": [
                "wells are not necessary if you have geophysics",
            ],
        },
        "status": "draft",
        "quality_notes": {
            "author": "Marine",
            "source_question": "Real research-direction question from a hydrogeophysics PhD candidate",
            "review_notes": "Frontier-difficulty (5); expect reviewer disagreement.",
            "last_reviewed_date": None,
            "last_reviewed_by": None,
        },
    },
]


# ============================================================================
# COMBINED SEED SET
# ============================================================================

SEED_QAS: List[Dict] = (
    CALIBRATION_QAS
    + PAPER_INTERPRETATION_QAS
    + INTEGRATION_QAS
    + VOCABULARY_QAS
    + REFUSAL_QAS
    + JOINT_OBSERVATION_QAS
)

if __name__ == "__main__":
    # Quick self-check when run as a script
    from collections import Counter

    print(f"Seed QA count: {len(SEED_QAS)}")
    print(f"  Calibration:           {len(CALIBRATION_QAS)}")
    print(f"  Paper interpretation:  {len(PAPER_INTERPRETATION_QAS)}")
    print(f"  Integration:           {len(INTEGRATION_QAS)}")
    print(f"  Vocabulary:            {len(VOCABULARY_QAS)}")
    print(f"  Refusal:               {len(REFUSAL_QAS)}")
    print(f"  Joint observation:     {len(JOINT_OBSERVATION_QAS)}")
    print()

    qt = Counter(qa["query_type"] for qa in SEED_QAS)
    print("Query types:")
    for k, v in sorted(qt.items()):
        print(f"  {k:30s} {v}")
    print()

    diff = Counter(qa["difficulty"] for qa in SEED_QAS)
    print("Difficulty distribution:")
    for k, v in sorted(diff.items()):
        print(f"  {k}: {v}")
    print()

    disc_counts = Counter()
    for qa in SEED_QAS:
        for d in qa["primary_disciplines"]:
            disc_counts[d] += 1
    print("Discipline coverage (each QA counted once per discipline it touches):")
    for k, v in sorted(disc_counts.items()):
        print(f"  {k:30s} {v}")
