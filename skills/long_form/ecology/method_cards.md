---
discipline: ecology
card_type: method
schema_version: v3
---

# Ecology — method cards

Each card describes one measurement technique, instrument, or dataset relevant to ecology. Format follows `docs/card_format_spec.md`. Cards that share infrastructure with hydrology (`MC-hydro-eddycov`, `MC-hydro-isotopes`) are included here with ecology-specific framing rather than as duplicate cards; the underlying instrument is the same.

---

## MC-eco-eddycov: Eddy covariance from the ecology perspective

**What it is**: the same instrument cluster as `MC-hydro-eddycov` (FLUXNET / AmeriFlux / ICOS sonic-anemometer + gas-analyzer towers), interpreted for ecosystem-carbon and ecosystem-physiology applications. The defining observation of ecosystem carbon flux: continuous, 30-minute NEE, GPP (derived), R_eco (derived), at the ~1 km² footprint.

**What you can retrieve**:
- NEE [µmol/m²/s] at 30-min resolution; daily, monthly, annual aggregates after gap-filling.
- GPP and R_eco via flux-partitioning (Reichstein et al. 2005 nighttime-extrapolation, Lasslop et al. 2010 light-response).
- Co-located ET (LE), sensible heat (H), and ancillary climate variables.
- Latent-heat ↔ CO₂ joint analyses: water-use efficiency WUE = GPP/ET; intrinsic WUE iWUE = GPP/g_s; the leaf-scale ET-GPP coupling experimentally accessible (`TC-16`).
- Standard processing: ONEFlux pipeline; FLUXNET2015 release (Pastorello et al. 2020).

**Failure modes**:
- Energy-balance closure 10–30% gap shared with the hydrology side; carbon-flux interpretation typically more forgiving than ET interpretation.
- Flux partitioning to GPP / R_eco depends on model assumptions; nighttime R_eco extrapolation can mis-estimate daytime values.
- Footprint heterogeneity at sites that mix vegetation types or where tower height is small relative to spatial heterogeneity.
- Disturbance events (fire, harvest, blowdown) make the footprint non-stationary; analysis windows must account for this.

**Cross-discipline uses**:
- **Hydrology**: shared infrastructure (`MC-hydro-eddycov`); WUE closes the ET-GPP joint budget.
- **Atmospheric**: ER decomposition feeds atmospheric carbon-cycle inverse problems; surface-energy balance closure feeds NWP land-surface model validation.
- **Agricultural sciences**: AmeriFlux croplands provide GPP and ET for crop-model validation; managed-ecosystem responses to irrigation and fertilizer captured.

**When you see this in a paper**: same caveats as `MC-hydro-eddycov`. For GPP-specific work, confirm flux-partitioning method and the relative weight of nighttime vs. daytime data in the partition.

**Anchor citations**:
- Baldocchi, D. D. (2003). Assessing the eddy covariance technique for evaluating carbon dioxide exchange rates of ecosystems: past, present and future. *Global Change Biology*, 9(4), 479–492. doi:10.1046/j.1365-2486.2003.00629.x
- Pastorello, G., et al. (2020). The FLUXNET2015 dataset and the ONEFlux processing pipeline for eddy covariance data. *Scientific Data*, 7, 225. doi:10.1038/s41597-020-0534-3

**Related cards**: `MC-hydro-eddycov`, `CC-eco-GPP`, `CC-eco-LAI`, `CC-hydro-ET`, `TC-16`, `PD-forest-mortality`

---

## MC-eco-remote-sensing: Landsat, Sentinel-2, MODIS, GEDI, SIF, NDVI/EVI/NIRv

**What it is**: the satellite-remote-sensing toolkit for ecosystem observation. Optical sensors (Landsat 1972–present at 30 m, Sentinel-2 since 2015 at 10 m, MODIS daily at 250–1,000 m, VIIRS daily at 375 m) produce visible / near-IR / SWIR reflectance from which vegetation indices (NDVI, EVI, NIRv) and biophysical retrievals (LAI, fAPAR) are derived. GEDI spaceborne lidar (2019–present; Dubayah et al. 2020) measures canopy structure and biomass directly. Solar-induced fluorescence (SIF) from OCO-2, TROPOMI provides a direct GPP proxy.

