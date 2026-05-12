---
discipline: hydrology
card_type: phenomenon
schema_version: v3
---

# Hydrology — phenomenon dossiers

Each dossier describes one real-world hydrological phenomenon with cross-discipline observability. Format follows `docs/card_format_spec.md`.

---

## PD-AR-landslide: Atmospheric-river-driven PNW landslide

**Setting**: the U.S. Pacific Northwest (western Washington, Oregon, northern California) and analogous wet-temperate orographic margins (British Columbia, southern Chile, New Zealand South Island). Atmospheric rivers (ARs) deliver 30–50% of West Coast annual precipitation in a handful of multi-day events between November and March (Ralph et al. 2019); the largest ARs reliably trigger shallow landslides and debris flows in the coastal range and the Cascades. Canonical events: 1996 Oregon storms; 2007 Chehalis floods; 2017 Oroville; January 2023 California ARs (≈ 700 landslides documented). Post-fire windows (Cannon et al. 2008) have shifted, lower thresholds due to root-cohesion loss.

**Mechanism (4-step chain)**:
1. **(Atmospheric)** AR makes landfall; orographic enhancement on windward slopes produces > 200 mm precipitation in 24–48 h (`MC-atm-ERA5`, GPM IMERG).
2. **(Hydrology)** Infiltration and unsaturated-zone wetting raise the water table; pressure-diffusion timescale `CC-hydro-D` controls how quickly the perched / shallow groundwater pressure rises in the failure-plane vicinity.
3. **(Hydrology + geotech)** Transient pore-pressure rise (`CC-hydro-p`) reduces σ' on the candidate failure surface; Mohr-Coulomb shear strength `CC-geotech-MohrCoulomb` falls until factor of safety `CC-geotech-FS` < 1 (Iverson 2000 transient infiltration model).
4. **(Geomorphology + ecology)** Failure mobilizes as shallow translational slide → debris flow; sediment delivered to channels alters downstream Q and habitat; recovery is paced by root-system regrowth (Sidle & Ochiai 2006).

**Observables per discipline**:
- **Atmospheric**: IVT (integrated vapor transport), AR Scale (Ralph et al. 2019), GPM IMERG precipitation, NOAA-MRMS QPE; ERA5 reanalysis for hindcasts.
- **Hydrology**: tipping-bucket rain gauges, USGS NWIS streamflow (`MC-hydro-NWIS`), SNOTEL antecedent SWE, antecedent SMAP soil moisture (`MC-hydro-SMAP`).
- **Geotechnical engineering**: slope inclinometers, piezometers, occasionally CPT-based ground-truth characterization (`MC-geotech-CPT`).
- **Geomorphology**: post-event landslide inventories (optical, SAR, lidar-derived DEM differencing); long-term sediment-flux records.
- **Seismology**: high-frequency seismic noise from bedload mobilization (Burtin et al. 2008; `CC-seismo-noise`); rare seismic detection of large debris flows.
- **Ecology**: forest cover, root cohesion contribution, post-fire root-strength decay timescale.

**Open questions for translator-agent integration**:
- Operational coupling of AR forecasts to slope-stability forecasts is regionally uneven; NOAA AR Scale and USGS landslide hazard products are evolving toward but not yet integrated nationally.
- Post-fire pore-pressure response timescales (root-cohesion loss + macropore-driven preferential flow) are poorly constrained at the watershed scale.
- ML landslide-inventory pipelines (Tanyas et al. 2017) give rapid post-event ground truth; pre-event probabilistic forecasting at the slope scale remains aspirational.

**Anchor papers**:
- Iverson, R. M. (2000). Landslide triggering by rain infiltration. *Water Resources Research*, 36(7), 1897–1910. doi:10.1029/2000WR900090
- Ralph, F. M., Rutz, J. J., Cordeira, J. M., Dettinger, M., Anderson, M., Reynolds, D., Schick, L. J., & Smallcomb, C. (2019). A scale to characterize the strength and impacts of atmospheric rivers. *Bulletin of the American Meteorological Society*, 100(2), 269–289. doi:10.1175/BAMS-D-18-0023.1
- Cannon, S. H., Gartner, J. E., Wilson, R. C., Bowers, J. C., & Laber, J. L. (2008). Storm rainfall conditions for floods and debris flows from recently burned areas in southwestern Colorado and southern California. *Geomorphology*, 96(3–4), 250–269. doi:10.1016/j.geomorph.2007.03.019

