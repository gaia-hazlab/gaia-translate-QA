---
discipline: seismology
card_type: method
schema_version: v3
---

# Seismology — method cards

Each card describes one measurement technique, instrument, or dataset relevant to seismology, with what it measures, resolution, failure modes, and cross-discipline reuse. Format follows `docs/card_format_spec.md`.

---

## MC-seismo-broadband: Broadband seismometers and global/regional networks

**What it is**: three-component velocity sensors with flat response across seismological bands of interest (typically 0.01–360 s). Workhorse sensor types: Streckeisen STS-1/STS-2, Nanometrics Trillium 120/240/360, Güralp CMG-3T/3ESPC. Networks: Global Seismographic Network (GSN, IRIS/USGS), USArray, Advanced National Seismic System (ANSS), national networks (PNSN, NCSN, SCSN in the US Pacific).

**What you can retrieve**:
- Continuous three-component ground velocity in counts → m/s via instrument response.
- Standard data formats: miniSEED, ASDF, SAC.
- FDSN web services for waveforms, station metadata, event catalogs.
- ObsPy (Beyreuther et al. 2010) is the Python standard; SeisIO.jl for Julia.
- Data center: EarthScope (formed 2023 by IRIS-UNAVCO merger), serving via ds.iris.edu and earthscope.org.

**Failure modes**:
- Mass-position drift and tilt sensitivity (long-period quality loss).
- Ocean-bottom installations (OBS): noisy due to swell, currents, biological scratching.
- Thermal noise in shallow vault installations.
- Some networks have aliasing or timing problems at older or undermaintained stations.
- Spatial bias: dense in seismically-active developed regions, sparse in cratons, oceans, polar regions.

**Cross-discipline uses**:
- **Hydrology**: continuous broadband records detect responses to atmospheric and hydrologic loading (Johnson, Fu & Bürgmann 2017 framework); high-frequency noise correlates with streamflow (Burtin et al. 2008).
- **Atmospheric sciences**: large storms imprint on microseism intensity; volcanic plumes and explosions are recorded in infrasound co-sited with seismic.
- **Geomorphology**: shallow-landslide signals, glacier dynamics, rockfalls.
- **Near-surface geophysics**: regional broadband data feed ambient-noise tomography at near-surface resolutions.

**When you see this in a paper**: confirm (1) instrument type and response correction method, (2) sample rate, (3) data center and DOI for the network. PNSN and ANSS data are routinely DOI-citable via EarthScope; explicit DOIs are increasingly expected.

**Anchor citations**:
- Beyreuther, M., et al. (2010). ObsPy: A Python toolbox for seismology. *Seismological Research Letters*, 81(3), 530–533. doi:10.1785/gssrl.81.3.530
- Ringler, A. T., Anthony, R. E., Aster, R. C., Hutt, C. R., & Pearce, J. (2020). Accurate characterization of seismometer response and applications to seismology. *Annual Review of Earth and Planetary Sciences*, 48, 449–475. doi:10.1146/annurev-earth-053018-060102

**Related cards**: `MC-seismo-DAS`, `MC-seismo-ambient-noise`, `CC-seismo-noise`

---

## MC-seismo-DAS: Distributed acoustic sensing (DAS)

**What it is**: laser-interferometric measurement of axial strain along an optical fiber, sampling at meter-scale spacing over kilometers of cable. Each meter of fiber becomes a quasi-seismic channel; arrays of 10,000+ channels are routine. Pioneering installations: Stanford DAS-1 (Ajo-Franklin et al. 2019), Sacramento Basin (Lindsey et al. 2017), Mt. Etna (Currenti et al. 2021).

**What you can retrieve**:
- Continuous axial strain rate, convertible to particle velocity for incident-wave directions near-parallel to the cable.
- Channel spacing 1–10 m; gauge length typically 2–10 m.
- Sample rates up to kHz.
- Deployments: dark telecom fiber (city/regional scale), dedicated cables (focused studies), borehole DAS, submarine DAS.
- Data is large: a 10-km, 1-m, 1-kHz array produces ~1 TB/day at single precision.

