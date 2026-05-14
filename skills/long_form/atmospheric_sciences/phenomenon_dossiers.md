---
discipline: atmospheric_sciences
card_type: phenomenon
schema_version: v3
---

# Atmospheric sciences — phenomenon dossiers

Each dossier describes one real-world atmospheric phenomenon with cross-discipline observability. Format follows `docs/card_format_spec.md`.

---

## PD-atmospheric-river: Atmospheric rivers and west-coast moisture transport

**Setting**: filamentary corridors of intense water-vapor transport in the lower troposphere, typically 2,000–4,000 km long × < 1,000 km wide, with IVT > 250 kg/(m·s) (`CC-atm-IVT`). Deliver 30–50% of annual precipitation to the U.S. West Coast in a handful of multi-day events between November and March (Ralph et al. 2019). Canonical AR-5 events: January 2017 California (Oroville spillway crisis), January 2023 California, 1996 Oregon-Washington floods. ARs also affect western Europe, southern Chile, southern South America, and New Zealand.

**Mechanism (4-step chain)**:
1. **(Atmospheric)** Extratropical cyclones over the Pacific organize moisture into low-level jets (LLJ) ahead of cold fronts; the warm conveyor belt advects subtropical moisture poleward at 20–40 m/s.
2. **(Atmospheric)** Sustained IVT > 250 kg/(m·s) along a filamentary axis defines the AR; intense events exceed 1,250 kg/(m·s) (AR-5 scale).
3. **(Atmospheric + topography)** Orographic enhancement on windward slopes (Cascades, Sierra, Olympics, Coast Range) multiplies precipitation rates 2–5× via forced ascent; precipitation totals reach 100–500 mm in 24 h.
4. **(Hydrology + geomorph + geotech)** Downstream cascade: snowmelt + rain-on-snow → streamflow extremes → channel-forming floods (`PD-river-floods`) + shallow landslides (`PD-AR-landslide`) + debris flows (`PD-debris-flow`); dam safety becomes the multi-day decision (`PD-dam-levee-safety`).

**Observables per discipline**:
- **Atmospheric**: IVT, AR Scale (`CC-atm-IVT`); ERA5 reanalysis (`MC-atm-ERA5`); GPM/IMERG QPE (`MC-atm-GPM`); NEXRAD/MRMS (`MC-atm-NEXRAD`); GNSS-derived IWV (`MC-atm-GNSS-IWV`).
- **Hydrology**: NWIS peak streamflow records (`MC-hydro-NWIS`); SNOTEL antecedent SWE; SMAP soil moisture (`MC-hydro-SMAP`).
- **Geomorphology**: post-event lidar DoD for channel and hillslope change (`MC-geomorph-lidar`).
- **Geotechnical engineering**: instrumented embankments, piezometers, dam-spillway monitoring (`PD-dam-levee-safety`).
- **Seismology**: high-frequency seismic noise from bedload transport (`CC-seismo-noise`, `TC-14`); microseism intensification from concurrent ocean storms (`PD-microseism`).
- **Ecology**: AR-replenished snowpack supports late-summer ecological flows; immediate impacts on riparian ecosystems.

**Open questions for translator-agent integration**:
- Climate-change intensification: thermodynamic Clausius-Clapeyron scaling gives ~7%/K, but observed AR intensification in CMIP6 frequently exceeds this (Espinoza et al. 2018); the dynamical contribution is the open question.
- Coupled hillslope-channel sediment response during ARs as an integrated geomorph-hydro problem (Gaia mountain-to-sea agenda).
- Operational coupling of AR forecasts to landslide, debris-flow, and dam-safety decisions is regionally uneven; NOAA AR Scale + USGS landslide hazard products are still evolving toward integration.

**Anchor papers**:
- Ralph, F. M., Rutz, J. J., Cordeira, J. M., Dettinger, M., Anderson, M., Reynolds, D., Schick, L. J., & Smallcomb, C. (2019). A scale to characterize the strength and impacts of atmospheric rivers. *Bulletin of the American Meteorological Society*, 100(2), 269–289. doi:10.1175/BAMS-D-18-0023.1
- Dettinger, M. D., Ralph, F. M., Das, T., Neiman, P. J., & Cayan, D. R. (2011). Atmospheric rivers, floods and the water resources of California. *Water*, 3(2), 445–478. doi:10.3390/w3020445
- Espinoza, V., Waliser, D. E., Guan, B., Lavers, D. A., & Ralph, F. M. (2018). Global analysis of climate change projection effects on atmospheric rivers. *Geophysical Research Letters*, 45(9), 4299–4308. doi:10.1029/2017GL076968

**Related cards**: `CC-atm-IVT`, `CC-atm-precip`, `CC-atm-q`, `MC-atm-ERA5`, `MC-atm-GPM`, `PD-AR-landslide`, `PD-river-floods`, `PD-debris-flow`, `PD-dam-levee-safety`, `TC-15`