**Related cards**: `CC-hydro-p`, `CC-hydro-D`, `CC-geotech-FS`, `CC-geotech-MohrCoulomb`, `CC-seismo-noise`, `TC-02`, `TC-11`, `MC-hydro-SMAP`, `MC-hydro-NWIS`

---

## PD-aquifer-depletion: Irrigation-driven aquifer depletion

**Setting**: heavily pumped agricultural basins globally. Canonical: California Central Valley (40% U.S. fruit/nut supply; ≈ 100 km³ depleted 1920–2020; Faunt et al. 2016); High Plains / Ogallala aquifer (≈ 250 km³ cumulative depletion); North China Plain; Punjab; Saudi Arabia (now functionally drained). All show GRACE TWS declines, well-level falls, and InSAR-detected subsidence. The dominant anthropogenic perturbation to the global freshwater system; Konikow (2011) estimates groundwater depletion contributed 0.4 mm/yr to 20th-century sea-level rise.

**Mechanism (3-step chain)**:
1. **(Agriculture + hydrology)** Pumping > recharge (`CC-hydro-recharge`); water table or piezometric head drops; long-term decline is the dominant signal.
2. **(Hydrology + geotech)** Pressure decline propagates into adjacent low-permeability aquitards by diffusion (`CC-hydro-D`); effective stress increases (`CC-hydro-p`, `CC-geotech-MohrCoulomb`); aquitards consolidate inelastically beyond preconsolidation (`CC-geotech-cv`).
3. **(Geotech)** Surface subsidence accumulates as integrated aquitard compaction; storage loss is largely permanent because Sₛ_inelastic >> Sₛ_elastic.

**Observables per discipline**:
- **Hydrology**: USGS NWIS well-level records (`MC-hydro-NWIS`), GRACE TWS anomalies (`MC-hydro-GRACE`), pumping inventories (state-by-state coverage varies hugely), local irrigation district metering.
- **Geotechnical engineering**: aquitard m_v from oedometer (`MC-geotech-triaxial`), extensometer compaction at depth intervals (Central Valley network), piezometer transients.
- **Near-surface geophysics**: InSAR (Sentinel-1, ALOS) at cm/yr precision over decades — the dominant modern observable for subsidence rate.
- **Agricultural sciences**: irrigation demand, cropping pattern, return-flow estimates, economic value of water.
- **Seismology**: stress changes from poroelastic loading can modulate regional seismicity (Wicks et al. 2001 Las Vegas; Amos et al. 2014 Central Valley).
- **Ecology**: phreatophyte mortality, riparian habitat loss, baseflow decline in connected streams.

**Open questions for translator-agent integration**:
- Permanent inelastic compaction is irreversible storage loss; the link to long-term water security is direct but rarely quantified outside USGS reports.
- Joint inversion of InSAR + GRACE + well levels for aquitard properties is an active hydrogeophysics frontier (Smith et al. 2017).
- Climate-driven recharge changes interact with anthropogenic withdrawal; attribution to climate vs. management is methodologically difficult.

**Anchor papers**:
- Scanlon, B. R., Faunt, C. C., Longuevergne, L., Reedy, R. C., Alley, W. M., McGuire, V. L., & McMahon, P. B. (2012). Groundwater depletion and sustainability of irrigation in the US High Plains and Central Valley. *Proceedings of the National Academy of Sciences*, 109(24), 9320–9325. doi:10.1073/pnas.1200311109
- Faunt, C. C., Sneed, M., Traum, J., & Brandt, J. T. (2016). Water availability and land subsidence in the Central Valley, California, USA. *Hydrogeology Journal*, 24(3), 675–684. doi:10.1007/s10040-015-1339-x
- Konikow, L. F. (2011). Contribution of global groundwater depletion since 1900 to sea-level rise. *Geophysical Research Letters*, 38(17), L17401. doi:10.1029/2011GL048604

