---
discipline: agricultural_sciences
card_type: method
schema_version: v3
---

# Agricultural sciences — method cards

Each card describes one measurement technique, instrument, or dataset relevant to agricultural sciences. Format follows `docs/card_format_spec.md`.

---

## MC-ag-soil-moisture: In-situ soil-moisture instruments for agriculture

**What it is**: the suite of in-situ soil-moisture instruments used in agricultural management and research: time-domain reflectometry (TDR) probes, frequency-domain reflectometry (FDR) capacitance sensors, neutron probes, and gypsum blocks. Distinct in deployment context from the satellite (`MC-hydro-SMAP`) and intermediate-scale (`MC-hydro-COSMOS`) methods, though all measure the same physical quantity. Foundational for irrigation scheduling, crop modeling validation, and yield-mapping support.

**What you can retrieve**:
- Volumetric soil water content θ [m³/m³] at point scale, typically 5–60 cm depths.
- Continuous time series at automated sites (USDA SCAN network, state climate networks like WSU AgWeatherNet, Texas A&M TexMesonet).
- Depth profiles at multi-sensor stations for root-zone moisture inference.
- Sensor calibration to gravimetric water content via in-situ sampling.

**Failure modes**:
- TDR / FDR sensors calibrated to mineral soils underestimate water content in high-organic-matter soils.
- Local heterogeneity at the cm scale (root channels, stones) means point sensors don't represent the surrounding meter.
- Neutron-probe access tubes require careful installation and gradually degrade; modern preference for non-radioactive alternatives.
- Soil disturbance during sensor installation creates artifacts that persist for weeks to months.

**Cross-discipline uses**:
- **Hydrology**: ground-truth for SMAP (`MC-hydro-SMAP`) and COSMOS (`MC-hydro-COSMOS`); same physical observable at different footprints.
- **Atmospheric**: surface-layer model validation; flash-drought monitoring requires sub-monthly resolution.
- **Ecology**: rooting-zone water availability is the proximate driver of plant water status; ecology eddy-covariance towers usually include co-located soil-moisture sensors.

**When you see this in a paper**: confirm sensor type, depth, calibration, and number of sensors per site; spatial representativeness scales with sensor count, not site count.

**Anchor citations**:
- Robinson, D. A., Campbell, C. S., Hopmans, J. W., Hornbuckle, B. K., Jones, S. B., Knight, R., Ogden, F., Selker, J., & Wendroth, O. (2008). Soil moisture measurement for ecological and hydrological watershed-scale observatories: A review. *Vadose Zone Journal*, 7(1), 358–389. doi:10.2136/vzj2007.0143
- Schaefer, G. L., Cosh, M. H., & Jackson, T. J. (2007). The USDA Natural Resources Conservation Service Soil Climate Analysis Network (SCAN). *Journal of Atmospheric and Oceanic Technology*, 24(12), 2073–2077. doi:10.1175/2007JTECHA930.1

**Related cards**: `MC-hydro-SMAP`, `MC-hydro-COSMOS`, `MC-hydro-eddycov`, `CC-ag-PAW`, `CC-ag-irrigation-demand`

---

## MC-ag-OpenET: Satellite-derived ET for water-rights and irrigation accounting

**What it is**: a suite of remote-sensing-based actual-ET retrievals using surface-energy-balance methods. METRIC (Mapping Evapotranspiration at high Resolution with Internalized Calibration; Allen et al. 2007) and its descendants — SSEBop (operational SSEB), SEBAL, PT-JPL, DisALEXI — combine satellite thermal-IR land-surface temperature with auxiliary inputs (R_n, surface roughness, vegetation indices) to estimate actual ET at 30–250 m. The OpenET initiative (Melton et al. 2021) integrates multiple algorithms into a single operational product for the western U.S.

**What you can retrieve**:
- Actual ET [mm/day, mm/month, mm/yr] at 30 m (Landsat) to 250 m (MODIS), with monthly cadence.
- Algorithm comparison: 6 algorithms within OpenET disagree by 10–30% on the same field, providing implicit uncertainty estimate.
- Field- and parcel-scale ET for water-rights accounting; integrated state-level legal frameworks (California SGMA, Colorado).
- Access: OpenET portal (openet.io); Google Earth Engine; USGS National Water Census.

