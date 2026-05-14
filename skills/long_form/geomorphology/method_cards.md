---
discipline: geomorphology
card_type: method
schema_version: v3
---

# Geomorphology — method cards

Each card describes one measurement technique, instrument, or dataset relevant to geomorphology, with what it measures, resolution, failure modes, and cross-discipline reuse. Format follows `docs/card_format_spec.md`.

---

## MC-geomorph-lidar: Airborne / terrestrial lidar and structure-from-motion photogrammetry

**What it is**: high-resolution topographic measurement using laser pulses (airborne, terrestrial, or drone-mounted lidar) or photogrammetric reconstruction from optical imagery (Structure-from-Motion, SfM; Westoby et al. 2012). The modern morphometric backbone: bare-earth DEMs at 0.5–1 m resolution from airborne lidar; sub-cm point clouds from terrestrial scanners and drone SfM.

**What you can retrieve**:
- Bare-earth DEM after vegetation filtering; vegetation-canopy elevation; multi-return point clouds.
- DEM-of-Difference (DoD): topographic change between two surveys for landslide volumes, channel migration, dam-spillway erosion (Wheaton et al. 2010).
- Geomorphic metrics: slope, curvature, ksn (`CC-geomorph-ksn`), drainage density, hillslope length.
- Datasets: USGS 3DEP (continental-scale lidar coverage), OpenTopography portal, NCALM commissions for high-priority sites.

**Failure modes**:
- Dense canopy obscures bare-earth returns; quality varies with leaf-on vs. leaf-off acquisition.
- DoD uncertainty is dominated by point-cloud registration error and elevation noise; volumetric change requires careful error propagation (Brasington-Wheaton framework).
- SfM is only as good as the GPS ground control and photo overlap; without GCPs, scale and absolute elevation drift.
- Snow cover, water, and dark surfaces give poor returns.

**Cross-discipline uses**:
- **Hydrology**: lidar-derived channel networks feed `MC-hydro-modeling` MODFLOW/ParFlow surface-water grids and AR-driven flood-routing models.
- **Geotechnical engineering**: high-resolution slope morphometry for `CC-geotech-FS` analyses and landslide hazard mapping.
- **Seismology**: lidar reveals fault-scarp morphology — direct paleoseismology (`PD-fault-scarp`).
- **Ecology**: vegetation-canopy heights from lidar feed biomass and habitat-structure models.

**When you see this in a paper**: confirm point density (pts/m²), survey date, vegetation correction method, and DoD uncertainty (Limit of Detection at 95% confidence). DoD volumes without uncertainty quantification are unreliable.

**Anchor citations**:
- Wheaton, J. M., Brasington, J., Darby, S. E., & Sear, D. A. (2010). Accounting for uncertainty in DEMs from repeat topographic surveys: Improved sediment budgets. *Earth Surface Processes and Landforms*, 35(2), 136–156. doi:10.1002/esp.1886
- Westoby, M. J., Brasington, J., Glasser, N. F., Hambrey, M. J., & Reynolds, J. M. (2012). 'Structure-from-Motion' photogrammetry: A low-cost, effective tool for geoscience applications. *Geomorphology*, 179, 300–314. doi:10.1016/j.geomorph.2012.08.021
- Roering, J. J., Mackey, B. H., Marshall, J. A., Sweeney, K. E., Deligne, N. I., Booth, A. M., Handwerger, A. L., & Cerovski-Darriau, C. (2013). 'You are HERE': Connecting the dots with airborne lidar for geomorphic fieldwork. *Geomorphology*, 200, 172–183. doi:10.1016/j.geomorph.2013.04.009

**Related cards**: `MC-geomorph-DEM-analysis`, `MC-geomorph-InSAR`, `MC-geotech-CPT`, `CC-geomorph-ksn`, `PD-fault-scarp`

---

## MC-geomorph-cosmogenic: Cosmogenic isotopes for erosion rates and exposure dating

**What it is**: in-situ produced cosmogenic nuclides (¹⁰Be, ²⁶Al, ³⁶Cl, ¹⁴C) accumulate in surface rocks via spallation reactions with cosmic-ray neutrons. Their concentrations give either surface exposure ages (for stable surfaces) or steady-state erosion rates (for eroding surfaces). The dominant method for quantifying landscape denudation at 10³–10⁵ yr timescales (`CC-geomorph-erosion-rate`).

