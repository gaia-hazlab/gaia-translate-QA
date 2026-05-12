---
discipline: geotechnical_engineering
card_type: translation
schema_version: v3
---

# Geotechnical engineering — translation cards

Cross-discipline bridges originating from geotechnical engineering. Complements `TC-01` (diffusion, where c_v is one of the diffusivities), `TC-02` (effective stress, where Mohr-Coulomb is the geotech instantiation), and `TC-04` (power laws, which include landslide size statistics). Format follows `docs/card_format_spec.md`.

---

## TC-10: Linear seismology ↔ nonlinear geotechnical site response

**Shared structure**: vertical propagation of seismic SH waves through a layered near-surface column. In the small-strain limit the problem is purely elastic (linear Vs profile + complex impedance + transfer function). At engineering ground-motion levels the soil becomes nonlinear: stiffness degrades (G/Gmax, `CC-geotech-G-Gmax`), damping increases, and in saturated cohesionless layers pore pressure rises until liquefaction. The two communities — seismology / NSG and geotechnical engineering — write the same wave equation in different regimes and historically have not always communicated.

**Discipline-specific manifestations**:
- **Seismology / NSG**: 1D linear-elastic transfer functions from `MC-seismo-MASW` Vs profiles; ambient-noise H/V (`MC-geotech-HVSR`) and SSR for site-effect estimation; full physics-based 3D simulation (SW4, SCEC BBP). Valid for γ < ≈ 10⁻⁴.
- **Geotechnical engineering**: equivalent-linear (SHAKE91) and nonlinear (DEEPSOIL, OpenSees) site response with G/Gmax(γ) and ξ(γ) curves from `MC-geotech-cyclic-labs`. Required when γ > ≈ 10⁻⁴ or when liquefaction is plausible.
- **Hydrology**: pore-pressure response (`CC-geotech-PorePressure`) provides the coupling that makes the geotechnical problem fundamentally different from the seismological one — once σ' drops, the assumed elastic-medium framework no longer applies.

**When the analogy holds**:
- Small-strain regime (γ < 10⁻⁴): linear seismology is correct; geotechnical and seismological transfer functions agree.
- Stiff soils and rock, high V_s30: nonlinearity threshold is rarely exceeded.
- Short-duration moderate shaking on dense or unsaturated sites.

**When the analogy breaks**:
- High PGA on soft sites (V_s30 < 360 m/s) routinely produces γ > 10⁻³; equivalent-linear underpredicts and fully nonlinear is required.
- Saturated cohesionless layers — pore-pressure generation is a wholly geotechnical phenomenon outside the seismological framework.
- Basin-edge focusing and 3D effects break 1D assumptions on both sides.

**Translator agent move**: when a paper reports a "site amplification factor" or "transfer function," determine the input strain regime. For small-strain or weak-motion studies, linear seismology is sufficient. For design-level ground motion on soft soils or for liquefiable sites, the geotechnical nonlinear framework (`MC-geotech-numerical`, `CC-geotech-G-Gmax`) is mandatory. Retrieve both sides; flag any paper that uses linear transfer functions to interpret strong-motion records on soft soils.

**Anchor citations**:
- Idriss, I. M., & Sun, J. I. (1992). *User's manual for SHAKE91*. UC Davis.
- Hashash, Y. M. A., et al. (2020). *DEEPSOIL 7.0, User Manual*. University of Illinois Urbana-Champaign.
- Stewart, J. P., et al. (2014). Amplification factors for spectral acceleration in active regions. *Bull. Seismol. Soc. Am.*, 104(6), 3019–3036. doi:10.1785/0120130319

**Related cards**: `CC-geotech-G-Gmax`, `CC-seismo-Vs`, `MC-geotech-numerical`, `MC-seismo-MASW`, `PD-site-response`, `TC-12`

---

## TC-11: Engineered factor of safety ↔ natural hillslope stability

**Shared structure**: slope stability is governed by the Mohr-Coulomb condition τ_d > τ_f → failure, expressed as FS = τ_f/τ_d < 1. The same equation is written by geotechnical engineers analyzing engineered slopes (cuts, fills, embankments, dam slopes) and by geomorphologists analyzing natural hillslopes under transient rainfall pore pressure. Boundary conditions, drainage assumptions, and forcing differ; the underlying physics is identical.

**Discipline-specific manifestations**:
- **Geotechnical engineering**: limit-equilibrium FS (Bishop, Janbu, Spencer, Morgenstern-Price); deterministic c', φ' from `MC-geotech-triaxial`; design FS targets 1.3–1.5; Newmark coseismic displacement (`PD-coseismic-landslide`).
- **Geomorphology**: infinite-slope FS with transient pore pressure (Iverson 2000); spatial models (SHALSTAB, Montgomery & Dietrich 1994; SINMAP); regionalized c', φ' from soil maps; landslide-inventory and statistical-machine-learning models trained on historical inventories.
- **Hydrology**: AR-driven rainfall (`PD-AR-landslide`) generates the transient pore-pressure forcing; subsurface stormflow timescales (`CC-hydro-D`) set the response.
- **Ecology**: root cohesion adds an apparent c'_root (Sidle & Ochiai 2006); root-strength loss after wildfire is a major source of post-fire landslide hazard.

**When the analogy holds**:
- Translatable parameters: c', φ', Sᵤ are physically the same quantities across the two communities.
- The shallow-failure (1–3 m), thin-soil, rainfall-triggered case is well captured by the infinite-slope simplification of Mohr-Coulomb.
- Newmark coseismic displacement and rainfall-triggered FS reduction can be combined for joint-hazard analysis.