**What you can retrieve**:
- 30-m to 250-m time series of NDVI, EVI, NIRv from MODIS, Landsat, Sentinel-2.
- Canopy-height and above-ground-biomass maps from GEDI.
- Solar-induced fluorescence (SIF) at 750 nm or 740 nm; the most direct optical GPP proxy.
- Land-cover, land-use change products (Hansen Global Forest Change, Landsat-based).
- Access: Google Earth Engine, AWS Open Data, NASA Earthdata, USGS Earth Explorer.

**Failure modes**:
- Cloud cover gaps in optical imagery; tropical sites have months-long data gaps in some years.
- Saturation of NDVI / EVI at LAI > 4–5; NIRv (Badgley et al. 2017) saturates less.
- Atmospheric correction is non-trivial; Landsat surface-reflectance products (LaSRC) and Sentinel-2 Level-2A are operational but have known biases.
- GEDI is currently temporally and spatially sparse (lidar-track sampling); not a continuous canopy map.

**Cross-discipline uses**:
- **Hydrology**: NDVI / fAPAR time series feed dryland ET estimation (PT-JPL, METRIC); used in MC-hydro-modeling land-surface configurations.
- **Atmospheric**: vegetation albedo and phenology from optical remote sensing inform land-surface-model performance.
- **Geomorphology**: post-disturbance vegetation recovery from optical time series; complements `MC-geomorph-lidar` for canopy-structure change after fire or landslide.
- **Agricultural sciences**: yield-forecasting from time-series NDVI / EVI; canopy nitrogen status from red-edge indices.

**When you see this in a paper**: confirm sensor, product level, atmospheric correction, and gap-filling method; the answer depends on every link in this chain. SIF interpretation is sensitive to retrieval method.

**Anchor citations**:
- Running, S. W., Nemani, R. R., Heinsch, F. A., Zhao, M., Reeves, M., & Hashimoto, H. (2004). A continuous satellite-derived measure of global terrestrial primary production. *BioScience*, 54(6), 547–560. doi:10.1641/0006-3568(2004)054[0547:ACSMOG]2.0.CO;2
- Dubayah, R., et al. (2020). The Global Ecosystem Dynamics Investigation: High-resolution laser ranging of the Earth's forests and topography. *Science of Remote Sensing*, 1, 100002. doi:10.1016/j.srs.2020.100002
- Badgley, G., Field, C. B., & Berry, J. A. (2017). Canopy near-infrared reflectance and terrestrial photosynthesis. *Science Advances*, 3(3), e1602244. doi:10.1126/sciadv.1602244

**Related cards**: `CC-eco-LAI`, `CC-eco-GPP`, `MC-eco-eddycov`, `MC-geomorph-lidar`, `PD-phenology-shift`, `PD-forest-mortality`

---

## MC-eco-FIA-NEON-LTER: Long-term ecological plot networks

**What it is**: the systematic in-situ plot networks that anchor ecosystem science. **USDA Forest Inventory and Analysis (FIA)**: ~150,000 plots across the U.S. revisited on 5-10-yr cycles; the operational forest-biomass and tree-mortality dataset (Smith et al. 2009). **NEON** (National Ecological Observatory Network): 47 fixed sites with co-located atmospheric, soil, plant, animal, and water sampling at standardized protocols. **LTER** (Long-Term Ecological Research): 28 sites with decadal+ time series. **GFBI** and **ForestGEO** for global tree-plot networks.

**What you can retrieve**:
- FIA: tree-level inventory (species, DBH, height, condition); plot-level basal area, biomass, mortality rates; reported by USDA Forest Service.
- NEON: standardized hydrology, soil moisture, eddy covariance, vegetation phenology, animal monitoring, eDNA.
- LTER: site-specific multi-decadal records of community composition, productivity, and disturbance.
- All freely accessible through respective data portals.

**Failure modes**:
- FIA plot locations are coordinates-fuzzed for landowner privacy; exact spatial collocation with remote-sensing pixels has small jitter.
- NEON terrestrial vs. aquatic protocols differ; cross-site comparisons require careful protocol harmonization.
- LTER site coverage is uneven globally; Latin America and Africa underrepresented.
- Plot sampling tends to be biased toward low-disturbance areas; high-disturbance landscapes underrepresented.

