---
discipline: ecology
card_type: phenomenon
schema_version: v3
---

# Ecology — phenomenon dossiers

Each dossier describes one real-world ecological phenomenon with cross-discipline observability. Format follows `docs/card_format_spec.md`.

---

## PD-forest-mortality: Drought- and disturbance-driven forest mortality

**Setting**: large-scale tree mortality events driven by drought, heat, insects, and fire — singly or as cascading interactions. Allen et al. (2010) compiled a global syntheses showing emerging climate-driven mortality across diverse forest biomes. Canonical events: Western U.S. piñon-pine die-off 2002–2004 (Breshears et al. 2005); Australian dieback 2002–2010; 2020 California 2nd-year drought mortality. PNW relevance: Douglas-fir bark-beetle outbreaks and 2021-heat-dome-driven canopy browning.

**Mechanism (3-step chain)**:
1. **(Atmospheric + hydrology)** Multi-year drought or acute heat-VPD events (`PD-heat-dome`, `PD-flash-drought`) impose carbon-starvation or hydraulic-failure conditions on trees.
2. **(Ecology)** Two-mode failure: (a) hydraulic failure — xylem cavitation under sustained low water potential; (b) carbon starvation — depleted carbohydrate reserves as stomatal closure prevents photosynthesis (McDowell et al. 2008 framework).
3. **(Ecology + biotic)** Weakened trees become susceptible to bark beetles, defoliators, and pathogens; positive feedbacks between climate stress and biotic agents amplify mortality.

**Observables per discipline**:
- **Ecology**: FIA inventories (`MC-eco-FIA-NEON-LTER`) show mortality rates; NDVI / EVI / SIF declines (`MC-eco-remote-sensing`); aerial-survey insect-damage mapping (USDA Forest Service ADS).
- **Atmospheric**: ERA5 temperature, VPD, and precipitation reanalysis (`MC-atm-ERA5`); SPEI and other drought indices.
- **Hydrology**: SMAP soil moisture (`MC-hydro-SMAP`); streamflow changes from canopy loss; GRACE for regional water-storage decline.
- **Geomorphology**: root-cohesion decay following mortality elevates landslide susceptibility (`CC-eco-root-cohesion`, `PD-post-fire-erosion`); altered hillslope hydrology.
- **Agricultural sciences**: economic-impact assessments; tree-crop losses from same drivers.

**Open questions for translator-agent integration**:
- Predictability: which trees die in a drought event remains the holy grail; species-specific safety margins, hydraulic traits, and microsite conditions all matter.
- Climate-change attribution: increasing trend in tree mortality is well-documented but attribution to anthropogenic warming requires careful framework (Williams et al. 2013).
- Cascading post-mortality fire: dead-tree fuels can elevate fire risk for years; post-mortality forests sometimes have different fire-regime characteristics than living-but-stressed forests.

**Anchor papers**:
- Allen, C. D., et al. (2010). A global overview of drought and heat-induced tree mortality reveals emerging climate change risks for forests. *Forest Ecology and Management*, 259(4), 660–684. doi:10.1016/j.foreco.2009.09.001
- McDowell, N., Pockman, W. T., Allen, C. D., Breshears, D. D., Cobb, N., Kolb, T., Plaut, J., Sperry, J., West, A., Williams, D. G., & Yepez, E. A. (2008). Mechanisms of plant survival and mortality during drought. *New Phytologist*, 178(4), 719–739. doi:10.1111/j.1469-8137.2008.02436.x
- Williams, A. P., et al. (2013). Temperature as a potent driver of regional forest drought stress and tree mortality. *Nature Climate Change*, 3(3), 292–297. doi:10.1038/nclimate1693

**Related cards**: `CC-eco-GPP`, `CC-eco-LAI`, `CC-eco-root-cohesion`, `CC-atm-q`, `CC-atm-T`, `MC-eco-remote-sensing`, `MC-eco-FIA-NEON-LTER`, `PD-heat-dome`, `PD-flash-drought`, `PD-bark-beetle-outbreak`, `PD-post-fire-erosion`

---

## PD-salmon-habitat: Pacific Northwest salmon habitat and hydrologic regime

**Setting**: anadromous Pacific salmon (Oncorhynchus spp. — Chinook, Coho, Sockeye, Pink, Chum, Steelhead) inhabit PNW rivers and tributaries throughout their freshwater life-history phases. Each species has distinct spawn-timing, incubation, juvenile-rearing, smolt-migration, and adult-return phenology. Habitat quality is a function of flow regime (`CC-eco-IHA`), water temperature, sediment substrate (`CC-geomorph-Qs`), riparian cover, and dam/diversion configuration. Five PNW Chinook populations are listed under the U.S. Endangered Species Act; the Snake River sockeye is critically endangered.

