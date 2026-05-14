---
discipline: agricultural_sciences
card_type: concept
schema_version: v3
---

# Agricultural sciences — concept cards

Each card defines one core agricultural variable, equation, or measured quantity, with units, numerical ranges, and explicit hooks into the other Gaia disciplines. Format follows `docs/card_format_spec.md`.

---

## CC-ag-ET0: Reference evapotranspiration and crop coefficient [mm/day, dimensionless]

**Quantity**: reference evapotranspiration ET₀ [mm/day] — the rate of evaporation from a standardized reference grass surface (12 cm height, fully shading the ground, well-watered) under given climate conditions. Crop ET = K_c × ET₀, where K_c is a stage-specific crop coefficient (Allen et al. 1998, FAO-56). The operational language of irrigation scheduling, crop water demand estimation, and ET-based water-rights accounting.

**Defining relation**: FAO-56 Penman-Monteith form: ET₀ = [0.408 Δ (R_n − G) + γ (900/(T+273)) u_2 (e_s − e_a)] / [Δ + γ (1 + 0.34 u_2)]; combines net radiation R_n, vapor pressure deficit e_s − e_a, wind u_2, and temperature T. K_c varies by crop and growth stage: K_c,initial ≈ 0.3, K_c,mid ≈ 1.0–1.2, K_c,late ≈ 0.3–0.7.

**Typical ranges**:
- ET₀ in cool wet temperate climates (PNW winter): 0.5–2 mm/day.
- ET₀ in arid summer (Central Valley, Arizona): 6–10 mm/day.
- Crop ET integrated over growing season: 400–1,000 mm for major field crops.
- K_c for closed maize canopy at peak: ≈ 1.20.

**Cross-discipline equivalents**:
- **Hydrology**: ET₀ is the FAO-56 standardization of `CC-hydro-ET`; the inputs to Penman-Monteith are atmospheric variables shared with `CC-hydro-ET`.
- **Atmospheric sciences**: ET₀ is essentially a diagnostic of atmospheric moisture demand (R_n, VPD, wind), independent of crop or vegetation; the *physical* ET demand.
- **Ecology**: K_c framework parallels but does not equal canopy-conductance modeling (`CC-eco-GPP`); K_c is calibrated empirically, g_s is mechanistic.

**When you see this in a paper**: confirm Penman-Monteith form (FAO-56 vs. ASCE Standardized vs. Penman 1948); K_c values are crop-, region-, and stage-specific; using textbook values out-of-region introduces bias. K_c implicitly assumes well-watered conditions; stress coefficients modify K_c for water-limited situations.

**Anchor citations**:
- Allen, R. G., Pereira, L. S., Raes, D., & Smith, M. (1998). *Crop Evapotranspiration: Guidelines for Computing Crop Water Requirements*. FAO Irrigation and Drainage Paper 56.
- Allen, R. G., Walter, I. A., Elliott, R. L., Howell, T. A., Itenfisu, D., Jensen, M. E., & Snyder, R. L. (2005). *The ASCE standardized reference evapotranspiration equation*. ASCE.

**Related cards**: `CC-hydro-ET`, `CC-atm-q`, `CC-atm-radiation`, `MC-hydro-eddycov`, `MC-ag-OpenET`, `CC-ag-PAW`, `CC-ag-yield-water-response`, `TC-18`

---

## CC-ag-PAW: Plant available water [mm, m³/m³ × root depth]

**Quantity**: the volume of soil water available to plants between field capacity θ_FC (water held against gravity drainage, typically −0.033 MPa matric potential) and permanent wilting point θ_PWP (water unavailable to most crops, typically −1.5 MPa). PAW = (θ_FC − θ_PWP) × root depth [mm of water per root-zone depth]. Foundational for irrigation scheduling — irrigation is triggered when soil-moisture depletion exceeds an allowable fraction of PAW (often 50% for most field crops).

**Defining relation**: van Genuchten (1980) soil-water-retention curve θ(ψ) describes the relationship between water content and matric potential; θ_FC and θ_PWP are points on the curve. Texture is the primary control: sandy soils have low PAW (~50 mm/m), silt loams high (~200 mm/m), clays variable. Pedotransfer functions (ROSETTA; `MC-ag-soil-data`) estimate retention curves from texture and bulk density.

**Typical ranges**:
- Sandy soils: PAW = 50–100 mm/m root depth.
- Loams: PAW = 150–200 mm/m.
- Clay soils: PAW = 100–200 mm/m (depends on clay activity).
- Typical maize root depth: 1.5 m; PAW available ≈ 200–300 mm.
- Allowable depletion before irrigation trigger: 40–60% of PAW for most field crops.

