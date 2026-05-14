---
discipline: ecology
card_type: concept
schema_version: v3
---

# Ecology — concept cards

Each card defines one core ecological variable, equation, or measured quantity, with units, numerical ranges, and explicit hooks into the other Gaia disciplines. Format follows `docs/card_format_spec.md`.

---

## CC-eco-GPP: Gross primary productivity, NPP, NEE [µmol/m²/s, g C/m²/yr]

**Quantity**: gross primary productivity (GPP) is the rate of CO₂ fixation by photosynthesis [µmol/m²/s or g C/m²/yr]. Net primary productivity NPP = GPP − R_a (autotrophic respiration); net ecosystem exchange NEE = R_eco − GPP (sign convention: positive flux to atmosphere; net ecosystem productivity NEP = −NEE). The foundational carbon-flux observable in ecosystem science; coupled to ET through stomatal conductance at the leaf (`TC-16`).

**Defining relation**: GPP separated from observed NEE via flux-partitioning algorithms (Reichstein et al. 2005; nighttime-ER extrapolation) applied to eddy-covariance F_C records. Stomatal conductance g_s couples GPP to ET: A = g_s (C_a − C_i) for CO₂ and E = g_s (e_sat − e) for water, sharing the same g_s in the proportionality (Ball-Berry, Medlyn schemes). Solar-induced fluorescence SIF (Badgley et al. 2017) provides a direct optical proxy for GPP.

**Typical ranges**:
- Tropical rainforest GPP: 2,500–3,500 g C/m²/yr.
- Temperate deciduous forest: 1,200–1,800 g C/m²/yr.
- Boreal forest: 400–800 g C/m²/yr.
- Tundra / arid shrubland: 100–400 g C/m²/yr.
- Croplands (managed, fertilized): 1,500–2,500 g C/m²/yr.

**Cross-discipline equivalents**:
- **Hydrology**: GPP and ET share the stomatal-conductance gate at the leaf; the ecology-hydrology bridge through `TC-16`. Drought-induced stomatal closure reduces both fluxes simultaneously.
- **Atmospheric sciences**: GPP is the dominant terrestrial sink in the carbon cycle; large-scale climate change in temperature and CO₂ modify GPP (CO₂-fertilization, drought stress).
- **Agricultural sciences**: managed-ecosystem analog — crop GPP × radiation-use efficiency × harvest index = yield; coupling to crop models (`MC-ag-crop-models`).

**When you see this in a paper**: confirm flux-partitioning method (nighttime vs. daytime; Reichstein vs. Lasslop); GPP is *derived* from NEE plus model assumptions, not a direct measurement. Year-to-year variability in GPP is dominated by phenology timing and drought events.

**Anchor citations**:
- Beer, C., et al. (2010). Terrestrial gross carbon dioxide uptake: Global distribution and covariation with climate. *Science*, 329(5993), 834–838. doi:10.1126/science.1184984
- Reichstein, M., et al. (2005). On the separation of net ecosystem exchange into assimilation and ecosystem respiration. *Global Change Biology*, 11(9), 1424–1439. doi:10.1111/j.1365-2486.2005.001002.x
- Badgley, G., Field, C. B., & Berry, J. A. (2017). Canopy near-infrared reflectance and terrestrial photosynthesis. *Science Advances*, 3(3), e1602244. doi:10.1126/sciadv.1602244

**Related cards**: `CC-eco-LAI`, `CC-hydro-ET`, `CC-atm-q`, `MC-hydro-eddycov`, `MC-eco-eddycov`, `TC-16`, `PD-forest-mortality`, `PD-phenology-shift`

---

## CC-eco-IHA: Indicators of hydrologic alteration [various]

**Quantity**: a 33-metric framework (Richter et al. 1996) characterizing ecologically meaningful aspects of a streamflow time series. Five groups: magnitude (mean monthly flows), duration (1-, 3-, 7-, 30-, 90-day extremes), timing (date of annual minimum and maximum), frequency (high- and low-flow pulse counts), and rate of change (rise and fall rates). Used to quantify the impact of dams, diversions, climate change, and land use on river-ecosystem flow regime.

