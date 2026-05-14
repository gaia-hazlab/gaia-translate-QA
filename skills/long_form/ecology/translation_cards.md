---
discipline: ecology
card_type: translation
schema_version: v3
---

# Ecology — translation cards

Cross-discipline bridges originating from ecology. Complements `TC-06` (watershed mass balance) and `TC-13` (sediment-water-carbon conservation), both already touching ecology. Format follows `docs/card_format_spec.md`.

---

## TC-16: ET–GPP coupling at the leaf — the ecology-hydrology bridge

**Shared structure**: at the leaf scale, water vapor flux (transpiration) and CO₂ flux (photosynthesis) pass through the same stomata; both fluxes are gated by stomatal conductance g_s. The flux equations are E = g_s × VPD (transpiration) and A = g_s × (C_a − C_i) (photosynthesis), sharing g_s. This makes ET and GPP not independent but jointly controlled by the same physiological process. At ecosystem scale, eddy covariance simultaneously measures both fluxes, so the joint observation is directly accessible (`MC-hydro-eddycov`, `MC-eco-eddycov`). The coupling is the deepest hydrology-ecology bridge in the corpus.

**Discipline-specific manifestations**:
- **Hydrology**: ET is a major term in the watershed water balance (`TC-06`); under drought, stomatal closure reduces ET, leaving more water for runoff or soil-storage but at the cost of GPP and biomass production.
- **Ecology**: GPP is the dominant ecosystem-state observable; stomatal closure under VPD stress reduces both productivity and water use simultaneously. Plant hydraulic safety margins (`PD-forest-mortality`) constrain how aggressively a plant can transpire.
- **Atmospheric sciences**: leaf-scale physiology aggregates to land-atmosphere CO₂ and H₂O fluxes that close the global carbon and water cycles at the surface; coupled climate models depend on it (`MC-eco-process-models`).
- **Agricultural sciences**: water-use efficiency WUE = GPP/ET is the key managed-ecosystem metric; high WUE × adequate yield is the modern crop-breeding target.

**When the analogy holds**:
- Healthy, non-stressed vegetation under moderate VPD; the stomatal-conductance coupling is robust.
- Daytime conditions when light is the limiting factor for photosynthesis (not water).
- Aggregated to canopy or ecosystem scale via eddy covariance, where the joint flux signature is observable.

**When the analogy breaks**:
- Severe drought decouples the two fluxes: stomatal closure terminates both, but xylem cavitation (hydraulic failure) and carbon starvation operate on different timescales; mortality can follow distinct pathways (McDowell et al. 2008).
- Soil-evaporation contribution to ET dilutes the GPP-ET link; partitioning ET into transpiration vs. evaporation is essential for the coupling analysis.
- C3 vs. C4 vs. CAM photosynthetic pathways have different g_s controls; crops with C4 metabolism (maize, sorghum) have higher intrinsic WUE.
- High-CO₂ atmospheric conditions reduce g_s and decouple GPP increases from ET decreases (the CO₂-fertilization effect on the water cycle).

**Translator agent move**: when a paper reports either ET or GPP under climate-change or land-use scenarios, retrieve the paired card and the joint coupling. Ask: is the GPP-ET joint response consistent? Studies that increase GPP without changing ET (or vice versa) need explanation. Field experimental tools: eddy covariance at the same tower; isotope-based ET partitioning; sap-flux + chamber measurements at species scale.

**Anchor citations**:
- Beer, C., et al. (2009). Temporal and among-site variability of inherent water use efficiency at the ecosystem level. *Global Biogeochemical Cycles*, 23(2), GB2018. doi:10.1029/2008GB003233
- McDowell, N., et al. (2008). Mechanisms of plant survival and mortality during drought. *New Phytologist*, 178(4), 719–739. doi:10.1111/j.1469-8137.2008.02436.x
- Medlyn, B. E., et al. (2011). Reconciling the optimal and empirical approaches to modelling stomatal conductance. *Global Change Biology*, 17(6), 2134–2144. doi:10.1111/j.1365-2486.2010.02375.x

