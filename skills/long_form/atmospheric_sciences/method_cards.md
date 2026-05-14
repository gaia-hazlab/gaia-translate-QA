---
discipline: atmospheric_sciences
card_type: method
schema_version: v3
---

# Atmospheric sciences — method cards

Each card describes one measurement technique, instrument, or dataset relevant to atmospheric sciences. Format follows `docs/card_format_spec.md`.

---

## MC-atm-radiosonde: Radiosondes and the upper-air network

**What it is**: balloon-borne sensor packages launched globally twice daily (00 and 12 UTC) measuring vertical profiles of T, RH, p, and (with GPS tracking) u and v. The U.S. NWS operates ~70 launch sites; the global GUAN network has ~800. The foundational direct in-situ observation of the free atmosphere; assimilated into all operational NWP and reanalysis.

**What you can retrieve**:
- Vertical profiles 0–30 km with ~10-m vertical resolution from launch to balloon burst.
- Daily synoptic-scale T, q, wind, and stability metrics (CAPE, CIN, lifted index).
- Global archives: IGRA (Integrated Global Radiosonde Archive), University of Wyoming sounding archive.
- Drift-corrected wind fields from GPS-tracked balloons.

**Failure modes**:
- Network is sparse over oceans, polar regions, and most of Africa, Asia, and South America; reanalysis fills the gap with model + remote-sensing assimilation.
- Sensor biases (especially humidity at low T) require routine correction; consistency across sensor generations is non-trivial for climate-trend work.
- Twice-daily sampling aliases sub-synoptic variability; field campaigns add radiosondes for transient phenomena.

**Cross-discipline uses**:
- **Hydrology**: TCWV / IWV from radiosonde provides ground truth for GNSS-derived precipitable water (`MC-atm-GNSS-IWV`); inputs to AR moisture-budget closure.
- **Seismology**: not direct; but atmospheric-pressure variability captured by radiosondes is the ultimate source of long-period seismic noise (`PD-microseism`).
- **Ecology / agriculture**: VPD profiles drive the boundary-layer-vegetation coupling that controls daytime stomatal conductance.

**When you see this in a paper**: confirm sensor type and bias-correction lineage; humidity records pre-2000 have larger uncertainty than post-2000 RS92/RS41-class sondes. Wind-profile reliability degrades when balloons drift far from launch site.

**Anchor citations**:
- Durre, I., Vose, R. S., & Wuertz, D. B. (2006). Overview of the integrated global radiosonde archive. *Journal of Climate*, 19(1), 53–68. doi:10.1175/JCLI3594.1

**Related cards**: `MC-atm-ERA5`, `MC-atm-GNSS-IWV`, `CC-atm-T`, `CC-atm-q`, `PD-microseism`

---

## MC-atm-ERA5: ERA5 and modern atmospheric reanalysis

**What it is**: ERA5 (Hersbach et al. 2020) is the European Centre for Medium-Range Weather Forecasts (ECMWF) fifth-generation atmospheric reanalysis, providing 0.25° × 0.25° × hourly fields of 100+ variables back to 1940 (with degraded quality before 1979). Built by 4D-Var assimilation of observations into the IFS atmospheric model. Companion: NASA MERRA-2 (Gelaro et al. 2017), NOAA CFSR. ERA5 is the de-facto reference dataset for most Earth-science applications.

**What you can retrieve**:
- T, q, u, v, w, p, geopotential height at 137 model levels (and standard pressure levels).
- Surface variables: 2 m T, 10 m wind, total precipitation, surface fluxes (R_n, H, LE, G).
- Vertically integrated quantities: TCWV, IVT (key for AR identification, `CC-atm-IVT`).
- Access: Copernicus Climate Data Store (CDS) API; ARCO ERA5 on Google Cloud (zarr, optimized for analysis).

