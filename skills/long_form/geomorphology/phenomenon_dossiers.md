---
discipline: geomorphology
card_type: phenomenon
schema_version: v3
---

# Geomorphology — phenomenon dossiers

Each dossier describes one real-world geomorphic phenomenon with cross-discipline observability. Format follows `docs/card_format_spec.md`.

---

## PD-debris-flow: Rainfall-, runoff-, and volcano-driven debris flows

**Setting**: rapid (m/s) gravity-driven flows of water-saturated debris in steep channels. Three principal genetic classes for the Pacific Northwest and analogous regions: (1) rainfall-triggered shallow-landslide-to-debris-flow transitions on burned and unburned slopes (Iverson 1997 mechanics; Cannon et al. 2008 post-fire thresholds); (2) glacial-outburst-driven flows at high-altitude volcanic edifices (Mt. Rainier, Mt. Hood); (3) volcanic lahars from edifice collapse, dome explosions, or pyroclastic-flow-snow interactions. Mt. Rainier's Osceola Mudflow (~5,600 yr BP) reached Puget Sound and is the canonical PNW reference (Crandell 1971; Vallance & Scott 1997).

**Mechanism (4-step chain)**:
1. **(Hydrology + ecology)** Antecedent moisture, intense rainfall (often AR-driven `PD-AR-landslide`), or rapid snowmelt saturates colluvium and channel deposits; post-fire hydrophobicity and root-cohesion loss elevate both runoff and supply (`PD-post-fire-erosion`).
2. **(Geotech + geomorph)** Slope failure mobilizes hillslope debris (Iverson 2000, `TC-02`) or channel-bed entrainment incorporates loose material; the landslide-to-debris-flow transition occurs at ≈ 50% water content.
3. **(Geomorph)** A coarse-grained boulder front precedes a finer-grained tail; D-Claw (`MC-geomorph-debris-flow-modeling`) captures the granular Mohr-Coulomb mechanics and pore-pressure feedback.
4. **(Geomorph + hydrology + ecology)** Inundation and channel reconfiguration deliver sediment downstream; recovery occurs over years to decades.

**Observables per discipline**:
- **Geomorph**: post-event lidar DoD (`MC-geomorph-lidar`) for runout volume and inundation extent; deposit stratigraphy for paleo-event chronology; cosmogenic exposure dating (`MC-geomorph-cosmogenic`) of source areas.
- **Seismology**: passive seismic detection of debris-flow signature (Burtin et al. 2008 framework, `CC-seismo-noise`); local broadband and DAS arrays at instrumented basins.
- **Hydrology**: rain-gauge records (NWIS `MC-hydro-NWIS`), SMAP antecedent soil moisture, stream-stage spikes.
- **Geotechnical engineering**: D-Claw / RAMMS / FLO-2D runout simulations (`MC-geomorph-debris-flow-modeling`); design-event hazard maps for infrastructure.
- **Atmospheric sciences**: AR forecasting (IVT, AR-Scale); QPE for nowcasting.
- **Ecology**: pre- and post-event riparian and channel-substrate inventories; salmonid-redd disturbance assessment.

**Open questions for translator-agent integration**:
- Real-time multi-sensor detection and forecasting at the Cascade volcanic edifices is an active GAIA HazLab agenda; the Manuela Köpfli + Akash Kharita work on multi-sensor hydromechanical integration speaks directly to this.
- Climate-change attribution of post-fire debris-flow frequency under shifting precipitation regimes (Cannon et al. 2008 thresholds derived in CA / CO may not transfer to PNW).
- The lahar-glacial-lake coupling at Rainier remains poorly instrumented; eruption + glacier interaction is a frontier.

**Anchor papers**:
- Iverson, R. M. (1997). The physics of debris flows. *Reviews of Geophysics*, 35(3), 245–296. doi:10.1029/97RG00426
- Cannon, S. H., Gartner, J. E., Wilson, R. C., Bowers, J. C., & Laber, J. L. (2008). Storm rainfall conditions for floods and debris flows from recently burned areas. *Geomorphology*, 96(3–4), 250–269. doi:10.1016/j.geomorph.2007.03.019
- Crandell, D. R. (1971). *Postglacial lahars from Mount Rainier volcano, Washington*. USGS Professional Paper 677. doi:10.3133/pp677
- Vallance, J. W., & Scott, K. M. (1997). The Osceola Mudflow from Mount Rainier: Sedimentology and hazard implications of a huge clay-rich debris flow. *Geological Society of America Bulletin*, 109(2), 143–163. doi:10.1130/0016-7606(1997)109<0143:TOMFMR>2.3.CO;2