---

## PD-heat-dome: Extreme-heat events and the 2021 Pacific Northwest heat dome

**Setting**: persistent anomalous high-pressure systems that trap heat in the lower troposphere for days, producing multi-day extreme-temperature events. Canonical recent event: 25–30 June 2021 PNW heat dome, with Lytton BC reaching 49.6 °C (a Canadian record) and Portland 46.7 °C; estimated 1,400+ excess deaths regionally (Philip et al. 2022 attribution analysis). Similar events: 2003 Europe, 2010 Russia, 2022 Europe, 2022 China, 2023 Texas-Northern Mexico.

**Mechanism (3-step chain)**:
1. **(Atmospheric)** Persistent anticyclone (often Ω-block or omega-block configuration) suppresses cloud cover and vertical mixing; adiabatic compression and downward turbulent transport warm the lower troposphere.
2. **(Atmospheric + land surface)** Surface heating raises sensible-heat flux H; dry antecedent soils mean little energy goes to LE (`MC-hydro-eddycov` energy partition); positive feedback amplifies surface T.
3. **(Atmospheric)** High VPD + low PBL height (clear skies + subsidence) maximize daytime T extremes; nighttime T also elevated due to suppressed boundary-layer turbulent cooling.

**Observables per discipline**:
- **Atmospheric**: gridded surface T (ERA5, gridded gauge products like nClimGrid); upper-air heights (500 hPa Z) for the dome structure.
- **Hydrology**: streamflow drops; SMAP soil moisture (`MC-hydro-SMAP`) typically shows pre-event drying.
- **Ecology**: forest mortality from heat + drought stress (Allen et al. 2010 framework, `PD-forest-mortality`); vegetation indices NDVI/EVI capture the multi-week impact.
- **Agricultural sciences**: crop yield losses from heat-stressed grain filling; livestock mortality.
- **Seismology**: thermoelastic forcing of dv/v (`CC-seismo-dvv`) signature reflects the subsurface T response (Hillers et al. 2015).
- **Human health / society**: hospital admissions and mortality records; the largest direct human-impact metric.

**Open questions for translator-agent integration**:
- Climate-change attribution: the 2021 PNW event was made ~150× more likely by anthropogenic warming (Philip et al. 2022 rapid-attribution analysis); analogous attribution is now operational.
- Post-event ecosystem recovery: PNW forests showed significant drought-induced canopy browning lasting months; mortality follow-up is multi-year.
- Operational forecasting at 1–2 weeks lead is mature; sub-seasonal-to-seasonal (S2S) and seasonal forecasting of heat domes remains skill-limited.

**Anchor papers**:
- Philip, S. Y., et al. (2022). Rapid attribution analysis of the extraordinary heat wave on the Pacific coast of the US and Canada in June 2021. *Earth System Dynamics*, 13(4), 1689–1713. doi:10.5194/esd-13-1689-2022
- Bartusek, S., Kornhuber, K., & Ting, M. (2022). 2021 North American heatwave amplified by climate change-driven nonlinear interactions. *Nature Climate Change*, 12(12), 1143–1150. doi:10.1038/s41558-022-01520-4
- Schumacher, D. L., Singh, J., Hauser, M., Fischer, E. M., Wild, M., & Seneviratne, S. I. (2024). Exacerbated summer European warming not captured by climate models. *npj Climate and Atmospheric Science*, 7, 12. doi:10.1038/s41612-024-00580-x

**Related cards**: `CC-atm-T`, `CC-atm-q`, `CC-atm-pressure`, `CC-atm-PBL`, `MC-atm-ERA5`, `PD-forest-mortality`, `PD-flash-drought`, `CC-eco-GPP`, `CC-seismo-dvv`

---

## PD-flash-drought: Flash droughts and rapid-onset moisture-deficit cascades

**Setting**: rapid-onset drought episodes that develop over weeks to ~1 month, distinguishing them from conventional droughts (months to years). Mechanism: combined precipitation deficit and elevated VPD / ET demand. Canonical event: U.S. Northern Plains 2017 (Otkin et al. 2018 retrospective). The concept was articulated by Otkin and colleagues to distinguish a class of events that disproportionately damage crops and ecosystems before traditional drought indicators flag concern.

**Mechanism (3-step chain)**:
1. **(Atmospheric)** Persistent ridge pattern suppresses precipitation; concurrent heat and high VPD elevate atmospheric demand for moisture.
2. **(Land surface)** Surface soil moisture (`MC-hydro-SMAP`) and root-zone moisture drop rapidly; ET partitioning shifts from transpiration to limited evaporation as plants close stomata under high VPD.
3. **(Ecology + agriculture)** Vegetation stress visible in NDVI / EVI / SIF within weeks; crop yield reduction during sensitive phenological stages (flowering, grain filling) is the dominant economic impact. Cascading to streamflow occurs over 1–3 months.