**Mechanism (4-step life-history-flow chain)**:
1. **(Hydrology + ecology)** Adult spawn migration timing is cued to flow and temperature; barriers (dams) and altered timing (regulated rivers, late snowmelt) disrupt spawning.
2. **(Ecology + geomorph)** Spawning gravels need specific size distribution (15–150 mm), depth, and flow velocity; sediment fining or aggradation (`PD-river-floods`, `PD-debris-flow`) destroys redds.
3. **(Hydrology + ecology)** Egg incubation requires stable hyporheic-zone flow and cool temperatures (< 15 °C); summer heat-dome events lethal to adults and fry.
4. **(Ecology + hydrology)** Juvenile-rearing and smolt-out-migration timing depend on flow regime; IHA framework (`CC-eco-IHA`) quantifies the suite of relevant flow attributes.

**Observables per discipline**:
- **Ecology**: redd counts (visual surveys, eDNA quantification `MC-eco-eDNA`); juvenile rotary-screw-trap counts; adult dam fish-counts (Bonneville, Lower Granite); SNAP and tribal monitoring datasets.
- **Hydrology**: NWIS daily streamflow (`MC-hydro-NWIS`); IHA computation for impact assessment.
- **Geomorphology**: spawning-substrate surveys; channel-bed mobility (post-`PD-river-floods` redd scour).
- **Atmospheric**: heat-dome (`PD-heat-dome`) impacts on summer-run adults; AR-driven flood events scour redds during incubation.
- **Geotechnical engineering**: dam-passage facilities (fish ladders, surface collectors); reservoir-temperature management.

**Open questions for translator-agent integration**:
- Climate-change vulnerability assessment: warming streams + altered snowmelt timing + reduced summer baseflow constitute a multi-stressor challenge; population-specific risk assessment is the active management question.
- Habitat-restoration efficacy: post-dam-removal recovery (Elwha River 2011–2014 dam removals; Goldsmith et al. 2014) is a natural experiment of large scope.
- Joint hydrologic-ecologic-geomorphologic modeling integrates `PD-salmon-habitat` directly with `PD-river-floods` and post-fire sediment delivery.

**Anchor papers**:
- Poff, N. L., et al. (1997). The natural flow regime. *BioScience*, 47(11), 769–784. doi:10.2307/1313099
- Bisson, P. A., et al. (2009). Conservation of aquatic biodiversity in Pacific Northwest forests: A roadmap. *Fisheries*, 34(3), 124–134. doi:10.1577/1548-8446-34.3.124
- Mantua, N. J., Tohver, I., & Hamlet, A. F. (2010). Climate change impacts on streamflow extremes and summertime stream temperature and their possible consequences for freshwater salmon habitat in Washington State. *Climatic Change*, 102(1–2), 187–223. doi:10.1007/s10584-010-9845-2

**Related cards**: `CC-eco-IHA`, `CC-eco-species-diversity`, `CC-hydro-Q`, `CC-geomorph-Qs`, `MC-hydro-NWIS`, `MC-eco-eDNA`, `TC-17`, `PD-river-floods`, `PD-post-fire-erosion`, `PD-heat-dome`

---

## PD-phenology-shift: Vegetation phenology and climate-driven shifts

**Setting**: the seasonal timing of vegetation activity (greenup, peak canopy, senescence, dormancy) across temperate, boreal, and Mediterranean biomes. Long-term observation reveals systematic shifts in PNW and globally — earlier spring greenup, later autumn senescence, lengthening growing seasons. Foundational long-term datasets: USA-NPN (USA National Phenology Network), USFS aerial surveys, BBC Springwatch, satellite NDVI archives back to 1981 (AVHRR), Landsat back to 1972.

**Mechanism (3-step chain)**:
1. **(Atmospheric)** Temperature and day-length cues trigger greenup; species- and biome-specific dormancy-break thresholds; T-and-photoperiod interactions.
2. **(Ecology)** Greenup drives rapid LAI increase (`CC-eco-LAI`), GPP rise (`CC-eco-GPP`), and water cycling intensification.
3. **(Atmospheric + ecology)** Earlier greenup → earlier seasonal water depletion → drought stress later in growing season; pattern is documented across multiple biomes (Buermann et al. 2018).