**Cross-discipline equivalents**:
- **Hydrology**: PAW is essentially the agricultural equivalent of the soil-water-storage component of the watershed balance; same observable, different framing.
- **Ecology**: rooting depth and PAW jointly control plant water access; deep-rooted species access groundwater (`CC-eco-plant-water-source`).
- **Geotechnical engineering**: van Genuchten retention curves are shared with unsaturated soil mechanics; the same water-retention physics drives Bishop effective stress (`TC-02`).

**When you see this in a paper**: confirm whether θ_FC is measured (drainage curve after 24–48 h) or estimated from pedotransfer functions; the two can differ by 5–10%. Root-depth assumption matters greatly; effective root depth varies by crop and season.

**Anchor citations**:
- van Genuchten, M. T. (1980). A closed-form equation for predicting the hydraulic conductivity of unsaturated soils. *Soil Science Society of America Journal*, 44(5), 892–898. doi:10.2136/sssaj1980.03615995004400050002x
- Allen, R. G., Pereira, L. S., Raes, D., & Smith, M. (1998). FAO Irrigation and Drainage Paper 56.

**Related cards**: `CC-ag-ET0`, `CC-ag-irrigation-demand`, `CC-hydro-recharge`, `MC-hydro-SMAP`, `MC-hydro-COSMOS`, `MC-ag-soil-data`, `MC-ag-soil-moisture`

---

## CC-ag-yield-water-response: Yield response to water and water-productivity [dimensionless, kg/m³]

**Quantity**: the empirical relationship between crop yield and water supply. FAO-33 framework (Doorenbos & Kassam 1979): (1 − Y_a/Y_m) = K_y (1 − ET_a/ET_m), where Y_a is actual yield, Y_m is maximum potential yield, ET_a / ET_m is actual / potential ET ratio, and K_y is the crop-specific water-deficit yield-response factor. Crop water productivity CWP = yield/ET [kg/m³] is the bottom-line water-use-efficiency metric.

**Defining relation**: K_y captures how sensitively yield responds to water stress at each growth stage. Most field crops show K_y < 1 for vegetative stages and K_y > 1 for reproductive stages (flowering, grain filling) — implying that the same proportional water deficit at flowering produces larger yield reduction than at vegetative stages. AquaCrop (FAO) embeds this as a process-level model rather than a stage-specific lookup.

**Typical ranges**:
- K_y values (FAO-33): maize 1.25 overall, K_y 1.5 at flowering; wheat 1.0 overall; potato 1.1 overall.
- CWP for maize: 1.5–2.5 kg/m³ in well-managed systems; can exceed 3 with stress-tolerant varieties.
- CWP for wheat: 0.8–1.5 kg/m³.
- CWP for rice (paddy): 0.5–1.0 kg/m³.

**Cross-discipline equivalents**:
- **Ecology**: parallel to but not identical to ecosystem water-use efficiency WUE = GPP/ET (`CC-eco-GPP`); crop CWP uses economic yield, not biomass.
- **Hydrology**: water-productivity benchmarks set the economic context for irrigation water-allocation decisions; key input to water-economics framing.
- **Atmospheric**: under climate change, simultaneous CO₂-fertilization (raising photosynthesis at fixed g_s) and rising VPD (raising water demand) produce regime-dependent CWP changes.

**When you see this in a paper**: confirm whether yield is in grain mass, biomass, calories, or economic value; the unit choice strongly affects ranking. Water accounting must distinguish ET (consumed) from withdrawal (some returns to system); CWP often computed on whichever is convenient.

**Anchor citations**:
- Doorenbos, J., & Kassam, A. H. (1979). *Yield Response to Water*. FAO Irrigation and Drainage Paper 33.
- Steduto, P., Hsiao, T. C., Raes, D., & Fereres, E. (2009). AquaCrop — the FAO crop model to simulate yield response to water: I. Concepts and underlying principles. *Agronomy Journal*, 101(3), 426–437. doi:10.2134/agronj2008.0139s

**Related cards**: `CC-ag-ET0`, `CC-ag-irrigation-demand`, `CC-ag-PAW`, `MC-ag-crop-models`, `PD-agricultural-drought`, `PD-climate-adaptation-cropping`

---

## CC-ag-SOC: Soil organic carbon stock [kg C/m², t C/ha]

**Quantity**: total organic carbon mass in the soil profile per unit area [kg C/m² or t C/ha]. SOC = bulk density × depth × organic-C fraction (mass-based). A major terrestrial carbon pool — the top 1 m holds ≈ 1,500 Gt C globally (Jobbágy & Jackson 2000), twice the atmospheric C pool. SOC change is a primary lever in climate-change mitigation through agricultural practices (cover-cropping, conservation tillage, regenerative agriculture).

