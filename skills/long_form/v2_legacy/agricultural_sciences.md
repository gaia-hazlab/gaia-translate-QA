# Agricultural sciences — Gaia translator skill file

Companion discipline file. Citation policy as in `atmospheric_sciences.md`.

## Core variables and equations

- Reference evapotranspiration ET₀ via Penman-Monteith (Allen et al. 1998, FAO-56). Crop ET = Kc · ET₀, where Kc is a stage-specific crop coefficient.
- Soil water balance over root zone: dS/dt = P + I − ET − D − Q (precipitation, irrigation, ET, deep drainage, runoff). Same equation as bucket-model hydrology.
- Plant available water PAW = θ_FC − θ_PWP (field capacity − permanent wilting point), expressed per unit root depth.
- Yield response to water (Doorenbos & Kassam 1979 FAO-33): (1 − Yₐ/Yₘ) = Kᵧ (1 − ETₐ/ETₘ).
- Soil organic carbon Stocks SOC = bulk density × depth × C-fraction.
- Crop water productivity CWP = yield / ET.
- Nitrogen-use efficiency NUE; greenhouse-gas fluxes N₂O, CH₄ (rice paddies), CO₂.

## Methods

- Soil moisture: in-situ TDR/FDR, neutron probe, COSMOS cosmic-ray neutron sensors, SMAP/SMOS satellite. Same observable that ambient-noise seismology infers via dv/v.
- ET estimation: lysimeters, eddy covariance (shared with ecology and atmosphere), satellite-based METRIC, SSEBop, PT-JPL, ECOSTRESS, OpenET.
- Crop yield mapping: yield-monitor combine data, Landsat/Sentinel time series, MODIS NDVI/EVI, UAV NDRE.
- Crop models: DSSAT (Jones et al. 2003), APSIM (Holzworth et al. 2014), AquaCrop (FAO), CropSyst.
- Agricultural censuses: USDA NASS Cropland Data Layer (CDL); Census of Agriculture.
- Soil characterization: SSURGO, gSSURGO, ROSETTA pedotransfer functions; NRCS lab data.

## Phenomena studied

- Drought stress and yield loss; flash drought (Otkin et al. 2018).
- Irrigation-induced groundwater depletion: Ogallala/High Plains, California Central Valley (Famiglietti 2014; Scanlon et al. 2012). Drives subsidence (Faunt et al. 2016 in Central Valley: locally >10 m cumulative).
- Soil salinization in irrigated arid lands.
- Nutrient runoff and downstream eutrophication (Gulf of Mexico hypoxia, Lake Erie HABs).
- Tillage-induced erosion and post-tillage windblown dust (the 1930s Dust Bowl mechanism).
- Pesticide leaching and groundwater contamination.
- Cropping pattern adaptation under climate change.

## Translation hooks

- **→ Hydrology**: agriculture is by far the dominant human modifier of the water cycle. ~70% of global freshwater withdrawal is irrigation. ET₀ Penman-Monteith machinery is identical between fields. Pumping signatures show up as well-hydrograph drawdowns, GRACE storage anomalies, and surface subsidence.
- **→ Atmospheric sciences**: short-term reliance on weather forecasts (irrigation scheduling, freeze warnings); long-term reliance on climate projections (crop suitability).
- **→ Geomorphology**: cropland is the dominant non-roads source of anthropogenic sediment in many basins (Montgomery 2007 PNAS). Tillage erosion + wind erosion + post-harvest gullying.
- **→ Geotechnical engineering**: irrigation pumping → consolidation → land subsidence in Central Valley is the canonical case study; the same effective-stress mechanism that drives liquefaction works in reverse here.
- **→ Seismology**: aquifer depletion changes crustal loading; documented seasonal seismicity modulation in California (Johnson et al. 2017). Provides a direct anthropogenic-driver signal.
- **→ Ecology**: agriculture is a managed ecosystem. Cover-cropping, agroforestry, and regenerative practices sit at the interface.
- **→ Near-surface geophysics**: ERT, EMI, GPR, MASW used for irrigation management, drainage tile mapping, and root-zone characterization (Romero-Ruiz et al. 2018 review).

## Foundational references

- Penman, H. L. (1948). Natural evaporation from open water, bare soil and grass. *Proc. R. Soc. Lond. A*, 193(1032), 120–145. doi:10.1098/rspa.1948.0037
- Monteith, J. L. (1965). Evaporation and environment. *Symposia of the Society for Experimental Biology*, 19, 205–234.
- Doorenbos, J., & Kassam, A. H. (1979). *Yield Response to Water*. FAO Irrigation and Drainage Paper 33.
- Allen, R. G., Pereira, L. S., Raes, D., & Smith, M. (1998). *Crop Evapotranspiration: Guidelines for Computing Crop Water Requirements*. FAO Irrigation and Drainage Paper 56.
- Jones, J. W., et al. (2003). The DSSAT cropping system model. *European Journal of Agronomy*, 18(3–4), 235–265. doi:10.1016/S1161-0301(02)00107-7
- Scanlon, B. R., et al. (2012). Groundwater depletion and sustainability of irrigation in the US High Plains and Central Valley. *PNAS*, 109(24), 9320–9325. doi:10.1073/pnas.1200311109
- Famiglietti, J. S. (2014). The global groundwater crisis. *Nature Climate Change*, 4(11), 945–948. doi:10.1038/nclimate2425
- Holzworth, D. P., et al. (2014). APSIM – Evolution towards a new generation of agricultural systems simulation. *Environmental Modelling & Software*, 62, 327–350. doi:10.1016/j.envsoft.2014.07.009
- Faunt, C. C., Sneed, M., Traum, J., & Brandt, J. T. (2016). Water availability and land subsidence in the Central Valley, California, USA. *Hydrogeology Journal*, 24(3), 675–684. doi:10.1007/s10040-015-1339-x
- Johnson, C. W., Fu, Y., & Bürgmann, R. (2017). Seasonal water storage, stress modulation, and California seismicity. *Science*, 356(6343), 1161–1164. doi:10.1126/science.aak9547
- Otkin, J. A., et al. (2018). Flash droughts: A review and assessment of the challenges. *Bull. Amer. Meteor. Soc.*, 99(5), 911–919. doi:10.1175/BAMS-D-17-0149.1
- Montgomery, D. R. (2007). Soil erosion and agricultural sustainability. *PNAS*, 104(33), 13268–13272. doi:10.1073/pnas.0611508104
- Romero-Ruiz, A., et al. (2018). A review of geophysical methods for soil structure characterization. *Reviews of Geophysics*, 56(4), 672–697. doi:10.1029/2018RG000611
