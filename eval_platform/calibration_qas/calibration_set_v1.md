# Calibration QAs — v1

Three QAs used both (a) live in the kickoff meeting for group calibration discussion and (b) pre-populated in every reviewer's scoring sheet as the first three rows. The design intent for each is annotated in the "Calibration target" line so the meeting facilitator can steer the discussion if scores stray far from the intent.

These are *not* part of the production eval set. They exist to align reviewer use of the rubric before the independent scoring round.

---

## QA-CAL-01 — clearly good

**Discipline tag**: seismology + geotechnical engineering
**Query type**: paper interpretation / cross-discipline integration
**Difficulty (1–5)**: 3
**Calibration target**: a strong answer; Technical accuracy = 5, Citations = 5, Cross-discipline integration = 5, Overall = 4.5–5.

### Question

> I just read Boulanger & Idriss (2014) on CPT and SPT liquefaction-triggering procedures. I'm a seismologist working on the Nisqually basin and I want to understand how this connects to my work on Vs30 and ambient-noise dv/v. What should I take away?

### Model answer (the chatbot's response)

> Boulanger & Idriss (2014) update the Seed–Idriss "simplified procedure" framework for evaluating liquefaction triggering from in-situ tests. The core observable is the cyclic stress ratio CSR = 0.65 (a_max/g)(σ_v0/σ'_v0) r_d (your `CC-geotech-CSR-CRR`), normalized by overburden K_σ and magnitude scaling factor MSF; this is compared against a cyclic resistance ratio CRR estimated from the in-situ test (SPT N₁,₆₀ or CPT q_c1N).
>
> Three direct seismology-side connections you should track:
>
> 1. **The a_max input is yours.** PGA from NGA-West2 or NGA-Sub (Boore et al. 2014, doi:10.1193/070113EQS184M) is the engineering demand. Your seismicity model and ground-motion simulations feed CSR directly through `MC-geotech-GMPE`.
>
> 2. **Vs1 → CRR via the Andrus–Stokoe (2000) curve.** The Vs-based triggering criterion (doi:10.1061/(ASCE)1090-0241(2000)126:11(1015)) uses your `CC-seismo-Vs` directly, restricted to the upper 30 m (`CC-geotech-Vs30` regime in `TC-12`). For Nisqually, basin Vs profiles from MASW and ambient-noise tomography produce different shallow Vs than borehole; the Vs-based liquefaction curve is sensitive to which one you trust.
>
> 3. **Ambient-noise dv/v is a coseismic and postseismic monitor, not a pre-event triggering indicator.** dv/v decreases of 10⁻⁴ to 10⁻³ are routinely observed after strong shaking (Brenguier et al. 2008, doi:10.1126/science.1160944), partly reflecting transient G/Gmax reduction (`CC-geotech-G-Gmax`, `TC-10`). Useful for tracking post-event recovery of site stiffness; not predictive of CRR at a never-tested site.
>
> The cleanest cross-discipline next step for the Nisqually basin: a joint inversion combining MASW (`MC-seismo-MASW`), ambient-noise tomography (`MC-seismo-ambient-noise`), and the borehole control (CPT-Vs, `MC-geotech-CPT`) into one Vs profile that resolves the "missing middle" (50 m – 1 km depth) (`TC-12`). Boulanger–Idriss CSR/CRR uses only the upper-30 m portion; basin amplification (`PD-site-response`) needs the full profile.

**Retrieved cards / context**: `CC-geotech-CSR-CRR`, `CC-seismo-Vs`, `CC-geotech-Vs30`, `MC-geotech-CPT`, `MC-seismo-MASW`, `TC-10`, `TC-12`, `PD-liquefaction`, `PD-site-response`.

**Gold reference**: an answer like the above is the target. A 5-score answer correctly identifies the Vs1-CRR link, distinguishes pre-event triggering from postseismic monitoring (the dv/v point), and proposes a concrete cross-discipline action.

---

## QA-CAL-02 — clearly bad

**Discipline tag**: vocabulary disambiguation
**Query type**: vocabulary collision / refusal test
**Difficulty (1–5)**: 2 (the rubric calls for a quick refusal; the chatbot did not)
**Calibration target**: a weak answer with a fabricated citation; Technical accuracy = 1, Citations = 1, Vocabulary precision = 1, Refusal correctness = 1, Overall = 1–1.5.

### Question

> Can seismic attenuation Q tell me about streamflow Q in a watershed? They have the same symbol, so there should be some kind of relation I can exploit. What papers explore this?

### Model answer (the chatbot's response)

> Yes, there is an interesting emerging literature exploiting the dual meaning of Q. The shared symbol reflects that both quantities measure energy dissipation: seismic Q characterizes elastic energy loss per oscillation, and streamflow Q in a watershed similarly measures hydraulic energy throughput. Recent work by Smith et al. (2019, *Journal of Hydrological Geophysics*, doi:10.1029/2019HG045783) shows that seismic Q in fluvial deposits correlates with mean annual discharge Q via the Q–Q theorem of Aki–Larose interferometry. The basic intuition is that wetter sediments have higher attenuation (lower seismic Q) and that watersheds with higher discharge therefore systematically show lower seismic Q in their bed material.
>
> You can compute the Q–Q correlation by fitting log(seismic Q) = a − b log(streamflow Q) using ambient-noise records and USGS NWIS data at co-located sites. Typical b values are 0.3–0.6 across U.S. midcontinent basins.

**Retrieved cards / context**: (chatbot did not retrieve any cards before responding; this is part of the failure).

**Gold reference**: the correct answer is a clean refusal pattern from `agent_playbook.md`: the two Q's are a vocabulary collision. Seismic Q is dimensionless and measures elastic attenuation (`CC-seismo-Q`); streamflow Q has units of m³/s and is a volumetric discharge (`CC-hydro-Q`). They share a symbol, not physics. The chatbot should *refuse* to assert a relation, *not* invent one. The "Q–Q theorem of Aki–Larose interferometry" does not exist; the Smith et al. (2019) citation is fabricated.

**Note for facilitator**: every reviewer should immediately spot the fabricated citation; if any reviewer scores Citations > 2, the rubric explanation needs another pass. This is the QA designed to verify reviewers understand that citation-fabrication is a hard-fail.

---

## QA-CAL-03 — contested

**Discipline tag**: hydrology + seismology
**Query type**: integration / joint observation
**Difficulty (1–5)**: 4
**Calibration target**: a mixed answer where reviewers will reasonably disagree; Technical accuracy = 3–4, Citations = 4–5, Cross-discipline integration = 3–4, Overall = 3–4 with high variance across reviewers. This is the QA that surfaces rubric-interpretation differences.

### Question

> Can I replace groundwater-monitoring well networks in California with ambient seismic noise dv/v? I'm building a proposal to deploy dense seismic arrays in the Central Valley and I want to claim dv/v as a hydrology product.

### Model answer (the chatbot's response)

> dv/v from ambient-noise cross-correlation (`CC-seismo-dvv`, `MC-seismo-ambient-noise`) is sensitive to subsurface property changes including water content and effective stress, and the seismology–hydrology coupling is now well documented (Sens-Schönfelder & Wegler 2006, doi:10.1029/2006GL027797; Clements & Denolle 2018, doi:10.1029/2018GL077706; Lecocq et al. 2017, doi:10.1038/s41598-017-14468-9). For a basin-scale aquifer like the Central Valley, the literature supports dv/v as a *complement* to well networks, not a replacement.
>
> Three reasons it cannot fully replace wells:
>
> 1. **Calibration is site-specific.** The conversion of dv/v to a hydrologic state variable (storage S, head h, soil moisture θ) requires a local petrophysical calibration; without an existing well network at the site, the calibration is unconstrained (`TC-03`).
>
> 2. **Thermoelastic and source-distribution effects must be removed.** A multi-year dv/v signal includes ≥ 10⁻⁴-level contributions from temperature (Hillers et al. 2015) and from changes in the ambient-noise source distribution; separating the hydrologic component requires the same care as for any geophysical inverse problem.
>
> 3. **Vertical resolution is coarse.** dv/v at typical 0.5–5 Hz bands integrates over depths of tens of meters; you cannot distinguish a shallow soil-moisture change from a confined-aquifer head change without independent depth-localization, which usually requires wells.
>
> So the right framing for your proposal is: dense seismic deployment + a strategically retained subset of the well network gives spatially continuous monitoring at lower long-term cost than the well network alone. The well network anchors the petrophysics; dv/v fills the spatial gaps.

**Retrieved cards / context**: `CC-seismo-dvv`, `MC-seismo-ambient-noise`, `TC-03`, `CC-hydro-h`, `CC-hydro-S`, `PD-aquifer-depletion`.

**Gold reference**: the answer is *defensible* but reviewers may legitimately differ on:

- Is the "complement, not replacement" framing correctly nuanced, or does it underclaim? Some reviewers might score Cross-discipline integration high (5) for the strategic framing; others might score it 3 for hedging on a question where the literature has stronger claims than what the chatbot reports (e.g., Clements & Denolle 2018 is more specific about *what* hydrologic variable dv/v actually recovers).
- The citation discipline is reasonable but doesn't engage with the Central Valley specifically — should the chatbot have flagged the lack of Central-Valley-specific literature? Reviewers may score Citations 4 (citations are accurate) or 3 (incomplete coverage of the regional context).
- Is the proposal-shaped framing helpful (Usefulness 4–5) or paternalistic (Usefulness 3)?

**Note for facilitator**: this QA is the productive part of the calibration meeting. Expect 1–2 score-unit disagreement across reviewers. The goal of the discussion is *not* to reach consensus; it is to surface the rubric anchors that each reviewer is implicitly using, so that during independent scoring those anchors are aligned.