**Defining relation**: SOC dynamics integrate inputs (root and shoot detritus, manure, char) and losses (heterotrophic respiration R_h, erosion, leaching). Steady-state SOC at a site reflects the balance of inputs minus decomposition; tillage disrupts soil aggregates and accelerates R_h. The "4 per 1000" initiative (COP21 Paris) targets 0.4%/yr SOC increase as a climate-mitigation goal.

**Typical ranges**:
- Cropland SOC (0–30 cm): 2–6 kg C/m² (20–60 t C/ha).
- Grassland SOC (0–30 cm): 4–8 kg C/m² (40–80 t C/ha).
- Forest SOC (0–1 m): 8–20 kg C/m² (80–200 t C/ha).
- Tropical peat soils: > 20 kg C/m².
- Annual SOC gain from regenerative practices: 0.1–0.5 t C/ha/yr (modest; "4 per 1000" target is aspirational).

**Cross-discipline equivalents**:
- **Ecology**: SOC turnover is the dominant component of R_eco; coupling to GPP through the soil-respiration loop (`CC-eco-trophic-flow`).
- **Geomorphology**: erosional sediment carries POC; cumulative erosional carbon export from cropland is non-trivial (Lal 2003 framework); shared concern with `TC-13`.
- **Atmospheric**: SOC decomposition releases CO₂ to atmosphere; carbon-cycle attribution uses SOC stocks and turnover rates.
- **Hydrology**: SOC modifies soil hydraulic properties (porosity, retention, infiltration); ROSETTA pedotransfer functions account.

**When you see this in a paper**: confirm sampling depth (0–30 cm vs. full profile to 1 m or 2 m); equivalent-soil-mass vs. fixed-depth comparisons matter under varying bulk density; analytical method (dry combustion vs. wet oxidation vs. loss-on-ignition) affects results.

**Anchor citations**:
- Jobbágy, E. G., & Jackson, R. B. (2000). The vertical distribution of soil organic carbon and its relation to climate and vegetation. *Ecological Applications*, 10(2), 423–436. doi:10.1890/1051-0761(2000)010[0423:TVDOSO]2.0.CO;2
- Lal, R. (2004). Soil carbon sequestration impacts on global climate change and food security. *Science*, 304(5677), 1623–1627. doi:10.1126/science.1097396
- Minasny, B., et al. (2017). Soil carbon 4 per mille. *Geoderma*, 292, 59–86. doi:10.1016/j.geoderma.2017.01.002

**Related cards**: `CC-eco-trophic-flow`, `CC-geomorph-Qs`, `CC-ag-NUE`, `MC-ag-soil-data`, `TC-13`, `PD-tillage-erosion`

---

## CC-ag-NUE: Nitrogen-use efficiency and agricultural GHG fluxes [kg yield / kg N, dimensionless]

**Quantity**: nitrogen-use efficiency NUE = yield / N input; partial-factor productivity PFP_N. Distinct from agronomic NUE (the increase in yield per unit N added vs. control). Closely related: agricultural greenhouse-gas emissions — N₂O from soil microbial nitrification/denitrification (the dominant agricultural GHG in many systems), CH₄ from flooded rice paddies and enteric fermentation, CO₂ from soil tillage and fossil-fuel-energy inputs.

**Defining relation**: N balance: input (synthetic fertilizer + manure + atmospheric deposition + biological N fixation) = output (harvested N + leaching + denitrification + volatilization + accumulation in soil organic N). NUE is rarely > 0.5 in conventional crop systems globally; losses are dominated by leaching of NO₃⁻ to groundwater and N₂O emission to atmosphere.

**Typical ranges**:
- NUE for maize in U.S.: 0.4–0.7 (yield/N input by mass; depending on management).
- NUE for rice (Asia): 0.3–0.5; lower due to volatilization in flooded paddies.
- N₂O emission factor: ≈ 1% of applied N becomes N₂O (IPCC default).
- CH₄ from flooded rice: 0–20 kg/ha-season; varies with water management.
- Agricultural GHG share of total anthropogenic: ≈ 25% (IPCC AR6 WG3).

**Cross-discipline equivalents**:
- **Hydrology**: N leaching → groundwater nitrate contamination; nutrient export drives downstream eutrophication (`PD-nutrient-runoff`).
- **Atmospheric**: N₂O is a long-lived GHG with ~300× CO₂ warming; agricultural N₂O is the dominant N₂O source.
- **Ecology**: N inputs alter community composition (nitrophile dominance, biodiversity loss); aquatic N inputs drive hypoxia.
- **Geomorphology**: sediment-associated N runoff couples nutrient export to sediment delivery; agroforestry buffer strips reduce both.