**Cross-discipline uses**:
- **Hydrology / atmospheric**: NEON's co-located instrument suite provides multi-discipline observations at standardized sites.
- **Geomorphology**: FIA biomass + lidar = above-ground biomass maps; post-disturbance recovery quantified.
- **Agricultural sciences**: agricultural censuses (USDA NASS) have a parallel plot-based design philosophy.
- **Atmospheric**: validation data for remote-sensing GPP, LAI, NDVI products.

**When you see this in a paper**: identify the specific plot network and data version; FIA data revisions are regular and can change plot-level estimates between annual releases.

**Anchor citations**:
- Smith, W. B., Miles, P. D., Perry, C. H., & Pugh, S. A. (2009). *Forest resources of the United States, 2007: A technical document supporting the Forest Service 2010 RPA Assessment*. USDA Forest Service GTR WO-78. doi:10.2737/WO-GTR-78
- Schimel, D., et al. (2007). The era of continental-scale ecology. *Frontiers in Ecology and the Environment*, 5(2), 117–117. doi:10.1890/1540-9295(2007)5[117:TEOCE]2.0.CO;2
- Knapp, A. K., et al. (2012). Past, present, and future roles of long-term experiments in the LTER network. *BioScience*, 62(4), 377–389. doi:10.1525/bio.2012.62.4.9

**Related cards**: `CC-eco-LAI`, `CC-eco-species-diversity`, `MC-eco-remote-sensing`, `PD-forest-mortality`, `PD-phenology-shift`

---

## MC-eco-eDNA: Environmental DNA metabarcoding

**What it is**: the detection and quantification of taxa via DNA shed into the environment (water, soil, sediment, air) and amplified from samples. Pioneering work by Ficetola, Miaud, Pompanon, & Taberlet (2008) in water; metabarcoding standard since ≈ 2015. Now operational for fish surveys (e.g. UC Berkeley CALeDNA, U.S. NOAA), microbial community profiling, biodiversity inventories at unprecedented sampling efficiency.

**What you can retrieve**:
- Presence/absence of target taxa from water samples filtered through 0.45 µm membranes; relative abundance with significant uncertainty.
- Community-level metabarcoding (12S, COI, 18S, ITS markers) for fish, invertebrate, microbial, fungal communities.
- Long-term monitoring (e.g. CALeDNA storage of frozen filters for retrospective analysis).
- Standard pipelines: QIIME2, DADA2, OBITools.

**Failure modes**:
- DNA degradation: detection probability falls with time since deposition and water temperature; quantitative inference of population size is unreliable.
- PCR amplification bias favors some taxa over others; primer choice matters greatly.
- Reference-database completeness: misidentification or no-call for species not in reference databases.
- Contamination: requires careful field and lab protocols; cross-contamination invalidates results.

**Cross-discipline uses**:
- **Hydrology**: water-sample eDNA can complement gauge networks for ecological monitoring; same sampling logistic.
- **Seismology**: source-attribution mathematical framework (`TC-09`) — eDNA source identification is mathematically analogous to seismic source inversion (different forward operator, same Bayesian inverse-problem skeleton).
- **Agricultural sciences**: soil-microbial eDNA for soil-health assessment; pathogen surveillance in irrigated agriculture.
- **Atmospheric**: airborne eDNA emerging as a method (pollen tracking, microbial aerosols).

**When you see this in a paper**: confirm marker gene, PCR primers, reference database, and field-/lab-contamination controls. Quantitative inferences need explicit calibration; presence-absence inferences are more robust.

**Anchor citations**:
- Ficetola, G. F., Miaud, C., Pompanon, F., & Taberlet, P. (2008). Species detection using environmental DNA from water samples. *Biology Letters*, 4(4), 423–425. doi:10.1098/rsbl.2008.0118
- Deiner, K., et al. (2017). Environmental DNA metabarcoding: Transforming how we survey animal and plant communities. *Molecular Ecology*, 26(21), 5872–5895. doi:10.1111/mec.14350

**Related cards**: `CC-eco-species-diversity`, `MC-eco-PAM`, `TC-09`, `PD-salmon-habitat`

---

## MC-eco-PAM: Passive acoustic monitoring (bioacoustics)