**Failure modes**:
- Cloud-cover gaps in optical and thermal imagery; spatial-temporal gap-filling adds uncertainty.
- Thermal-IR sensitivity to surface conditions (bare soil vs. vegetation) requires careful surface-type segmentation.
- Algorithm disagreement is largest under partial canopy, irrigated arid environments, and post-disturbance landscapes — exactly the agriculturally-relevant cases.
- Validation against eddy-covariance ET (`MC-hydro-eddycov`) shows 10–25% MAE typical.

**Cross-discipline uses**:
- **Hydrology**: satellite ET closes the watershed-scale water balance (`TC-06`) where ground-based ET is unavailable; standard operational input.
- **Ecology**: same product is used for ecosystem-ET monitoring in non-agricultural contexts.
- **Water-rights and agricultural law**: U.S. western water-rights administration increasingly uses satellite ET to estimate consumptive use; SGMA (Sustainable Groundwater Management Act in California) is the canonical case.

**When you see this in a paper**: confirm algorithm (or OpenET ensemble), Landsat path/row, time period, gap-filling method; field-scale validation against eddy-covariance is preferred but rarely available.

**Anchor citations**:
- Allen, R. G., Tasumi, M., & Trezza, R. (2007). Satellite-based energy balance for mapping evapotranspiration with internalized calibration (METRIC) — Model. *Journal of Irrigation and Drainage Engineering*, 133(4), 380–394. doi:10.1061/(ASCE)0733-9437(2007)133:4(380)
- Melton, F. S., et al. (2021). OpenET: Filling a critical data gap in water management for the western United States. *Journal of the American Water Resources Association*, 58(6), 971–994. doi:10.1111/1752-1688.12956

**Related cards**: `CC-ag-ET0`, `CC-hydro-ET`, `MC-hydro-eddycov`, `MC-eco-remote-sensing`, `CC-ag-irrigation-demand`, `TC-06`

---

## MC-ag-crop-models: DSSAT, APSIM, AquaCrop, CropSyst

**What it is**: process-based crop simulation models that compute crop growth, water use, nutrient cycling, and yield from weather forcing, soil characteristics, and management decisions. The dominant models: DSSAT (Decision Support System for Agrotechnology Transfer; Jones et al. 2003); APSIM (Agricultural Production Systems sIMulator; Holzworth et al. 2014); AquaCrop (FAO; Steduto et al. 2009 explicit water-yield model); CropSyst, STICS, WOFOST in regional applications. Crop-model intercomparison (AgMIP) is the multi-model uncertainty estimator.

**What you can retrieve**:
- Daily simulated growth state (LAI, biomass, root depth, phenological stage).
- Water and nutrient balances; irrigation and fertilizer scheduling support.
- Yield prediction under specified management and weather; sensitivity to climate scenarios.
- Multi-model ensemble outputs via AgMIP harmonized protocols.

**Failure modes**:
- Calibration is crop- and region-specific; parameters from one cultivar / region don't transfer reliably.
- Most models don't simulate weeds, pests, diseases — assumed negligible or input as yield reduction factors.
- Yield-stage water-deficit response (K_y, `CC-ag-yield-water-response`) is empirical and uncertain at the most policy-relevant stages.
- CO₂-fertilization parameterizations show substantial inter-model variability; FACE experimental data calibrate but don't fully constrain.

**Cross-discipline uses**:
- **Hydrology**: crop models close the field-scale water budget; their ET outputs validate satellite ET products.
- **Atmospheric**: forced with NWP forecasts for seasonal yield prediction; CMIP-driven for climate-change impact assessment.
- **Ecology**: parallel to but distinct from ecosystem process models (`MC-eco-process-models`); managed-vs-natural ecosystem framing.
- **Geomorphology**: not direct; but post-erosion soil-depth losses degrade crop-model inputs over decades.

**When you see this in a paper**: identify the model, version, calibration data, and forcing. Multi-model ensembles (AgMIP) are the recommended approach; single-model results carry single-model uncertainty.

**Anchor citations**:
- Jones, J. W., et al. (2003). The DSSAT cropping system model. *European Journal of Agronomy*, 18(3–4), 235–265. doi:10.1016/S1161-0301(02)00107-7
- Holzworth, D. P., et al. (2014). APSIM — Evolution towards a new generation of agricultural systems simulation. *Environmental Modelling & Software*, 62, 327–350. doi:10.1016/j.envsoft.2014.07.009
- Steduto, P., Hsiao, T. C., Raes, D., & Fereres, E. (2009). AquaCrop — the FAO crop model to simulate yield response to water. *Agronomy Journal*, 101(3), 426–437. doi:10.2134/agronj2008.0139s
- Rosenzweig, C., et al. (2014). Assessing agricultural risks of climate change in the 21st century in a global gridded crop model intercomparison. *Proceedings of the National Academy of Sciences*, 111(9), 3268–3273. doi:10.1073/pnas.1222463110