**Defining relation**: each indicator is computed from a daily-Q time series (`CC-hydro-Q`, `MC-hydro-NWIS`); the canonical natural-flow regime is established from a pre-impact reference period and compared to post-impact for change detection. The Range of Variability Approach (Richter et al. 1997) uses the natural-regime distribution (25th–75th percentile) as the management target.

**Typical ranges** (illustrative):
- Annual peak flow: highly variable by basin; Q_2 to Q_100 spans factor 3–10.
- 7-day low flow Q_7 (baseflow indicator): basin-specific, used in habitat assessments.
- Pulse counts > 75th percentile / yr: 4–15 in natural temperate rivers.
- Rise rates after rainfall: m³/s/day; bankfull events have characteristic time signatures.

**Cross-discipline equivalents**:
- **Hydrology**: IHA is computed entirely from hydrologic data (`CC-hydro-Q`, `MC-hydro-NWIS`); the bridge to ecology is the *ecological interpretation* of those statistics, not the data themselves.
- **Geomorphology**: flow-regime metrics correlate with channel-forming discharge (`CC-geomorph-streampower`); the IHA framework predates ecologically-explicit geomorphic flow-regime work and is now jointly used.
- **Atmospheric**: AR-modulated flow regime shifts under climate change connect IHA to atmospheric drivers.

**When you see this in a paper**: confirm the reference (pre-impact) period definition; IHA's signal-to-noise depends on having ≥ 15 yr of pre- and post-impact records. The framework is descriptive, not mechanistic — it characterizes the alteration but does not predict the ecological response.

**Anchor citations**:
- Richter, B. D., Baumgartner, J. V., Powell, J., & Braun, D. P. (1996). A method for assessing hydrologic alteration within ecosystems. *Conservation Biology*, 10(4), 1163–1174. doi:10.1046/j.1523-1739.1996.10041163.x
- Richter, B. D., Baumgartner, J. V., Wigington, R., & Braun, D. P. (1997). How much water does a river need? *Freshwater Biology*, 37(1), 231–249. doi:10.1046/j.1365-2427.1997.00153.x
- Poff, N. L., et al. (1997). The natural flow regime. *BioScience*, 47(11), 769–784. doi:10.2307/1313099

**Related cards**: `CC-hydro-Q`, `MC-hydro-NWIS`, `CC-geomorph-streampower`, `TC-17`, `PD-salmon-habitat`

---

## CC-eco-plant-water-source: Plant water-source attribution from xylem isotopes [δ¹⁸O, δD ‰]

**Quantity**: the depth (or compartment) from which a plant transpires water, inferred from comparing xylem-water stable-isotope composition (δ¹⁸O, δD) with potential source compartments — recent precipitation, soil-water profiles, groundwater, surface streams. Each compartment carries a distinctive isotopic signature; xylem water inherits the signature of the compartment the plant drew from, since transpiration does not fractionate water during root uptake at most species' osmotic boundaries.

**Defining relation**: end-member mixing analysis δ_xylem = Σ f_i δ_i, where f_i is the fraction from source i, constrained by Σ f_i = 1. Two-source mixing is uniquely identifiable; three or more sources require Bayesian frameworks (MixSIAR) or paired δ¹⁸O–δD analyses. Deuterium-excess d = δD − 8 δ¹⁸O is conserved through soil profiles and identifies source-water history.

**Typical ranges**:
- δ¹⁸O of precipitation: −20 to +5 ‰ globally; temperate moisture ≈ −5 to −15 ‰.
- Groundwater δ¹⁸O: well-mixed, intermediate value reflecting long-term precipitation mean.
- Shallow soil water in arid environments: enriched (less negative) δ¹⁸O from evaporative fractionation.
- Cryptic root-water uptake from rock weathering products documented in some Mediterranean and savanna systems.

**Cross-discipline equivalents**:
- **Hydrology**: shares the isotope-method machinery (`MC-hydro-isotopes`) with recharge and source-water attribution; the same xylem-water sample also constrains recharge timing.
- **Atmospheric**: precipitation-isotope networks (GNIP / WMO-IAEA) anchor the precipitation end-member; AR moisture-source attribution (`PD-atmospheric-river`) uses the same machinery.
- **Geomorphology / ecohydrology**: rooting-depth inferences from plant-water source attribution feed hillslope-vegetation-hydrology models.