**What you can retrieve**:
- Catchment-mean erosion rates from ¹⁰Be in fluvial sediment (Granger et al. 1996), integrating over the basin and the cosmogenic-lifetime depth (~60 cm in rock).
- Bedrock exposure ages for moraines, fault scarps, terraces.
- Burial dating via paired ²⁶Al/¹⁰Be for cave sediments and deep deposits.
- Standard calculator: CRONUS-Earth online (Balco et al. 2008); raw AMS measurements typically at LLNL CAMS, PRIME Lab, or SUERC.

**Failure modes**:
- Production-rate calibration is altitude- and latitude-dependent; CRONUS scaling schemes (Lal-Stone, Lifton-Sato) disagree by ~5–15% in some settings.
- Inheritance: quartz grains carrying pre-existing ¹⁰Be give apparent exposure ages older than the actual surface age; mitigation via depth profiles.
- Steady-state assumption for catchment-mean rates can fail (post-glacial sediment slugs, landslide-dominated systems).
- Quartz mineralogy required for ¹⁰Be / ²⁶Al; carbonate, basalt, or quartz-free settings need ³⁶Cl or ¹⁴C.

**Cross-discipline uses**:
- **Seismology / tectonics**: cosmogenic exposure ages anchor paleoseismology of `PD-fault-scarp`; long-term denudation rates calibrate uplift–erosion balance.
- **Hydrology**: long-term sediment yield from cosmogenic rates compares with modern Q_s (`CC-geomorph-Qs`) — divergence diagnoses non-steady landscapes.
- **Climate**: glacial-moraine chronologies from cosmogenic dating anchor regional ice-sheet histories and climate reconstructions.

**When you see this in a paper**: confirm the scaling scheme, production-rate calibration site, attenuation length, and topographic shielding correction. Single-sample rates are noisy; meaningful interpretation usually requires multiple samples or depth profiles.

**Anchor citations**:
- Lal, D. (1991). Cosmic ray labeling of erosion surfaces. *Earth and Planetary Science Letters*, 104(2–4), 424–439. doi:10.1016/0012-821X(91)90220-C
- Granger, D. E., Kirchner, J. W., & Finkel, R. (1996). Spatially averaged long-term erosion rates measured from in situ–produced cosmogenic nuclides in alluvial sediment. *The Journal of Geology*, 104(3), 249–257. doi:10.1086/629823
- Balco, G., Stone, J. O., Lifton, N. A., & Dunai, T. J. (2008). A complete and easily accessible means of calculating surface exposure ages or erosion rates from ¹⁰Be and ²⁶Al measurements. *Quaternary Geochronology*, 3(3), 174–195. doi:10.1016/j.quageo.2007.12.001

**Related cards**: `CC-geomorph-erosion-rate`, `CC-geomorph-D`, `MC-hydro-isotopes`, `PD-landscape-evolution`, `PD-fault-scarp`

---

## MC-geomorph-DEM-analysis: DEM analysis software (TopoToolbox, RichDEM, FastScape)

**What it is**: the open-source software ecosystem for processing digital elevation models into geomorphic metrics. TopoToolbox (Schwanghart & Scherler 2014; Matlab) and its Python re-implementation TopoToolbox 3; RichDEM (Barnes 2014; high-performance flow routing); LSDTopoTools (Mudd et al. 2014); FastScape (Braun & Willett 2013; landscape evolution).

**What you can retrieve**:
- Flow-routing networks (D8, D∞ Tarboton 1997), drainage extraction, watershed delineation.
- Slope, curvature, ksn (`CC-geomorph-ksn`), chi-elevation transforms, knickpoint detection.
- Hypsometric integrals, hillslope-length distributions, ridgenet extraction.
- Sink-filling, breach-carving, pre-processing for hydrologic models that integrate with `MC-hydro-modeling`.

**Failure modes**:
- DEM artifacts (stripes, pits, contour-derived banding) propagate into slope and curvature; pre-processing critical.
- Flow-routing algorithm choice (D8 vs. D∞ vs. multiple-flow) affects basin boundaries and accumulation maps in low-relief settings.
- Concavity-regression methods are sensitive to fitting window and outlier handling; chi-method is generally more stable.
- Knickpoint detection is subjective; multiple algorithms give different counts.

**Cross-discipline uses**:
- **Hydrology**: drainage networks and watershed boundaries from DEM are the geometric inputs to `MC-hydro-modeling`.
- **Geotechnical engineering**: slope and curvature maps feed landslide-susceptibility models and `CC-geotech-FS` infinite-slope calculations.
- **Ecology**: terrain attributes (TWI, TPI, aspect, slope) are standard inputs to species-distribution models.

**When you see this in a paper**: confirm DEM source and resolution (10-m USGS vs. 1-m lidar); pre-processing (sink-filling, smoothing); flow-routing algorithm; parameter choices for ksn / concavity.