**Related cards**: `CC-hydro-S`, `CC-hydro-recharge`, `CC-hydro-D`, `CC-geotech-cv`, `CC-geotech-MohrCoulomb`, `MC-hydro-GRACE`, `MC-hydro-NWIS`, `PD-subsidence-consolidation`, `PD-drought`

---

## PD-induced-seismicity: Injection- and pumping-induced seismicity

**Setting**: regions where subsurface fluid pressure has been perturbed by human activity on critically stressed faults. Canonical cases: U.S. midcontinent wastewater-injection swarm (Oklahoma 2009–2017; peak Mw 5.8 Pawnee 2016; Ellsworth 2013); enhanced-geothermal-system events (Basel 2006 Mw 3.4 led to project termination; Pohang South Korea 2017 Mw 5.5 with population exposure); long-running examples include Rocky Mountain Arsenal (Healy et al. 1968), Geysers geothermal field. Emerging concern: CO₂ sequestration sites and lithium-brine production.

**Mechanism (3-step chain)**:
1. **(Hydrology)** Fluid injection raises pressure p in a permeable target horizon (`CC-hydro-p`); pressure migrates by diffusion (`CC-hydro-D`) along permeable pathways and into hydraulically connected faults.
2. **(Hydrology + seismology)** Effective normal stress σ_n − p on a pre-existing fault drops; Coulomb stress change ΔCFS = Δτ + μ' Δσ_n becomes positive on optimally oriented faults (`CC-seismo-stress`, `TC-02`).
3. **(Seismology)** Stick-slip rupture on the destabilized fault; magnitudes scale with the fault area available, not directly with injection volume (so single large events on long pre-existing structures are the dominant hazard). The r²/t cloud of triggered events expands as r ≈ √(4πDt) — the diagnostic measurement of fault-zone D (Shapiro & Dinske 2009).

**Observables per discipline**:
- **Seismology**: ML earthquake catalogs (`MC-seismo-ML`; 10× completeness gain), regional broadband, focal-mechanism inversions to discriminate fluid-driven slip vs. tectonic seismicity (`CC-seismo-source`).
- **Hydrology**: injection-volume and pressure records (FracFocus for U.S. unconventional; state regulators), monitoring-well piezometric responses, post-injection pressure decay.
- **Geotechnical engineering**: infrastructure vulnerability (housing stock, dams, pipelines) often unprepared for unexpected seismic hazard in mid-continent regions.
- **Geomorphology**: minimal direct geomorphic signature unless event is large enough to produce surface rupture (rare for induced events).
- **Atmospheric sciences**: ambient seismic noise modulation by injection-driven dv/v has been proposed but is not robust.

**Open questions for translator-agent integration**:
- Forecasting maximum magnitude from injection parameters remains the central open question (McGarr 2014 ceiling vs. fault-area-limited Shapiro framework give different answers).
- Disposal-well regulation under traffic-light schemes (Oklahoma, Alberta) is empirically motivated; physics-based real-time forecasting is aspirational.
- Cross-listing for CO₂ sequestration is incipient; long-term containment vs. induced-seismicity tradeoff is a frontier.

**Anchor papers**:
- Ellsworth, W. L. (2013). Injection-induced earthquakes. *Science*, 341(6142), 1225942. doi:10.1126/science.1225942
- Shapiro, S. A., & Dinske, C. (2009). Fluid-induced seismicity: Pressure diffusion and hydraulic fracturing. *Geophysical Prospecting*, 57(2), 301–310. doi:10.1111/j.1365-2478.2008.00770.x
- Goebel, T. H. W., & Brodsky, E. E. (2018). The spatial footprint of injection wells in a global compilation of induced earthquake sequences. *Science*, 361(6405), 899–904. doi:10.1126/science.aat5449

**Related cards**: `CC-hydro-p`, `CC-hydro-D`, `CC-seismo-stress`, `CC-seismo-source`, `CC-geotech-MohrCoulomb`, `MC-seismo-ML`, `TC-02`, `PD-eq-hydro-coupling`

---

## PD-drought: Hydrological drought

