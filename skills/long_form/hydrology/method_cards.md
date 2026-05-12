---
discipline: hydrology
card_type: method
schema_version: v3
---

# Hydrology — method cards

Each card describes one measurement technique, instrument, or dataset relevant to hydrology, with what it measures, resolution, failure modes, and cross-discipline reuse. Format follows `docs/card_format_spec.md`.

---

## MC-hydro-NWIS: USGS National Water Information System

**What it is**: the U.S. Geological Survey's operational water-data system: continuous streamflow at ~8,000 active stream gauges, groundwater levels at ~20,000 wells, water-quality records at thousands of sites, plus precipitation and reservoir storage. The single most-used hydrologic data source in the U.S.; FDSN-like in scale and central to all U.S. flood-frequency, drought, and groundwater studies. Comparable systems internationally include GRDC (Global Runoff Data Centre), EU Water Information System for Europe, BoM (Australia), and national networks.

**What you can retrieve**:
- Real-time and historical streamflow at ~15-minute resolution (Q in cfs and m³/s) with stage-Q rating curves.
- Continuous and discrete groundwater levels in ft and m.
- Water-quality records (DO, conductivity, nutrients, isotopes for select sites).
- Peak-flow series for flood-frequency analysis.
- Access: NWIS Web (https://waterdata.usgs.gov), NWIS REST services, dataRetrieval R package, hyriver Python package, BMI USGS.

**Failure modes**:
- Most U.S. basins (especially headwater) are ungauged; regional regression (StreamStats) fills the gap with substantial uncertainty.
- Rating-curve uncertainty can exceed 50% beyond the calibration range; extreme floods routinely require post-event field measurements to re-validate.
- Pre-1980 records have variable quality; many discontinued gauges have data-quality flags requiring care.
- Regulated vs. natural-flow status must be checked before using a gauge for any climate-trend or extreme-value analysis.

**Cross-discipline uses**:
- **Seismology**: streamflow Q correlates with high-frequency seismic noise (Burtin et al. 2008); coseismic stream-level steps are an `MC-seismo-broadband` ↔ NWIS bridge in `PD-eq-hydro-coupling`.
- **Geomorphology**: long Q records anchor flood-frequency power-law analyses (`TC-04`) and sediment-transport rating curves.
- **Ecology**: hydrologic-alteration indicators (`CC-eco-IHA`) derive directly from NWIS daily-Q time series.
- **Geotechnical engineering**: PMF/PMP design discharges for dam safety (`PD-dam-levee-safety`) reference long NWIS records.

**When you see this in a paper**: confirm the gauge ID and the data-retrieval date (the database is continuously revised); state regulation status; note if extreme statistics are extrapolated beyond the gauge record length.

**Anchor citations**:
- U.S. Geological Survey. (2023). USGS Water Data for the Nation. doi:10.5066/F7P55KJN
- Tasker, G. D., & Stedinger, J. R. (1989). An operational GLS model for hydrologic regression. *Journal of Hydrology*, 111(1–4), 361–375. doi:10.1016/0022-1694(89)90268-0

**Related cards**: `CC-hydro-Q`, `CC-hydro-h`, `PD-AR-landslide`, `PD-drought`, `PD-eq-hydro-coupling`

---

## MC-hydro-GRACE: GRACE / GRACE-FO satellite gravimetry

**What it is**: the Gravity Recovery and Climate Experiment (GRACE 2002–2017) and its follow-on (GRACE-FO 2018–present), twin-satellite missions whose inter-satellite K-band ranging recovers monthly time-variable gravity fields, from which total water storage (TWS) anomalies are estimated. The single most important observation for continental-scale groundwater monitoring; the only way to constrain total storage in ungauged basins.

**What you can retrieve**:
- Monthly TWS anomalies at ≥ 300 km native footprint (≈ mascon products at 1–3° grid; processed products at 0.5°).
- Equivalent-water-height anomalies in mm with ≈ 1 cm precision over large basins, degrading at smaller scale.
- Mass balance partitioning into soil moisture, snow, groundwater (with substantial model-assumption load).
- Access: NASA JPL GRACE Tellus, CSR mascons, GFZ, GRACE-FO Level-3 products.

**Failure modes**:
- Native footprint ≥ 300 km — coastal, mountainous, and small-basin signals are smeared.
- TWS → groundwater partitioning requires removing modeled snow, surface water, and soil moisture; the partitioning is model-assumption-loaded (Famiglietti 2014).
- The 11-month gap between GRACE end (2017) and GRACE-FO start (2018) creates an unavoidable discontinuity.
- Sub-monthly resolution unavailable; flash-drought attribution and rapid pumping events are below temporal resolution.

**Cross-discipline uses**:
- **Geotechnical engineering**: GRACE TWS depletion correlates with InSAR subsidence in heavily pumped basins; joint analysis constrains aquitard compressibility (`PD-subsidence-consolidation`, `MC-geotech-CPT`-derived m_v).
- **Seismology**: surface mass loading from GRACE modulates regional seismicity rates (Johnson et al. 2017; `PD-induced-seismicity`).
- **Atmospheric sciences / climate**: TWS is a load on the solid Earth (`PD-microseism` is a related but distinct loading channel) and an integrator of climate forcing.

**When you see this in a paper**: confirm the product (mascon vs. spherical-harmonic), the smoothing radius, and the leakage correction. Trend analyses near land-water boundaries require explicit handling of coastal leakage. The TWS-to-groundwater step always has uncertainty larger than the TWS retrieval itself.

**Anchor citations**:
- Tapley, B. D., Bettadpur, S., Watkins, M., & Reigber, C. (2004). The Gravity Recovery and Climate Experiment: Mission overview and early results. *Geophysical Research Letters*, 31(9), L09607. doi:10.1029/2004GL019920
- Rodell, M., Velicogna, I., & Famiglietti, J. S. (2009). Satellite-based estimates of groundwater depletion in India. *Nature*, 460(7258), 999–1002. doi:10.1038/nature08238
- Famiglietti, J. S. (2014). The global groundwater crisis. *Nature Climate Change*, 4(11), 945–948. doi:10.1038/nclimate2425

**Related cards**: `CC-hydro-S`, `PD-aquifer-depletion`, `PD-subsidence-consolidation`, `PD-drought`, `PD-induced-seismicity`

---

## MC-hydro-SMAP: SMAP / SMOS satellite soil moisture

**What it is**: passive L-band (1.4 GHz) microwave radiometry that retrieves surface (0–5 cm) soil moisture from emissivity. NASA SMAP (Soil Moisture Active Passive, 2015–present) and ESA SMOS (2009–present) are the primary operational missions. Surface soil moisture (volumetric, m³/m³) at ≈ 9 km enhanced grid (SMAP) and 25–35 km (SMOS), with global revisit every 2–3 days.

**What you can retrieve**:
- Volumetric surface soil moisture, with retrieval accuracy target ≤ 0.04 m³/m³ unbiased RMSE.
- Brightness temperature; vegetation optical depth (a proxy for biomass and canopy water content).
- Freeze/thaw state at high latitudes.
- Level-2 to Level-4 (assimilated) products; Level-4 (Reichle et al. 2019) merges SMAP with the NASA Catchment land-surface model for root-zone soil moisture.
- Access: NASA NSIDC, SMAP-EE in Google Earth Engine, SMOS through ESA.

**Failure modes**:
- Surface 0–5 cm only — root-zone inferences require model assimilation (Level-4) with its own assumptions.
- Dense forests, mountainous topography, frozen soil compromise retrieval.
- Radio-frequency interference contaminated significant areas (especially in Europe and Asia) early in the missions; mitigation is ongoing.
- Spatial mismatch: 9 km footprints contain substantial heterogeneity that point-scale validation networks cannot resolve.

**Cross-discipline uses**:
- **Ecology**: surface soil moisture controls ecosystem moisture stress and GPP via stomatal conductance (`CC-eco-GPP`); SMAP-derived land-surface temperature and VOD enable ecosystem-state monitoring.
- **Atmospheric sciences**: surface soil moisture closes the boundary-layer moisture budget and is the boundary condition for next-day temperature and precipitation forecasts.
- **Agricultural sciences**: SMAP underpins drought monitoring and irrigation decision support, particularly in the U.S. Drought Monitor.
- **Geotechnical engineering**: pre-rainstorm antecedent soil moisture modulates infiltration capacity and downstream pore-pressure response in shallow-landslide forecasting.

**When you see this in a paper**: confirm SMAP product level (L2 vs. L3 vs. L4) and resolution (radiometer vs. enhanced-resolution); check the validation reference (USDA SCAN, COSMOS, FLUXNET in-situ).

**Anchor citations**:
- Entekhabi, D., et al. (2010). The Soil Moisture Active Passive (SMAP) mission. *Proceedings of the IEEE*, 98(5), 704–716. doi:10.1109/JPROC.2010.2043918
- Kerr, Y. H., et al. (2012). The SMOS soil moisture retrieval algorithm. *IEEE Transactions on Geoscience and Remote Sensing*, 50(5), 1384–1403. doi:10.1109/TGRS.2012.2184548
- Reichle, R. H., et al. (2017). Assessment of the SMAP Level-4 Surface and Root-Zone Soil Moisture Product Using In Situ Measurements. *Journal of Hydrometeorology*, 18(10), 2621–2645. doi:10.1175/JHM-D-17-0063.1

**Related cards**: `CC-hydro-ET`, `MC-hydro-COSMOS`, `MC-hydro-eddycov`, `CC-eco-GPP`, `PD-drought`, `PD-AR-landslide`

---

## MC-hydro-COSMOS: Cosmic-ray neutron soil moisture

**What it is**: passive ground-based measurement using the moderating effect of soil hydrogen on cosmic-ray-generated neutrons. A bare neutron detector at 1.5 m above the surface integrates a roughly hemispherical footprint of 150–250 m radius and a depth of 10–70 cm that depends on wetness. Pioneered by Zreda et al. (2008), now operational as the COSMOS-USA, COSMOS-UK, and COSMOS-Europe networks.

**What you can retrieve**:
- Footprint-integrated soil moisture at hourly resolution.
- The intermediate spatial scale — between point-scale TDR/sensor networks and 9 km SMAP — that is otherwise unmeasured.
- Snow water equivalent at sites with consistent winter snow cover (with calibration).
- Biomass water content as a confounding signal that can also be estimated.

**Failure modes**:
- Site-specific calibration to in-situ soil-moisture surveys is required (typically 1–2 calibration campaigns per site).
- Snow, surface ponding, and dense vegetation all confound the signal and require correction.
- Depth sensitivity decreases as soil wets; the effective depth at field capacity is ~10 cm, at wilting point ~50 cm.
- Atmospheric pressure, water vapor, and incoming neutron flux all require correction (the latter from a network reference station).

**Cross-discipline uses**:
- **Ecology**: COSMOS integrates the depth most relevant to root-zone water availability and ET; co-located with FLUXNET towers gives a coupled moisture-flux site.
- **Agricultural sciences**: footprint matches typical field/crop-management scale; irrigation impact monitoring.
- **Atmospheric sciences**: ground truth for SMAP L2/L3 retrievals and L4 assimilation evaluation.

**When you see this in a paper**: confirm the calibration date and reference soil-moisture data; note the assumed effective sensing depth and whether depth-varying retrieval is applied; biomass-water correction approach.

**Anchor citations**:
- Zreda, M., Desilets, D., Ferré, T. P. A., & Scott, R. L. (2008). Measuring soil moisture content non-invasively at intermediate spatial scale using cosmic-ray neutrons. *Geophysical Research Letters*, 35(21), L21402. doi:10.1029/2008GL035655
- Zreda, M., et al. (2012). COSMOS: the COsmic-ray Soil Moisture Observing System. *Hydrology and Earth System Sciences*, 16(11), 4079–4099. doi:10.5194/hess-16-4079-2012
- Andreasen, M., Jensen, K. H., Desilets, D., Franz, T. E., Zreda, M., Bogena, H. R., & Looms, M. C. (2017). Status and perspectives on the cosmic-ray neutron method for soil moisture estimation. *Vadose Zone Journal*, 16(8). doi:10.2136/vzj2017.04.0086

**Related cards**: `MC-hydro-SMAP`, `MC-hydro-eddycov`, `CC-eco-GPP`, `PD-drought`

---

## MC-hydro-eddycov: Eddy-covariance flux towers (FLUXNET, AmeriFlux, ICOS)

**What it is**: turbulent-flux measurement using high-frequency (10–20 Hz) wind, water vapor, and CO₂ sensors to compute covariance fluxes of sensible heat H, latent heat LE, and CO₂ F_C. Operated as global networks — FLUXNET (~900 active sites), AmeriFlux (Americas), ICOS (Europe). The reference observation for coupled water-carbon-energy exchange at the ecosystem scale.

**What you can retrieve**:
- 30-minute H, LE, F_C, plus ancillary radiation, soil temperature/moisture, precipitation, air temperature, RH.
- Daily, monthly, annual aggregates after standard gap-filling and partitioning (Reichstein et al. 2005).
- ET from LE = ρ λ ET; GPP and ecosystem respiration from F_C decomposition.
- Footprint analysis (Kljun et al. 2015) showing the upwind area sampled.
- Pre-processed and quality-controlled data: FLUXNET2015 release (Pastorello et al. 2020); OneFlux pipeline; AmeriFlux BASE/AMP releases.

**Failure modes**:
- Energy-balance closure error 10–30% (H + LE < R_n − G) — a long-standing community issue that limits absolute-flux confidence.
- Nighttime stable boundary layer suppresses turbulence; u* filtering removes low-friction-velocity periods at the cost of nighttime data.
- Advective and storage corrections under stratification are difficult; closed-path vs. open-path analyzer differences.
- Footprint is upwind, time-varying, and asymmetric — co-location with discrete observations (soil moisture, biomass) requires careful spatial matching.

**Cross-discipline uses**:
- **Ecology**: F_C decomposition into GPP and respiration is the foundational observation for `CC-eco-GPP`.
- **Atmospheric sciences**: ET from LE closes the surface water budget and enters atmospheric reanalysis (`MC-atm-ERA5`) assimilation.
- **Agricultural sciences**: AmeriFlux croplands provide reference ET for irrigation modeling and crop-coefficient validation.
- **Hydrology**: continuous ET over a representative footprint — the cleanest observation for watershed-scale water-balance closure (`TC-06`).

**When you see this in a paper**: confirm tower height, footprint extent, gap-filling method, u* threshold, and whether storage and advection have been included.

**Anchor citations**:
- Baldocchi, D. D. (2003). Assessing the eddy covariance technique for evaluating carbon dioxide exchange rates of ecosystems: past, present and future. *Global Change Biology*, 9(4), 479–492. doi:10.1046/j.1365-2486.2003.00629.x
- Reichstein, M., et al. (2005). On the separation of net ecosystem exchange into assimilation and ecosystem respiration. *Global Change Biology*, 11(9), 1424–1439. doi:10.1111/j.1365-2486.2005.001002.x
- Pastorello, G., et al. (2020). The FLUXNET2015 dataset and the ONEFlux processing pipeline for eddy covariance data. *Scientific Data*, 7, 225. doi:10.1038/s41597-020-0534-3

**Related cards**: `CC-hydro-ET`, `CC-eco-GPP`, `CC-ag-ET0`, `MC-hydro-COSMOS`, `TC-06`, `PD-drought`

---

## MC-hydro-isotopes: Stable and radioactive water isotopes

**What it is**: tracers based on the natural abundances and decay of water-molecule isotopes. Stable isotopes (δ¹⁸O, δD) trace fractionation through evaporation and condensation; radioactive and anthropogenic isotopes (tritium ³H, ¹⁴C, CFCs, SF₆, ³⁶Cl) date groundwater on timescales from years to millennia. The single most flexible tool for source attribution and age dating in hydrology.

**What you can retrieve**:
- Source-area identification of precipitation, surface water, and groundwater via δ-δ space (LMWL vs. GMWL; Craig 1961).
- Recharge elevation, season, and source (continental vs. coastal moisture).
- Groundwater age and mean transit time from tritium peak, CFC and SF₆ piston-flow / exponential models.
- Plant-water-source partitioning (xylem-water δ¹⁸O matches soil-water profile or stream water) — the ecology-hydrology bridge.
- Analytical platforms: IRMS (high accuracy), CRDS (laser, field-portable); commercial labs and stand-alone field instruments (Picarro).

**Failure modes**:
- Fractionation during evaporation modifies LMWL slope; reference standards (VSMOW) and analytical uncertainty must be reported (typically ±0.1‰ δ¹⁸O, ±1.0‰ δD).
- Tritium has thermonuclear bomb-peak signature that complicates age dating in the 1960s–80s decade window; modern tritium is approaching pre-bomb background.
- Lumped-parameter age models (piston flow, exponential, exponential-piston flow) all have known biases relative to the actual age distribution.
- Sample preservation and shipping affect outcome; CFC and SF₆ degas easily.

**Cross-discipline uses**:
- **Ecology**: plant-water-source attribution from xylem-water isotopes (`CC-eco-plant-water-source`).
- **Atmospheric sciences**: precipitation-isotope networks (GNIP, WMO/IAEA) anchor moisture-source attribution for atmospheric-river events.
- **Seismology / inverse problems**: Bayesian source attribution is the same machinery used in earthquake source inversion (`TC-09`).
- **Agricultural sciences**: irrigation-source tracking, forensics on nitrate and pesticide contamination.

**When you see this in a paper**: confirm reference standard (VSMOW), analytical platform, and whether end-member mixing assumptions are independently validated.

**Anchor citations**:
- Craig, H. (1961). Isotopic variations in meteoric waters. *Science*, 133(3465), 1702–1703. doi:10.1126/science.133.3465.1702
- Dansgaard, W. (1964). Stable isotopes in precipitation. *Tellus*, 16(4), 436–468. doi:10.1111/j.2153-3490.1964.tb00181.x
- Clark, I. D., & Fritz, P. (1997). *Environmental Isotopes in Hydrogeology*. CRC Press.

**Related cards**: `CC-hydro-recharge`, `CC-hydro-ET`, `CC-eco-plant-water-source`, `MC-atm-ERA5`, `TC-09`, `PD-AR-landslide`, `PD-drought`

---

## MC-hydro-modeling: Process-based hydrologic models (MODFLOW, ParFlow, CLM, SWAT, WRF-Hydro)

**What it is**: the family of process-based numerical models that solve coupled equations for groundwater flow, vadose-zone flow, surface runoff, channel routing, and land-atmosphere exchange. Different models emphasize different parts of the chain: MODFLOW (saturated groundwater, USGS workhorse since McDonald & Harbaugh 1988); ParFlow (3D variably-saturated coupled groundwater-surface); CLM (Community Land Model, coupled with WRF and Earth-system models); SWAT (catchment-scale, agriculture and land use); WRF-Hydro (coupled with WRF atmospheric model, basis of the U.S. National Water Model).

**What you can retrieve**:
- Spatially distributed h, soil moisture, ET, Q time series under specified forcing.
- Hindcasts driven by observed forcing; forecasts driven by NWP output.
- Sensitivity to land-use, climate, pumping, and management scenarios.
- Standard supporting tools: Modflow6, ParFlow-CLM, FloPy, ParFlowGO, NLDAS-2 forcing, NOAA NWM operational output.

**Failure modes**:
- Equifinality (Beven 2006): many parameter sets fit the calibration data equally well, but predict different futures; uncertainty quantification is non-optional.
- Model intercomparison routinely shows factor-of-2 differences in ET, Q, recharge across structurally similar models given the same forcing.
- Sub-grid heterogeneity (preferential flow, fracture flow, hillslope hydrology) is parameterized, not resolved.
- Climate-change extrapolation outside the calibration regime is reliable only to the extent that model physics, not parameter calibration, governs the response.

**Cross-discipline uses**:
- **Atmospheric sciences**: coupled atmosphere-land models (WRF-Hydro, CLM in CESM) close the surface water cycle and feed back to atmospheric humidity; assimilation via `TC-05`.
- **Geotechnical engineering**: pumping scenarios from MODFLOW feed consolidation and subsidence models (`PD-subsidence-consolidation`).
- **Agricultural sciences**: SWAT and CLM forecasts inform irrigation demand, nitrate transport, and yield modeling.
- **Ecology**: ParFlow-CLM and similar integrated models give the moisture-state fields needed for ecosystem dynamics.

**When you see this in a paper**: confirm model version, forcing dataset, calibration period and metric, and whether uncertainty quantification is structural (multiple models) or parametric (single model, many parameter sets).

**Anchor citations**:
- McDonald, M. G., & Harbaugh, A. W. (1988). *A modular three-dimensional finite-difference ground-water flow model*. USGS Techniques of Water-Resources Investigations Book 6, Chapter A1.
- Kollet, S. J., & Maxwell, R. M. (2006). Integrated surface-groundwater flow modeling: A free-surface overland flow boundary condition in a parallel groundwater flow model. *Advances in Water Resources*, 29(7), 945–958. doi:10.1016/j.advwatres.2005.08.006
- Lawrence, D. M., et al. (2019). The Community Land Model version 5: Description of new features, benchmarking, and impact of forcing uncertainty. *Journal of Advances in Modeling Earth Systems*, 11(12), 4245–4287. doi:10.1029/2018MS001583
- Beven, K. (2006). A manifesto for the equifinality thesis. *Journal of Hydrology*, 320(1–2), 18–36. doi:10.1016/j.jhydrol.2005.07.007

**Related cards**: `CC-hydro-K`, `CC-hydro-recharge`, `CC-hydro-ET`, `CC-hydro-Q`, `MC-atm-ERA5`, `TC-05`, `TC-06`, `PD-aquifer-depletion`, `PD-drought`