**Failure modes**:
- Directional sensitivity: fiber records axial strain only; orthogonal motion is invisible at first order.
- Cable coupling: poorly coupled cables (loose conduit, dry soil) are noisy; well-cemented borehole or trench-buried cables are quietest.
- Phase unwrapping and noise floor are interrogator-dependent (Silixa iDAS, OptaSense ODH, Febus A1).
- Processing pipelines are not yet standardized; reproducibility across labs is an ongoing concern.

**Cross-discipline uses**:
- **Hydrology**: DAS can monitor water-table changes via velocity changes (`TC-03`); densely samples earthquake-water-level coupling in real time.
- **Near-surface geophysics**: continuous passive imaging at unprecedented spatial density.
- **Geotechnical engineering**: foundation health monitoring; the Denolle Group's AEI SubSonic product applies DAS to subsurface infrastructure monitoring.
- **Ecology / biology**: low-frequency DAS captures whale calls (deep-ocean fibers), elephant footsteps, biological activity adjacent to cables.
- **Atmospheric sciences**: ionospheric perturbations from large earthquakes detectable on long DAS lines.

**When you see this in a paper**: check (1) interrogator type and gauge length, (2) coupling method, (3) processing pipeline (often not open-source), (4) whether velocity conversion has been performed correctly for the wave-direction-to-fiber geometry.

**Anchor citations**:
- Zhan, Z. (2020). Distributed acoustic sensing turns fiber-optic cables into sensitive seismic antennas. *Annual Review of Earth and Planetary Sciences*, 48, 415–438. Note: see also Lindsey & Martin (2021) below.
- Lindsey, N. J., & Martin, E. R. (2021). Fiber-optic seismology. *Annual Review of Earth and Planetary Sciences*, 49, 309–336. doi:10.1146/annurev-earth-072420-065213
- Ajo-Franklin, J. B., et al. (2019). Distributed acoustic sensing using dark fiber for near-surface characterization and broadband seismic event detection. *Scientific Reports*, 9, 1328. doi:10.1038/s41598-018-36675-8

**Related cards**: `MC-seismo-broadband`, `MC-seismo-ambient-noise`, `CC-seismo-dvv`, `PD-liquefaction`

---

## MC-seismo-ambient-noise: Ambient-noise cross-correlation and interferometry

**What it is**: cross-correlation of long time series of ambient seismic noise between station pairs converges (under ideal source-distribution conditions) to the empirical Green's function between the two stations. Once mature only for surface waves, the method now routinely retrieves body waves and is the basis of time-lapse monitoring via dv/v (`CC-seismo-dvv`).

**What you can retrieve**:
- Surface-wave dispersion (group and phase velocity vs. period) between station pairs.
- 2D phase-velocity maps; 3D shear-velocity models via dispersion inversion (Shapiro et al. 2005).
- Time-lapse dv/v at the station-pair or station-coda level.
- Standardized software: MSNoise (Lecocq et al. 2014), NoisePy (Jiang & Denolle 2020 — Denolle Group), SeisNoise.jl.

**Failure modes**:
- Source distribution non-uniformity: ocean-storm-dominated noise yields directional bias in Green's-function recovery.
- Earthquake contamination: large transient events must be removed by spectral whitening, time-domain normalization, or noise-only segment selection.
- Frequency band trade-offs: long periods (10–30 s) sample deep; short periods (0.5–5 s) sample upper crust. Coda-wave dv/v extracts complementary information.
- Phase-velocity inversion to Vs has tomographic non-uniqueness; assumed parametrization matters.

**Cross-discipline uses**:
- **Hydrology**: dv/v ↔ groundwater storage / soil moisture (`TC-03`); shallow-aquifer monitoring with surface-station arrays.
- **Near-surface geophysics**: noise-correlation tomography supplants traditional active-source surveys for many imaging targets.
- **Geotechnical engineering**: Vs depth profile from dispersion is the primary input for site-response analysis (`PD-liquefaction`).
- **Volcanology / glaciology**: pre-eruption dv/v changes (Brenguier et al. 2008b Piton de la Fournaise), englacial monitoring.