**Setting**: precipitation-deficit-driven moisture deficit propagating through soil moisture, streamflow, and groundwater storage. Distinguished from meteorological drought (precipitation deficit alone) by the cascade through hydrologic compartments with lagging timescales (months → years for groundwater). Canonical events: California 2012–2016 (>$5B agricultural loss; > 100 million dead trees; Asner et al. 2016); Murray-Darling 2001–2009; Horn of Africa 2010–2011, 2020–2022; Western U.S. megadrought 2000–present (Williams et al. 2022 attribution to anthropogenic forcing). "Flash drought" (Otkin et al. 2018) is a newer category — rapid onset over weeks, atmospherically driven through high VPD and ET demand.

**Mechanism (cascading chain)**:
1. **(Atmospheric)** Precipitation deficit and elevated vapor-pressure deficit, often associated with persistent ridges and warm sea-surface temperature patterns; AR drought (absence of expected AR landfalls) is the dominant West Coast mechanism.
2. **(Hydrology)** Soil-moisture deficit develops (`MC-hydro-SMAP`); ET demand outstrips supply; root-zone storage depletes.
3. **(Hydrology + ecology)** Streamflow drops (`CC-hydro-Q`, `MC-hydro-NWIS`); baseflow declines as the water table falls; some streams cease flowing.
4. **(Hydrology + agriculture)** Groundwater pumping increases as surface supplies fail (`PD-aquifer-depletion`); aquifer storage declines (`MC-hydro-GRACE`).
5. **(Ecology + geomorphology)** Vegetation mortality (Allen et al. 2010); fire risk rises; post-fire debris-flow hazards (overlap with `PD-AR-landslide`).

**Observables per discipline**:
- **Atmospheric**: SPI / SPEI drought indices (Vicente-Serrano 2010); reanalysis (`MC-atm-ERA5`); evaporative demand drought index EDDI.
- **Hydrology**: SMAP / SMOS soil moisture; NWIS streamflow; GRACE TWS; the U.S. Drought Monitor integrates these.
- **Ecology**: NDVI, EVI, SIF (Sun-induced fluorescence) for vegetation stress; tree-mortality inventories.
- **Agricultural sciences**: yield-gap inventories (USDA NASS), insurance claims, water-allocation records.
- **Geotechnical engineering**: dam-water-level records relevant to spillway and emergency-storage capacity; subsidence acceleration in over-pumped basins.

**Open questions for translator-agent integration**:
- Drought definition disagreement: which compartment, which timescale, which threshold? Multi-index frameworks (e.g., U.S. Drought Monitor) are pragmatic but not mechanistic.
- Climate-change attribution: how much of recent drought is anthropogenic vs. internal variability (Williams et al. 2022 framework for Western U.S.)?
- Flash drought is rapid enough to require sub-monthly observation; SMAP and `MC-hydro-eddycov` networks help, but spatial coverage is uneven.
- Recovery dynamics — what reaches pre-drought state and what doesn't (groundwater rarely fully recovers).

**Anchor papers**:
- Mishra, A. K., & Singh, V. P. (2010). A review of drought concepts. *Journal of Hydrology*, 391(1–2), 202–216. doi:10.1016/j.jhydrol.2010.07.012
- Otkin, J. A., Svoboda, M., Hunt, E. D., Ford, T. W., Anderson, M. C., Hain, C., & Basara, J. B. (2018). Flash droughts: A review and assessment of the challenges imposed by rapid-onset droughts in the United States. *Bulletin of the American Meteorological Society*, 99(5), 911–919. doi:10.1175/BAMS-D-17-0149.1
- Allen, C. D., et al. (2010). A global overview of drought and heat-induced tree mortality reveals emerging climate change risks for forests. *Forest Ecology and Management*, 259(4), 660–684. doi:10.1016/j.foreco.2009.09.001
- Williams, A. P., Cook, B. I., & Smerdon, J. E. (2022). Rapid intensification of the emerging southwestern North American megadrought in 2020–2021. *Nature Climate Change*, 12(3), 232–234. doi:10.1038/s41558-022-01290-z

**Related cards**: `CC-hydro-Q`, `CC-hydro-ET`, `CC-hydro-recharge`, `MC-hydro-SMAP`, `MC-hydro-GRACE`, `MC-hydro-eddycov`, `MC-atm-ERA5`, `PD-aquifer-depletion`, `PD-AR-landslide`

