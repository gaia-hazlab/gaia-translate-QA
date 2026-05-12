"""Additional 10 seed QAs that span the new disciplines added in v2.

Concatenates onto the original 50 in seed_qa_dataset.py via the build script.
Each item uses the same schema as SEED_QAS in seed_qa_dataset.py.
"""
from __future__ import annotations


ADDITIONAL_SEED_QAS: list[dict] = [
    # ---------- Atmospheric sciences ↔ geomorphology + hydrology ----------
    {
        "id": "gaia-eval-051",
        "type": "phenomenon_multi_lens",
        "source_discipline": "atmospheric_sciences",
        "target_discipline": "multi",
        "difficulty": "moderate",
        "translation_pattern": "unification",
        "question": (
            "A category-4 atmospheric river makes landfall on the Olympic Peninsula in February. "
            "Trace the same event through the lenses of (a) atmospheric sciences, (b) hydrology, "
            "(c) geomorphology, and (d) seismology. What is each discipline measuring, and what is "
            "the dominant timescale of response each one resolves?"
        ),
        "golden_answer": (
            "(a) Atmospheric sciences resolves the AR as an elongated band of integrated water vapor "
            "transport (IVT, typically 500–1000+ kg/m/s) on hourly–daily timescales, observed via GFS/IFS "
            "forecast fields and verified against GNSS-derived precipitable water and GPM/IMERG "
            "precipitation. The AR-scale framework (Ralph et al. 2019) characterizes intensity by IVT and "
            "duration. (b) Hydrology resolves the surface response as a precipitation pulse driving "
            "saturated-zone infiltration, soil-moisture rise, stream-stage rise; timescales are hours "
            "(infiltration) to days (peak flood) to weeks (baseflow recession). USGS NWIS streamflow and "
            "SNOTEL snowpack are the observables. (c) Geomorphology resolves sediment mobilization: "
            "rainfall-triggered shallow landslides via pore-pressure rise on the Iverson 2000 timescale "
            "of hours, debris-flow generation on minutes-to-hours, channel-bed mobilization on hours-to-"
            "days, knickpoint retreat on years. Most of the observable geomorphic work happens during "
            "these storm events. (d) Seismology resolves the event in two distinct bands: long-period "
            "(below ~0.1 Hz) loading signals from the precipitation load and possible eq triggering, and "
            "high-frequency (1–50 Hz) seismic radiation from landslides, debris flows, and bedload "
            "transport. dv/v from ambient noise responds on the soil-moisture timescale (days). "
            "The unifying observation: this is one event sampled at four very different timescales by "
            "four instrument networks that mostly do not talk to each other — exactly the integration "
            "the translator agent should enable."
        ),
        "key_references": [
            "Ralph et al. 2019",
            "Iverson 2000",
            "Hersbach et al. 2020",
            "Clements & Denolle 2018",
            "Larose et al. 2015",
        ],
        "reasoning_steps": [
            "Identify the atmospheric observable (IVT) and its timescale (hourly).",
            "Identify the hydrologic observable (streamflow/soil moisture) and its timescale (hourly–weekly).",
            "Identify the geomorphic observable (landslide, sediment flux) and its timescale (hours–years).",
            "Identify the seismic observables (loading signal, ambient noise dv/v, landslide seismicity) and their bands.",
            "Make explicit the synthesis point: same event, four timescales, four networks.",
        ],
        "critique_score": 4,
        "critique_notes": "Strong cross-discipline framing. Could add specific PNW example (e.g. Feb 2017 ARs).",
        "status": "draft",
    },

    # ---------- Geotech ↔ seismology (liquefaction, deeper into Vs30) ----------
    {
        "id": "gaia-eval-052",
        "type": "concept_translation",
        "source_discipline": "geotechnical_engineering",
        "target_discipline": "seismology",
        "difficulty": "moderate",
        "translation_pattern": "unification",
        "question": (
            "Vs30 appears in the ASCE 7 building code, in NGA-West2 ground-motion models, and in MASW "
            "site characterization. Explain the variable, the role it plays in each of those three "
            "contexts, and the precise sense in which it is the same number in all three."
        ),
        "golden_answer": (
            "Vs30 is the time-averaged shear-wave velocity in the upper 30 m: Vs30 = 30 / Σ(Δzᵢ / Vsᵢ). "
            "It is a single scalar summary of the shallow shear-wave profile. (1) In ASCE 7, Vs30 maps a "
            "site to one of six site classes (A–F) that determine code-specified short-period and 1-s "
            "amplification factors Fₐ, Fᵥ applied to mapped spectral accelerations. (2) In NGA-West2 GMMs "
            "(Boore et al. 2014), Vs30 enters as an explicit predictor in the empirical functional form, "
            "calibrated against thousands of strong-motion records to capture the empirical correlation "
            "between shallow stiffness and surface ground-motion intensity. (3) In MASW (Park, Miller & "
            "Xia 1999) — the canonical near-surface geophysical method — Vs30 is computed from a Vs(z) "
            "profile recovered by inverting Rayleigh-wave dispersion measured on a surface array. The "
            "*same number* in all three because it is defined as a property of the medium, not of an "
            "instrument or a code: a 30-m depth-averaged shear-wave slowness integral. The caveat: in "
            "practice MASW gives the best in-situ direct measurement, code site classes lump into discrete "
            "bins that lose resolution at boundaries, and GMMs treat Vs30 as a proxy for the deeper "
            "profile it imperfectly represents. The translator's interesting move is that Vs30 is *also* "
            "the variable Andrus & Stokoe 2000 use as the basis of Vs-based liquefaction triggering, "
            "tying site response to liquefaction susceptibility through a single shared measurement."
        ),
        "key_references": [
            "Park, Miller & Xia 1999",
            "Andrus & Stokoe 2000",
            "Boore et al. 2014",
        ],
        "reasoning_steps": [
            "State the definition of Vs30 explicitly.",
            "Explain its role in ASCE 7 site classification.",
            "Explain its role as a GMM predictor.",
            "Explain its role as an MASW deliverable.",
            "Make the unification claim: it is a medium property, the three uses are the same number.",
            "Note the bridge to liquefaction triggering as a bonus translation.",
        ],
        "critique_score": 5,
        "critique_notes": "Clean unification across geotech / seismo / NS-geophysics.",
        "status": "draft",
    },

    # ---------- Ecology ↔ geomorphology + hydrology (root reinforcement) ----------
    {
        "id": "gaia-eval-053",
        "type": "concept_translation",
        "source_discipline": "ecology",
        "target_discipline": "geomorphology",
        "difficulty": "moderate",
        "translation_pattern": "unification",
        "question": (
            "How does the Sidle & Ochiai (2006) root-reinforcement framework modify the Iverson (2000) "
            "rainfall-triggered landslide model, and what is the net effect of post-fire root decay on "
            "hillslope factor-of-safety in a steep, forested Cascades catchment?"
        ),
        "golden_answer": (
            "The Iverson 2000 transient-pore-pressure model gives FS = (c' + (σ − p) tan φ') / τ_d, with p "
            "rising as a diffusion-equation response to rainfall infiltration. Sidle & Ochiai 2006 (and "
            "the broader root-cohesion literature, e.g. Schmidt et al. 2001 Canadian Geotech J) treat "
            "live and recently-dead root networks as an additive apparent-cohesion term: c'_total = c'_soil "
            "+ c_root, where c_root depends on root area ratio, root tensile strength, and orientation. "
            "Mature Douglas-fir or western hemlock stands can contribute c_root ≈ 1–10 kPa, often dominating "
            "the cohesion term in low-cohesion glacial colluvium. After stand-replacing fire, c_root drops "
            "on a 2–10-yr decay timescale as fine roots decompose faster than new roots establish. The "
            "window of minimum c_root, typically 3–8 yr post-fire, coincides with the highest landslide "
            "and debris-flow activity (Wondzell & King 2003; Cannon et al. 2010 specifically for debris "
            "flows). The translator's point is that the geomorphic FS equation contains an explicit "
            "ecological state variable (c_root), which is the cleanest example of an ecology ↔ "
            "geomorphology coupling. Coupling is closed via hydrology (the p term) and atmospheric "
            "sciences (the precipitation forcing), making post-fire debris flows a four-discipline problem."
        ),
        "key_references": [
            "Iverson 2000",
            "Sidle & Ochiai 2006",
            "Cannon et al. 2010",
        ],
        "reasoning_steps": [
            "Write out the Iverson FS equation.",
            "Define c_root as an additive contribution to apparent cohesion.",
            "Quantify the typical magnitude (1–10 kPa).",
            "Describe the post-fire decay timescale (years).",
            "Tie to observed post-fire landslide / debris-flow windows.",
            "Close the loop across four disciplines.",
        ],
        "critique_score": 4,
        "critique_notes": "Strong but could use a specific Cascades case study (e.g. North Cascades, 2003 B&B Complex).",
        "status": "draft",
    },

    # ---------- Agriculture ↔ hydrology ↔ geotech ↔ seismology (Central Valley) ----------
    {
        "id": "gaia-eval-054",
        "type": "integration_digital_twin",
        "source_discipline": "agricultural_sciences",
        "target_discipline": "multi",
        "difficulty": "hard",
        "translation_pattern": "unification",
        "question": (
            "Design the minimum observable state vector and the minimum process couplings for a "
            "California Central Valley digital twin that simultaneously serves (a) sustainable "
            "groundwater management under SGMA, (b) subsidence-driven infrastructure damage forecasting, "
            "and (c) seasonally-modulated seismicity tracking on the San Andreas system."
        ),
        "golden_answer": (
            "State vector (per grid cell or aquifer compartment): (1) hydrologic — water table elevation, "
            "specific storage, vertical hydraulic conductivity, soil moisture (root-zone and full column); "
            "(2) agricultural — irrigated area by crop, applied irrigation depth, reference ET (Penman-"
            "Monteith from atmospheric forcing), actual ET from OpenET ensemble; (3) geomechanical — "
            "vertical effective stress, cumulative compaction (clay layers), elastic and inelastic "
            "skeletal compressibility (Faunt et al. 2016 framework); (4) seismic — crustal loading "
            "anomaly (mass redistribution from depletion), Coulomb stress change on mapped faults. "
            "Process couplings: (i) atmospheric → ag (forcing), (ii) ag → hydro (irrigation and pumping), "
            "(iii) hydro → geotech (pore-pressure ↔ effective stress ↔ consolidation, in clay layers "
            "irreversibly), (iv) geotech → infrastructure (subsidence, well-casing damage, canal-grade "
            "loss), (v) hydro+geotech → seismic (mass change → load change → ΔCFS on faults). "
            "Observation network: GRACE/GRACE-FO for monthly TWS, InSAR (Sentinel-1, NISAR) for "
            "subsidence, USGS NWIS wells for head, GNSS for vertical motion, SCSN/USArray for seismicity, "
            "USDA NASS CDL for crop area, OpenET for ET. Documented signal chain: Scanlon et al. 2012 "
            "for depletion, Faunt et al. 2016 for subsidence, Johnson et al. 2017 for seasonal "
            "seismicity modulation. The translator agent's role here is to make explicit that what "
            "looks like three separate problems (water, infrastructure, faults) share the same state "
            "variables and most of the same observation network."
        ),
        "key_references": [
            "Scanlon et al. 2012",
            "Faunt et al. 2016",
            "Johnson et al. 2017",
            "Allen et al. 1998",
        ],
        "reasoning_steps": [
            "List the hydrologic state variables.",
            "List the agricultural state variables.",
            "List the geomechanical state variables.",
            "List the seismic state variables.",
            "Specify the five process couplings.",
            "Map state variables to observation networks.",
            "Articulate the unification claim: three problems, one state vector.",
        ],
        "critique_score": 5,
        "critique_notes": "Excellent integration item. Adjacent to a real funded line of work.",
        "status": "draft",
    },

    # ---------- Near-surface geophysics ↔ hydrology + critical zone ----------
    {
        "id": "gaia-eval-055",
        "type": "method_translation",
        "source_discipline": "near_surface_geophysics",
        "target_discipline": "hydrology",
        "difficulty": "moderate",
        "translation_pattern": "homology",
        "question": (
            "Compare time-lapse ERT, time-lapse seismic dv/v from ambient noise, and GNSS-IR for "
            "tracking shallow soil-moisture changes in a critical-zone observatory setting. What does "
            "each one actually measure, what depth does it sample, and what is the dominant failure "
            "mode for each?"
        ),
        "golden_answer": (
            "(1) Time-lapse ERT measures bulk electrical resistivity ρ_e as a function of position and "
            "time; via Archie's law (Archie 1942) and pedotransfer models it inverts to water content "
            "θ. Depth sample: array-dependent, typically 0 to several meters for dipole-dipole "
            "configurations, deeper with larger arrays. Failure mode: temperature contamination (ρ_e "
            "depends on both θ and T; the seasonal T signal can dominate without correction) and "
            "sensitivity loss with depth. (2) Time-lapse dv/v from ambient seismic noise (Sens-Schönfelder "
            "& Wegler 2006 framework) measures small fractional changes in seismic velocity inferred from "
            "stretching of the coda; via empirical or poroelastic models (Lecocq et al. 2017; Clements & "
            "Denolle 2018), this maps to soil-moisture or groundwater changes. Depth sample: depends on "
            "frequency band; 1 Hz samples to ~100s of meters, 10 Hz samples shallow critical zone. "
            "Failure mode: thermo-elastic strain from surface T changes can mimic the storage signal, "
            "and the dv/v ↔ θ calibration is site-specific. (3) GNSS-IR (Larson 2016) interprets the "
            "amplitude and phase of GNSS multipath as a function of soil dielectric, recovering θ in the "
            "top few cm beneath the antenna. Depth sample: shallow (< 5 cm). Failure mode: footprint "
            "is ~1000 m² but heterogeneous, and snow/vegetation strongly contaminate the signal. "
            "Critical translation point: the three methods sample different depths and different "
            "physical properties (resistivity, seismic velocity, dielectric), and they fail in different "
            "modes — joint inversion across them (Linde et al. 2006 architecture) is strictly more "
            "informative than any one alone."
        ),
        "key_references": [
            "Archie 1942",
            "Sens-Schönfelder & Wegler 2006",
            "Larson 2016",
            "Clements & Denolle 2018",
            "Binley et al. 2015",
        ],
        "reasoning_steps": [
            "For ERT: physical property, depth, failure mode.",
            "For dv/v: physical property, depth, failure mode.",
            "For GNSS-IR: physical property, depth, failure mode.",
            "Synthesize: complementary depth/property sensitivity.",
            "Recommend joint inversion as the strictly better path.",
        ],
        "critique_score": 4,
        "critique_notes": "Could add quantitative sensitivity numbers per method.",
        "status": "draft",
    },

    # ---------- Atmospheric sciences ↔ seismology (data assimilation as bridge) ----------
    {
        "id": "gaia-eval-056",
        "type": "method_translation",
        "source_discipline": "atmospheric_sciences",
        "target_discipline": "seismology",
        "difficulty": "hard",
        "translation_pattern": "homology",
        "question": (
            "4D-Var and Ensemble Kalman Filter assimilation are the workhorses of operational atmospheric "
            "forecasting. How would you adapt them to a continuous seismic monitoring problem — say, "
            "real-time stress and seismicity-rate state estimation on a fault system? What are the "
            "structural similarities and what are the load-bearing differences?"
        ),
        "golden_answer": (
            "Structural similarity: both problems are sequential state estimation in a system governed by "
            "a forward physical model M(x) (NWP physics for atmosphere; rate-state friction or "
            "poroelastic stress evolution for faults), with sparse noisy observations y = H(x) + ε. The "
            "Kalman family recursion x⁺ = x⁻ + K(y − Hx⁻), K = P⁻Hᵀ(HP⁻Hᵀ + R)⁻¹ applies in both. "
            "Evensen 1994 EnKF extends this to nonlinear high-dimensional systems by replacing analytical "
            "covariance with sample covariance over an ensemble. 4D-Var minimizes a cost function over a "
            "time window using adjoint-derived gradients. These are directly portable to seismology. "
            "Load-bearing differences: (a) the atmospheric forward model has decades of physics-based "
            "tuning at relatively low computational cost per ensemble member; seismic forward models for "
            "fault systems mix physics-based rate-state with empirical statistics (ETAS) and Coulomb "
            "stress calculations, with weaker first-principles grounding for some inputs. (b) Atmospheric "
            "observations are dense and reasonably well-modeled noise; seismic observations are clustered "
            "in time (eq catalogs are point processes, not gridded fields) and have non-Gaussian noise "
            "via detection completeness. (c) Atmospheric DA targets days-ahead prediction; seismic state "
            "estimation typically targets nowcast and conditional hazard, with formal forecasts at much "
            "longer horizons. The most direct adaptation is the EnKF framework applied to slow-slip "
            "and tremor catalogs in subduction-zone settings, with the rate-state model as M(x). "
            "Greg Hakim's paleo-DA group has shown the most progress in adapting NWP DA to non-meteoro-"
            "logical Earth systems; their machinery is directly applicable here."
        ),
        "key_references": [
            "Evensen 1994",
            "Hersbach et al. 2020",
            "Reichle 2008",
        ],
        "reasoning_steps": [
            "State the shared sequential-estimation framework.",
            "Write the Kalman update equation common to both.",
            "Identify the 4D-Var cost function for the atmospheric case.",
            "Identify three load-bearing differences (model maturity, observation density, time horizon).",
            "Suggest a concrete adaptation (EnKF + rate-state for SSE catalogs).",
            "Reference paleo-DA as proof of methodology portability.",
        ],
        "critique_score": 4,
        "critique_notes": "Hakim's paleo-DA reference is a Marine-specific bridge; useful for evaluating the agent on UW context awareness.",
        "status": "draft",
    },

    # ---------- Cross-cutting: NAS report citation ----------
    {
        "id": "gaia-eval-057",
        "type": "historical_foundational",
        "source_discipline": "multi",
        "target_discipline": "multi",
        "difficulty": "easy",
        "translation_pattern": "unification",
        "question": (
            "The NSF EAR decadal survey 'A Vision for NSF Earth Sciences 2020-2030: Earth in Time' "
            "(NASEM 2020, doi:10.17226/25761) identifies 12 priority research questions. Which subset "
            "are directly addressable by a Gaia-style multidisciplinary translator agent, and why?"
        ),
        "golden_answer": (
            "Of the 12 priority questions in NASEM 2020 (Earth in Time), the ones most directly addressable "
            "by an agentic multidisciplinary integrator are those that explicitly span solid Earth, "
            "surface, and fluid envelopes: 'How do earthquakes, volcanic eruptions, and other geohazards "
            "occur and how can their impacts be reduced?' (couples seismology + geotechnical + geomorph + "
            "atmospheric forcing); 'How does the critical zone influence the climate system, and how does "
            "the climate system influence the critical zone?' (couples atmospheric + ecology + hydrology + "
            "geomorphology + near-surface geophysics); 'How do biogeochemical cycles evolve?' (couples "
            "ecology + hydrology + atmosphere); 'How does water move through the Earth, and how do "
            "Earth materials, life, and water interact?' (the most explicitly multidisciplinary). The "
            "translator agent's contribution is not to *answer* these questions but to (a) decompose them "
            "into discipline-specific subquestions tractable by existing literature, (b) propose joint-"
            "observation strategies that cross discipline-specific instrument networks, and (c) make "
            "explicit the shared state variables (effective stress, ET, soil moisture, surface "
            "deformation) that link the subquestions. Earlier NAS reports — NRC 2001 (doi:10.17226/9981, "
            "the report that named the Critical Zone) and NRC 2010 *Landscapes on the Edge* "
            "(doi:10.17226/12700) — provide the framing language for these integrations. The NASA-led "
            "Earth-observation decadal NASEM 2018 *Thriving on Our Changing Planet* "
            "(doi:10.17226/24938) is the complementary observation-side companion."
        ),
        "key_references": [
            "NASEM 2020 doi:10.17226/25761",
            "NRC 2001 doi:10.17226/9981",
            "NRC 2010 doi:10.17226/12700",
            "NASEM 2018 doi:10.17226/24938",
        ],
        "reasoning_steps": [
            "Identify which of the 12 questions are explicitly cross-disciplinary.",
            "For each selected question, name the disciplines it couples.",
            "Articulate the translator agent's three contributions (decompose, joint observation, shared state).",
            "Cite the supporting NAS reports correctly.",
        ],
        "critique_score": 5,
        "critique_notes": "Useful as a 'context' QA that anchors the agent in the funding-landscape reality.",
        "status": "draft",
    },

    # ---------- Ecology ↔ seismology (ambient field) ----------
    {
        "id": "gaia-eval-058",
        "type": "method_translation",
        "source_discipline": "ecology",
        "target_discipline": "seismology",
        "difficulty": "moderate",
        "translation_pattern": "analogy",
        "question": (
            "Passive acoustic monitoring (PAM) in ecology (acoustic indices, BirdNET-style deep-learning "
            "species detection) and passive seismic monitoring (ambient noise tomography, dv/v) share more "
            "than just the word 'passive'. What signal-processing techniques are reusable across the two, "
            "and what is the deepest conceptual analogy?"
        ),
        "golden_answer": (
            "Reusable techniques: (1) spectrogram-based feature extraction and STFT preprocessing are "
            "identical; (2) deep-learning detectors (CNNs on log-mel spectrograms in PAM; CNNs on "
            "spectrograms or waveform inputs in PhaseNet/EQTransformer for seismology — Zhu & Beroza "
            "2019, Mousavi et al. 2020) use nearly identical architectures; (3) acoustic indices (ACI, "
            "BI, NDSI) and seismic noise statistics (PSD percentiles, McNamara & Buland 2004 framework) "
            "are both statistical summaries of the ambient field; (4) cross-correlation across array "
            "elements is used both for seismic Green's-function recovery (Shapiro & Campillo 2004) and "
            "for acoustic source localization. The deepest conceptual analogy is the Aki-Larose theorem: "
            "an isotropic diffuse field cross-correlated between two sensors recovers the impulse "
            "response between them. This statistical-mechanical equipartition principle applies equally "
            "to acoustic fields (with appropriate caveats about scatterer density and source distribution) "
            "and to seismic fields. The practical implication: ecological PAM networks could in principle "
            "be analyzed with the same ambient-field machinery seismology developed in the past 20 "
            "years, and conversely seismic-monitoring infrastructure could in some bands provide eco-"
            "acoustic information. Hillers et al. 2015 specifically documents wind-driven tree sway "
            "contaminating seismic ambient-field data — making the cross-disciplinary coupling concrete."
        ),
        "key_references": [
            "Shapiro & Campillo 2004",
            "Zhu & Beroza 2019",
            "Mousavi et al. 2020",
            "Hillers et al. 2015",
        ],
        "reasoning_steps": [
            "Enumerate shared signal-processing techniques.",
            "Identify the deep theoretical bridge (Aki-Larose / diffuse field equipartition).",
            "Note the practical implication for cross-discipline reuse.",
            "Cite the concrete coupling (tree sway in seismic noise).",
        ],
        "critique_score": 4,
        "critique_notes": "Could add a specific BirdNET reference; otherwise solid.",
        "status": "draft",
    },

    # ---------- Geotech ↔ atmospheric sciences (extreme precip → embankment) ----------
    {
        "id": "gaia-eval-059",
        "type": "phenomenon_multi_lens",
        "source_discipline": "atmospheric_sciences",
        "target_discipline": "geotechnical_engineering",
        "difficulty": "moderate",
        "translation_pattern": "unification",
        "question": (
            "An aging earth-fill dam in the Cascades faces increasing AR frequency and intensity under "
            "warming-driven Clausius-Clapeyron scaling. Walk through the chain of physical mechanisms by "
            "which an atmospheric-sciences trend (intensifying ARs) translates into a geotechnical "
            "failure-probability change."
        ),
        "golden_answer": (
            "Step 1 (atmospheric sciences): Clausius-Clapeyron scaling implies ~7%/K increase in "
            "saturation vapor pressure, propagating to ~7%/K intensification of heavy precipitation in "
            "moisture-rich AR events (Held & Soden 2006; Trenberth 2011). In observational PNW records "
            "and CMIP6 downscaling, AR intensity is rising at or above this scaling, with frequency of "
            "category-4/5 events projected to increase substantially. Step 2 (atmospheric → hydrology): "
            "more intense ARs produce higher peak precipitation intensities and longer-duration "
            "sequences. Step 3 (hydrology → hydraulics): reservoir inflow exceeds spillway design "
            "capacity more often; reservoir levels are held higher for longer. Step 4 (hydrology → "
            "geotech): elevated reservoir level imposes elevated phreatic surface in the embankment. "
            "Pore-pressure diffusion into the embankment follows the Terzaghi 1925 consolidation "
            "equation with c_v ≈ k/(γ_w m_v). For a typical compacted-fill embankment with k = 10⁻⁷ m/s "
            "and characteristic length 30 m, the diffusion timescale is days-to-weeks — comparable to AR "
            "event duration. Step 5 (geotech): elevated steady-state pore pressure reduces effective "
            "stress and Mohr-Coulomb shear strength on potential slip surfaces, lowering FS. Sustained "
            "high-pore-pressure events also drive piping/internal erosion failure modes. Net effect: "
            "the failure-probability change is the convolution of the AR intensity-duration-frequency "
            "shift with the embankment's pore-pressure response function. The translator agent's role "
            "is to make this chain explicit: a single climate signal cascades through five disciplinary "
            "models, each with quantifiable propagation."
        ),
        "key_references": [
            "Held & Soden 2006",
            "Trenberth 2011",
            "Terzaghi 1925",
            "Ralph et al. 2019",
        ],
        "reasoning_steps": [
            "Quantify the Clausius-Clapeyron driver.",
            "Map to AR intensification.",
            "Map AR intensity to reservoir hydrology.",
            "Map reservoir level to embankment pore pressure (Terzaghi consolidation).",
            "Map pore pressure to FS via Mohr-Coulomb.",
            "Articulate the convolution view of failure-probability change.",
        ],
        "critique_score": 4,
        "critique_notes": "Solid five-step chain. Could add specific examples (Howard Hanson, Mud Mountain).",
        "status": "draft",
    },

    # ---------- Critical zone integration (cross_cutting → all) ----------
    {
        "id": "gaia-eval-060",
        "type": "integration_digital_twin",
        "source_discipline": "cross_cutting",
        "target_discipline": "multi",
        "difficulty": "hard",
        "translation_pattern": "unification",
        "question": (
            "The Critical Zone framework (NRC 2001, NASEM 2020) is meant to unify hydrology, geomorphology, "
            "ecology, soil science, and biogeochemistry under one observational and theoretical umbrella. "
            "What does it offer the Gaia translator agent that a discipline-pair approach does not, "
            "and where does the CZ frame run out?"
        ),
        "golden_answer": (
            "What the CZ frame offers: (1) a shared spatial volume — from top of canopy to base of "
            "active groundwater — that all the constituent disciplines can agree on as the relevant "
            "domain, sidestepping the boundary debates that derail multidisciplinary integration. "
            "(2) A shared set of state variables — water content, weathering depth, soil organic carbon, "
            "regolith thickness — that span the historical discipline boundaries. (3) Institutional "
            "support from NSF (CZO/CZNet) and the NAS reports, which lowers the activation energy for "
            "funded cross-disciplinary projects (NRC 2001; NRC 2010; NASEM 2020 Earth in Time priority "
            "question on CZ-climate coupling). (4) A widely shared methodology stack — hydrogeophysics "
            "(Binley et al. 2015; Parsekian et al. 2015), eddy-covariance, isotope tracers, cosmogenic "
            "dating — that any CZ-anchored study can draw from without re-justifying. (5) A vocabulary "
            "for time integration of biophysical processes (regolith production rate, residence time "
            "distributions) that a discipline-pair view tends to leave implicit. "
            "Where the CZ frame runs out: (1) Solid-Earth scale processes (faulting, deep groundwater, "
            "magmatism) and atmospheric-scale processes (synoptic meteorology, AR dynamics) sit outside "
            "the CZ volume by definition, even though they force what happens inside it. The Gaia "
            "translator must explicitly extend the CZ frame upward (to atmospheric forcing) and downward "
            "(to seismogenic depths) to do its job. (2) Anthropogenic process modification — irrigation, "
            "land cover change, induced seismicity — is acknowledged but historically under-emphasized "
            "in CZ science compared to geotechnical / agricultural / engineering perspectives. (3) The "
            "CZ frame is observation-centric and weaker on the digital-twin / forecasting layer, which "
            "is exactly the gap the Gaia digital-twin work fills. So: adopt the CZ vocabulary and the "
            "volume framing; extend upward, downward, and forward in time."
        ),
        "key_references": [
            "NRC 2001 doi:10.17226/9981",
            "NRC 2010 doi:10.17226/12700",
            "NASEM 2020 doi:10.17226/25761",
            "Binley et al. 2015",
            "Parsekian et al. 2015",
            "Brantley, Goldhaber & Ragnarsdottir 2007",
        ],
        "reasoning_steps": [
            "List the five things the CZ frame provides.",
            "List the three boundaries where it runs out.",
            "Frame the translator agent's value-add as extending CZ vertically (atm + solid) and forward in time (twin).",
            "Cite the institutional NAS reports correctly.",
        ],
        "critique_score": 5,
        "critique_notes": "Strong reflective item; positions Gaia explicitly against the CZ frame.",
        "status": "draft",
    },
]


if __name__ == "__main__":
    import json

    print(json.dumps(ADDITIONAL_SEED_QAS, indent=2))