**When the analogy breaks**:
- Engineered slopes have controlled drainage, designed geometry, and (often) instrumentation; natural slopes have heterogeneous stratigraphy, root reinforcement, and transient hydrology that engineering FS analysis treats as nuisance.
- Deep-seated landslides involve 3D failure surfaces poorly modeled by infinite slope.
- Engineering FS targets a single-event probability; geomorphological time-integrated hillslope evolution is a different statistical question.

**Translator agent move**: when a paper reports an FS, identify (a) the failure-surface geometry (infinite slope vs. limit equilibrium vs. 3D FEM), (b) the drainage assumption (drained c'/φ' vs. undrained Sᵤ), and (c) the forcing (static vs. transient pore pressure vs. cyclic). Cross-retrieve the geomorphological and geotechnical sides — engineers and geomorphologists rarely cite each other but solve the same equation.

**Anchor citations**:
- Iverson, R. M. (2000). Landslide triggering by rain infiltration. *Water Resources Research*, 36(7), 1897–1910. doi:10.1029/2000WR900090
- Montgomery, D. R., & Dietrich, W. E. (1994). A physically based model for the topographic control on shallow landsliding. *Water Resources Research*, 30(4), 1153–1171. doi:10.1029/93WR02979
- Sidle, R. C., & Ochiai, H. (2006). *Landslides: Processes, Prediction, and Land Use*. AGU Water Resources Monograph 18. doi:10.1029/WM018

**Related cards**: `CC-geotech-FS`, `CC-geotech-MohrCoulomb`, `CC-geotech-PorePressure`, `CC-hydro-p`, `PD-AR-landslide`, `PD-coseismic-landslide`

---

## TC-12: Vs across depth regimes — geotech borehole, NSG/MASW, seismic tomography

**Shared structure**: shear-wave velocity Vs = √(μ/ρ) is one physical quantity, but four geoscience subfields measure it at incompatible depth and resolution regimes. The "Vs profile" reported in a paper is a regime-specific slice of the same field; joint inversion across regimes is the frontier. Engineering V_s30 — the time-averaged Vs in the upper 30 m — is a derived top-of-stack quantity that compresses the geotechnical sampling regime into a single number for design-code site classification (ASCE 7, Eurocode 8, NEHRP).

**Discipline-specific manifestations**:
- **Geotechnical engineering** (borehole regime, `MC-geotech-CPT`): downhole, crosshole, seismic CPT; vertical resolution 0.5–1 m; depth typically 5–30 m; 1D under-the-borehole; primary input to V_s30.
- **Near-surface geophysics** (surface-wave regime, `MC-seismo-MASW`): MASW, ReMi; depth 5–50 m active-source, 50–200 m passive; dispersion-inversion non-uniqueness.
- **Applied seismology** (ambient-noise regime, `MC-seismo-ambient-noise`): noise-correlation tomography; depth 0.1–10 km depending on frequency; well-suited to sedimentary basins.
- **Deep seismology** (tomography regime, `MC-seismo-tomography`): body- and surface-wave tomography, receiver functions, FWI; depth 1–200 km; resolution 10–100 km.

**When the analogy holds**:
- Vs is the same physical quantity at all depths; joint inversion across regimes is mathematically clean where overlap zones exist.
- V_s30 and the upper-30 m portion of a MASW profile agree well in homogeneous soils; SCPT and MASW typically within 10–20%.
- Basin-scale tomography and surface-wave NSG overlap at 0.05–0.5 km — the hydrogeophysical joint-imaging window.

**When the analogy breaks**:
- "Missing middle" — 50 m – 1 km — is undersampled by both geotech (too deep) and seismology (too shallow). For basin amplification problems this is exactly the depth that matters.
- V_s30 hides information: two sites with identical V_s30 but different impedance below 30 m amplify differently (`PD-site-response`). Engineering codes are slow to incorporate Z_1.0, Z_2.5 basin depths.
- Anisotropy (`TC-07`): tomographic Vs is azimuthally averaged; borehole Vs is direction-specific.

**Translator agent move**: when a paper reports a "Vs profile" or "V_s30," identify (a) the depth range and method, (b) whether basin or 3D structure was considered, (c) whether the derived V_s30 or Z_1.0 is being applied beyond its validity. Surface the next-regime literature: a V_s30 paper should hear about ambient-noise tomography in the same basin; a regional-tomography paper should hear about the borehole control. The "missing middle" is the most productive joint-inversion target.

**Anchor citations**:
- Boore, D. M. (2004). Estimating V_s30 (or NEHRP site classes) from shallow velocity models (depths < 30 m). *Bull. Seismol. Soc. Am.*, 94(2), 591–597. doi:10.1785/0120030105
- Foti, S., et al. (2018). Guidelines for the good practice of surface wave analysis: a product of the InterPACIFIC project. *Bulletin of Earthquake Engineering*, 16(6), 2367–2420. doi:10.1007/s10518-017-0206-7
- Shapiro, N. M., Campillo, M., Stehly, L., & Ritzwoller, M. H. (2005). High-resolution surface-wave tomography from ambient seismic noise. *Science*, 307(5715), 1615–1618. doi:10.1126/science.1108339

**Related cards**: `CC-seismo-Vs`, `CC-geotech-G-Gmax`, `MC-geotech-CPT`, `MC-seismo-MASW`, `MC-seismo-ambient-noise`, `MC-seismo-tomography`, `MC-geotech-HVSR`, `MC-geotech-GMPE`, `PD-site-response`, `PD-liquefaction`, `TC-07`, `TC-08`, `TC-10`
