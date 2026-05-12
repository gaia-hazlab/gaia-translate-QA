---
discipline: geotechnical_engineering
card_type: method
schema_version: v3
---

# Geotechnical engineering — method cards

Each card describes one measurement technique, instrument, or dataset relevant to geotechnical engineering, with what it measures, resolution, failure modes, and cross-discipline reuse. Format follows `docs/card_format_spec.md`.

---

## MC-geotech-CPT: Cone Penetration Test and seismic CPT

**What it is**: an instrumented 10 or 15 cm² cone pushed into the ground at a constant 20 mm/s, continuously logging tip resistance q_c [MPa], sleeve friction f_s [kPa], and pore-pressure u₂ behind the cone [kPa]. The seismic-CPT (SCPT) variant adds a geophone in the sounding rod for downhole Vs measurement at each push depth. Standard ASTM D5778; widely used worldwide, in many countries the primary site-investigation method.

**What you can retrieve**:
- Continuous (1–2 cm) depth profiles of q_c, f_s, u₂ to ≈ 30 m typical, deeper with heavy rigs.
- Soil-behavior-type classification (Robertson 1990 chart from normalized q_c, F_r, B_q).
- Liquefaction-triggering input q_c1N for `CC-geotech-CSR-CRR`.
- Vs profile from SCPT at ≈ 1 m intervals.
- Pore-pressure dissipation tests give c_v (`CC-geotech-cv`) and k.
- Software: standard processing in CPeT-IT, CLiq, CPT-Pro.

**Failure modes**:
- Refusal in gravel and cobbles; cannot penetrate dense or cemented layers.
- Cone wear and saturation of the u₂ filter degrade pore-pressure measurement.
- Soil-behavior-type charts are empirical and miscalibrate in unusual mineralogies.
- Vs from SCPT samples ≈ 1 m around the rod, sensitive to nearfield effects.

**Cross-discipline uses**:
- **Hydrology**: pore-pressure dissipation gives in-situ k for unconsolidated aquifers.
- **Seismology**: SCPT-Vs anchors the shallow end of the Vs profile (`TC-12`); inputs to nonlinear site response (`MC-geotech-numerical`).
- **Near-surface geophysics**: independent control on MASW dispersion inversion (`MC-seismo-MASW`).

**When you see this in a paper**: confirm cone area (10 vs. 15 cm² differ in q_c), pore-pressure filter location (u₁/u₂/u₃), and whether normalization to in-situ stress has been applied.

**Anchor citations**:
- Robertson, P. K. (1990). Soil classification using the cone penetration test. *Canadian Geotechnical Journal*, 27(1), 151–158. doi:10.1139/t90-014
- Lunne, T., Robertson, P. K., & Powell, J. J. M. (1997). *Cone Penetration Testing in Geotechnical Practice*. Blackie/Spon Press.

**Related cards**: `MC-geotech-SPT`, `MC-seismo-MASW`, `CC-geotech-CSR-CRR`, `CC-geotech-Su`, `CC-geotech-cv`, `TC-12`

---

## MC-geotech-SPT: Standard Penetration Test

**What it is**: a 51 mm split-spoon sampler driven into the bottom of a borehole by a 63.5 kg hammer dropped 760 mm; the count N to drive the spoon 300 mm (after a 150 mm seating drive) is the raw SPT N-value. Standard ASTM D1586. Legacy method but ubiquitous: most pre-2000 site investigations and most regional geotechnical databases (e.g., USGS NGL — Next Generation Liquefaction) are SPT-based.

**What you can retrieve**:
- N-values at 1.5 m typical intervals over the borehole depth.
- Disturbed soil samples for index testing (grain size, Atterberg limits, fines content).
- Corrected N₆₀ (60% energy) and N₁,₆₀ (overburden- and energy-corrected) for liquefaction analysis.
- Empirical correlations to φ', Dr, Su, Vs (Ohta-Goto 1978 for Vs).

**Failure modes**:
- Hammer energy varies 30–100% across rigs; without measured energy ratio, N is poorly defined.
- Coarse-gravel layers produce spurious high N.
- Disturbance during sampling degrades index test quality.
- N is much less repeatable than CPT q_c (factor 2–3 scatter on the same soil).

**Cross-discipline uses**:
- **Seismology / engineering**: N₁,₆₀ is the legacy axis for liquefaction-triggering catalogs (`CC-geotech-CSR-CRR`).
- **Hydrology**: SPT samples enable grain-size-based K estimation (Hazen, Kozeny-Carman).
- **Geomorphology**: SPT N profiles in unconsolidated deposits map stratigraphy at regional scale.

**When you see this in a paper**: confirm energy correction method (calibrated hammer, free-fall vs. cathead-and-rope); pre-1980 N data without energy correction should be flagged as uncertain.