**Failure modes**:
- Reanalysis is *not* observation; in data-sparse regions and times it reflects model dynamics.
- Spurious trends from changes in the observing system (jumps when new satellite streams come online); ERA5 is better than its predecessors but not bias-free.
- Precipitation in reanalysis is model-derived, often biased especially in mountainous and convective settings; satellite-derived products (`MC-atm-GPM`) preferred for precipitation analysis.
- Resolution insufficient for orographic precipitation on the windward Cascades; downscaling required for hydrology and geomorphology applications.

**Cross-discipline uses**:
- **Hydrology**: ERA5 forcing drives `MC-hydro-modeling` MODFLOW/CLM/ParFlow runs in ungauged basins.
- **Geomorphology**: long-term ERA5 climatologies anchor landscape-evolution-model forcing.
- **Ecology**: ERA5 + Landsat NDVI is the standard combination for vegetation-climate analysis.
- **Seismology**: ERA5 pressure and wind fields feed environmental-noise modeling for microseism source attribution.

**When you see this in a paper**: confirm the variable's reanalysis quality class (which observations constrain it where), the spatial resolution at the analysis grid vs. interpolated, and whether downscaling has been applied for hydrology applications.

**Anchor citations**:
- Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999–2049. doi:10.1002/qj.3803
- Gelaro, R., et al. (2017). The Modern-Era Retrospective Analysis for Research and Applications, Version 2 (MERRA-2). *Journal of Climate*, 30(14), 5419–5454. doi:10.1175/JCLI-D-16-0758.1

**Related cards**: `MC-atm-radiosonde`, `MC-atm-NWP`, `MC-hydro-modeling`, `CC-atm-IVT`, `TC-05`, `PD-atmospheric-river`

---

## MC-atm-GPM: Global Precipitation Measurement satellite mission (IMERG)

**What it is**: NASA-JAXA Global Precipitation Measurement (GPM) mission, with a core observatory (GMI passive microwave + DPR dual-frequency precipitation radar, 2014–present) and a constellation of partner microwave satellites. The IMERG (Integrated Multi-satellite Retrievals for GPM) algorithm produces precipitation estimates at 0.1° × 30-min globally. The successor to TRMM (1997–2015) and the modern operational satellite precipitation product.

**What you can retrieve**:
- IMERG Early (4 h latency), Late (14 h), and Final (3-month, gauge-calibrated) products.
- Surface precipitation rate [mm/h]; precipitation type (rain vs. snow, convective vs. stratiform).
- Vertical hydrometeor profiles from DPR over a narrow swath.
- Access: NASA GPM data archive (PMM), Google Earth Engine, climateserv.

**Failure modes**:
- Underestimates orographic precipitation in mountainous terrain (Cascades, Sierra, Andes); gauge correction in IMERG-Final helps but doesn't fix it.
- Light precipitation and snowfall poorly retrieved; high-latitude cold-season records have larger uncertainty.
- Convective intense rainfall underestimated; biases largest at the highest-impact tails.
- Polar coverage degrades for satellites in inclined orbits.

**Cross-discipline uses**:
- **Hydrology**: GPM-derived P forces flood forecasting in ungauged basins; the operational input to ParFlow, WRF-Hydro, and the U.S. National Water Model in many ungauged settings.
- **Geomorphology**: real-time AR-driven landslide and debris-flow nowcasting (NASA LHASA model) uses GPM precipitation as forcing.
- **Agricultural sciences**: drought monitoring in data-sparse regions of Africa, Asia, and South America.

**When you see this in a paper**: confirm which IMERG version (latest is V07); product (Early/Late/Final); gauge-correction status. Mountainous-terrain results need explicit cross-comparison with gauges or radar.