**When you see this in a paper**: confirm (1) the noise-preprocessing chain (one-bit normalization vs. spectral whitening vs. RMS), (2) the assumed source distribution, (3) the dispersion-picking method, (4) for dv/v studies, whether thermoelastic and hydrologic effects have been separated.

**Anchor citations**:
- Shapiro, N. M., Campillo, M., Stehly, L., & Ritzwoller, M. H. (2005). High-resolution surface-wave tomography from ambient seismic noise. *Science*, 307(5715), 1615–1618. doi:10.1126/science.1108339
- Bensen, G. D., et al. (2007). Processing seismic ambient noise data to obtain reliable broad-band surface wave dispersion measurements. *Geophysical Journal International*, 169(3), 1239–1260. doi:10.1111/j.1365-246X.2007.03374.x
- Jiang, C., & Denolle, M. A. (2020). NoisePy: A new high-performance Python tool for ambient-noise seismology. *Seismological Research Letters*, 91(3), 1853–1866. doi:10.1785/0220190364

**Related cards**: `MC-seismo-MASW`, `MC-seismo-tomography`, `CC-seismo-dvv`, `TC-03`

---

## MC-seismo-MASW: Multichannel analysis of surface waves (and SASW, ReMi)

**What it is**: surface-wave method that uses an active or passive source and a linear receiver array to extract the dispersion curve (phase velocity vs. frequency) of Rayleigh (or Love) waves, then inverts the dispersion for a 1D Vs depth profile beneath the array.

**What you can retrieve**:
- 1D Vs(z) profile to ~30–50 m depth for typical active-source MASW; deeper with passive (ReMi, Refraction Microtremor) or hybrid methods.
- Vs30 directly, for site-classification purposes.
- 2D pseudosection by rolling the array; nearly 3D with crossed lines.
- Software: SurfSeis (Kansas Geological Survey), Geopsy, dispersion tools in ObsPy/MSNoise.