**Anchor citations**:
- Skempton, A. W. (1986). Standard penetration test procedures and the effects in sands of overburden pressure, relative density, particle size, ageing and overconsolidation. *Géotechnique*, 36(3), 425–447. doi:10.1680/geot.1986.36.3.425
- Youd, T. L., et al. (2001). Liquefaction resistance of soils: Summary report from the 1996 NCEER and 1998 NCEER/NSF workshops. *J. Geotech. Geoenviron. Eng.*, 127(10), 817–833. doi:10.1061/(ASCE)1090-0241(2001)127:10(817)

**Related cards**: `MC-geotech-CPT`, `CC-geotech-CSR-CRR`, `CC-geotech-Su`, `PD-liquefaction`

---

## MC-geotech-HVSR: Microtremor horizontal-to-vertical spectral ratio

**What it is**: passive single-station method (Nakamura 1989) computing the spectral ratio H/V of ambient seismic noise to estimate the site fundamental resonance frequency f_0 and (with assumptions) the contrast at the bedrock interface. A peak in H/V near f_0 = Vs/(4H) reveals the impedance contrast above bedrock; widely used as a rapid, low-cost site characterization.

**What you can retrieve**:
- Site fundamental period T_0 = 1/f_0; useful for design-code site classification.
- With multiple stations: depth-to-bedrock H ≈ Vs_avg/(4 f_0) under simple-layer assumptions.
- Joint inversion with MASW dispersion gives Vs profile to greater depth than MASW alone.
- Standard processing: Geopsy (Wathelet et al. 2020), SESAME guidelines, ObsPy.

**Failure modes**:
- The H/V peak is robust; the amplitude is not — only ratios of peak frequencies are reliable.
- 2D/3D basin effects produce additional peaks and shoulders that 1D theory cannot interpret.
- Industrial noise and traffic at specific frequencies can be mistaken for site peaks.
- Soft sediment over hard bedrock gives a clear peak; gradational profiles can give weak or absent peaks.

**Cross-discipline uses**:
- **Seismology**: f_0 from H/V matches receiver-function Moho peaks at the appropriate scale; the same physics.
- **Near-surface geophysics**: rapid reconnaissance before active-source MASW or ERT.
- **Earthquake engineering**: site-period match with structural fundamental period flags amplification hazard (Mexico City lake bed; `PD-site-response`).

**When you see this in a paper**: confirm SESAME peak-quality criteria (signal-to-noise, peak persistence, azimuthal stability); single-station H/V without those checks is provisional.

**Anchor citations**:
- Nakamura, Y. (1989). A method for dynamic characteristics estimation of subsurface using microtremor on the ground surface. *Quarterly Report of RTRI*, 30(1), 25–33.
- SESAME (2004). *Guidelines for the implementation of the H/V spectral ratio technique on ambient vibrations*. European Commission project SESAME, deliverable D23.12.

**Related cards**: `MC-seismo-MASW`, `MC-seismo-ambient-noise`, `CC-seismo-Vs`, `CC-geotech-G-Gmax`, `PD-site-response`

---

## MC-geotech-triaxial: Triaxial and direct-shear laboratory testing

**What it is**: the workhorse laboratory test suite for soil strength and stiffness. The triaxial apparatus applies independent axial and confining stresses to a cylindrical specimen (typically 38–100 mm diameter) under controlled drainage and pore-pressure measurement. Standard variants: consolidated-drained (CD), consolidated-undrained (CU), unconsolidated-undrained (UU). Companion tests: direct shear (a single-plane shear box) and oedometer (1D consolidation under K_0 conditions).

**What you can retrieve**:
- Drained strength parameters c', φ' from a set of CD or CU triaxials at different confining stresses.
- Undrained strength Su (`CC-geotech-Su`) from UU triaxial.
- Pore-pressure response (Skempton A, B; `CC-geotech-PorePressure`) from CU.
- Stress–strain stiffness, including small-strain Gmax with bender elements.
- Consolidation parameters c_v, m_v, OCR from oedometer (`CC-geotech-cv`).
- Standards: ASTM D7181 (CD), D4767 (CU), D2850 (UU), D3080 (direct shear), D2435 (oedometer).

**Failure modes**:
- Sample disturbance — especially for soft sensitive clays — biases strength low.
- Saturation incomplete; B-check must be reported.
- Stress paths in routine tests do not always match field loading; specialized tests (true triaxial, hollow cylinder) cover non-axisymmetric paths.
- Strain-rate effects in undrained tests (10× rate ↔ ≈ 10% strength).