**Observables per discipline**:
- **Atmospheric**: standardized precipitation evapotranspiration index SPEI; evaporative demand drought index EDDI; ERA5 reanalysis (`MC-atm-ERA5`).
- **Hydrology**: SMAP soil moisture rapid-decline detection; NWIS streamflow with 1–3 month lag (`MC-hydro-NWIS`); GRACE TWS over multi-month windows (`MC-hydro-GRACE`).
- **Ecology**: NDVI/EVI rapid drops; SIF as an early-warning leading indicator before NDVI changes.
- **Agricultural sciences**: USDA NASS crop progress reports show yield-stage stress; crop insurance claims spike.
- **Geomorphology**: post-flash-drought wildfire risk rises; subsequent storms increase debris-flow risk in burned watersheds (`PD-post-fire-erosion`).

**Open questions for translator-agent integration**:
- Predictability: flash droughts have shorter lead times than conventional drought; sub-seasonal-to-seasonal forecasting is the relevant target.
- Causality: how much is anthropogenic warming (driving VPD) vs. internal variability (precipitation deficit)?
- Quantitative flash-drought definition is contested; multiple competing indices (rapid-onset SPEI, EDDI, root-zone soil moisture decline) classify the same event differently.

**Anchor papers**:
- Otkin, J. A., Svoboda, M., Hunt, E. D., Ford, T. W., Anderson, M. C., Hain, C., & Basara, J. B. (2018). Flash droughts: A review and assessment of the challenges imposed by rapid-onset droughts in the United States. *Bulletin of the American Meteorological Society*, 99(5), 911–919. doi:10.1175/BAMS-D-17-0149.1
- Pendergrass, A. G., et al. (2020). Flash droughts present a new challenge for subseasonal-to-seasonal prediction. *Nature Climate Change*, 10(3), 191–199. doi:10.1038/s41558-020-0709-0

**Related cards**: `CC-atm-T`, `CC-atm-q`, `CC-atm-precip`, `MC-hydro-SMAP`, `MC-hydro-GRACE`, `MC-hydro-NWIS`, `CC-eco-GPP`, `PD-drought`, `PD-agricultural-drought`, `PD-forest-mortality`

---

## PD-convective-storm: Severe thunderstorms, hail, tornadoes, and lightning

**Setting**: deep moist convective systems producing severe weather — large hail, tornadoes, damaging straight-line winds, cloud-to-ground lightning, and flash flooding. Mesoscale convective systems (MCS) account for the majority of summer warm-season precipitation in the central U.S. Tornadic supercells produce > 1,000 confirmed tornadoes annually in the U.S. (NOAA SPC). PNW-relevant: lightning ignition of wildfires, summer thunderstorms triggering debris flows on burned watersheds, occasional supercell incursions east of the Cascades.

**Mechanism (4-step chain)**:
1. **(Atmospheric)** Conditional instability (high CAPE, often > 1,500 J/kg) + sufficient vertical wind shear + lifting trigger (front, dryline, terrain, outflow boundary).
2. **(Atmospheric + cloud microphysics)** Rapid moist-adiabatic ascent generates supersaturation, hydrometeor formation, electrification, and large hail in supercell updrafts.
3. **(Atmospheric)** Mesocyclone organization in supercells; rear-flank downdraft generates surface vorticity that intensifies into tornadoes under specific conditions.
4. **(Atmospheric + surface)** Surface damage: tornadoes EF-0 through EF-5; hail > 5 cm; downbursts > 50 m/s; lightning ignition.

**Observables per discipline**:
- **Atmospheric**: NEXRAD radar (`MC-atm-NEXRAD`) for structure, rotation, hail signature; GOES (`MC-atm-GOES`) GLM for lightning; surface mesonets for damaging winds.
- **Seismology**: thunderstorm acoustic and seismic signatures are routinely detected (Anderson-Frey, Marine Denolle, Akash Kharita ongoing work at UW; the storm-detector model in GAIA HazLab is an active research area).
- **Geomorphology**: localized flash-flood-driven channel changes; post-fire debris-flow triggers under intense convective rainfall (Cannon et al. 2008; `PD-post-fire-erosion`).
- **Ecology**: lightning ignition is the dominant ignition source for U.S. western wildfires; tornado-induced forest blowdowns create canopy gaps.
- **Agricultural sciences**: hail damages standing crops; high-wind damage to mature grain crops.