**Related cards**: `CC-eco-GPP`, `CC-eco-LAI`, `CC-eco-plant-water-source`, `CC-hydro-ET`, `CC-atm-q`, `MC-eco-eddycov`, `MC-hydro-eddycov`, `TC-06`, `PD-forest-mortality`, `PD-flash-drought`

---

## TC-17: Indicators of Hydrologic Alteration — flow regime as ecological observable

**Shared structure**: the natural-flow regime is a structuring force for river ecosystems. The Richter et al. (1996) Indicators of Hydrologic Alteration (IHA, `CC-eco-IHA`) framework reduces a daily-discharge time series to 33 ecologically meaningful metrics covering flow magnitude, duration, timing, frequency, and rate of change. The ecological response — invertebrate communities, fish populations, riparian vegetation, salmonid life-history success (`PD-salmon-habitat`) — is structured by these flow-regime attributes. The framework bridges the hydrologic data record to the ecological consequence and is the dominant cross-discipline tool for environmental-flow management.

**Discipline-specific manifestations**:
- **Hydrology**: the IHA suite is computed entirely from a daily-Q record (`CC-hydro-Q`, `MC-hydro-NWIS`); the bridge is the *ecological interpretation*, not new hydrologic measurement.
- **Ecology**: ecological-flow requirement assessment uses the natural-regime distribution (25th–75th percentile by IHA metric) as the management target; the *Range of Variability Approach* (Richter et al. 1997) sets restoration goals.
- **Geomorphology**: channel-forming discharges and bed mobility (`CC-geomorph-streampower`) are direct flow-regime consequences; IHA-style framing parallels geomorphic-effective-flow concepts (Wolman & Miller 1960).
- **Agricultural sciences**: water rights and consumptive-use diversions modify the flow regime; integration with IHA quantifies the ecosystem cost of agricultural withdrawal.
- **Atmospheric sciences**: climate-change-driven flow-regime shifts (earlier snowmelt, intensified ARs) are the upstream driver of IHA changes.

**When the analogy holds**:
- Pre- and post-impact records of ≥ 15 yr are available; IHA's signal-to-noise depends on adequate baseline data.
- The ecological-response function is reasonably documented at the river or basin of interest.
- Climate non-stationarity is small relative to the impact signal (or is explicitly modeled).

**When the analogy breaks**:
- Highly modified rivers where the natural-flow regime never existed in the available data record; alternative reference frameworks needed.
- Ecosystems where geomorphic / chemical / temperature factors dominate over flow regime (e.g., warm-water systems where T is the main constraint).
- The framework is descriptive — it characterizes the alteration but does not predict species-specific ecological consequences; coupling to species-specific habitat-suitability models requires additional information.

**Translator agent move**: when a paper reports water-management actions, channel restoration, or hydrologic-regime-driven ecological change, retrieve the IHA card and the relevant `CC-hydro-Q` / `MC-hydro-NWIS` infrastructure. The framework integrates seven decades of ecology-hydrology research and is the operational language for environmental flows.

**Anchor citations**:
- Richter, B. D., Baumgartner, J. V., Powell, J., & Braun, D. P. (1996). A method for assessing hydrologic alteration within ecosystems. *Conservation Biology*, 10(4), 1163–1174. doi:10.1046/j.1523-1739.1996.10041163.x
- Poff, N. L., et al. (1997). The natural flow regime. *BioScience*, 47(11), 769–784. doi:10.2307/1313099
- Arthington, A. H., Bunn, S. E., Poff, N. L., & Naiman, R. J. (2006). The challenge of providing environmental flow rules to sustain river ecosystems. *Ecological Applications*, 16(4), 1311–1318. doi:10.1890/1051-0761(2006)016[1311:TCOPEF]2.0.CO;2

**Related cards**: `CC-eco-IHA`, `CC-eco-species-diversity`, `CC-hydro-Q`, `MC-hydro-NWIS`, `CC-geomorph-streampower`, `PD-salmon-habitat`, `PD-river-floods`
