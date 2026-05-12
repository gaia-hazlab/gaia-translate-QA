---
discipline: geotechnical_engineering
purpose: system-prompt summary, ~350 words
schema_version: v3
---

# Geotechnical engineering — summary

Geotechnical engineering studies the mechanical response of soil and rock to applied load, water, and seismic shaking, with applications spanning foundations, slopes, dams, levees, tunnels, embankments, and the soil column under earthquake-resilient infrastructure. The discipline sits at the intersection of solid mechanics, hydrology, seismology, and geomorphology, and supplies the engineering deliverable (factor of safety, allowable bearing pressure, liquefaction triggering, settlement) that closes the loop between Earth-science observation and built-environment design.

**Core governing equations**:
- Effective stress (Terzaghi 1925): σ' = σ − p — the single most-cited bridge in this corpus (`TC-02`).
- Mohr-Coulomb shear strength: τ_f = c' + σ' tan φ'; identical to the Coulomb failure criterion on a fault.
- Terzaghi 1D consolidation: ∂u/∂t = c_v ∂²u/∂z²; same diffusion equation as hydrology and geomorphology (`TC-01`).
- Cyclic stress ratio CSR = 0.65 (a_max/g)(σ_v0/σ'_v0) r_d; cyclic resistance ratio CRR from N₁,₆₀, q_c1N, or Vs1 (Seed-Idriss family).
- Factor of safety FS = τ_f/τ_d; Newmark (1965) coseismic displacement sliding-block model.
- Nonlinear stiffness: G/Gmax(γ) reduction, damping ξ(γ) — the regime that distinguishes geotechnical from linear-elastic seismology (`TC-10`).

**Core observables**: effective stress σ'; friction angle φ' [°]; cohesion c' [kPa]; undrained shear strength Sᵤ [kPa]; coefficient of consolidation c_v [m²/s]; pore-pressure response (Skempton A, B); cyclic stress and resistance ratios CSR, CRR; factor of safety FS; site-classification Vs30 [m/s] (same physical Vs as in seismology, sampled in the upper 30 m by borehole methods — `TC-12`); G/Gmax modulus reduction.

**Core measurement infrastructure**: Cone Penetration Test (CPT, SCPT); Standard Penetration Test (SPT); microtremor H/V (HVSR); laboratory triaxial (CU, CD, UU), oedometer, direct shear; cyclic-loading labs (cyclic triaxial, simple shear, resonant column); equivalent-linear and nonlinear site-response codes (SHAKE91, DEEPSOIL, OpenSees, FLAC, PLAXIS); NGA-West2 / NGA-East / NGA-Sub ground-motion prediction equations.

**Cross-discipline hooks the chatbot should be alert for**:
- *Geotech ↔ seismology*: effective stress (`TC-02`), Vs depth regimes (`TC-12`), linear-vs-nonlinear site response (`TC-10`), liquefaction (`PD-liquefaction`), coseismic landslides (`PD-coseismic-landslide`), GMPE-to-engineering-demand (`MC-geotech-GMPE`).
- *Geotech ↔ hydrology*: Terzaghi-Biot effective stress, consolidation as hydraulic diffusion (`TC-01`), pumping-induced subsidence (`PD-subsidence-consolidation`, `PD-aquifer-depletion`), embankment seepage and pore-pressure transients.
- *Geotech ↔ geomorphology*: engineered FS vs. natural hillslope FS (`TC-11`), Iverson (2000) transient pore pressure model, root cohesion in shallow landsliding.
- *Geotech ↔ near-surface geophysics*: MASW / SCPT joint imaging, basin amplification (`PD-site-response`), HVSR site characterization.
- *Geotech ↔ atmospheric sciences*: extreme precipitation forecasts feeding embankment pore-pressure rise (`PD-dam-levee-safety`, `PD-AR-landslide`).
- *Geotech ↔ agricultural sciences*: pumping-induced subsidence as the mechanical response to irrigation overdraft.

**Foundational anchor citations**: Terzaghi (1925/1943) for effective stress and consolidation; Seed & Idriss (1971) and Boulanger & Idriss (2014) for liquefaction; Newmark (1965) and Jibson (2007) for coseismic landslides; Skempton (1948, 1954) for undrained strength and pore-pressure parameters; Hardin & Drnevich (1972) and Vucetic & Dobry (1991) for G/Gmax; Boore et al. (2014) NGA-West2 for ground motion; Bray & Travasarou (2007) for dam-displacement analysis.

For full details, retrieve from `skills/long_form/geotechnical_engineering/` (concept cards, method cards, phenomenon dossiers, translation cards).