**Related cards**: `CC-geomorph-Qs`, `CC-geotech-MohrCoulomb`, `CC-geotech-PorePressure`, `CC-seismo-noise`, `MC-geomorph-debris-flow-modeling`, `MC-geomorph-lidar`, `PD-AR-landslide`, `PD-post-fire-erosion`, `PD-volcanic-seismicity`, `TC-02`, `TC-14`

---

## PD-river-floods: Atmospheric-river-driven river floods

**Setting**: extreme river floods in the U.S. West Coast and analogous wet-temperate margins. ARs deliver 30–50% of West Coast annual precipitation in a handful of multi-day events (Ralph et al. 2019). Canonical events: 1996 PNW floods (Oregon, Washington, $1B damages); 1997 California floods; January 2017 California; 2022 Pakistan (catastrophic). The geomorphic counterpart to the hillslope-focused `PD-AR-landslide`: this dossier tracks the channel and floodplain response.

**Mechanism (4-step chain)**:
1. **(Atmospheric)** AR makes landfall; orographic enhancement on windward slopes produces > 200 mm precipitation in 24–48 h.
2. **(Hydrology)** Saturation-excess and infiltration-excess runoff fill stream channels; bankfull discharge often exceeded by 5–20× in the largest events (`CC-hydro-Q`, `MC-hydro-NWIS`); SNOTEL antecedent SWE and rain-on-snow events amplify peak flows.
3. **(Geomorph)** Channel does geomorphic work: bed mobilization (`CC-geomorph-tau`), bedload pulse (`CC-geomorph-Qs`), bank erosion, avulsion, floodplain inundation. Stream power scales with Q × S; mountain channels can reach 10³ W/m² in extreme events.
4. **(Ecology + geotech)** Sediment redistribution alters salmonid habitat; flood-induced bank failure threatens infrastructure (`PD-dam-levee-safety`).

**Observables per discipline**:
- **Hydrology**: NWIS peak-flow records (`MC-hydro-NWIS`); rating-curve extrapolation at extreme stages has high uncertainty; flood-frequency analysis (`CC-geomorph-flood-frequency`).
- **Geomorph**: pre- and post-event lidar DoD (`MC-geomorph-lidar`) for channel migration and sediment redistribution; suspended-sediment and bedload monitoring (`MC-geomorph-sediment-monitoring`).
- **Atmospheric**: IVT, AR-Scale, NOAA-MRMS QPE, ERA5 reanalysis.
- **Seismology**: bedload-derived seismic noise (`CC-seismo-noise`) provides continuous in-event bedload monitoring at instrumented basins (`TC-14`).
- **Ecology**: post-event channel and riparian inventories; salmonid redd disturbance; IHA (`CC-eco-IHA`) framework for hydrologic alteration.

**Open questions for translator-agent integration**:
- Climate-change intensification of AR-driven extremes: are flood-frequency curves no longer stationary (Milly et al. 2008)? Updated covariate flood-frequency frameworks are emerging.
- Coupled hillslope-channel sediment routing during ARs: how does shallow-landslide sediment input (`PD-AR-landslide`) translate into downstream Q_s amplification?
- Multi-hazard cascades (flood + landslide + dam stress + downstream sedimentation) are the Gaia mountain-to-sea agenda; physics-based forecasting frameworks are aspirational.

**Anchor papers**:
- Wolman, M. G., & Miller, J. P. (1960). Magnitude and frequency of forces in geomorphic processes. *The Journal of Geology*, 68(1), 54–74. doi:10.1086/626637
- Ralph, F. M., Rutz, J. J., Cordeira, J. M., Dettinger, M., Anderson, M., Reynolds, D., Schick, L. J., & Smallcomb, C. (2019). A scale to characterize the strength and impacts of atmospheric rivers. *Bulletin of the American Meteorological Society*, 100(2), 269–289. doi:10.1175/BAMS-D-18-0023.1
- Slater, L. J., & Villarini, G. (2017). On the impact of gaps on trend detection in extreme streamflow time series. *International Journal of Climatology*, 37(10), 3976–3983. doi:10.1002/joc.4954
- Costa, J. E., & O'Connor, J. E. (1995). Geomorphically effective floods. *Natural and Anthropogenic Influences in Fluvial Geomorphology*, AGU Geophysical Monograph 89, 45–56. doi:10.1029/GM089p0045