**Failure modes**:
- Higher-mode contamination at high frequencies leads to systematic Vs underestimation if interpreted as fundamental mode.
- Lateral heterogeneity violates the 1D inversion assumption; 2D effects require array-tomography approaches.
- Inversion non-uniqueness: multiple Vs(z) profiles can match a single dispersion curve at acceptable misfit.
- Limited deep resolution (you can't resolve below ~ array length / 2).

**Cross-discipline uses**:
- **Near-surface geophysics**: MASW is fundamentally a near-surface-geophysics tool; seismology and NSG share the technique.
- **Geotechnical engineering**: primary field method for Vs30 site-response characterization; required by most modern seismic-design codes.
- **Hydrology**: MASW can detect the water table (saturation increases Vs by 5–15%), providing a passive characterization tool.
- **Archeology / forensics**: MASW used to image buried features in soft sediments.

**When you see this in a paper**: confirm (1) source type (sledgehammer, weight drop, vibroseis, passive), (2) array length and geometry, (3) whether higher modes have been considered, (4) inversion regularization and starting model assumptions.

**Anchor citations**:
- Park, C. B., Miller, R. D., & Xia, J. (1999). Multichannel analysis of surface waves. *Geophysics*, 64(3), 800–808. doi:10.1190/1.1444590
- Foti, S., et al. (2018). Guidelines for the good practice of surface wave analysis: a product of the InterPACIFIC project. *Bulletin of Earthquake Engineering*, 16(6), 2367–2420. doi:10.1007/s10518-017-0206-7

**Related cards**: `MC-seismo-ambient-noise`, `MC-seismo-tomography`, `CC-seismo-Vs`, `PD-liquefaction`

---

## MC-seismo-tomography: Seismic tomography (body wave, surface wave, full-waveform)

**What it is**: iterative inversion of seismic observables (travel times, dispersion curves, full waveforms) for 3D models of subsurface elastic properties (Vp, Vs, density, anisotropy, attenuation).

**What you can retrieve**:
- Body-wave tomography: 3D Vp and Vp/Vs from teleseismic and regional travel-time data; resolution ~10–100 km depending on station density and event distribution.
- Surface-wave tomography: phase- and group-velocity maps inverted to 3D Vs; sensitive 5–200 km depth.
- Full-waveform inversion (FWI): direct waveform matching for kilometer-scale resolution at exploration scales and increasingly at regional scales.
- Ambient-noise tomography (combined with `MC-seismo-ambient-noise`): well-suited to areas lacking earthquakes.

**Failure modes**:
- Resolution non-uniformity: well-illuminated regions (dense station coverage and crossing ray paths) are sharply resolved; the rest is smeared.
- Damping/regularization choices dictate apparent feature amplitude and continuity; the "preferred model" is a regularization-and-data combination.
- Linearization assumption fails for strong velocity contrasts; iterative non-linear methods (FWI) are computationally expensive and sensitive to starting models.
- Synthetic resolution tests (checkerboards) characterize *recoverability of a specific feature pattern*, not absolute resolution.

**Cross-discipline uses**:
- **Hydrology**: subsurface structure (basin geometry, basement depth, fracture zones) constrains aquifer architecture.
- **Geotechnical engineering**: deep basin tomography reveals 3D site-amplification structure that 1D Vs30 misses entirely.
- **Near-surface geophysics**: complementary to ERT, GPR for hydrostratigraphy. Joint geophysical inversion (`TC-08`) couples the methods explicitly.
- **Geodynamics**: mantle tomography reveals subduction-zone geometry, plumes, and craton roots.

**When you see this in a paper**: examine (1) the model regularization scheme, (2) resolution tests with realistic noise, (3) whether reported features exceed the resolution scale and amplitude established by tests, (4) data weighting and outlier handling.

**Anchor citations**:
- Virieux, J., & Operto, S. (2009). An overview of full-waveform inversion in exploration geophysics. *Geophysics*, 74(6), WCC1–WCC26. doi:10.1190/1.3238367
- Romanowicz, B. (2003). Global mantle tomography: Progress status in the past 10 years. *Annual Review of Earth and Planetary Sciences*, 31, 303–328. doi:10.1146/annurev.earth.31.091602.113555

**Related cards**: `MC-seismo-ambient-noise`, `MC-seismo-MASW`, `MC-nsg-ERT`, `TC-08`

---

## MC-seismo-ML: Machine-learning earthquake catalogs (PhaseNet, EQTransformer)

**What it is**: deep-learning pickers and associators that detect, identify, locate, and characterize earthquakes from continuous waveforms. Trained on millions of labeled examples from existing catalogs (STEAD, Mousavi et al. 2019). Outputs are picks (P, S arrival times with uncertainty) and event associations; downstream tasks include magnitude estimation, focal mechanism, and de-noising.

**What you can retrieve**:
- 10–100× more events than conventional analyst or STA/LTA pipelines, especially below Mc ≈ 1.5.
- Picks with statistical uncertainty enabling downstream uncertainty propagation.
- Standard models: PhaseNet (Zhu & Beroza 2019), EQTransformer (Mousavi et al. 2020), GaMMA association (Zhu et al. 2022), DeepDenoiser.
- Production pipelines: EarthScope is integrating ML pickers; SCEDC and PNSN have ML-augmented catalogs in deployment.

**Failure modes**:
- Training-data bias: models trained on California catalogs may underperform in Cascadia, mid-continent, or subduction-zone settings.
- False positives in noisy environments (cities, near coastlines); explicit station-noise modeling helps.
- Magnitude estimation from ML-detected events is non-trivial and often a separate model.
- Pickers do not solve waveform calibration; if the data is wrong, the catalog is wrong.
- Reproducibility: model versions matter; results are tied to specific weights.

**Cross-discipline uses**:
- **Hydrology**: 10× more complete induced-seismicity catalogs (`PD-induced-seismicity`) enable better r²/t pressure-diffusion fits and tighter triggering-rate quantification.
- **Geotechnical engineering**: dense microseismicity maps near critical infrastructure (dams, wells) for monitoring.
- **Volcanology**: pre-eruption microseismicity tracked at lower Mc gives earlier and more confident eruption forecasts.
- **Denolle Group**: this is an active research area for the group; the cloud-native pipeline development at UW directly produces these catalogs.

**When you see this in a paper**: confirm (1) which model and version, (2) training-data domain shift to the study region, (3) Mc evaluation (the catalog's claimed completeness must be tested by Gutenberg-Richter fit), (4) location method (NonLinLoc, hypoinverse, etc.) and its uncertainties.

**Anchor citations**:
- Zhu, W., & Beroza, G. C. (2019). PhaseNet: A deep-neural-network-based seismic arrival-time picking method. *Geophysical Journal International*, 216(1), 261–273. doi:10.1093/gji/ggy423
- Mousavi, S. M., Sheng, Y., Zhu, W., & Beroza, G. C. (2019). STanford EArthquake Dataset (STEAD): A global data set of seismic signals for AI. *IEEE Access*, 7, 179464–179476. doi:10.1109/ACCESS.2019.2947848
- Mousavi, S. M., Ellsworth, W. L., Zhu, W., Chuang, L. Y., & Beroza, G. C. (2020). Earthquake transformer—an attentive deep-learning model for simultaneous earthquake detection and phase picking. *Nature Communications*, 11, 3952. doi:10.1038/s41467-020-17591-w

**Related cards**: `MC-seismo-broadband`, `MC-seismo-DAS`, `CC-seismo-magnitude`, `CC-seismo-GR`, `PD-induced-seismicity`

---

## MC-seismo-EarthScope: EarthScope/IRIS DMC and FDSN data services

**What it is**: the data infrastructure backbone of academic seismology. EarthScope (formed 2023 by the merger of IRIS and UNAVCO) operates the U.S. national seismic data archive and the GAGE Facility for geodesy. Other FDSN (Federation of Digital Seismograph Networks) data centers serve regional networks worldwide (GFZ, INGV, BGR, ORFEUS, GeoNet, etc.).

**What you can retrieve**:
- Continuous waveforms and event-windowed records from public networks.
- Station metadata (instrument response, channel inventory) as StationXML.
- Earthquake catalogs from QuakeML feeds.
- Standard access via FDSN web services (fdsnws-dataselect, fdsnws-station, fdsnws-event).
- Python via ObsPy clients; command line via mseedindex / robust-by-design infrastructure.

**Failure modes**:
- Historical data quality varies: pre-2000 records often have instrument-response issues or timing errors.
- Restricted-access networks require permission and proper acknowledgment.
- DOIs for networks and individual events are increasingly available but still inconsistent across providers.

**Cross-discipline uses**:
- All cross-discipline uses of seismology data flow through this infrastructure. Especially relevant:
  - **Hydrology** + **agricultural sciences**: for induced-seismicity studies in heavily-pumped basins (Oklahoma, Central Valley).
  - **Ecology / biology**: ocean-bottom seismometer recordings contain whale calls and biological choruses; FDSN data has been mined for ecoacoustics.
  - **Atmospheric sciences**: bolide events, thunderstorm signals, infrasound co-sited with seismic.

**When you see this in a paper**: every seismology study should cite the network DOIs (e.g., the IU network is 10.7914/SN/IU). Increasingly required by journals. Reproducibility hinges on the FDSN client + request specification.

**Anchor citations**:
- Hutko, A. R., Bahavar, M., Trabant, C., Weekly, R. T., Van Fossen, M., & Ahern, T. (2017). Data products at the IRIS-DMC: Growth and usage. *Seismological Research Letters*, 88(3), 892–903. doi:10.1785/0220160190
- Trabant, C., et al. (2012). Data products at the IRIS DMC: Stepping stones for research and other applications. *Seismological Research Letters*, 83(5), 846–854. doi:10.1785/0220120032

**Related cards**: `MC-seismo-broadband`, `MC-seismo-ambient-noise`, `MC-seismo-ML`