**Cross-discipline uses**:
- **Hydrology**: oedometer m_v feeds Sₛ for poroelastic storage in compressible aquifers.
- **Geomorphology**: drained c', φ' on natural slope soils feed `CC-geotech-FS` for hillslope stability.
- **Seismology / rock mechanics**: triaxial extended to rock samples for crustal failure laws.

**When you see this in a paper**: confirm sample provenance (undisturbed Shelby tube vs. block sample vs. reconstituted), saturation B, and the consolidation stress path before shearing.

**Anchor citations**:
- Bishop, A. W., & Henkel, D. J. (1962). *The Measurement of Soil Properties in the Triaxial Test* (2nd ed.). Edward Arnold, London.
- Wood, D. M. (1990). *Soil Behaviour and Critical State Soil Mechanics*. Cambridge University Press. doi:10.1017/CBO9781139878272

**Related cards**: `CC-geotech-MohrCoulomb`, `CC-geotech-Su`, `CC-geotech-cv`, `CC-geotech-PorePressure`, `MC-geotech-cyclic-labs`

---

## MC-geotech-cyclic-labs: Cyclic triaxial, cyclic simple shear, and resonant column

**What it is**: dynamic-loading laboratory tests that characterize soil response to seismic-frequency cyclic strains. Cyclic triaxial (CTX): cyclic axial loading on a triaxial specimen. Cyclic direct simple shear (CDSS): plane-strain cyclic shear, the closest lab analog to one-dimensional vertically propagating SH-wave loading. Resonant column (RC): high-frequency torsional excitation of a hollow cylinder for small-strain Gmax and γ < 10⁻⁴ damping.

**What you can retrieve**:
- Cyclic resistance ratio CRR vs. number of cycles to liquefaction (`CC-geotech-CSR-CRR`).
- Modulus-reduction and damping curves G/Gmax(γ) and ξ(γ) over γ = 10⁻⁶ to 10⁻² (RC for small, CTX/CDSS for large strain) — feeding `CC-geotech-G-Gmax`.
- Pore-pressure generation models under cyclic loading.
- Standards: ASTM D5311 (CTX), D8296 (DSS), D4015 (RC).

**Failure modes**:
- Membrane compliance in CTX overestimates volumetric response of dilatant sand.
- Sample reconstitution method (moist tamping, water pluviation, dry pluviation) produces different fabrics and different CRR even at the same density.
- RC small-strain Gmax from lab samples is often lower than in-situ Vs-derived Gmax by 10–30% due to disturbance.
- Frequency dependence: lab loading at ≈ 1 Hz extrapolated to seismic ≈ 1–10 Hz adds uncertainty for plastic clays.

**Cross-discipline uses**:
- **Seismology**: damping curves ξ(γ) underlie nonlinear site response (`MC-geotech-numerical`) and contribute to apparent Q (`CC-seismo-Q`) in the near surface.
- **Near-surface geophysics**: bender-element and RC Vs link laboratory and field measurement (`MC-seismo-MASW`, `MC-geotech-CPT`).

**When you see this in a paper**: confirm reconstitution method, frequency of loading, and how cyclic resistance is defined (e.g., 5% double-amplitude axial strain in CTX vs. rᵤ = 1).

**Anchor citations**:
- Hardin, B. O., & Drnevich, V. P. (1972). Shear modulus and damping in soils: Design equations and curves. *J. Soil Mech. Found. Div. (ASCE)*, 98(7), 667–692.
- Idriss, I. M., & Boulanger, R. W. (2008). *Soil Liquefaction During Earthquakes*. EERI Monograph MNO-12.

**Related cards**: `MC-geotech-triaxial`, `CC-geotech-CSR-CRR`, `CC-geotech-G-Gmax`, `PD-liquefaction`, `PD-site-response`

---

## MC-geotech-numerical: 1D/2D nonlinear site response and SSI codes

**What it is**: numerical codes that propagate seismic motion through a layered soil column or 2D/3D model. Equivalent-linear codes (SHAKE91, Strata) iterate linear analyses at strain-compatible (G, ξ) from `CC-geotech-G-Gmax` curves; fully nonlinear codes (DEEPSOIL, OpenSees, FLAC) time-integrate constitutive laws and can include pore-pressure generation. Soil-structure interaction (SSI) couples the soil column to a structural model.

**What you can retrieve**:
- Surface time histories and response spectra from a bedrock input motion.
- Strain, stress, and pore-pressure profiles vs. depth and time.
- Site-amplification transfer functions (often compared to linear `MC-seismo-MASW`-derived predictions).
- For liquefaction-capable analyses: pore-pressure generation, post-liquefaction settlement, lateral spread.
- Codes: SHAKE91 (Idriss & Sun 1992); DEEPSOIL (Hashash et al. 2020); OpenSees (McKenna 2011); FLAC, PLAXIS (commercial).