**Open questions for translator-agent integration**:
- Climate-change response is regime-dependent: tornado frequency shifts geographically and temporally; hail size statistics depend on competing CAPE-shear changes.
- Seismic detection of storms (Akash Kharita's work) is a frontier; integrating with NEXRAD for ground-truth and at-distance early warning.
- Operational sub-hourly forecasting of severe storms is improving (Warn-on-Forecast initiative) but tornado lead times remain ~10–15 min.

**Anchor papers**:
- Brooks, H. E., Lee, J. W., & Craven, J. P. (2003). The spatial distribution of severe thunderstorm and tornado environments from global reanalysis data. *Atmospheric Research*, 67–68, 73–94. doi:10.1016/S0169-8095(03)00045-0
- Trapp, R. J., Diffenbaugh, N. S., Brooks, H. E., Baldwin, M. E., Robinson, E. D., & Pal, J. S. (2007). Changes in severe thunderstorm environment frequency during the 21st century caused by anthropogenically enhanced global radiative forcing. *Proceedings of the National Academy of Sciences*, 104(50), 19719–19723. doi:10.1073/pnas.0705494104

**Related cards**: `CC-atm-T`, `CC-atm-q`, `CC-atm-wind`, `MC-atm-NEXRAD`, `MC-atm-GOES`, `CC-seismo-noise`, `PD-post-fire-erosion`, `PD-debris-flow`

---

## PD-extreme-precip-intensification: Climate-driven intensification of extreme precipitation

**Setting**: a class of phenomena rather than a single event: the documented and projected intensification of extreme-precipitation rates under anthropogenic warming. The thermodynamic component (Clausius-Clapeyron scaling, ~7%/K of additional column moisture) is robust; the dynamical component (storm intensification, AR strengthening, MCS organization) is the open research frontier. Observed: 1.5–2× intensification in 1-h to 24-h precipitation extremes globally since mid-20th century (Westra et al. 2014; IPCC AR6 Ch. 11).

**Mechanism (Clausius-Clapeyron + dynamical components)**:
1. **(Atmospheric thermodynamics)** Warming raises saturation vapor pressure ~7%/K (Clausius-Clapeyron); column moisture available for precipitation increases proportionally at fixed RH.
2. **(Atmospheric dynamics)** Storm-scale updraft strengthening, MCS organization, AR intensification can produce super-CC scaling. Lenderink & van Meijgaard (2008) showed sub-daily extremes scaling 14%/K in Europe.
3. **(Cascading impact)** Same atmospheric forcing drives flood, landslide, and debris-flow intensification (`PD-AR-landslide`, `PD-river-floods`, `PD-debris-flow`).

**Observables per discipline**:
- **Atmospheric**: gauge-based and reanalysis-based extreme-precipitation indices (Rx1day, Rx5day, R99p, R99pTOT from ETCCDI); CMIP6 ensemble projections.
- **Hydrology**: flood-frequency analyses (`CC-geomorph-flood-frequency`) increasingly show nonstationarity (Milly et al. 2008 "stationarity is dead"); covariate flood-frequency frameworks emerging.
- **Geomorphology**: landslide-inventory and debris-flow records under shifting precipitation thresholds (`PD-AR-landslide`, `PD-post-fire-erosion`).
- **Geotechnical engineering**: design-storm specifications (PMP, PMF) under revision for dam-safety analyses (`PD-dam-levee-safety`).
- **Insurance and society**: claim records and economic impact assessments track intensification.

**Open questions for translator-agent integration**:
- Distinguishing thermodynamic from dynamical contributions requires high-resolution models or process-based decomposition; the standard CMIP archive is coarse for the latter.
- AR-specific intensification: Espinoza et al. (2018) found > CC scaling in CMIP6; mechanism is the dynamical component.
- Compound extremes (heat + precip, drought-then-flood) are increasingly documented as the most damaging class; statistical frameworks for compound extremes are still developing (Zscheischler et al. 2018).

**Anchor papers**:
- Westra, S., Fowler, H. J., Evans, J. P., Alexander, L. V., Berg, P., Johnson, F., Kendon, E. J., Lenderink, G., & Roberts, N. M. (2014). Future changes to the intensity and frequency of short-duration extreme rainfall. *Reviews of Geophysics*, 52(3), 522–555. doi:10.1002/2014RG000464
- Lenderink, G., & van Meijgaard, E. (2008). Increase in hourly precipitation extremes beyond expectations from temperature changes. *Nature Geoscience*, 1(8), 511–514. doi:10.1038/ngeo262
- Zscheischler, J., et al. (2018). Future climate risk from compound events. *Nature Climate Change*, 8(6), 469–477. doi:10.1038/s41558-018-0156-3

**Related cards**: `CC-atm-q`, `CC-atm-precip`, `CC-atm-IVT`, `PD-atmospheric-river`, `PD-AR-landslide`, `PD-river-floods`, `PD-dam-levee-safety`, `TC-15`
