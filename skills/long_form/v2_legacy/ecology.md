# Ecology — Gaia translator skill file

Companion discipline file. Citation policy as in `atmospheric_sciences.md`.

## Core variables and equations

- Gross primary productivity (GPP), net primary productivity (NPP), autotrophic respiration Rₐ, heterotrophic respiration Rₕ, net ecosystem exchange NEE = Rₑcₒ − GPP (carbon-flux convention: positive to atmosphere).
- Evapotranspiration ET = T + E_soil + E_intercept; transpiration governed by Penman-Monteith with stomatal conductance gₛ (Jarvis 1976; Monteith 1965 — shared with hydrology / agriculture).
- Leaf area index LAI, photosynthetically active radiation PAR, fraction absorbed fAPAR.
- Vegetation indices: NDVI = (NIR − Red)/(NIR + Red); EVI, NIRv (Badgley et al. 2017); solar-induced fluorescence SIF.
- Lotka-Volterra population dynamics; logistic growth dN/dt = rN(1 − N/K).
- Species-area relationship S = c A^z (MacArthur & Wilson 1967).
- Root reinforcement: apparent cohesion contribution c_root → modifies the geotechnical FS equation (Sidle & Ochiai 2006).
- Trophic transfer efficiency ~10% (Lindeman 1942).

## Methods

- Eddy covariance: AmeriFlux, FLUXNET networks (Baldocchi 2003) — measures CO₂, H₂O, sensible heat fluxes at 10–30 Hz. Same instrument cluster hydrology uses for ET and atmospheric science uses for boundary-layer fluxes.
- Remote sensing: Landsat (since 1972), Sentinel-2, MODIS, VIIRS for NDVI/EVI/LAI; GEDI spaceborne lidar for canopy structure (Dubayah et al. 2020); airborne lidar; UAV multispectral.
- Forest Inventory and Analysis (FIA) plots, NEON sites, LTER sites.
- Soil organic carbon stocks via SoilGrids, ISRIC, USDA-NRCS.
- eDNA, camera traps, acoustic monitoring (passive acoustic monitoring shares signal processing with seismology).
- Process models: CLM/ELM (NCAR/DOE), Ecosys, ED2, JULES.

## Phenomena studied

- Vegetation phenology (greenup, senescence) and its drivers (T, precip, day length).
- Forest mortality from drought, beetles, fire. Western US bark beetle outbreaks since 2000.
- Post-disturbance succession: post-fire, post-landslide, post-flood.
- Carbon-cycle response to climate: CO₂ fertilization, drought-induced productivity loss.
- Riparian and hyporheic zone ecology — direct overlap with hydrology.
- Species range shifts under warming.
- Invasive species dynamics.

## Translation hooks

- **→ Hydrology**: ET partitioning between T (vegetation-controlled) and E (soil) is a vegetation-ecology problem. Riparian vegetation regulates baseflow. Snowpack-vegetation-runoff feedbacks. The agriculture skill's reference ET is essentially an ecology-hydrology hybrid.
- **→ Geomorphology**: vegetation modifies hillslope diffusion (Roering et al. 2010), root cohesion controls landslide susceptibility (Sidle & Ochiai 2006). Post-fire vegetation loss is the cleanest experimental case for vegetation control on hillslopes (Cannon et al. 2010).
- **→ Seismology**: ambient seismic field correlates with tree sway and wind (Hillers et al. 2015), so vegetation density biases noise-based monitoring. Bioacoustics and seismic detection of animals share signal-processing techniques.
- **→ Atmospheric sciences**: vegetation–atmosphere coupling via stomatal conductance affects boundary layer humidity and temperature; the Lindroth/Bonan vegetation-climate literature.
- **→ Agricultural sciences**: ecology is the parent science; agriculture is a managed-ecosystem subdiscipline.
- **→ Near-surface geophysics**: soil moisture inferred from electromagnetic and seismic methods is the most ecology-relevant geophysical observable.

## Foundational references

- Lindeman, R. L. (1942). The trophic-dynamic aspect of ecology. *Ecology*, 23(4), 399–417. doi:10.2307/1930126
- MacArthur, R. H., & Wilson, E. O. (1967). *The Theory of Island Biogeography*. Princeton Univ. Press.
- Jarvis, P. G. (1976). The interpretation of the variations in leaf water potential and stomatal conductance found in canopies in the field. *Phil. Trans. R. Soc. Lond. B*, 273(927), 593–610. doi:10.1098/rstb.1976.0035
- Baldocchi, D. D. (2003). Assessing the eddy covariance technique for evaluating carbon dioxide exchange rates of ecosystems: past, present and future. *Global Change Biology*, 9(4), 479–492. doi:10.1046/j.1365-2486.2003.00629.x
- Sidle, R. C., & Ochiai, H. (2006). *Landslides: Processes, Prediction, and Land Use*. AGU Water Resources Monograph 18. doi:10.1029/WM018
- Cannon, S. H., et al. (2010). Predicting the probability and volume of postwildfire debris flows in the intermountain western United States. *GSA Bulletin*, 122(1–2), 127–144. doi:10.1130/B26459.1
- Roering, J. J., Marshall, J., Booth, A. M., Mort, M., & Jin, Q. (2010). Evidence for biotic controls on topography and soil production. *Earth Planet. Sci. Lett.*, 298(1–2), 183–190. doi:10.1016/j.epsl.2010.07.040
- Hillers, G., Ben-Zion, Y., Landès, M., & Campillo, M. (2015). Interaction of microseisms with crustal heterogeneity: A case study from the San Jacinto Fault Zone area. *Geochem. Geophys. Geosyst.*, 16(8), 2603–2618. doi:10.1002/2015GC005881
- Badgley, G., Field, C. B., & Berry, J. A. (2017). Canopy near-infrared reflectance and terrestrial photosynthesis. *Science Advances*, 3(3), e1602244. doi:10.1126/sciadv.1602244
- Dubayah, R., et al. (2020). The Global Ecosystem Dynamics Investigation: High-resolution laser ranging of the Earth's forests and topography. *Science of Remote Sensing*, 1, 100002. doi:10.1016/j.srs.2020.100002