**Related cards**: `CC-hydro-Q`, `CC-geomorph-streampower`, `CC-geomorph-tau`, `CC-geomorph-Qs`, `CC-geomorph-flood-frequency`, `MC-hydro-NWIS`, `MC-geomorph-lidar`, `PD-AR-landslide`, `PD-dam-levee-safety`, `TC-04`, `TC-14`

---

## PD-landscape-evolution: Long-timescale landscape response to climate and tectonics

**Setting**: the integrated geomorphic response of orogens, passive margins, and continental interiors to long-term forcing by tectonics (rock uplift), climate (precipitation, glaciation), and lithology over 10⁵–10⁸ yr. Canonical orogens: Himalaya–Tibet, Andes, European Alps, Taiwan, New Zealand Southern Alps, Cascadia. Foundational research questions: do landscapes reach steady state between uplift and erosion (and how fast)? What's the relative role of climate vs. tectonics?

**Mechanism**:
1. **(Tectonics → geomorphology)** Rock uplift U raises bedrock toward the surface; chemical and physical weathering produce soil at rates set by the soil-production function (Heimsath et al. 1997).
2. **(Climate → hydrology → geomorphology)** Precipitation and ET drive discharge (`CC-hydro-Q`); discharge × slope drives channel incision (stream power, `CC-geomorph-streampower`); hillslope diffusion (`CC-geomorph-D`) and landslides (`CC-geomorph-landslide-size`) carry hillslope material to channels.
3. **(Glaciation, when relevant)** Pleistocene ice cover restructures landscapes via U-shaped valleys, glacial conditioning of bedrock for post-glacial debuttressing landslides, and pulses of sediment delivery.
4. **(Geomorph → tectonics, feedback)** Erosional unloading drives isostatic rebound and may localize uplift; the "tectonic aneurysm" feedback in active orogens (Zeitler et al. 2001 Nanga Parbat) couples climate, erosion, and tectonics on 10⁶-yr timescales.

**Observables per discipline**:
- **Geomorph**: cosmogenic catchment-mean erosion rates (`MC-geomorph-cosmogenic`); thermochronology (apatite (U-Th)/He, fission-track) for 10⁶–10⁸-yr exhumation; ksn maps (`CC-geomorph-ksn`); long-profile knickpoint distributions.
- **Geology / tectonics**: bedrock geochronology, GPS-derived surface velocities, structural mapping; paleoseismology constrains fault slip rates over 10⁴–10⁶ yr (`PD-fault-scarp`).
- **Climate**: paleoclimate proxies (oxygen-isotope curves, pollen, lake sediments) anchor the forcing time series.
- **Modeling**: Landlab and FastScape (`MC-geomorph-landlab`) for hypothesis testing.

**Open questions for translator-agent integration**:
- Climate-tectonic coupling: causality remains debated (Whipple 2009 vs. Molnar & England 1990 frames). High-resolution paired cosmogenic + thermochronologic + climate datasets are the test bed.
- Transient landscapes after glaciation: most Cascadia and Pacific NW landscapes are not in steady state; cosmogenic vs. modern Q_s comparisons reveal post-glacial sediment slugs still working through the system.
- Climate-change predictions: how do future precipitation regimes change long-term landscape evolution? Models are exploratory rather than predictive at decadal scales.

**Anchor papers**:
- Whipple, K. X., & Tucker, G. E. (1999). Dynamics of the stream-power river incision model. *Journal of Geophysical Research*, 104(B8), 17661–17674. doi:10.1029/1999JB900120
- Willenbring, J. K., & von Blanckenburg, F. (2010). Long-term stability of global erosion rates and weathering during late-Cenozoic cooling. *Nature*, 465(7295), 211–214. doi:10.1038/nature09044
- Whipple, K. X. (2009). The influence of climate on the tectonic evolution of mountain belts. *Nature Geoscience*, 2(2), 97–104. doi:10.1038/ngeo413
- Zeitler, P. K., et al. (2001). Erosion, Himalayan geodynamics, and the geomorphology of metamorphism. *GSA Today*, 11(1), 4–9. doi:10.1130/1052-5173(2001)011<0004:EHGATG>2.0.CO;2