**When you see this in a paper**: confirm extraction method (cryogenic vacuum extraction is standard but generates known artifacts in clay-rich soils); the mixing-analysis posterior uncertainty; whether end-member compositions are characterized at the actual site.

**Anchor citations**:
- Dawson, T. E., Mambelli, S., Plamboeck, A. H., Templer, P. H., & Tu, K. P. (2002). Stable isotopes in plant ecology. *Annual Review of Ecology and Systematics*, 33, 507–559. doi:10.1146/annurev.ecolsys.33.020602.095451
- McDonnell, J. J. (2014). The two water worlds hypothesis: Ecohydrological separation of water between streams and trees? *WIREs Water*, 1(4), 323–329. doi:10.1002/wat2.1027
- Brooks, J. R., Barnard, H. R., Coulombe, R., & McDonnell, J. J. (2010). Ecohydrologic separation of water between trees and streams in a Mediterranean climate. *Nature Geoscience*, 3(2), 100–104. doi:10.1038/ngeo722

**Related cards**: `CC-hydro-recharge`, `CC-hydro-ET`, `CC-eco-LAI`, `MC-hydro-isotopes`, `MC-eco-isotopes`, `TC-16`, `PD-forest-mortality`

---

## CC-eco-LAI: Leaf area index, fAPAR, vegetation indices [dimensionless]

**Quantity**: leaf area index LAI = total one-sided leaf area / ground area [m²/m², dimensionless]. The light-intercepting surface that drives canopy photosynthesis, transpiration, and turbulent exchange. Related: fAPAR (fraction of absorbed photosynthetically active radiation; ≈ 1 − exp(−k LAI) for canopy with extinction coefficient k); NDVI, EVI, NIRv, and SIF as satellite proxies.

**Defining relation**: Beer-Lambert canopy attenuation I/I_0 = exp(−k LAI cos⁻¹θ), with k ≈ 0.5–0.7. Stand-level GPP scales approximately with fAPAR × PAR × LUE (light-use efficiency); the MODIS GPP algorithm (Running et al. 2004) uses this product directly.

**Typical ranges**:
- Bare ground: LAI = 0; fAPAR ≈ 0; NDVI ≈ 0.05–0.15.
- Grasslands: LAI = 1–3.
- Temperate forests: LAI = 3–6.
- Tropical rainforest: LAI = 6–8.
- Crop closed canopy (maize, soy at peak): LAI = 3–6.
- NDVI dynamic range: 0.1 (sparse) – 0.9 (dense closed canopy).

**Cross-discipline equivalents**:
- **Hydrology**: LAI controls canopy interception and ET partitioning between transpiration (vegetation-controlled) and evaporation (soil/wet-surface); riparian LAI affects baseflow.
- **Atmospheric sciences**: LAI feeds back to climate through albedo, surface roughness, transpiration; vegetation-climate coupling is the canonical land-surface-model emphasis.
- **Geomorphology**: canopy biomass and LAI proxy for root-cohesion changes after disturbance (post-fire, beetle outbreak); links to landslide susceptibility (`PD-post-fire-erosion`, `CC-eco-root-cohesion`).
- **Agriculture**: crop NDVI / EVI time series are the operational yield-forecasting signal; UAV NDRE has displaced ground-based LAI in many production-scale workflows.

**When you see this in a paper**: confirm LAI definition (one-sided vs. all-sided; effective vs. true), measurement method (LAI-2200 plant canopy analyzer vs. allometric vs. satellite-derived), and time of year. Satellite NDVI / EVI saturate at LAI > 4–5 in dense canopies.

**Anchor citations**:
- Asner, G. P., Scurlock, J. M. O., & A. Hicke, J. (2003). Global synthesis of leaf area index observations: implications for ecological and remote sensing studies. *Global Ecology and Biogeography*, 12(3), 191–205. doi:10.1046/j.1466-822X.2003.00026.x
- Running, S. W., Nemani, R. R., Heinsch, F. A., Zhao, M., Reeves, M., & Hashimoto, H. (2004). A continuous satellite-derived measure of global terrestrial primary production. *BioScience*, 54(6), 547–560. doi:10.1641/0006-3568(2004)054[0547:ACSMOG]2.0.CO;2