**When you see this in a paper**: confirm NUE definition (numerous variants exist); GHG-emission methodology (tier 1 IPCC default vs. tier 2 country-specific vs. tier 3 process-model); accounting boundary (cradle-to-farm-gate vs. broader).

**Anchor citations**:
- Cassman, K. G., Dobermann, A., & Walters, D. T. (2002). Agroecosystems, nitrogen-use efficiency, and nitrogen management. *Ambio*, 31(2), 132–140. doi:10.1579/0044-7447-31.2.132
- Davidson, E. A. (2009). The contribution of manure and fertilizer nitrogen to atmospheric nitrous oxide since 1860. *Nature Geoscience*, 2(9), 659–662. doi:10.1038/ngeo608
- Smith, P., et al. (2014). Agriculture, forestry and other land use (AFOLU). In *Climate Change 2014: Mitigation of Climate Change* (IPCC WG3 AR5), Ch. 11. Cambridge University Press.

**Related cards**: `CC-ag-SOC`, `CC-ag-yield-water-response`, `CC-eco-trophic-flow`, `PD-nutrient-runoff`, `PD-agricultural-drought`, `TC-18`

---

## CC-ag-irrigation-demand: Irrigation withdrawal and demand [m³/ha, km³/yr]

**Quantity**: the volume of water withdrawn for irrigation [m³/ha-season at field scale; km³/yr at regional or national scale]. Globally, irrigation accounts for ≈ 70% of freshwater withdrawals (Wisser et al. 2008; FAO AQUASTAT). Computed as ET demand × area − effective precipitation, with system-efficiency adjustments; or directly metered at withdrawal points (where infrastructure exists).

**Defining relation**: gross irrigation = (crop ET − effective precipitation) / irrigation efficiency. Irrigation efficiency η: surface flood ≈ 40–60%; sprinkler ≈ 60–80%; drip ≈ 80–95%. Net consumptive use is the irrigation portion that becomes ET vs. returns to system (drainage, return flow).

**Typical ranges**:
- Gross irrigation for arid maize (Central Valley): 500–800 mm/season (≈ 5,000–8,000 m³/ha).
- Gross irrigation for arid rice (paddy): 800–1,500 mm/season.
- U.S. total irrigation withdrawal: ≈ 90 km³/yr (USGS).
- Central Valley groundwater pumping: ≈ 10–20 km³/yr; > recharge in dry years.
- Global irrigation withdrawal: ≈ 2,700 km³/yr (Wisser et al. 2008).

**Cross-discipline equivalents**:
- **Hydrology**: irrigation pumping → groundwater drawdown → aquifer depletion (`PD-aquifer-depletion`); the integrated water-cycle modification that drives the agricultural-side framing.
- **Geotechnical engineering**: pumping → consolidation → land subsidence (`PD-subsidence-consolidation`); the irrigation-side framing of the same physical phenomenon.
- **Atmospheric**: irrigation increases local ET, modifying boundary-layer humidity and downwind precipitation (Lo & Famiglietti 2013).
- **Seismology**: aquifer depletion alters surface loading; modulates seasonal-to-decadal seismicity in some heavily-pumped regions (Johnson et al. 2017).

**When you see this in a paper**: confirm whether withdrawal is gross or net (consumptive); irrigation efficiency assumption; the source distinction (groundwater vs. surface vs. inter-basin transfer). Withdrawal data from agricultural censuses can be coarse; satellite ET inversion (`MC-ag-OpenET`) gives ET directly.

**Anchor citations**:
- Wisser, D., Frolking, S., Douglas, E. M., Fekete, B. M., Vörösmarty, C. J., & Schumann, A. H. (2008). Global irrigation water demand: Variability and uncertainties arising from agricultural and climate data sets. *Geophysical Research Letters*, 35(24), L24408. doi:10.1029/2008GL035296
- Lo, M.-H., & Famiglietti, J. S. (2013). Irrigation in California's Central Valley strengthens the southwestern U.S. water cycle. *Geophysical Research Letters*, 40(2), 301–306. doi:10.1002/grl.50108
- Famiglietti, J. S. (2014). The global groundwater crisis. *Nature Climate Change*, 4(11), 945–948. doi:10.1038/nclimate2425

**Related cards**: `CC-ag-ET0`, `CC-ag-yield-water-response`, `CC-hydro-recharge`, `CC-hydro-h`, `PD-aquifer-depletion`, `PD-subsidence-consolidation`, `PD-agricultural-drought`, `TC-18`