**What it is**: continuous recording of ambient acoustic environments (terrestrial soundscapes, marine bioacoustics) to detect species presence, behavior, and community structure. Terrestrial: AudioMoth, Wildlife Acoustics SM4, etc. Marine: ocean-bottom hydrophones, towed arrays, the broader ARGO floats. Shares signal-processing techniques with seismology — same Fourier-spectral methods, ML pickers, source detection; vocabulary collision warning for "noise" between disciplines (`CC-seismo-noise` vs. soundscape ecology).

**What you can retrieve**:
- Continuous broadband audio recordings; species-specific calls and chorus events; biodiversity indices (acoustic complexity, evenness).
- Whale calls, dolphin clicks, bat echolocation, bird dawn chorus, frog vocalizations, anuran phenology.
- ML pipelines for species-specific detection (BirdNET, Whisperseek-derived systems for marine).
- Shares OBSs with seismology; whale calls have been mined from FDSN seismic data for years.

**Failure modes**:
- Acoustic detection probability falls off with distance and is highly directional (some calls anisotropic).
- Identification often requires call-library matches; absent reference recordings, ID is uncertain.
- Anthropogenic noise (shipping, traffic, wind farms) masks bioacoustic signals; SNR-limited in many environments.
- Bioacoustic vs. seismic noise vocabulary collision: same physical signal channel (acoustic, infrasound) but separate community traditions; cross-discipline integration is incipient.

**Cross-discipline uses**:
- **Seismology**: marine seismic data (e.g., ocean-bottom seismometers in `MC-seismo-broadband`) often contain whale-call signatures usable for marine-mammal monitoring; DAS submarine cables (`MC-seismo-DAS`) capture both seismic and bioacoustic.
- **Atmospheric**: bird and bat migration tracked by both NEXRAD (`MC-atm-NEXRAD`) and PAM; complementary monitoring.
- **Hydrology**: hyporheic-zone aquatic acoustics for stream-ecosystem state characterization (emerging).

**When you see this in a paper**: confirm hardware sensitivity, recording schedule, detection algorithm, and identification reference; the citizen-science boom in PAM (BirdNET, Merlin, etc.) increases coverage but adds heterogeneity in protocol.

**Anchor citations**:
- Sueur, J., & Farina, A. (2015). Ecoacoustics: The ecological investigation and interpretation of environmental sound. *Biosemiotics*, 8(3), 493–502. doi:10.1007/s12304-015-9248-x
- Stowell, D. (2022). Computational bioacoustics with deep learning: A review and roadmap. *PeerJ*, 10, e13152. doi:10.7717/peerj.13152

**Related cards**: `CC-seismo-noise`, `MC-seismo-DAS`, `MC-seismo-broadband`, `MC-eco-eDNA`, `CC-eco-species-diversity`

---

## MC-eco-process-models: Process-based ecosystem models (CLM, ELM, ED2, JULES)

**What it is**: numerical models that simulate ecosystem function (carbon, water, nitrogen cycling; vegetation dynamics) from process-level physiology. CLM (Community Land Model, NCAR; Lawrence et al. 2019); ELM (Energy Exascale Earth System Model land component, DOE); ED2 (Ecosystem Demography 2); JULES (UK Met Office); LPJ-GUESS (Lund-Potsdam-Jena). Distinct from but related to crop models (`MC-ag-crop-models`).

**What you can retrieve**:
- Coupled water-carbon-nitrogen fluxes (GPP, R_eco, NEE, ET, runoff, soil moisture) at 0.1°–1° grid.
- Vegetation dynamics: plant functional types, phenology, succession, mortality.
- Coupled climate-vegetation simulations; CLM in CESM is the operational climate-model land surface.
- Disturbance representation: fire (e.g., FATES in CLM5), harvest, land-use change.

**Failure modes**:
- Equifinality (Beven 2006): multiple parameter sets fit observations equally well.
- Parameter calibration is local; transferring parameters across biomes adds substantial uncertainty.
- Disturbance regimes (fire, beetle, blowdown) are parameterized rather than predicted in most models.
- Coupling among C-N-water cycles is incomplete; nutrient limitation often missing or simplified.