**Related cards**: `CC-eco-GPP`, `CC-eco-root-cohesion`, `CC-hydro-ET`, `CC-atm-radiation`, `MC-eco-remote-sensing`, `PD-phenology-shift`

---

## CC-eco-root-cohesion: Root reinforcement and apparent cohesion [kPa]

**Quantity**: apparent cohesion c_root [kPa] contributed by plant roots to soil shear strength in the Mohr-Coulomb framework. Quantitative root reinforcement (Wu et al. 1979, Pollen-Bradford fiber-bundle model) sums tensile-strength contributions of all roots crossing a potential failure surface; modern models (Schwarz et al. 2010 RBMw) treat progressive failure rather than simultaneous breaking.

**Defining relation**: in the Mohr-Coulomb model with roots, τ_f = c'_soil + c_root + (σ_n − u) tan φ'; root cohesion adds to soil cohesion. Magnitude scales with root area ratio RAR, tensile strength T_r, and load-sharing structure of the root network. Post-disturbance (fire, deforestation, beetle outbreak), root cohesion decays exponentially as roots die and decompose; recovery on regrowth schedule.

**Typical ranges**:
- Mature forest c_root: 1–25 kPa depending on species and depth (Sidle & Ochiai 2006 compilation).
- PNW Douglas-fir mature stand: 5–15 kPa near surface, decreasing with depth.
- Grassland / shrubland c_root: 0.5–5 kPa.
- Post-fire decay timescale: half-life 3–10 yr; complete loss in heavily burned watersheds within 5–8 yr (Sidle & Ochiai 2006 framework).
- Post-clearcut: peak landslide-susceptibility window 5–15 yr after harvest.

**Cross-discipline equivalents**:
- **Geotechnical engineering**: c_root adds linearly to c' in `CC-geotech-MohrCoulomb`; for shallow rainfall-triggered slides on natural slopes (`PD-AR-landslide`, `PD-coseismic-landslide`), c_root often controls the FS (`CC-geotech-FS`, `TC-11`).
- **Geomorphology**: vegetation-mediated control on hillslope diffusion (Roering et al. 2010); post-fire erosion window driven by root-cohesion loss (`PD-post-fire-erosion`).
- **Hydrology**: same root system that provides cohesion also accesses soil water; the coupled biogeomorphic-hydrologic system.

**When you see this in a paper**: confirm the field-measurement basis (in-situ pullout, direct shear with roots, or modeled from RAR and species-specific T_r); values from one site / species don't transfer reliably. Time-since-disturbance is the dominant control on the practical c_root at a given location.

**Anchor citations**:
- Sidle, R. C., & Ochiai, H. (2006). *Landslides: Processes, Prediction, and Land Use*. AGU Water Resources Monograph 18. doi:10.1029/WM018
- Pollen-Bantle, N. (2007). Temporal and spatial variability in root reinforcement of streambanks. *Catena*, 69(3), 197–205. doi:10.1016/j.catena.2006.05.004
- Schwarz, M., Cohen, D., & Or, D. (2010). Root-soil mechanical interactions during pullout and failure of root bundles. *Journal of Geophysical Research: Earth Surface*, 115(F4), F04035. doi:10.1029/2009JF001603

**Related cards**: `CC-geotech-MohrCoulomb`, `CC-geotech-FS`, `CC-eco-LAI`, `PD-AR-landslide`, `PD-post-fire-erosion`, `TC-11`

---

## CC-eco-species-diversity: Species diversity and community ecology metrics [dimensionless, species/area]

**Quantity**: Shannon diversity H' = −Σ p_i ln(p_i), Simpson diversity D = 1 − Σ p_i²; species richness S (count); species-area S = c A^z (MacArthur & Wilson 1967 with z ≈ 0.25 for islands). Foundational for biogeography, conservation, and quantifying anthropogenic and climate-driven biodiversity change.

**Defining relation**: MacArthur-Wilson equilibrium between immigration and extinction sets the species-area relation. Lotka-Volterra dN_i/dt = r_i N_i (1 − Σ a_ij N_j / K_i) for community dynamics. Trophic levels and food-web structure (Lindeman 1942 ~10% trophic-transfer efficiency rule of thumb).

