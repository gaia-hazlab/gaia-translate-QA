---
discipline: atmospheric_sciences
purpose: system-prompt summary, ~350 words
schema_version: v3
---

# Atmospheric sciences — summary

Atmospheric sciences studies the structure, dynamics, and composition of Earth's atmosphere and its interaction with the land, ocean, and biosphere. The discipline is the forcing-side anchor of the GAIA translator's hazard agenda: atmospheric rivers, heat domes, flash droughts, and convective storms drive the cascades through hydrology, geomorphology, geotechnical engineering, and ecology that the translator's other cards document. Atmospheric science also contributes the most mature data-assimilation machinery in the geosciences (`TC-05`), making it the methodological template for many Earth-system inverse problems.

**Core governing equations**:
- Primitive equations: rotating Navier-Stokes + continuity + thermodynamic energy + moisture conservation.
- Hydrostatic balance ∂p/∂z = −ρg; geostrophic balance −f k × u = −(1/ρ)∇p.
- Clausius-Clapeyron de_sat/dT ≈ L_v e_sat / (R_v T²) — the thermodynamic anchor of intensifying extremes (`TC-15`).
- Buoyancy frequency N² = (g/θ) ∂θ/∂z for atmospheric stability.
- Monin-Obukhov similarity in the surface layer; Penman-Monteith for evaporative demand.

**Core observables**: temperature T and potential temperature θ; specific humidity q, RH, vapor pressure deficit VPD; precipitation rate; wind (u, v, w) and surface stress; surface pressure and geopotential height Z; integrated vapor transport IVT (the AR observable); planetary-boundary-layer depth and stability; net radiation R_n and surface energy balance terms H, LE, G.

**Core measurement infrastructure**: radiosondes (NWS network, GUAN globally); ERA5 and MERRA-2 reanalysis; GPM/IMERG satellite precipitation; NEXRAD/MRMS Doppler radar; GNSS-IWV from CORS / SuomiNet (shared infrastructure with seismology and geodesy); WRF, MPAS, IFS, GFS, CMIP6 numerical weather and climate models; GOES-R series geostationary imagery (and Himawari, Meteosat, FY-4 globally).

**Cross-discipline hooks the chatbot should be alert for**:
- *Atmospheric ↔ hydrology*: precipitation as watershed forcing, AR-driven flood events (`PD-atmospheric-river`), watershed mass balance (`TC-06`).
- *Atmospheric ↔ geomorphology*: AR-triggered landslides and floods (`PD-AR-landslide`, `PD-river-floods`), debris flows (`PD-debris-flow`), post-fire windows (`PD-post-fire-erosion`).
- *Atmospheric ↔ geotechnical engineering*: dam and levee safety under design-storm intensification (`PD-dam-levee-safety`); extreme-precipitation revisions of PMP/PMF.
- *Atmospheric ↔ seismology*: microseism generation from storm-driven ocean waves (`PD-microseism`); pressure-loading contributions to ambient noise (`CC-seismo-noise`); ionospheric and infrasound coupling at large earthquakes.
- *Atmospheric ↔ ecology*: temperature and VPD drive phenology, GPP, and drought-mortality (`PD-forest-mortality`); heat domes (`PD-heat-dome`) trigger multi-week ecosystem stress.
- *Atmospheric ↔ agricultural sciences*: irrigation scheduling, flash drought (`PD-flash-drought`), climate-adaptation cropping shifts.
- *Atmospheric ↔ near-surface geophysics*: ground truth for satellite microwave soil-moisture retrievals; pressure-loading effects on InSAR.

**Foundational anchor citations**: Charney et al. (1950) for the first numerical weather forecast; Lorenz (1963) for deterministic chaos; Manabe & Wetherald (1967) for radiative-convective climate modeling; Held & Soden (2006) for hydrologic-cycle response to warming; Hersbach et al. (2020) for ERA5 reanalysis; Ralph et al. (2019) for the AR Scale; Longuet-Higgins (1950) for the atmosphere → ocean → microseism mechanism; Evensen (1994) for ensemble data assimilation.

For full details, retrieve from `skills/long_form/atmospheric_sciences/` (concept cards, method cards, phenomenon dossiers, translation cards).