**Anchor citations**:
- Hou, A. Y., et al. (2014). The Global Precipitation Measurement mission. *Bulletin of the American Meteorological Society*, 95(5), 701–722. doi:10.1175/BAMS-D-13-00164.1
- Huffman, G. J., Bolvin, D. T., Braithwaite, D., Hsu, K., Joyce, R., Kidd, C., Nelkin, E. J., Sorooshian, S., Tan, J., & Xie, P. (2020). Integrated Multi-satellite Retrievals for the Global Precipitation Measurement (GPM) Mission (IMERG). *Satellite Precipitation Measurement*, 343–353. Springer. doi:10.1007/978-3-030-24568-9_19

**Related cards**: `CC-atm-precip`, `MC-atm-NEXRAD`, `MC-atm-ERA5`, `MC-hydro-modeling`, `PD-atmospheric-river`, `PD-AR-landslide`

---

## MC-atm-NEXRAD: NEXRAD Doppler radar network (WSR-88D)

**What it is**: the U.S. NEXRAD network of 159 Doppler weather radars (S-band, dual-polarization since 2013). Continuous coverage of the continental U.S., Alaska, Hawaii, Puerto Rico, with overlapping coverage in populated areas. Standard products: reflectivity Z [dBZ], radial velocity, spectrum width, and dual-pol differential phase / cross-correlation for hydrometeor classification.

**What you can retrieve**:
- 6-min volume scans at 0.5°–19.5° tilt; ~250-m radial resolution.
- Quantitative precipitation estimates (QPE) via Z-R relations or dual-pol algorithms (MRMS — NOAA Multi-Radar Multi-Sensor merged product).
- Severe-weather detections: tornado vortex signature, mesocyclone, hail signature.
- Continuous data via NCEI archive; Level-II raw scans, Level-III derived products.

**Failure modes**:
- Beam blockage by terrain in mountainous regions; PNW Cascades have significant blockage on the windward side.
- Bright-band contamination near the freezing level inflates Z.
- Range degradation: resolution decreases with distance; coverage gaps far from any radar.
- Convective-precipitation Z-R relations are highly variable; modern dual-pol algorithms reduce but do not eliminate bias.

**Cross-discipline uses**:
- **Hydrology**: NEXRAD-derived MRMS QPE is the operational rainfall forcing for flash-flood forecasting and post-event hydrology reconstruction.
- **Geomorphology**: short-duration intense rainfall captured by NEXRAD (not by 6-h or daily gauge) is the meaningful trigger for shallow landslides and debris flows.
- **Ecology**: NEXRAD also detects biological aerial activity — bird and bat migrations are routinely tracked (Stepanian et al. 2014); ambient acoustic / vegetation activity is a side product.

**When you see this in a paper**: confirm which radar(s) and time period (the dual-pol upgrade transition in 2013 changes QPE quality); whether the work uses Level-II raw data or a derived Level-III/MRMS product. Terrain-blockage masks should accompany QPE maps in mountainous regions.

**Anchor citations**:
- Crum, T. D., & Alberty, R. L. (1993). The WSR-88D and the WSR-88D Operational Support Facility. *Bulletin of the American Meteorological Society*, 74(9), 1669–1687. doi:10.1175/1520-0477(1993)074<1669:TWATWO>2.0.CO;2
- Zhang, J., et al. (2016). Multi-Radar Multi-Sensor (MRMS) Quantitative Precipitation Estimation: Initial Operating Capabilities. *Bulletin of the American Meteorological Society*, 97(4), 621–638. doi:10.1175/BAMS-D-14-00174.1

**Related cards**: `CC-atm-precip`, `MC-atm-GPM`, `MC-hydro-modeling`, `PD-convective-storm`, `PD-atmospheric-river`

---

## MC-atm-GNSS-IWV: GNSS-derived precipitable water vapor

**What it is**: integrated water vapor (IWV, equivalent to TCWV in mm of liquid water) inferred from the wet delay in GNSS (GPS, GLONASS, Galileo, BeiDou) signals reaching ground stations. Bevis et al. (1992) demonstrated meteorological use; now operational at thousands of stations globally with 5-minute sampling and a few-mm accuracy. The continuous-IWV observation that bridges GPS geodesy and atmospheric science.