**Typical ranges**:
- Local plant-species richness: 1–200 species/m² across biomes.
- Tropical forest plot: 200–400 tree species per ha.
- Species-area exponent z: 0.15–0.40 typical.
- Stream invertebrate richness: 50–200 species per km of unimpaired reach.

**Cross-discipline equivalents**:
- **Hydrology**: hydrologic alteration via `CC-eco-IHA` translates into invertebrate and fish-community diversity loss; well-documented dose-response in regulated rivers.
- **Geomorphology**: channel-bed heterogeneity (substrate, refugia) determines stream-biotic diversity; sediment-yield changes (`CC-geomorph-Qs`) propagate through.
- **Agricultural sciences**: agricultural-landscape simplification reduces biodiversity at the landscape scale; agroforestry, prairie-strip integration are the partial reversals.
- **Atmospheric**: climate-change-driven range shifts redistribute community composition; loss of climate-niche overlap is a leading extinction-risk indicator.

**When you see this in a paper**: confirm which diversity metric and what scale (alpha, beta, gamma); rarity-weighted diversity is more useful for conservation than naive richness; presence-absence vs. abundance-weighted metrics tell different stories.

**Anchor citations**:
- MacArthur, R. H., & Wilson, E. O. (1967). *The Theory of Island Biogeography*. Princeton University Press.
- Magurran, A. E. (2004). *Measuring Biological Diversity*. Blackwell Publishing.
- Tilman, D. (1996). Biodiversity: Population versus ecosystem stability. *Ecology*, 77(2), 350–363. doi:10.2307/2265614

**Related cards**: `CC-eco-IHA`, `CC-eco-trophic-flow`, `PD-salmon-habitat`, `PD-forest-mortality`

---

## CC-eco-trophic-flow: Trophic flux, food-web structure, NEE decomposition [g C/m²/yr]

**Quantity**: the flux of energy / carbon / nutrients between trophic levels in an ecosystem, conventionally with ~10% transfer efficiency per level (Lindeman 1942 rule, plus order-of-magnitude variations). Closely linked to NEE decomposition: NEE = R_eco − GPP, with R_eco = R_a (autotrophic) + R_h (heterotrophic, the consumer + decomposer respiration).

**Defining relation**: Lindeman (1942) trophic-dynamic framework; ecological efficiencies (gross production efficiency, assimilation efficiency, net production efficiency) compound through trophic levels. Modern food-web theory replaces strict pyramids with networked flow analyses (Allesina & Tang 2012 stability theorems).

**Typical ranges**:
- Trophic-transfer efficiency: 5–25% (10% is a rough mean).
- Apex-predator biomass: 0.1–1% of NPP across systems.
- Soil-respiration R_h: 50–80% of NPP in temperate forests.
- Decomposer biomass: 5–25% of total ecosystem biomass.

**Cross-discipline equivalents**:
- **Hydrology**: stream food webs depend on allochthonous vs. autochthonous carbon inputs; AR-driven sediment pulses alter detrital-base food webs.
- **Atmospheric**: terrestrial decomposition (R_h) is a major source in the atmospheric carbon cycle; soil-temperature and -moisture responses to climate change feed back through R_h.
- **Geomorphology**: erosional carbon export (POC, DOC) couples geomorphic and biogeochemical fluxes (`TC-13`); steep mountain belts deliver disproportionately to ocean carbon burial.
- **Agricultural sciences**: managed ecosystems have truncated trophic structure; the ecology-agriculture interface in agroecology.

**When you see this in a paper**: confirm whether trophic positions are inferred from gut-contents, isotopic positions (δ¹⁵N), or expert assignment; isotope-based trophic-position estimates are scale-dependent and assumption-dependent.

**Anchor citations**:
- Lindeman, R. L. (1942). The trophic-dynamic aspect of ecology. *Ecology*, 23(4), 399–417. doi:10.2307/1930126
- Pauly, D., & Christensen, V. (1995). Primary production required to sustain global fisheries. *Nature*, 374(6519), 255–257. doi:10.1038/374255a0
- Allesina, S., & Tang, S. (2012). Stability criteria for complex ecosystems. *Nature*, 483(7388), 205–208. doi:10.1038/nature10832

**Related cards**: `CC-eco-GPP`, `CC-eco-species-diversity`, `MC-eco-isotopes`, `TC-13`, `PD-salmon-habitat`