**Related cards**: `CC-geomorph-erosion-rate`, `CC-geomorph-streampower`, `CC-geomorph-ksn`, `CC-geomorph-D`, `MC-geomorph-cosmogenic`, `MC-geomorph-landlab`, `PD-fault-scarp`, `TC-13`

---

## PD-fault-scarp: Fault-scarp morphology and coseismic surface deformation

**Setting**: geomorphic preservation and degradation of coseismic surface ruptures and accumulated scarps over multiple earthquake cycles. Canonical examples: Basin and Range normal faults (decades of paleoseismology); San Andreas system right-lateral offsets in landforms; Cascadia coseismic uplift recorded in ghost forests and emerged paleoshorelines. The geomorphic complement to seismology's `PD-megathrust` (source mechanics) and `PD-coseismic-landslide` (immediate hillslope response): this dossier tracks the longer-term scarp-and-offset record that anchors paleoseismology.

**Mechanism (3-step chain)**:
1. **(Seismology)** Coseismic slip creates a fresh scarp (vertical offset for normal/reverse faults) or lateral offset (strike-slip); scale ≈ slip × cos(dip) for the vertical scarp component (`CC-seismo-source`).
2. **(Geomorph)** Diffusion-controlled scarp degradation begins immediately: high-curvature crest erodes, debris accumulates at the base; the morphology evolves toward equilibrium with κ × t setting the smoothing length (`CC-geomorph-D`; Hanks 2000 review).
3. **(Geomorph + chronology)** Successive earthquakes superimpose new offsets on the degrading scarp; the cumulative-offset / age relationship reveals slip rate; cosmogenic dating of preserved bedrock surfaces (`MC-geomorph-cosmogenic`) anchors the timescale.

**Observables per discipline**:
- **Geomorph**: high-resolution scarp morphology from lidar (`MC-geomorph-lidar`); scarp profiles fit diffusion models for age estimates; offset stream channels and alluvial-fan deposits.
- **Seismology**: trenching records discrete paleoseismic events; coseismic rupture geometry from waveform inversion (`CC-seismo-source`).
- **Geodesy / InSAR**: modern coseismic deformation fields (`MC-geomorph-InSAR`) directly imaged for recent events; calibrates the relationship between rupture and geomorphic signal.
- **Geochronology**: cosmogenic dating of fault-scarp surfaces and dated stratigraphic markers (paleosols, tephras) in trenches.
- **Hydrology**: scarps disrupt drainage patterns; offset alluvial fans record long-term scarp formation.

**Open questions for translator-agent integration**:
- Sub-Holocene paleoseismic record at offshore megathrusts (Cascadia subduction zone): turbidite stratigraphy (Goldfinger et al. 2012) complements onshore coastal-subsidence evidence (`PD-megathrust`).
- Diffusion-modeling-based scarp dating has order-of-magnitude uncertainty; integration with cosmogenic ages and stratigraphic markers tightens this.
- Climate-modulated scarp degradation: humid climates degrade scarps faster than arid; comparison of scarps in different climate zones constrains κ.

**Anchor papers**:
- Wallace, R. E. (1977). Profiles and ages of young fault scarps, north-central Nevada. *Geological Society of America Bulletin*, 88(9), 1267–1281. doi:10.1130/0016-7606(1977)88<1267:PAAOYF>2.0.CO;2
- Hanks, T. C. (2000). The age of scarplike landforms from diffusion-equation analysis. *Quaternary Geochronology: Methods and Applications*, AGU Reference Shelf 4, 313–338. doi:10.1029/RF004p0313
- Avouac, J.-P. (2003). Mountain building, erosion, and the seismic cycle in the Nepal Himalaya. *Advances in Geophysics*, 46, 1–80. doi:10.1016/S0065-2687(03)46001-9

**Related cards**: `CC-geomorph-D`, `CC-geomorph-erosion-rate`, `CC-seismo-source`, `CC-seismo-magnitude`, `MC-geomorph-lidar`, `MC-geomorph-cosmogenic`, `MC-geomorph-InSAR`, `PD-megathrust`, `PD-coseismic-landslide`