---

## PD-eq-hydro-coupling: Earthquake-triggered hydrologic changes

**Setting**: regional far-field responses to moderate-to-large earthquakes. Documented globally; canonical examples include the 1964 Alaska earthquake (well-level oscillations across the continent; Wang & Manga 2010), 1989 Loma Prieta streamflow steps, 2002 Mw 7.9 Denali well-level oscillations in California (Hsieh et al. 2006), 2011 Mw 9.0 Tōhoku transient groundwater responses observed across the Pacific Rim. Two distinct response classes: rapid coseismic oscillations from dynamic stress (passing surface waves) vs. slower postseismic changes from permeability and pore-pressure-field redistribution.

**Mechanism (two-class typology)**:

*Coseismic dynamic response*:
1. **(Seismology)** Surface waves transit the site, applying transient pore-pressure forcing.
2. **(Hydrology)** Well levels oscillate at the period of the passing wave train; amplitude depends on barometric efficiency and aquifer properties; this is a direct seismometer signal in confined aquifers.

*Postseismic / static stress response*:
1. **(Seismology)** Static stress field changes around the rupture (`CC-seismo-stress`, `CC-seismo-source`).
2. **(Hydrology + geotech)** Permanent pore-pressure changes from poroelastic stress coupling; permeability changes from fracture opening/closing on existing structures (Wang & Manga 2010 framework).
3. **(Hydrology)** Streamflow steps, spring discharge changes (sometimes sustained for years), well-level shifts, mud-volcano activation.

**Observables per discipline**:
- **Seismology**: regional broadband (`MC-seismo-broadband`), dv/v from ambient noise (`CC-seismo-dvv`) tracking postseismic relaxation — directly linked to hydrologic changes via `TC-03`.
- **Hydrology**: continuous well-level monitoring (NWIS, regional networks), streamflow gauges, spring-discharge campaigns.
- **Geotechnical engineering**: nearby infrastructure monitoring; instrumented embankments showing pore-pressure transients.
- **Geomorphology**: triggered landslide inventories (`PD-coseismic-landslide`) often modify watershed hydrology long after the event.

**Open questions for translator-agent integration**:
- Predictive model for the streamflow / well-level response to a given magnitude / distance combination is empirical (Wang & Manga 2010) but does not generalize cleanly outside well-instrumented regions.
- Mechanism partitioning — pore-pressure redistribution vs. permeability change — is debated for individual case studies; isotope and chemistry tracers (`MC-hydro-isotopes`) can sometimes discriminate.
- dv/v ↔ hydrology coupling postseismically is an active topic (Brenguier et al. 2008 Parkfield; many follow-ons) and overlaps with `TC-03`.

**Anchor papers**:
- Wang, C.-Y., & Manga, M. (2010). *Earthquakes and Water*. Springer. doi:10.1007/978-3-642-00810-8
- Hsieh, P. A., Townend, J., Becker, T. W., & Reichow, M. K. (2006). Hydraulic response of an alluvial aquifer to the 2002 Mw 7.9 Denali fault, Alaska, earthquake. *Bulletin of the Seismological Society of America*, 96(6S), S367–S381. doi:10.1785/0120050823
- Manga, M., Brodsky, E. E., & Boone, M. (2003). Response of streamflow to multiple earthquakes. *Geophysical Research Letters*, 30(5), 1214. doi:10.1029/2002GL016618
- Brenguier, F., Campillo, M., Hadziioannou, C., Shapiro, N. M., Nadeau, R. M., & Larose, E. (2008). Postseismic relaxation along the San Andreas fault at Parkfield from continuous seismological observations. *Science*, 321(5895), 1478–1481. doi:10.1126/science.1160944

**Related cards**: `CC-hydro-p`, `CC-hydro-h`, `CC-hydro-K`, `CC-seismo-stress`, `CC-seismo-dvv`, `MC-seismo-broadband`, `MC-hydro-NWIS`, `TC-02`, `TC-03`, `PD-induced-seismicity`, `PD-megathrust`
