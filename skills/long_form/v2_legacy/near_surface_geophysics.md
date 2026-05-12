# Near-surface geophysics — Gaia translator skill file

Companion discipline file. Citation policy as in `atmospheric_sciences.md`.

Near-surface geophysics is the connective tissue between the deep-Earth and surface-Earth disciplines. It images the substrate that hydrology, geomorphology, geotechnical engineering, ecology, and agriculture all care about. It shares wave physics with seismology and electromagnetic physics with environmental engineering.

## Core variables and equations

- Seismic refraction/reflection: travel-time t(x) and the slope/intercept method; reflection coefficient R = (Z₂ − Z₁)/(Z₂ + Z₁) with acoustic impedance Z = ρV.
- Dispersion of Rayleigh waves: phase velocity c(f) increases with depth-averaged Vs. MASW (Park, Miller & Xia 1999) inverts c(f) → Vs(z).
- HVSR (Nakamura 1989): horizontal-to-vertical spectral ratio peak f₀ ≈ Vs/(4H) reveals sediment-bedrock interface depth.
- Electrical resistivity ρ_e (Ω·m); Archie's law σ = σ_w φ^m S_w^n connects bulk resistivity to porosity, water saturation, fluid conductivity (Archie 1942 — same equation petrophysicists use at depth).
- Electromagnetic induction (TEM/FEM): apparent conductivity σ_a as a function of transmitter-receiver geometry and frequency.
- GPR: two-way travel time t = 2d/v, with v = c/√(εᵣ μᵣ); dielectric permittivity ε for water-content estimation via Topp 1980 (εᵣ ≈ 3 + 9.3θ + 146θ² − 76.7θ³).
- Magnetics: total field anomaly ΔF; gravity: free-air and Bouguer anomalies.

## Methods

- MASW (multichannel analysis of surface waves) for Vs profiling (Park et al. 1999).
- Seismic refraction tomography for bedrock topography and weathering thickness.
- Electrical resistivity tomography (ERT) for water-table and contaminant plume mapping; time-lapse ERT for monitoring infiltration.
- GPR for soil layering, permafrost, root-zone water content, archaeology, infrastructure (rebar in concrete, utility location).
- Airborne electromagnetics (AEM) for regional aquifer mapping (e.g. AEM of Mississippi Embayment, Central Valley).
- Distributed Acoustic Sensing (DAS): repurposes telecom fiber as a dense seismic / strain array — the Gaia group's active method (Lindsey & Martin 2021 review).
- HVSR microtremor surveys for site characterization without active source.
- Joint inversion: MASW + ERT + gravity to break ambiguity (Linde et al. 2006).

## Phenomena studied

- Depth to water table and water-table dynamics (ERT, GPR).
- Bedrock topography under soil/regolith — the soil-production interface.
- Frozen-ground (permafrost) extent and thaw dynamics.
- Contaminant plume migration.
- Engineering site characterization (Vs30 for ASCE 7 design code) — direct interface with geotechnical engineering.
- Archaeological prospection (non-destructive subsurface imaging).
- Infrastructure monitoring (DAS for pipelines, tunnels, dams).
- Critical zone architecture — the depth-to-bedrock, regolith thickness, fracture density that controls hydrologic storage and weathering.

## Translation hooks

- **→ Seismology**: same physics, different depth range and frequency band. Surface-wave dispersion is the bridge — methods scale from MASW (m–100 m) to ambient noise tomography (km–10 km). DAS is the technology where the two communities are merging.
- **→ Hydrology**: ERT and GPR are the primary geophysical probes of water content and water-table depth at the catchment scale (Binley et al. 2015 review). Time-lapse seismic dv/v from ambient noise probes the same volume.
- **→ Geotechnical engineering**: Vs30 from MASW is the bridge variable. HVSR provides the resonant frequency for site amplification calculations.
- **→ Geomorphology**: imaging the soil-bedrock interface gives the regolith depth needed in soil-production-rate inversions (Heimsath 1997 framework). Lidar topography + ERT bedrock + cosmogenic dating is a powerful combination.
- **→ Ecology**: imaging the rooting zone, soil moisture, and substrate properties that determine plant water availability.
- **→ Agricultural sciences**: soil structure, drainage tile mapping, irrigation-management diagnostics (Romero-Ruiz et al. 2018).
- **→ Atmospheric sciences**: less direct, but ground-truth for satellite microwave retrievals of soil moisture (SMAP) often comes from co-located geophysical surveys.

## Foundational references

- Archie, G. E. (1942). The electrical resistivity log as an aid in determining some reservoir characteristics. *Transactions of the AIME*, 146(1), 54–62. doi:10.2118/942054-G
- Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. *Water Resources Research*, 16(3), 574–582. doi:10.1029/WR016i003p00574
- Nakamura, Y. (1989). A method for dynamic characteristics estimation of subsurface using microtremor on the ground surface. *QR RTRI*, 30(1), 25–33.
- Park, C. B., Miller, R. D., & Xia, J. (1999). Multichannel analysis of surface waves. *Geophysics*, 64(3), 800–808. doi:10.1190/1.1444590
- Linde, N., Binley, A., Tryggvason, A., Pedersen, L. B., & Revil, A. (2006). Improved hydrogeophysical characterization using joint inversion of cross-hole electrical resistance and ground-penetrating radar traveltime data. *Water Resources Research*, 42(12), W12404. doi:10.1029/2006WR005131
- Binley, A., Hubbard, S. S., Huisman, J. A., Revil, A., Robinson, D. A., Singha, K., & Slater, L. D. (2015). The emergence of hydrogeophysics for improved understanding of subsurface processes over multiple scales. *Water Resources Research*, 51(6), 3837–3866. doi:10.1002/2015WR017016
- Parsekian, A. D., Singha, K., Minsley, B. J., Holbrook, W. S., & Slater, L. D. (2015). Multiscale geophysical imaging of the critical zone. *Reviews of Geophysics*, 53(1), 1–26. doi:10.1002/2014RG000465
- Romero-Ruiz, A., et al. (2018). A review of geophysical methods for soil structure characterization. *Reviews of Geophysics*, 56(4), 672–697. doi:10.1029/2018RG000611
- Lindsey, N. J., & Martin, E. R. (2021). Fiber-optic seismology. *Annu. Rev. Earth Planet. Sci.*, 49, 309–336. doi:10.1146/annurev-earth-072420-065213
