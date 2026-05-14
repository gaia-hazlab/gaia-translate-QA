---
discipline: near_surface_geophysics
purpose: system-prompt summary, ~350 words
schema_version: v3
---

# Near-surface geophysics — summary

Near-surface geophysics (NSG) studies the upper 0–500 m of the subsurface using elastic, electrical, electromagnetic, and gravitational physics. It is the connective tissue between deep-Earth and surface-Earth disciplines: NSG images the substrate that hydrology, geomorphology, geotechnical engineering, ecology, and agriculture all depend on, but at depths where surface-wave physics meets engineering tests and where the petrophysical foundations of hydrogeophysics live. Its operational identity is multi-method joint imaging of the critical zone (`TC-19`); the substrate observations enable downstream process-based modeling across the other eight disciplines.

**Core governing equations**:
- Archie's law σ_bulk = σ_w × φ^m × S_w^n (Archie 1942); the foundational petrophysics for resistivity → water saturation.
- Topp's equation ε_r ≈ 3 + 9.3θ + 146θ² − 76.7θ³ (Topp 1980); ε → soil water content.
- Reflection coefficient R = (Z₂ − Z₁)/(Z₂ + Z₁) at acoustic-impedance contrasts.
- Rayleigh-wave dispersion c(f) → V_s(z) via MASW.
- Maxwell's equations for time- and frequency-domain electromagnetic inductive methods.
- Bouguer-corrected gravity for subsurface density imaging.

**Core observables**: electrical resistivity ρ_e and conductivity σ; relative dielectric permittivity ε_r; acoustic impedance Z and reflection coefficient R; EM conductivity from TEM, FEM, AEM; Bouguer gravity anomaly; total-field magnetic anomaly ΔF; subsurface V_p (refraction tomography) and V_s (MASW, surface-wave inversion).

**Core measurement infrastructure**: electrical resistivity tomography (ERT, including time-lapse and cross-borehole); ground-penetrating radar (GPR); airborne electromagnetic surveys (AEM — VTEM, SkyTEM, TEMPEST); seismic refraction tomography (complementary to seismology's MASW); ground and airborne gravimetry; ground and airborne magnetics; joint-inversion frameworks (cross-gradient and petrophysical coupling).

**Cross-discipline hooks the chatbot should be alert for**:
- *NSG ↔ hydrology*: hydrogeophysics — the foundational coupling. Aquifer-architecture mapping (`PD-aquifer-architecture`); contaminant-plume tracking (`PD-contaminant-plume`); water-table imaging (Binley et al. 2015 framework).
- *NSG ↔ seismology*: shared substrate; MASW is the bridge method (`MC-seismo-MASW`); joint geophysical inversion (`TC-08`).
- *NSG ↔ geotechnical engineering*: V_s30 site characterization (`MC-seismo-MASW`, `CC-seismo-Vs`, `TC-12`); HVSR site response (`MC-geotech-HVSR`); refraction for bedrock depth.
- *NSG ↔ geomorphology*: regolith-bedrock interface for soil-production studies (Heimsath framework); paleochannel mapping; permafrost / active-layer dynamics (`PD-permafrost-thaw`).
- *NSG ↔ ecology*: rooting-zone water-content imaging via ERT and GPR; SoilGrids-like substrate mapping at site scale.
- *NSG ↔ agricultural sciences*: in-field σ maps for soil-texture / salinity / drainage (Romero-Ruiz et al. 2018); precision-agriculture-scale decision support.
- *NSG ↔ atmospheric sciences*: less direct; but ground truth for satellite microwave soil-moisture retrievals (SMAP, `MC-hydro-SMAP`).

**Foundational anchor citations**: Archie (1942) for the petrophysical resistivity-saturation link; Topp et al. (1980) for the ε-water-content relation; Nakamura (1989) HVSR; Park, Miller & Xia (1999) MASW; Gallardo & Meju (2003) cross-gradient joint inversion; Linde et al. (2006) and Binley et al. (2015) for hydrogeophysics; Parsekian et al. (2015) for multi-method critical-zone imaging; Brantley et al. (2007) for CZ-as-integrative-framework.

For full details, retrieve from `skills/long_form/near_surface_geophysics/` (concept cards, method cards, phenomenon dossiers, translation cards).