**Observables per discipline**:
- **Ecology**: ground phenology observations (USA-NPN, Project BudBurst); satellite NDVI / EVI date-of-50%-greenup; SIF for GPP-specific phenology.
- **Atmospheric**: ERA5 temperature time series; growing-degree-day accumulations; frost-date records.
- **Hydrology**: snowmelt timing shifts (SNOTEL records); streamflow-center-of-volume date earlier under earlier snowmelt + greenup.
- **Agricultural sciences**: crop-phenology shifts affect cropping calendars; CDL time-series captures cropping changes.

**Open questions for translator-agent integration**:
- The "earlier greenup → earlier dryness" hypothesis is well-supported but the magnitude is debated; depends on antecedent precipitation and species.
- Sub-annual phenology shifts (autumn senescence, leaf-color timing) are less well-studied than spring; the autumn season has more biome- and species-specific variation.
- Mismatch with trophic dependents (pollinators, migratory birds, insect emergence) is a separate axis of phenology-shift impact (Visser & Both 2005 ecological mismatch framework).

**Anchor papers**:
- Richardson, A. D., et al. (2013). Climate change, phenology, and phenological control of vegetation feedbacks to the climate system. *Agricultural and Forest Meteorology*, 169, 156–173. doi:10.1016/j.agrformet.2012.09.012
- Buermann, W., et al. (2018). Widespread seasonal compensation effects of spring warming on northern plant productivity. *Nature*, 562(7725), 110–114. doi:10.1038/s41586-018-0555-7
- Visser, M. E., & Both, C. (2005). Shifts in phenology due to global climate change: The need for a yardstick. *Proceedings of the Royal Society B*, 272(1581), 2561–2569. doi:10.1098/rspb.2005.3356

**Related cards**: `CC-eco-LAI`, `CC-eco-GPP`, `CC-atm-T`, `CC-atm-q`, `MC-eco-remote-sensing`, `MC-eco-FIA-NEON-LTER`, `PD-forest-mortality`, `PD-flash-drought`

---

## PD-bark-beetle-outbreak: Bark-beetle outbreaks in Western U.S. forests

**Setting**: native bark beetles (Dendroctonus and Ips spp.) routinely kill trees in Western U.S. and Canadian forests, but climate-driven outbreaks since the 1990s have caused mortality at unprecedented spatial scale. Mountain pine beetle (MPB, Dendroctonus ponderosae) in British Columbia killed ~18 million ha of lodgepole pine 1996–2014; PNW Douglas-fir bark beetle, mountain pine beetle, and western spruce budworm produce regional and stand-scale mortality. Climate-driven warmth reduces winter kill of larvae and accelerates generation time, the proximate mechanism.

**Mechanism (4-step chain)**:
1. **(Atmospheric + ecology)** Warmer winters and longer summers reduce winter mortality of beetle larvae and accelerate generation time — the climate-driven amplification mechanism (Bentz et al. 2010).
2. **(Ecology)** Drought-stressed trees produce weaker defensive resin response, lowering tree resistance to attack; mass-attack threshold for successful colonization is exceeded.
3. **(Ecology + biotic)** Mass attack overwhelms host trees; bluestain fungal symbionts hasten tree death by disrupting water transport; mortality occurs within months to a year.
4. **(Ecology + geomorph)** Post-mortality landscape: dead-tree fuels modify fire regime (sometimes elevated, sometimes shifted to ground-fire regime); root-cohesion decay over 5–10 yr post-mortality elevates landslide hazard (`CC-eco-root-cohesion`).

**Observables per discipline**:
- **Ecology**: aerial-survey damage mapping (USDA Forest Service ADS); FIA mortality plots (`MC-eco-FIA-NEON-LTER`); satellite NDVI / SIF declines as standing-dead canopy fades.
- **Atmospheric**: winter-T minimum records; growing-degree-day accumulations relative to beetle thresholds.
- **Geomorphology**: post-outbreak landslide hazard windows; mid-decadal time lag between mortality and root-cohesion loss.
- **Hydrology**: streamflow-yield increases following defoliation / mortality (less canopy interception, less ET); documented in Colorado and BC.

**Open questions for translator-agent integration**:
- Climate-driven range expansion: MPB poleward and into novel hosts (jack pine in BC, lodgepole-jack pine hybrids) is documented but the future trajectory is uncertain.
- Post-outbreak fire regime: empirical results are mixed; severity of post-mortality fires depends on time-since-mortality and fuel structure.
- Joint hydrologic-ecologic monitoring of bark-beetle outbreaks: streamflow + LAI + soil-moisture cross-correlations are an active research area.