**Anchor citations**:
- Tarboton, D. G. (1997). A new method for the determination of flow directions and upslope areas in grid digital elevation models. *Water Resources Research*, 33(2), 309–319. doi:10.1029/96WR03137
- Schwanghart, W., & Scherler, D. (2014). TopoToolbox 2 — MATLAB-based software for topographic analysis and modeling. *Earth Surface Dynamics*, 2(1), 1–7. doi:10.5194/esurf-2-1-2014
- Mudd, S. M., Harel, M. A., Hurst, M. D., Grieve, S. W. D., & Marrero, S. M. (2014). The CAIRN method: Automated, reproducible calculation of catchment-averaged denudation rates from cosmogenic nuclide concentrations. *Earth Surface Dynamics*, 4(2), 655–674.

**Related cards**: `MC-geomorph-lidar`, `MC-geomorph-landlab`, `CC-geomorph-ksn`, `CC-geomorph-D`, `MC-hydro-modeling`

---

## MC-geomorph-landlab: Landscape evolution modeling (Landlab, FastScape, CHILD, CAESAR-Lisflood)

**What it is**: process-based numerical models that simulate landscape evolution under combined hillslope diffusion, fluvial incision, sediment transport, and tectonic uplift over 10²–10⁷ yr. Landlab (Tucker et al. 2001; Hobley et al. 2017) is the community Python framework; FastScape (Braun & Willett 2013) is the high-performance counterpart for large domains; CAESAR-Lisflood (Coulthard et al. 2013) couples flood and sediment-transport at event scale.

**What you can retrieve**:
- Steady-state and transient landscape responses to specified tectonic, climatic, and lithologic forcing.
- Sediment-flux time series at any point in the simulated network.
- Event-scale (CAESAR-Lisflood): hydrograph response, channel evolution, flood-sediment routing.
- Coupled hillslope-fluvial dynamics (Landlab `flow_accumulator`, `fastscape_eroder`, `linear_diffuser` components).

**Failure modes**:
- Parameters (K, m, n in stream power; κ in hillslope diffusion) are calibrated, not measured; equifinality (different parameter sets fit equally well).
- Scale-grid resolution coupled with timestep determines numerical stability; CFL-like criteria apply.
- Lateral processes (meandering, debris flows, mass wasting) are typically parameterized rather than resolved.
- Long-time-simulation outputs are exploratory hypotheses, not predictions.

**Cross-discipline uses**:
- **Hydrology**: Landlab and CAESAR-Lisflood are increasingly used as coupled hydrology-geomorphology models; share `CC-hydro-K` substrate properties.
- **Climate-tectonics**: standard tool for testing climate-erosion feedbacks (Whipple 2009; Roe et al. 2008).
- **Geotechnical engineering**: long-timescale evolution of dam catchments for sediment-yield projections (`PD-dam-levee-safety`).

**When you see this in a paper**: confirm the calibration approach, sensitivity tests, and whether the model output is presented as a prediction or as an exploration of a hypothesis space.

**Anchor citations**:
- Tucker, G. E., Lancaster, S. T., Gasparini, N. M., & Bras, R. L. (2001). The Channel-Hillslope Integrated Landscape Development (CHILD) Model. In *Landscape Erosion and Evolution Modeling*, Springer, 349–388. doi:10.1007/978-1-4615-0575-4_12
- Hobley, D. E. J., Adams, J. M., Nudurupati, S. S., Hutton, E. W. H., Gasparini, N. M., Istanbulluoglu, E., & Tucker, G. E. (2017). Creative computing with Landlab. *Earth Surface Dynamics*, 5(1), 21–46. doi:10.5194/esurf-5-21-2017
- Coulthard, T. J., Neal, J. C., Bates, P. D., Ramirez, J., de Almeida, G. A. M., & Hancock, G. R. (2013). Integrating the LISFLOOD-FP 2D hydrodynamic model with the CAESAR model: Implications for modelling landscape evolution. *Earth Surface Processes and Landforms*, 38(15), 1897–1906. doi:10.1002/esp.3478

**Related cards**: `MC-geomorph-DEM-analysis`, `MC-hydro-modeling`, `CC-geomorph-streampower`, `CC-geomorph-D`, `PD-landscape-evolution`

---

## MC-geomorph-debris-flow-modeling: Debris-flow runout models (D-Claw, RAMMS, FLO-2D)

