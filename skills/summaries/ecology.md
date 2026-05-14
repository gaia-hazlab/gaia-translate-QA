---
discipline: ecology
purpose: system-prompt summary, ~350 words
schema_version: v3
---

# Ecology — summary

Ecology studies the interactions among organisms, between organisms and their environment, and the structure and function of ecosystems. The discipline bridges the GAIA HazLab agenda at multiple points: vegetation modulates hillslope stability (root cohesion in landslides), ET is co-controlled by physiology and atmospheric demand (the ET-GPP coupling), hydrologic regime structures aquatic communities (IHA framework, salmon habitat), and post-disturbance trajectories tie geomorphic and biological recovery together.

**Core governing equations**:
- Stomatal-conductance coupling: E = g_s × VPD and A = g_s × (C_a − C_i) share g_s — the ET-GPP joint control (`TC-16`).
- Net ecosystem exchange NEE = R_eco − GPP; flux partitioning via Reichstein et al. (2005).
- Lotka-Volterra competitive dynamics; logistic growth dN/dt = rN(1 − N/K).
- Species-area S = c A^z (MacArthur & Wilson 1967).
- Root reinforcement: c_root added to soil cohesion in Mohr-Coulomb FS.
- Trophic-transfer efficiency ~10% rule of thumb (Lindeman 1942).

**Core observables**: gross / net primary productivity GPP / NPP and net ecosystem exchange NEE; leaf area index LAI and fAPAR (and proxies NDVI, EVI, NIRv, SIF); root reinforcement c_root [kPa]; xylem-water δ¹⁸O / δD for plant-water source attribution; indicators of hydrologic alteration (IHA) for stream ecology; species diversity (Shannon, Simpson, richness); trophic structure from δ¹⁵N positions.

**Core measurement infrastructure**: eddy-covariance flux towers (FLUXNET / AmeriFlux / ICOS — shared with hydrology); optical and lidar remote sensing (Landsat / Sentinel-2 / MODIS / GEDI / SIF from OCO-2 / TROPOMI); long-term plot networks (USDA FIA, NEON, LTER, ForestGEO); environmental DNA metabarcoding; passive acoustic monitoring (terrestrial AudioMoth / marine OBSs); process models CLM / ELM / ED2 / JULES.

**Cross-discipline hooks the chatbot should be alert for**:
- *Ecology ↔ hydrology*: ET-GPP leaf coupling (`TC-16`), IHA framework (`TC-17`), plant-water source via isotopes (`CC-eco-plant-water-source`), salmon habitat in PNW (`PD-salmon-habitat`).
- *Ecology ↔ geomorphology*: root cohesion controls slope stability (`CC-eco-root-cohesion`, `TC-11`); post-fire windows (`PD-post-fire-erosion`, `PD-fire-recovery`).
- *Ecology ↔ atmospheric sciences*: VPD-driven stomatal closure → forest mortality (`PD-forest-mortality`); phenology shifts under warming (`PD-phenology-shift`).
- *Ecology ↔ geotechnical engineering*: post-fire and post-mortality root-cohesion decay alters hillslope FS calculations (`CC-geotech-FS`).
- *Ecology ↔ agricultural sciences*: agriculture as managed ecosystem; agroecology at the interface.
- *Ecology ↔ seismology*: ambient seismic field correlates with tree-sway and wind (Hillers et al. 2015); marine bioacoustics on OBSs (`MC-eco-PAM` ↔ `MC-seismo-broadband`); soundscape vocabulary collision with seismic "noise" (`agent_playbook.md`).
- *Ecology ↔ near-surface geophysics*: soil-moisture and root-zone imaging via ERT and GPR (`PD-aquifer-architecture`).

**Foundational anchor citations**: MacArthur & Wilson (1967) island biogeography; Lindeman (1942) trophic-dynamic aspect of ecology; Jarvis (1976) and Medlyn et al. (2011) for stomatal conductance; Baldocchi (2003) eddy-covariance review; Reichstein et al. (2005) flux partitioning; Allen et al. (2010) global forest mortality; Sidle & Ochiai (2006) for root cohesion in slope stability; Richter et al. (1996) for IHA framework; Poff et al. (1997) for natural-flow-regime concept.

For full details, retrieve from `skills/long_form/ecology/` (concept cards, method cards, phenomenon dossiers, translation cards).