**Related cards**: `CC-ag-ET0`, `CC-ag-PAW`, `CC-ag-yield-water-response`, `CC-ag-NUE`, `MC-eco-process-models`, `MC-hydro-modeling`, `PD-agricultural-drought`, `PD-climate-adaptation-cropping`

---

## MC-ag-yield-monitoring: In-field yield monitors and remote-sensing yield estimation

**What it is**: instrumented combine harvesters with mass-flow sensors (impact plates, optical sensors), GPS positions, and grain-moisture sensors that produce field-scale yield maps at the harvest pass. Complemented by remote-sensing yield estimation from Landsat / Sentinel-2 NDVI / EVI time series and UAV multispectral (NDRE for canopy nitrogen) imagery. Together they provide the operational yield-data backbone for precision agriculture.

**What you can retrieve**:
- Sub-field yield maps at 5–10 m grid resolution from combine yield monitors.
- Multi-year, in-season yield estimates from satellite NDVI/EVI time series.
- Anomaly detection: within-field yield-loss zones, cross-year yield consistency, climate-anomaly attribution.
- Aggregation: from yield-monitor data through USDA NASS (`MC-ag-NASS-CDL`) to county- and state-level yield records.

**Failure modes**:
- Yield-monitor calibration drift; mass-flow sensors require frequent calibration to gravimetric standards.
- GPS positioning errors propagate to spatial yield maps; differential GPS is now standard.
- Grain-moisture corrections vary by combine model; raw yield maps need post-processing.
- Satellite yield estimation has lower spatial resolution than in-field; biased toward dominant yield modes per pixel.

**Cross-discipline uses**:
- **Hydrology**: in-field yield variability often correlates with soil-moisture variability; pre-harvest satellite NDVI plus soil-moisture (`MC-hydro-SMAP`) maps support precision irrigation.
- **Atmospheric**: extreme-weather attribution to yield loss; insurance and crop-loss claims.
- **Ecology**: yield variability proxies for vegetation productivity at the highest-management-intensity end of the gradient.

**When you see this in a paper**: confirm calibration history and post-processing pipeline; yield-monitor data is rarely use-as-is. UAV-based NDRE / NDVI has high spatial resolution but small footprint (typically 30 m altitude × 5–10 mm GSD).

**Anchor citations**:
- Mulla, D. J. (2013). Twenty five years of remote sensing in precision agriculture: Key advances and remaining knowledge gaps. *Biosystems Engineering*, 114(4), 358–371. doi:10.1016/j.biosystemseng.2012.08.009
- Lobell, D. B. (2013). The use of satellite data for crop yield gap analysis. *Field Crops Research*, 143, 56–64. doi:10.1016/j.fcr.2012.08.008

**Related cards**: `MC-eco-remote-sensing`, `MC-hydro-SMAP`, `CC-ag-yield-water-response`, `MC-ag-NASS-CDL`, `PD-agricultural-drought`

---

## MC-ag-NASS-CDL: USDA NASS Cropland Data Layer and agricultural census

**What it is**: the U.S. Department of Agriculture's National Agricultural Statistics Service (NASS) operational data infrastructure. **Cropland Data Layer (CDL)** is an annual 30-m gridded crop-type classification for the contiguous U.S. (Boryan et al. 2011), based on Landsat / Sentinel-2 + ground-survey ground truth. **Census of Agriculture** is the 5-year complete inventory of U.S. farms (production, withdrawals, irrigation, livestock). **NASS Quick Stats** provides survey-based annual yield, acreage, and production at county and state level.

**What you can retrieve**:
- Annual CDL: 30-m crop-type maps with ~85–95% accuracy on major crops; less accurate for minor crops.
- Census of Agriculture: aggregated farm-level statistics; explicit privacy thresholds (no county-level data below ~10 farms).
- NASS Quick Stats: yield (bu/acre), acreage (acres), production (bu) by crop and year, back to mid-20th-century.
- Irrigation Survey: irrigation withdrawals by source (surface vs. groundwater), system type, application rate; updated every 5 years.

**Failure modes**:
- CDL classification accuracy degrades for rotation crops (wheat-fallow), cover crops (less spectrally distinct), and small parcels.
- Census data are coarse spatially and temporally for sub-county work; data fuzz at small geographies.
- Irrigation Survey is a probability sample, not a complete census; sampling error matters at fine spatial scales.