**What it is**: depth-averaged shallow-flow models that simulate the runout, inundation depth, velocity, and impact pressure of debris flows and lahars over digital terrain. D-Claw (Iverson & George 2014; USGS open-source) couples granular Mohr-Coulomb mechanics with two-phase pore-pressure feedback; RAMMS (Christen et al. 2010; commercial) uses Voellmy rheology; FLO-2D (O'Brien et al. 1993) is the dominant U.S. regulatory tool.

**What you can retrieve**:
- Inundation maps and travel times for design-event debris flows.
- Impact pressure and momentum for engineering-structure design.
- Sensitivity to source-volume, water-content, and rheology assumptions.
- Coupling with rainfall-triggered initiation (`PD-AR-landslide`) and post-fire runoff (`PD-post-fire-erosion`).

**Failure modes**:
- Rheological parameters (Voellmy μ, ξ; Bingham viscosity; D-Claw friction angle and pore-pressure relaxation) are calibrated to observed events and don't transfer reliably across watersheds.
- Source-volume specification is upstream of all model output; varies by order of magnitude across scenarios.
- Depth-averaging breaks down for very rapid flows in steep terrain (vertical accelerations matter).
- Entrainment along the runout path (channel scour, bank failure) often poorly characterized.

**Cross-discipline uses**:
- **Hydrology**: precipitation forcing from AR products (`PD-AR-landslide`); hydrograph from coupled rainfall-runoff models feeds initiation.
- **Geotechnical engineering**: Mohr-Coulomb framework shared (`CC-geotech-MohrCoulomb`); D-Claw explicitly couples geotech mechanics with debris-flow dynamics.
- **Volcanology**: lahar hazard from Mt. Rainier and other Cascade volcanoes (`PD-volcanic-seismicity`) uses these tools (Osceola Mudflow benchmark; Crandell 1971).
- **Geomorphology**: post-event channel reconfiguration constrains model rheology backwards.

**When you see this in a paper**: confirm rheology choice, source-volume scenario, calibration data, and whether the run is deterministic or probabilistic (ensemble across uncertain inputs).

**Anchor citations**:
- Iverson, R. M., & George, D. L. (2014). A depth-averaged debris-flow model that includes the effects of evolving dilatancy. I. Physical basis. *Proceedings of the Royal Society A*, 470(2170), 20130819. doi:10.1098/rspa.2013.0819
- Christen, M., Kowalski, J., & Bartelt, P. (2010). RAMMS: Numerical simulation of dense snow avalanches in three-dimensional terrain. *Cold Regions Science and Technology*, 63(1–2), 1–14. doi:10.1016/j.coldregions.2010.04.005
- Crandell, D. R. (1971). *Postglacial lahars from Mount Rainier volcano, Washington*. USGS Professional Paper 677. doi:10.3133/pp677

**Related cards**: `CC-geotech-MohrCoulomb`, `CC-geotech-PorePressure`, `PD-debris-flow`, `PD-AR-landslide`, `PD-post-fire-erosion`, `PD-volcanic-seismicity`

---

## MC-geomorph-sediment-monitoring: Fluvial sediment monitoring

**What it is**: in-situ measurement of sediment flux in rivers and streams. Three broad families: (1) suspended-sediment sampling (USGS standard depth-integrating samplers; Edwards & Glysson 1999); (2) bedload sampling (Helley-Smith samplers, bedload traps, slot samplers; Helley & Smith 1971); (3) acoustic and seismic surrogates that infer bedload flux from passive sensors (Burtin et al. 2008; Tsai et al. 2012; Gimbert et al. 2014). All feed the sediment continuity `CC-geomorph-Qs`.

**What you can retrieve**:
- Suspended-sediment concentration time series at USGS gauges (instantaneous, daily, annual); rating curves for ungauged extrapolation.
- Bedload flux at trap-equipped sites or via acoustic / seismic inversions.
- Sediment-budget closure: source-to-sink mass balance over a watershed.
- Datasets: USGS National Water Information System (`MC-hydro-NWIS`) sediment records; PNW-specific Sediment Tracking Network.

**Failure modes**:
- Rating curves Q_s = a Q^b have factor-2–10 uncertainty at extreme flows.
- Bedload sampling captures only a tiny fraction of the streambed; one storm can dominate decades of background record.
- Sample bias: most monitoring is at calm-flow conditions; the storm flows that move the mass are underrepresented.
- Seismic-noise bedload inversions (Gimbert et al. 2014 framework) are still being calibrated across diverse settings.

**Cross-discipline uses**:
- **Hydrology**: paired Q and Q_s gauge records close the sediment-water joint budget; `MC-hydro-NWIS` is the operational data source.
- **Seismology**: high-frequency seismic-noise PSD is a non-invasive bedload proxy (`CC-seismo-noise`, `TC-14`); allows continuous monitoring where sediment sampling is impossible.
- **Ecology**: sediment flux drives substrate, turbidity, and benthic-community structure.
- **Geotechnical engineering**: sediment delivery to reservoirs is the dominant non-seismic dam-safety concern over decade timescales.

**When you see this in a paper**: confirm sampler type and sampling regime (instantaneous vs. integrated); the suspended-sediment record's flow coverage; for seismic-derived bedload, the inversion framework and the validation data.

**Anchor citations**:
- Helley, E. J., & Smith, W. (1971). *Development and calibration of a pressure-difference bedload sampler*. USGS Open-File Report 73-108. doi:10.3133/ofr73108
- Edwards, T. K., & Glysson, G. D. (1999). *Field methods for measurement of fluvial sediment*. USGS Techniques of Water-Resources Investigations Book 3, Chapter C2. doi:10.3133/twri03C2
- Burtin, A., Bollinger, L., Vergne, J., Cattin, R., & Nábělek, J. L. (2008). Spectral analysis of seismic noise induced by rivers. *Journal of Geophysical Research: Solid Earth*, 113(B5), B05301. doi:10.1029/2007JB005034

**Related cards**: `CC-geomorph-Qs`, `CC-geomorph-tau`, `CC-seismo-noise`, `MC-hydro-NWIS`, `TC-14`, `PD-river-floods`

---

## MC-geomorph-InSAR: Interferometric SAR for surface deformation

**What it is**: interferometric synthetic aperture radar (InSAR) measures sub-cm to cm-scale surface deformation by differencing the phase of repeat SAR acquisitions. The dominant satellite-based geomorphology tool for slow landslide creep, post-seismic deformation, and ground subsidence. Sentinel-1 (free, 6–12-day revisit), ALOS-2, and the upcoming NISAR are the operational anchors.

**What you can retrieve**:
- Time series of line-of-sight surface deformation at 10–100 m resolution.
- Mean deformation rates (mm/yr) over multi-year stacks; SBAS, PSI (Persistent Scatterer) methods (Casu et al. 2006; Hooper et al. 2007).
- Coseismic displacement fields after large earthquakes; complements `PD-megathrust` and `PD-fault-scarp`.
- Slow-moving landslide inventories (Handwerger et al. 2019); subsidence in pumped aquifer basins (`PD-subsidence-consolidation`).

**Failure modes**:
- Vegetated terrain (dense forest) destroys coherence; PNW Cascadia landslide work uses careful site selection or L-band (ALOS, NISAR) to penetrate canopy.
- Atmospheric phase delay can mimic deformation; multi-pass averaging or weather-model correction (e.g., GACOS) is necessary.
- Steep terrain causes layover and shadow; sensitivity depends on look geometry.
- Line-of-sight only — must combine ascending and descending tracks (or geodesy) to recover 3D displacement.

**Cross-discipline uses**:
- **Seismology**: coseismic and postseismic deformation fields constrain rupture models and slip distributions (`CC-seismo-source`).
- **Geotechnical engineering**: subsidence in pumped basins (`PD-subsidence-consolidation`, `PD-aquifer-depletion`); reservoir-impoundment loading effects.
- **Hydrology**: indirect measurement of groundwater storage change via subsidence rate; complements `MC-hydro-GRACE`.
- **Volcanology**: edifice inflation precursors at Cascade volcanoes (`PD-volcanic-seismicity`).

**When you see this in a paper**: confirm the SAR mission, baseline configuration, atmospheric correction, and whether the line-of-sight result has been decomposed into horizontal and vertical components. Coherence maps should accompany deformation maps.

**Anchor citations**:
- Massonnet, D., & Feigl, K. L. (1998). Radar interferometry and its application to changes in the Earth's surface. *Reviews of Geophysics*, 36(4), 441–500. doi:10.1029/97RG03139
- Bürgmann, R., Rosen, P. A., & Fielding, E. J. (2000). Synthetic aperture radar interferometry to measure Earth's surface topography and its deformation. *Annual Review of Earth and Planetary Sciences*, 28, 169–209. doi:10.1146/annurev.earth.28.1.169
- Handwerger, A. L., Fielding, E. J., Huang, M.-H., Bennett, G. L., Liang, C., & Schulz, W. H. (2019). Widespread initiation, reactivation, and acceleration of landslides in the northern California Coast Ranges due to extreme rainfall. *Journal of Geophysical Research: Earth Surface*, 124(7), 1782–1797. doi:10.1029/2019JF005035

**Related cards**: `MC-geomorph-lidar`, `MC-hydro-GRACE`, `CC-seismo-source`, `PD-subsidence-consolidation`, `PD-fault-scarp`, `PD-AR-landslide`