---

## PD-post-fire-erosion: Post-wildfire hillslope and channel response

**Setting**: the multi-year geomorphic and hydrologic response of burned landscapes. Canonical settings: California chaparral and Sierra forests; PNW wildfire-affected drainages (2020 Oregon fires; 2023 Maui); SW U.S. monsoon-driven post-fire debris flows. Distinct from background sediment yield by orders of magnitude during the post-fire window; root-cohesion loss and altered runoff dominate hillslope and channel response for 3–10 years.

**Mechanism (4-step chain)**:
1. **(Ecology + soil)** Fire consumes vegetation and litter; hydrophobic compounds produce a water-repellent layer at 1–10 cm depth (DeBano 2000); root cohesion (≈ 1–10 kPa) decays over 3–10 yr post-fire.
2. **(Hydrology)** Hydrophobicity and canopy-interception loss increase runoff coefficients 2–10× for the first storms; infiltration-excess overland flow dominates.
3. **(Geomorph + geotech)** Reduced root cohesion drops `CC-geotech-FS` and lowers landslide / debris-flow rainfall thresholds (Cannon et al. 2008 intensity-duration framework).
4. **(Geomorph + ecology)** Cumulative post-fire sediment yield can be 10–1,000× pre-fire (Moody & Martin 2009); recovery paced by vegetation regrowth over 3–10 yr.

**Observables per discipline**:
- **Geomorph**: post-fire lidar DoD (`MC-geomorph-lidar`); sediment yield from gauging or reservoir surveys; channel-bed changes and aggradation patches.
- **Ecology**: NDVI / EVI satellite indices track vegetation recovery; root-strength time series from in-situ pullouts; BAER (Burn Area Emergency Response) severity maps.
- **Hydrology**: post-fire streamflow magnification; SMAP-derived antecedent moisture; rain-gauge intensity-duration triggering relations.
- **Geotech**: infinite-slope FS sensitivity analyses with time-varying c'_root; flume experiments on hydrophobic soils.
- **Atmospheric**: post-fire smoke modulating microclimate (less impactful than the surface changes); ARs delivering trigger storms (`PD-AR-landslide`).

**Open questions for translator-agent integration**:
- Climate-change implications: increasing fire frequency × intensifying storms compounds the post-fire window risk. Future modeling needs joint fire-climate-hydrology coupling.
- PNW-specific calibration: most post-fire debris-flow thresholds (Cannon et al.) derive from CA and CO; PNW analog work is incipient.
- Real-time monitoring of root-cohesion recovery at burned-watershed scale: NDVI is a proxy but the mechanical link is weak; field measurements are tedious.

**Anchor papers**:
- DeBano, L. F. (2000). The role of fire and soil heating on water repellency in wildland environments: A review. *Journal of Hydrology*, 231–232, 195–206. doi:10.1016/S0022-1694(00)00194-3
- Cannon, S. H., Gartner, J. E., Wilson, R. C., Bowers, J. C., & Laber, J. L. (2008). Storm rainfall conditions for floods and debris flows from recently burned areas in southwestern Colorado and southern California. *Geomorphology*, 96(3–4), 250–269. doi:10.1016/j.geomorph.2007.03.019
- Moody, J. A., & Martin, D. A. (2009). Synthesis of sediment yields after wildland fire in different rainfall regimes in the western United States. *International Journal of Wildland Fire*, 18(1), 96–115. doi:10.1071/WF07162
- Larsen, I. J., MacDonald, L. H., Brown, E., Rough, D., Welsh, M. J., Pietraszek, J. H., Libohova, Z., de Dios Benavides-Solorio, J., & Schaffrath, K. (2009). Causes of post-fire runoff and erosion: Water repellency, cover, or soil sealing? *Soil Science Society of America Journal*, 73(4), 1393–1407. doi:10.2136/sssaj2007.0432

**Related cards**: `CC-geomorph-Qs`, `CC-geomorph-D`, `CC-geotech-FS`, `CC-geotech-MohrCoulomb`, `CC-hydro-Q`, `PD-debris-flow`, `PD-AR-landslide`, `PD-coseismic-landslide`, `TC-11`
