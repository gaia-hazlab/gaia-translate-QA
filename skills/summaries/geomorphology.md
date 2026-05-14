---
discipline: geomorphology
purpose: system-prompt summary, ~350 words
schema_version: v3
---

# Geomorphology — summary

Geomorphology studies the form, formation, and evolution of Earth's surface — hillslopes, channels, drainage networks, fault scarps, landscape-scale topography — under the combined forcing of tectonics, climate, lithology, biology, and human activity. The discipline straddles two complementary directions: **process geomorphology** (what events move sediment now, at what rate, under what conditions) and **landscape evolution** (how a landscape integrates 10⁵–10⁸ yr of process to produce the morphology we see today).

**Core governing equations**:
- Hillslope diffusion ∂z/∂t = κ ∇²z (linear) or with nonlinear correction at S → S_c (Roering 1999); the geomorphic entry in `TC-01`.
- Stream-power bedrock incision E = K A^m S^n (Howard 1994; Whipple & Tucker 1999).
- Bed shear stress τ = ρ g R S and the Shields threshold τ_c* for grain entrainment; Meyer-Peter-Müller bedload q_b ~ (τ − τ_c)^1.5.
- Sediment continuity ∂z/∂t = U − ∇·Q_s; the geomorphic analog to the watershed water balance (`TC-13`).
- Cosmogenic-isotope erosion rate E from N concentration, production rate, and attenuation length (Lal 1991; Granger et al. 1996).
- Power-law / inverse-gamma forms for landslide and flood-frequency size distributions; shared statistical machinery with Gutenberg-Richter (`TC-04`, but with the explicit refusal of "shared statistics → shared physics").

**Core observables**: hillslope sediment diffusivity κ; stream power Ω; bed shear stress τ and Shields τ*; sediment flux Q_s (⚠️ symbol collision with hydrology Q for water discharge — `CC-hydro-Q`); long-term denudation rate E from cosmogenic isotopes; channel steepness index ksn; flood-frequency Q_T at return interval T; landslide size-frequency parameters (Malamud roll-over and tail exponent).

**Core measurement infrastructure**: airborne / terrestrial / drone lidar and Structure-from-Motion (USGS 3DEP, OpenTopography); cosmogenic isotopes (¹⁰Be / ²⁶Al / ³⁶Cl) via CRONUS-Earth; DEM-analysis software (TopoToolbox, RichDEM, LSDTopoTools); landscape-evolution models (Landlab, FastScape, CHILD, CAESAR-Lisflood); debris-flow runout models (D-Claw, RAMMS, FLO-2D); fluvial sediment monitoring (USGS NWIS suspended sediment, Helley-Smith bedload, seismic-noise inversion); InSAR (Sentinel-1, ALOS-2, NISAR).

**Cross-discipline hooks the chatbot should be alert for**:
- *Geomorph ↔ hydrology*: AR-driven landslides and floods (`PD-AR-landslide`, `PD-river-floods`), stream power vs. discharge, sediment continuity vs. water continuity (`TC-13`), watershed-budget closure (`TC-06`).
- *Geomorph ↔ seismology*: bedload transport ↔ high-frequency seismic noise (`TC-14`), fault-scarp morphology (`PD-fault-scarp`), coseismic landslides (`PD-coseismic-landslide`), landslide size statistics (`TC-04`).
- *Geomorph ↔ geotechnical engineering*: engineered FS ↔ natural hillslope FS (`TC-11`), Iverson 2000 transient pore-pressure mechanics (`TC-02`), debris-flow runout modeling.
- *Geomorph ↔ atmospheric sciences*: AR statistics, precipitation extremes, climate-erosion feedbacks.
- *Geomorph ↔ ecology*: root-cohesion contribution to slope stability (Sidle & Ochiai 2006), post-fire erosion (`PD-post-fire-erosion`), salmon habitat shaped by sediment regime.
- *Geomorph ↔ near-surface geophysics*: lidar DoD complements InSAR; joint geophysical imaging of subsurface stratigraphy.

**Foundational anchor citations**: Hack (1957) drainage-network law; Wolman & Miller (1960) magnitude-frequency framework; Howard (1994) and Whipple & Tucker (1999) for stream-power incision; Lal (1991) and Granger et al. (1996) for cosmogenic-isotope erosion rates; Iverson (1997) for debris-flow mechanics; Iverson (2000) for rainfall-triggered landslide pore-pressure model; Burtin et al. (2008) for seismic-bedload coupling; Malamud et al. (2004) for landslide statistics.

For full details, retrieve from `skills/long_form/geomorphology/` (concept cards, method cards, phenomenon dossiers, translation cards).