**Cross-discipline uses**:
- **Hydrology**: CLM, ELM, JULES all act as land-surface models in coupled atmosphere-land systems; the integrated forecasts feed `MC-hydro-modeling`.
- **Atmospheric**: terrestrial-carbon feedbacks in climate models depend on these processes; CO₂-fertilization, drought-induced productivity loss, fire-emissions are the major terms.
- **Agricultural sciences**: managed-ecosystem extensions (CLM-Crop, ELM-Crop) couple crop production with broader ecosystem function.

**When you see this in a paper**: confirm model version, configuration, forcing dataset, and calibration period. Multi-model ensembles or model intercomparison (TRENDY) is the working uncertainty estimate.

**Anchor citations**:
- Lawrence, D. M., et al. (2019). The Community Land Model version 5: Description of new features, benchmarking, and impact of forcing uncertainty. *Journal of Advances in Modeling Earth Systems*, 11(12), 4245–4287. doi:10.1029/2018MS001583
- Sitch, S., et al. (2015). Recent trends and drivers of regional sources and sinks of carbon dioxide. *Biogeosciences*, 12(3), 653–679. doi:10.5194/bg-12-653-2015

**Related cards**: `CC-eco-GPP`, `CC-eco-LAI`, `MC-hydro-modeling`, `MC-atm-NWP`, `MC-ag-crop-models`, `TC-05`, `TC-16`

---

## MC-eco-isotopes: Stable and radioactive isotopes for ecology

**What it is**: same toolkit as `MC-hydro-isotopes` (stable H, O, C, N isotopes plus tritium, ¹⁴C, ¹⁵N tracers), applied to ecology: plant-water-source identification (xylem isotopes; `CC-eco-plant-water-source`), trophic-position estimation from δ¹⁵N, food-web reconstruction from compound-specific isotopes, age and provenance of biological material.

**What you can retrieve**:
- Xylem-water δ¹⁸O / δD for plant-water-source attribution.
- Trophic position from δ¹⁵N (each level adds ~3.4‰); δ¹³C identifies C3 vs. C4 photosynthetic pathway and aquatic vs. terrestrial inputs.
- ¹⁴C bomb-spike dating of recent biomass and soil organic carbon turnover.
- Compound-specific isotopes (specific amino acids, fatty acids) for finer food-web resolution.
- Same lab infrastructure as `MC-hydro-isotopes` (IRMS, CRDS).

**Failure modes**:
- Trophic-fractionation factors are species- and tissue-dependent; literature compilations show large variance.
- Sample preservation and tissue choice affect outcomes; protocols must be reported.
- Mixing-model identifiability problems with > 3 sources without bayesian framework + prior information.
- Lab-to-lab inter-calibration matters; the IAEA standards (VSMOW for water, NBS-19 for carbonates, AIR for nitrogen) are the cross-lab anchors.

**Cross-discipline uses**:
- **Hydrology**: shared isotope-method infrastructure; xylem-isotope analyses + soil-water profile = ecohydrologic separation studies (McDonnell 2014 "two water worlds" hypothesis).
- **Geomorphology**: ¹⁴C burial dating of fluvial deposits anchors landscape-evolution chronologies (overlap with `MC-geomorph-cosmogenic`).
- **Atmospheric**: ¹³C / ¹⁴C in atmospheric CO₂ partitioning of carbon-cycle sources.
- **Seismology / inverse problems**: source-attribution framework (`TC-09`) is shared.

**When you see this in a paper**: same caveats as `MC-hydro-isotopes` for sample preservation and lab calibration; additional ecology-specific concern is tissue choice (xylem vs. leaf water gives different signals).

**Anchor citations**:
- Dawson, T. E., Mambelli, S., Plamboeck, A. H., Templer, P. H., & Tu, K. P. (2002). Stable isotopes in plant ecology. *Annual Review of Ecology and Systematics*, 33, 507–559. doi:10.1146/annurev.ecolsys.33.020602.095451
- Post, D. M. (2002). Using stable isotopes to estimate trophic position: Models, methods, and assumptions. *Ecology*, 83(3), 703–718. doi:10.1890/0012-9658(2002)083[0703:USITET]2.0.CO;2

**Related cards**: `MC-hydro-isotopes`, `CC-eco-plant-water-source`, `CC-eco-trophic-flow`, `CC-hydro-recharge`, `TC-09`