**What you can retrieve**:
- Continuous IWV at fixed-station precision (~1–2 mm) every 5 min.
- Networks: SuomiNet (UCAR/CDDIS); EUREF; PBO/EarthScope GAGE Facility (which also supports seismology and geodesy).
- IWV anomalies during AR landfall (often > 30 mm, vs. baseline 5–15 mm).
- Coupling with InSAR atmospheric-phase correction: GNSS IWV maps enable atmospheric-delay removal in deformation time series.

**Failure modes**:
- Requires accurate surface pressure for hydrostatic-delay separation; uncorrected pressure error propagates directly to IWV bias.
- Mountainous-terrain horizontal gradients are not captured by point-station IWV; assimilation into 3D fields requires multiple stations.
- IWV is column-integrated; vertical distribution requires radiosonde or radio occultation.

**Cross-discipline uses**:
- **Hydrology / atmospheric**: continuous IWV underpins AR detection at the point scale; ground truth for satellite TCWV products.
- **Seismology / geodesy**: same GNSS stations support geodetic time series (`MC-geomorph-InSAR`, `PD-megathrust`); shared infrastructure with seismic broadband.
- **Reflection-based hydrology**: GNSS-IR (Larson 2016) uses the same antennas to monitor soil moisture, snow depth, and water level — a separate technique on the same hardware.

**When you see this in a paper**: confirm pressure correction source and whether the network is from a continuous reference frame (CORS) or campaign deployment. Station-specific tropospheric mapping functions matter near coasts and mountains.

**Anchor citations**:
- Bevis, M., Businger, S., Herring, T. A., Rocken, C., Anthes, R. A., & Ware, R. H. (1992). GPS meteorology: Remote sensing of atmospheric water vapor using the Global Positioning System. *Journal of Geophysical Research: Atmospheres*, 97(D14), 15787–15801. doi:10.1029/92JD01517
- Larson, K. M. (2016). GPS interferometric reflectometry: Applications to surface soil moisture, snow depth, and vegetation water content in the western United States. *WIREs Water*, 3(6), 775–787. doi:10.1002/wat2.1167

**Related cards**: `CC-atm-q`, `CC-atm-IVT`, `MC-atm-radiosonde`, `MC-geomorph-InSAR`, `MC-hydro-COSMOS`, `PD-atmospheric-river`

---

## MC-atm-NWP: Numerical weather prediction (WRF, MPAS, IFS, GFS, CMIP)

**What it is**: numerical models that integrate the primitive equations forward in time to produce weather forecasts (hours to weeks) or climate projections (decades to centuries). Operational global NWP: ECMWF IFS, NOAA GFS, UK Met Office UM, German DWD ICON. Regional: WRF (Skamarock et al. 2008), MPAS, HRRR. Climate: CESM, GFDL, UKESM, MPI-ESM in CMIP6 multi-model archive.

**What you can retrieve**:
- Operational deterministic and ensemble forecasts at 0.1° – 1° global, 1–12 km regional, 1–4 km convection-permitting.
- Probabilistic forecasts from ensembles (ECMWF ENS, GEFS).
- Climate projections under SSP / RCP scenarios in CMIP6 multi-model archive.
- Reanalysis products (`MC-atm-ERA5`) are NWP runs with observation assimilation.
- Hydrology coupling: WRF-Hydro is the basis of the U.S. National Water Model.

**Failure modes**:
- Skill horizon: ~1 week for synoptic-scale, ~1 day for mesoscale convection, regime-dependent.
- Sub-grid physics parameterizations (convection, PBL, microphysics, land surface) dominate model differences; multi-model spread is the working uncertainty estimate at climate scales.
- Climate models routinely produce biased mean states; downscaling and bias correction needed for impact studies, with their own statistical assumptions.
- Convective storms at < 4 km grid spacing require convection-permitting setups; otherwise convection is parameterized and unreliable.