**Anchor papers**:
- Bentz, B. J., Régnière, J., Fettig, C. J., Hansen, E. M., Hayes, J. L., Hicke, J. A., Kelsey, R. G., Negrón, J. F., & Seybold, S. J. (2010). Climate change and bark beetles of the Western United States and Canada: Direct and indirect effects. *BioScience*, 60(8), 602–613. doi:10.1525/bio.2010.60.8.6
- Hicke, J. A., et al. (2012). Effects of biotic disturbances on forest carbon cycling in the United States and Canada. *Global Change Biology*, 18(1), 7–34. doi:10.1111/j.1365-2486.2011.02543.x
- Raffa, K. F., Aukema, B. H., Bentz, B. J., Carroll, A. L., Hicke, J. A., Turner, M. G., & Romme, W. H. (2008). Cross-scale drivers of natural disturbances prone to anthropogenic amplification: The dynamics of bark beetle eruptions. *BioScience*, 58(6), 501–517. doi:10.1641/B580607

**Related cards**: `CC-eco-LAI`, `CC-eco-GPP`, `CC-eco-root-cohesion`, `CC-atm-T`, `MC-eco-FIA-NEON-LTER`, `PD-forest-mortality`, `PD-post-fire-erosion`

---

## PD-fire-recovery: Post-fire ecosystem recovery and successional dynamics

**Setting**: the multi-year-to-decadal ecosystem-recovery trajectory of burned landscapes. Distinct from `PD-post-fire-erosion` (geomorphic side; rapid hillslope and channel response) — this dossier tracks the parallel biological recovery: vegetation regrowth, root-system reestablishment, soil-microbial recovery, animal-community reassembly. PNW: extensive 2020 Oregon fires, 2021 Bootleg Fire, ongoing megafire activity throughout the Western U.S. since the 2000s.

**Mechanism (4-step chain)**:
1. **(Disturbance)** Fire consumes vegetation, root systems (partially or fully), litter and soil organic matter (variable by severity).
2. **(Ecology + soil)** Soil-microbial communities recover on weeks-to-months timescales; mycorrhizal networks regenerate on months-to-years; understory plant recovery begins within months.
3. **(Ecology)** Conifer regeneration depends on seed sources (surviving trees, soil seed bank, post-fire seeding programs); successional trajectory regime-dependent (some PNW forests historically experienced mixed-severity fire).
4. **(Geomorph + ecology)** Root-cohesion (`CC-eco-root-cohesion`) recovers as vegetation reestablishes; post-fire landslide window (`PD-post-fire-erosion`) closes after ~5–10 yr in most temperate-climate cases.

**Observables per discipline**:
- **Ecology**: NDVI / EVI / SIF time series tracking canopy and understory recovery; FIA plot remeasurements after fire; bird-community surveys.
- **Atmospheric**: post-fire microclimate (often warmer, drier than pre-fire); climate-driven impacts on recovery rate.
- **Hydrology**: streamflow yield rises post-fire (less canopy interception, less ET), recovers as vegetation reestablishes; SMAP soil moisture (`MC-hydro-SMAP`).
- **Geomorphology**: post-fire sediment yield (`CC-geomorph-Qs`) often 10–1,000× pre-fire (Moody & Martin 2009); recovery paced by vegetation cover.
- **Agricultural sciences**: post-fire forest grazing rules; range-grass recovery for livestock.

**Open questions for translator-agent integration**:
- Climate-change-driven fire-regime shifts may alter successional trajectories; some forests fail to regenerate after fire under hotter-drier post-fire conditions.
- Type conversions (forest → grassland after severe fire) increasingly documented; lasting consequences for hydrology and ecology.
- Joint long-term monitoring of biological and geomorphic recovery: still relatively rare integrated programs.

**Anchor papers**:
- Stephens, S. L., et al. (2014). Temperate and boreal forest mega-fires: Characteristics and challenges. *Frontiers in Ecology and the Environment*, 12(2), 115–122. doi:10.1890/120332
- Stevens-Rumann, C. S., Kemp, K. B., Higuera, P. E., Harvey, B. J., Rother, M. T., Donato, D. C., Morgan, P., & Veblen, T. T. (2018). Evidence for declining forest resilience to wildfires under climate change. *Ecology Letters*, 21(2), 243–252. doi:10.1111/ele.12889
- Moody, J. A., & Martin, D. A. (2009). Synthesis of sediment yields after wildland fire in different rainfall regimes in the western United States. *International Journal of Wildland Fire*, 18(1), 96–115. doi:10.1071/WF07162

**Related cards**: `CC-eco-LAI`, `CC-eco-GPP`, `CC-eco-root-cohesion`, `CC-geomorph-Qs`, `CC-hydro-Q`, `MC-eco-FIA-NEON-LTER`, `PD-post-fire-erosion`, `PD-forest-mortality`
