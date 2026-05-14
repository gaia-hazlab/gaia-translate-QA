---
discipline: agricultural_sciences
purpose: system-prompt summary, ~350 words
schema_version: v3
---

# Agricultural sciences — summary

Agricultural sciences studies managed-ecosystem production of food, feed, fiber, and fuel — the practice and science of optimizing crop and livestock yield while managing inputs (water, fertilizer, energy, land) and outputs (yield, environmental externalities). The discipline is the dominant human modifier of the global water, sediment, and carbon cycles (`TC-18`); roughly 70% of freshwater withdrawals globally are for irrigation, 25% of anthropogenic GHG emissions are agricultural, and cropland is the leading non-roads sediment source in many basins.

**Core governing equations**:
- Penman-Monteith FAO-56 reference ET₀; crop ET = K_c × ET₀ (`CC-ag-ET0`).
- Soil water balance over root zone dS/dt = P + I − ET − D − Q (precip + irrigation − ET − drainage − runoff).
- van Genuchten retention curve θ(ψ); plant available water (`CC-ag-PAW`).
- FAO-33 yield-water-response (1 − Y_a/Y_m) = K_y (1 − ET_a/ET_m) (`CC-ag-yield-water-response`).
- Soil-organic-carbon stock SOC = bulk density × depth × C-fraction (`CC-ag-SOC`).

**Core observables**: reference ET₀ and crop coefficient K_c; plant available water PAW; yield-water response factor K_y and crop water productivity CWP; soil organic carbon SOC stock and turnover rate; nitrogen-use efficiency NUE and agricultural GHG fluxes (N₂O, CH₄, CO₂); irrigation withdrawal at field and regional scale.

**Core measurement infrastructure**: in-situ soil-moisture instruments (TDR, FDR, neutron probes, COSMOS, SMAP — shared with hydrology); satellite ET retrievals (METRIC, SSEBop, PT-JPL, OpenET); crop models (DSSAT, APSIM, AquaCrop, CropSyst); yield-monitor combine data + remote-sensing yield estimation (Landsat / Sentinel-2 / UAV NDRE); USDA NASS Cropland Data Layer and Census of Agriculture; SSURGO / ROSETTA soil-data infrastructure.

**Cross-discipline hooks the chatbot should be alert for**:
- *Agriculture ↔ hydrology*: irrigation-driven aquifer depletion (`PD-aquifer-depletion`); reference ET₀ as Penman-Monteith bridge (`TC-18`); nutrient leaching to groundwater.
- *Agriculture ↔ geotechnical engineering*: pumping-induced consolidation and land subsidence (`PD-subsidence-consolidation`); same effective-stress mechanism (`TC-02`).
- *Agriculture ↔ geomorphology*: tillage erosion and post-tillage windblown dust (`PD-tillage-erosion`); cropland as dominant non-roads sediment source (`TC-13`).
- *Agriculture ↔ ecology*: agriculture as managed ecosystem; agroecology at the interface; SOC and biodiversity coupling.
- *Agriculture ↔ atmospheric sciences*: agricultural N₂O is the dominant N₂O source; irrigation modifies regional ET and downwind precipitation (Lo & Famiglietti 2013); flash drought and yield loss (`PD-flash-drought`, `PD-agricultural-drought`).
- *Agriculture ↔ seismology*: aquifer depletion modulates seasonal-to-decadal seismicity (Johnson et al. 2017 California).
- *Agriculture ↔ near-surface geophysics*: ERT, EMI, GPR for irrigation management, drainage-tile mapping, and root-zone characterization (Romero-Ruiz et al. 2018).

**Foundational anchor citations**: Penman (1948) and Monteith (1965) for evapotranspiration; Allen et al. (1998) FAO-56 for reference ET; Doorenbos & Kassam (1979) FAO-33 for yield-water response; Wischmeier & Smith (1978) USLE for erosion; Jones et al. (2003) DSSAT and Holzworth et al. (2014) APSIM for crop modeling; Scanlon et al. (2012) for global irrigation-aquifer depletion; Famiglietti (2014) for the global groundwater crisis; Foley et al. (2011) for cultivated-planet framing; Montgomery (2007) for agricultural soil erosion.

For full details, retrieve from `skills/long_form/agricultural_sciences/` (concept cards, method cards, phenomenon dossiers, translation cards).