**Cross-discipline uses**:
- **Hydrology**: WRF-Hydro, CLM, ParFlow couple atmospheric forcing to surface and subsurface flow (`MC-hydro-modeling`).
- **Geomorphology**: storm-driven hazard nowcasting (post-fire debris flows, AR-driven landslides) is the operational application.
- **Agricultural sciences**: NWP outputs feed irrigation scheduling and crop-loss forecasts; seasonal forecasts (S2S) and CMIP projections drive adaptation planning.
- **Climate-impact attribution**: CMIP multi-model differences are the basis for climate-change attribution to extreme events.

**When you see this in a paper**: identify the model, version, grid spacing, ensemble configuration, and downscaling chain; the answer depends on every link in this chain.

**Anchor citations**:
- Skamarock, W. C., Klemp, J. B., Dudhia, J., Gill, D. O., Barker, D. M., Wang, W., & Powers, J. G. (2008). *A description of the Advanced Research WRF Version 3*. NCAR Technical Note NCAR/TN-475+STR. doi:10.5065/D68S4MVH
- Eyring, V., et al. (2016). Overview of the Coupled Model Intercomparison Project Phase 6 (CMIP6). *Geoscientific Model Development*, 9(5), 1937–1958. doi:10.5194/gmd-9-1937-2016

**Related cards**: `MC-atm-ERA5`, `MC-atm-radiosonde`, `MC-hydro-modeling`, `TC-05`, `PD-extreme-precip-intensification`

---

## MC-atm-GOES: Geostationary satellite imagery (GOES-R series)

**What it is**: NOAA's geostationary weather satellites — GOES-16 (East, 75.2°W), GOES-18 (West, 137.2°W), and successors — carrying the Advanced Baseline Imager (ABI) with 16 spectral channels at 0.5–2 km resolution and 5-min full-disk cadence (1-min mesoscale targets). The primary continuous observation of weather over the Americas. Comparable systems globally: Himawari-8/9 (Japan), Meteosat-11/12 (Europe), FY-4 (China).

**What you can retrieve**:
- Continuous cloud-top temperature, water vapor, fire detection, lightning (GLM Geostationary Lightning Mapper), and other derived products.
- Tracking of severe storms, hurricanes, smoke plumes, volcanic ash, dust storms.
- Quantitative cloud-top properties; convective initiation alerts (NOAA SPC).
- Access: NOAA NESDIS, AWS Open Data (real-time GOES on S3).

**Failure modes**:
- Fixed equatorial orbit means high latitudes have poor geometry; pixel size increases off-nadir.
- Optical channels useless at night except for thermal IR; some severe-weather signatures are nighttime-poor.
- No direct precipitation measurement; combined with passive microwave for QPE.
- Glint, aerosol, and cloud-edge artifacts in derived products require careful screening.

**Cross-discipline uses**:
- **Hydrology**: water-vapor channel tracks AR landfall in real time; cloud-top temperatures discriminate convective from stratiform precipitation contributions.
- **Geomorphology**: smoke and volcanic-ash plumes are routinely tracked, useful for post-eruption debris-flow forecasting (Cascade volcanoes).
- **Ecology / agriculture**: real-time fire detection (GOES "fire detection product") and burned-area mapping in conjunction with VIIRS.

**When you see this in a paper**: confirm GOES platform and time period (GOES-13/15 era pre-2017 had different imagery characteristics than GOES-R series); product version; spatial averaging applied.

**Anchor citations**:
- Schmit, T. J., Griffith, P., Gunshor, M. M., Daniels, J. M., Goodman, S. J., & Lebair, W. J. (2017). A closer look at the ABI on the GOES-R series. *Bulletin of the American Meteorological Society*, 98(4), 681–698. doi:10.1175/BAMS-D-15-00230.1

**Related cards**: `MC-atm-GPM`, `MC-atm-NEXRAD`, `MC-atm-ERA5`, `PD-atmospheric-river`, `PD-convective-storm`