**Failure modes**:
- Equivalent-linear underestimates response at strains > ≈ 0.1% — it cannot generate pore pressure, cannot soften beyond an iterated stiffness.
- Constitutive model choice dominates fully nonlinear outputs; calibration to laboratory data is essential.
- Input motion selection and scaling matter; PGA-only scaling produces different responses from full spectral matching.
- 2D basin effects are not captured by 1D codes.

**Cross-discipline uses**:
- **Seismology**: links source ground motion (`MC-geotech-GMPE`) to surface engineering demand; physics-based simulation (e.g., SW4) couples regional seismology to local site response.
- **Near-surface geophysics**: Vs profile from `MC-seismo-MASW` is the geometric input.
- **Hydrology**: pore-pressure generation modules couple to undrained `CC-geotech-PorePressure` response.

**When you see this in a paper**: identify the code, the constitutive model, the input motion suite, and whether equivalent-linear or fully nonlinear; equivalent-linear results above γ ≈ 0.1% should be cross-checked.

**Anchor citations**:
- Idriss, I. M., & Sun, J. I. (1992). *User's manual for SHAKE91*. Center for Geotechnical Modeling, UC Davis.
- Hashash, Y. M. A., et al. (2020). *DEEPSOIL 7.0, User Manual*. University of Illinois Urbana-Champaign.
- McKenna, F. (2011). OpenSees: A framework for earthquake engineering simulation. *Computing in Science & Engineering*, 13(4), 58–66. doi:10.1109/MCSE.2011.66

**Related cards**: `CC-geotech-G-Gmax`, `MC-geotech-cyclic-labs`, `MC-geotech-GMPE`, `PD-site-response`, `TC-10`

---

## MC-geotech-GMPE: Ground motion prediction equations (NGA-West2, NGA-East, NGA-Sub)

**What it is**: empirical models that predict ground-motion intensity measures (PGA, PGV, PSA at multiple periods) from earthquake source, path, and site parameters. The PEER NGA family is the modern reference: NGA-West2 (shallow crustal active regions; Bozorgnia et al. 2014), NGA-East (stable continental regions; PEER 2018), NGA-Subduction (Stewart et al. 2024). Built from global ground-motion databases with thousands of records per regression.

**What you can retrieve**:
- Median PGA, PGV, and pseudo-spectral acceleration PSA(T) as a function of Mw, R, V_s30, depth, mechanism.
- Intra-event and inter-event aleatory variability (σ, τ) for probabilistic hazard.
- USGS National Seismic Hazard Maps (Petersen et al. 2020 update) deliver design ground motion at every U.S. site.
- Site terms keyed on V_s30 (`CC-seismo-Vs`, `TC-12`) and increasingly on basin depth Z_1.0 or Z_2.5.

**Failure modes**:
- Extrapolation to large Mw or near-fault distances is poorly constrained; few data points exist at Mw > 7.5 within 10 km.
- Site amplification by V_s30 alone misses 3D basin amplification (`PD-site-response`).
- Stable-continental and subduction models have far fewer recordings than active-crustal; uncertainty is correspondingly higher.
- Mechanism classification (reverse, normal, strike-slip) sometimes ambiguous; affects predicted scaling.

**Cross-discipline uses**:
- **Seismology**: GMPEs are the empirical end of the source-to-site chain that physics-based simulation (e.g., SW4, SCEC BBP) seeks to replace.
- **Geotechnical engineering**: a_max from a GMPE is the input to `CC-geotech-CSR-CRR` and to nonlinear site response (`MC-geotech-numerical`).
- **Geomorphology**: Newmark displacement / coseismic-landslide hazard models (Jibson 2007) ingest GMPE PGA as forcing.

**When you see this in a paper**: confirm which GMPE(s), the magnitude/distance range of applicability, the V_s30 and site-term assumptions, and whether epistemic-uncertainty logic trees were applied.

**Anchor citations**:
- Boore, D. M., Stewart, J. P., Seyhan, E., & Atkinson, G. M. (2014). NGA-West2 equations for predicting PGA, PGV, and 5%-damped PSA. *Earthquake Spectra*, 30(3), 1057–1085. doi:10.1193/070113EQS184M
- Petersen, M. D., et al. (2020). The 2018 update of the U.S. National Seismic Hazard Model. *Earthquake Spectra*, 36(1), 5–41. doi:10.1177/8755293019878199
- Stewart, J. P., et al. (2024). NGA-Subduction global ground-motion models. *Earthquake Spectra*, 40(1), 31–62. doi:10.1177/87552930231180071

**Related cards**: `CC-seismo-magnitude`, `CC-seismo-Vs`, `CC-geotech-CSR-CRR`, `MC-geotech-numerical`, `PD-coseismic-landslide`, `TC-12`