**Cross-discipline uses**:
- **Hydrology**: CDL paired with `MC-hydro-modeling` enables crop-specific ET, irrigation, and nutrient simulations.
- **Atmospheric / climate**: long-term agricultural-acreage records enable attribution of climate-adaptation cropping shifts (`PD-climate-adaptation-cropping`).
- **Ecology**: agricultural-landscape-cover changes anchor biodiversity-loss studies (e.g., grassland conversion in U.S. Corn Belt 2005–2015).
- **Geomorphology**: tillage-erosion estimates use CDL to identify cropland subject to disturbance.

**When you see this in a paper**: confirm CDL year and product version (occasional retroactive revisions); for Census data, confirm year and the level of statistical disclosure mitigation; for Irrigation Survey, the sampling frame and weighting.

**Anchor citations**:
- Boryan, C., Yang, Z., Mueller, R., & Craig, M. (2011). Monitoring US agriculture: The US Department of Agriculture, National Agricultural Statistics Service, Cropland Data Layer Program. *Geocarto International*, 26(5), 341–358. doi:10.1080/10106049.2011.562309

**Related cards**: `MC-eco-remote-sensing`, `MC-ag-yield-monitoring`, `CC-ag-irrigation-demand`, `PD-tillage-erosion`, `PD-climate-adaptation-cropping`

---

## MC-ag-soil-data: SSURGO, gSSURGO, ROSETTA pedotransfer functions

**What it is**: the U.S. soil-mapping and soil-property infrastructure. **SSURGO** (Soil Survey Geographic Database) and its gridded version **gSSURGO** are the NRCS-maintained soil-survey for the U.S. at 1:24,000 scale; include soil texture, depth, water-retention characteristics, and management-relevant properties. **ROSETTA** (Schaap et al. 2001) and successor models are pedotransfer functions that estimate soil hydraulic properties (van Genuchten retention parameters, saturated hydraulic conductivity) from texture and bulk density. Global analogs: SoilGrids (ISRIC), HWSD (Harmonized World Soil Database, FAO).

**What you can retrieve**:
- Polygon-level soil-component descriptions (depth, texture by horizon, organic matter, drainage class).
- Estimated hydraulic properties via ROSETTA pedotransfer (θ_FC, θ_PWP, K_sat, van Genuchten parameters).
- Plant-available water (`CC-ag-PAW`) at field and watershed scales.
- Access: NRCS Web Soil Survey, NRCS Soil Data Access (database); R `soilDB` package.

**Failure modes**:
- Historical soil surveys are at coarse scale; sub-field variability not captured.
- Soil-property estimates from texture alone are coarse; site-specific measurements always preferred.
- Pedotransfer functions trained on Midwestern U.S. soils don't transfer reliably to volcanic, peat, or tropical soils.
- ROSETTA parameter sets degrade with depth (most calibrations are surface-focused).

**Cross-discipline uses**:
- **Hydrology**: soil hydraulic properties feed `MC-hydro-modeling` (MODFLOW boundary conditions, ParFlow surface-subsurface coupling, CLM/ELM land-surface representation).
- **Geomorphology**: soil-depth and texture inform `MC-geomorph-landlab` landscape-evolution-model initial conditions and parameterizations.
- **Ecology**: soil properties constrain rooting depth and plant water access (`CC-eco-plant-water-source`).
- **Geotechnical engineering**: SSURGO can inform initial-condition assumptions for site-investigation work; field measurements always supersede.

**When you see this in a paper**: confirm SSURGO version date; check whether the work uses native polygon resolution or aggregates to coarser grid; pedotransfer function and its appropriate-region calibration.

**Anchor citations**:
- Soil Survey Staff. (2024). *Soil Survey Geographic Database (SSURGO)*. USDA Natural Resources Conservation Service. [URL: nrcs.usda.gov]
- Schaap, M. G., Leij, F. J., & van Genuchten, M. T. (2001). ROSETTA: A computer program for estimating soil hydraulic parameters with hierarchical pedotransfer functions. *Journal of Hydrology*, 251(3–4), 163–176. doi:10.1016/S0022-1694(01)00466-8
- Hengl, T., et al. (2017). SoilGrids250m: Global gridded soil information based on machine learning. *PLoS ONE*, 12(2), e0169748. doi:10.1371/journal.pone.0169748

**Related cards**: `CC-ag-PAW`, `CC-ag-SOC`, `MC-hydro-modeling`, `MC-geomorph-landlab`, `CC-eco-plant-water-source`
