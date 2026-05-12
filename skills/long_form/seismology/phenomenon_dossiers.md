---
discipline: seismology
card_type: phenomenon
schema_version: v3
---

# Seismology — phenomenon dossiers

Each dossier describes one real-world seismological phenomenon with cross-discipline observability. Format follows `docs/card_format_spec.md`.

---

## PD-megathrust: Subduction megathrust earthquakes (Cascadia, Japan, Chile)

**Setting**: convergent plate boundaries where the down-going slab is locked against the overriding plate; recurrence centuries to millennia; magnitudes Mw 8.0–9.5. Cascadia (PNW): last full-margin event 26 January 1700, Mw ~9, with paleoseismic recurrence ~500 yr (Atwater 1987; Goldfinger et al. 2012).

**Mechanism (5-step chain)**:
1. **(Geodynamics + seismology)** Tectonic plate convergence loads the locked interface; geodetic surface deformation records strain accumulation (GPS, InSAR).
2. **(Seismology)** Interseismic period punctuated by slow slip events (SSEs) and tremor — `PD-slow-slip` — that release some strain aseismically on the deeper plate interface.
3. **(Seismology)** Coseismic rupture: typically nucleates at depth, propagates updip with rupture velocity 0.7–0.9 Vs over 100s–1,000s of km; durations 1–10 min for the largest.
4. **(Hydrology + geomorph)** Coastal subsidence (offshore) or uplift (onshore); ghost forests (Atwater 1987) record sudden submergence of coastal terrain.
5. **(Atmospheric + seismology)** Tsunami generation, infrasound/ionospheric coupling at largest magnitudes.

**Observables per discipline**:
- **Seismology**: regional broadband (PNSN), offshore OBSs, increasing DAS coverage; teleseismic for source inversion (`CC-seismo-source`).
- **Geodesy**: continuous GPS (PBO/EarthScope GAGE), InSAR for both inter- and coseismic deformation.
- **Hydrology**: well-water-level oscillations from passing surface waves; postseismic streamflow anomalies (`PD-eq-hydro-coupling`).
- **Geotechnical engineering**: ground motion intensity (PGA, PGV, duration) used in seismic hazard assessments (Cascadia Subduction Zone scenarios; FEMA P-1000).
- **Geomorph + paleoseismology**: turbidite stratigraphy (Goldfinger), coastal stratigraphy (Atwater), tsunami deposits.
- **Atmospheric / space**: ionospheric perturbations from 2011 Tōhoku and 2004 Sumatra (Heki 2011; Astafyeva 2019 review).

**Open questions for translator-agent integration**:
- Cascadia early-warning latency depends on offshore instrumentation density (OOI Regional Cabled Array; planned Strait of Juan de Fuca cabled extensions). DAS along submarine telecom cables (`MC-seismo-DAS`) is a transformative possibility.
- Megathrust rupture variability and "supercycles" remain incompletely understood; paleoseismology provides ground truth.
- The role of fluid pressure on the megathrust (`TC-02`) in modulating slip behavior is a frontier area.

**Anchor papers (retrieve for any megathrust query)**:
- Atwater, B. F. (1987). Evidence for great Holocene earthquakes along the outer coast of Washington State. *Science*, 236(4804), 942–944. doi:10.1126/science.236.4804.942
- Wang, K., Wells, R., Mazzotti, S., Hyndman, R. D., & Sagiya, T. (2003). A revised dislocation model of interseismic deformation of the Cascadia subduction zone. *Journal of Geophysical Research: Solid Earth*, 108(B1), 2026. doi:10.1029/2001JB001227
- Goldfinger, C., et al. (2012). Turbidite event history—Methods and implications for Holocene paleoseismicity of the Cascadia subduction zone. *USGS Professional Paper*, 1661-F. https://pubs.usgs.gov/pp/pp1661f/
- Heki, K. (2011). Ionospheric electron enhancement preceding the 2011 Tohoku-Oki earthquake. *Geophysical Research Letters*, 38(17), L17312. doi:10.1029/2011GL047908

**Related cards**: `CC-seismo-magnitude`, `CC-seismo-source`, `CC-seismo-stress`, `PD-slow-slip`, `PD-eq-hydro-coupling`, `PD-liquefaction`

---

## PD-liquefaction: Earthquake-induced liquefaction

**Setting**: cohesionless, saturated, loose-to-medium-dense sediments under cyclic loading. Critical for the U.S. Pacific Northwest: the 28 February 2001 Mw 6.8 Nisqually earthquake (Olympia, WA) produced widespread liquefaction in fill and alluvial deposits and is the Denolle Group's anchor case for the digital twin / NVIDIA pitch effort. Canonical events: Niigata 1964, Christchurch 2010–2011, Tōhoku 2011, Palu 2018.

**Mechanism (3-step chain)**:
1. **(Geotech + hydro)** Saturated sand has loose granular packing with positive σ' supporting the matrix.
2. **(Seismology + geotech)** Cyclic shear from S-wave arrivals causes incremental volumetric strain in undrained conditions; pore pressure rises; σ' = σ − p falls toward zero.
3. **(Geotech)** When σ' → 0 the soil loses shear strength; the medium behaves as a viscous fluid until pore pressure dissipates. Surface manifestations: sand boils, ground oscillation, lateral spreads, building tilt.

**Observables per discipline**:
- **Seismology**: ground motion intensity (PGA, PGV, duration). Modern shaking-intensity products (ShakeMap; Wald et al. 1999) drive liquefaction-hazard models.
- **Geotechnical engineering**: cyclic stress ratio (CSR) vs. cyclic resistance ratio (CRR) framework (Seed & Idriss 1971; Boulanger & Idriss 2014). CPT- and Vs-based liquefaction triggering curves.
- **Hydrology**: pore-pressure piezometers (rare in advance; lab settings primarily). Post-event observations of water-table changes, sand-boil ejecta.
- **Geomorphology**: liquefaction inventories (sand boils, lateral spreads); satellite InSAR for subsidence.
- **Near-surface geophysics**: Vs depth profiles (`CC-seismo-Vs`, `MC-seismo-MASW`) feed liquefaction susceptibility maps.

**Open questions for translator-agent integration**:
- High-resolution liquefaction susceptibility mapping from joint Vs + groundwater-table observations is an active area; the Nisqually digital twin is one example.
- Machine-learning liquefaction triggering models (Geyin & Maurer 2020) push beyond Seed-Idriss but need uncertainty quantification.
- DAS-based monitoring of liquefaction onset in real time is emerging (Spica et al. 2020 along submarine fiber, by analog).

**Anchor papers**:
- Seed, H. B., & Idriss, I. M. (1971). Simplified procedure for evaluating soil liquefaction potential. *Journal of the Soil Mechanics and Foundations Division (ASCE)*, 97(9), 1249–1273. doi:10.1061/JSFEAQ.0001662
- Boulanger, R. W., & Idriss, I. M. (2014). CPT and SPT based liquefaction triggering procedures. *Center for Geotechnical Modeling Report*, UCD/CGM-14/01, University of California, Davis.
- Wald, D. J., Quitoriano, V., Heaton, T. H., Kanamori, H., Scrivner, C. W., & Worden, C. B. (1999). TriNet "ShakeMaps": Rapid generation of peak ground motion and intensity maps for earthquakes in southern California. *Earthquake Spectra*, 15(3), 537–555. doi:10.1193/1.1586057

**Related cards**: `CC-seismo-Vs`, `CC-seismo-stress`, `CC-hydro-p`, `CC-geotech-MohrCoulomb`, `TC-02`, `MC-seismo-MASW`, `PD-megathrust`

---

## PD-slow-slip: Slow slip events and tectonic tremor

**Setting**: deep plate interfaces at subduction zones (Cascadia, Mexico, Japan, New Zealand) and along some transform faults. SSEs release seismic moment equivalent to Mw 6–7 events but over days to weeks, with no significant high-frequency radiation. Accompanied by tectonic tremor, a quasi-continuous low-amplitude signal at 1–10 Hz. Cascadia ETS (Episodic Tremor and Slip) has a ~14-month cycle.

**Mechanism**:
1. **(Geodynamics + seismology)** Down-dip extension of the locked seismogenic zone, in the transition region toward freely-creeping deeper slab.
2. **(Seismology)** Slow rupture with anomalously low rupture velocity (km/day rather than km/s), generating low-frequency earthquakes (LFEs) and tremor; constitutive behavior intermediate between stable sliding and stick-slip.
3. **(Geodesy)** GPS records ~mm-scale reversal in steady tectonic motion lasting weeks.

**Observables per discipline**:
- **Seismology**: tremor catalogs (PNSN automated detections, ML-augmented; `MC-seismo-ML`); LFE template matching.
- **Geodesy**: continuous GPS (PBO/EarthScope), occasionally creep meters.
- **Hydrology**: subtle pore-pressure modulation predicted but observationally challenging.
- **Geomorphology**: long-term deformation accommodated partly by SSEs vs. coseismic slip; relevant for fault-scarp budgets.

**Open questions for translator-agent integration**:
- Does the timing of ETS events influence the probability of megathrust nucleation (the "loading" question)? Statistical evidence is suggestive but inconclusive.
- Do fluid pressures (`TC-02`) on the deep interface modulate SSE recurrence? Geological/geochemical signatures are debated.
- ML-augmented LFE catalogs are revealing finer time structure; new statistics on SSE physics are emerging.

**Anchor papers**:
- Rogers, G., & Dragert, H. (2003). Episodic tremor and slip on the Cascadia subduction zone: The chatter of silent slip. *Science*, 300(5627), 1942–1943. doi:10.1126/science.1084783
- Beroza, G. C., & Ide, S. (2011). Slow earthquakes and nonvolcanic tremor. *Annual Review of Earth and Planetary Sciences*, 39, 271–296. doi:10.1146/annurev-earth-040809-152531
- Bürgmann, R. (2018). The geophysics, geology and mechanics of slow fault slip. *Earth and Planetary Science Letters*, 495, 112–134. doi:10.1016/j.epsl.2018.04.062

**Related cards**: `CC-seismo-source`, `CC-seismo-magnitude`, `PD-megathrust`

---

## PD-volcanic-seismicity: Volcanic earthquakes and eruption forecasting

**Setting**: volcanoes worldwide; canonical PNW: Mount St. Helens (1980 explosion, 2004–2008 dome-building), Mount Rainier (Denolle Group focus, ongoing monitoring), Mount Hood, Glacier Peak. Mt. Rainier is the highest-priority Cascade volcano due to its proximity to dense population and the lahar hazard.

**Mechanism (typology by signal class)**:
1. **(Seismology)** Volcano-tectonic (VT) earthquakes: small brittle-failure events from stress changes in the edifice; sharp-onset, broadband signals.
2. **(Seismology + fluid mechanics)** Long-period (LP) events (Chouet 1996): resonance of fluid-filled cracks; narrowband signals at 0.5–5 Hz.
3. **(Seismology)** Volcanic tremor: continuous quasi-harmonic signals from sustained magma/fluid flow.
4. **(Seismology + thermodynamics)** Pre-eruption acceleration of seismicity rate (Voight 1988 framework); dv/v changes (`CC-seismo-dvv`) detectable weeks to months in advance at some volcanoes (Brenguier et al. 2008b).

**Observables per discipline**:
- **Seismology**: dense local arrays; PNSN station coverage for Cascade volcanoes; dv/v monitoring from ambient noise (`MC-seismo-ambient-noise`).
- **Atmospheric sciences**: gas emissions (SO₂ via DOAS, FTIR), thermal anomalies from satellite IR, ash-plume tracking.
- **Geodesy**: InSAR and continuous GPS for edifice deformation.
- **Hydrology**: groundwater chemistry changes (Na, Cl, isotopes), heat flux to overlying glaciers, glacial lake drainage events.
- **Geomorphology**: lahar inundation mapping, debris-flow modeling (D-Claw, RAMMS); historical lahar deposits at Mt. Rainier (the Osceola Mudflow, ~5,600 yr BP, reached Puget Sound).

**Open questions for translator-agent integration**:
- Integration of seismology + gas + deformation + dv/v into a multi-sensor eruption-forecasting framework remains an open synthesis (the Denolle Group's digital twin direction).
- Glacier-lahar coupling: how do eruption-induced heating and glacial-lake stability propagate to downstream hazard? Direct hydro-geomorph-seismo translation problem.
- DAS along urban or telecom fibers could densely supplement the Cascades sparse monitoring (Mt. Hood/Rainier slopes).

**Anchor papers**:
- Chouet, B. (1996). Long-period volcano seismicity: Its source and use in eruption forecasting. *Nature*, 380(6572), 309–316. doi:10.1038/380309a0
- McNutt, S. R. (2005). Volcanic seismology. *Annual Review of Earth and Planetary Sciences*, 33, 461–491. doi:10.1146/annurev.earth.33.092203.122459
- Brenguier, F., Shapiro, N. M., Campillo, M., Ferrazzini, V., Duputel, Z., Coutant, O., & Nercessian, A. (2008b). Towards forecasting volcanic eruptions using seismic noise. *Nature Geoscience*, 1(2), 126–130. doi:10.1038/ngeo104

**Related cards**: `CC-seismo-dvv`, `CC-seismo-noise`, `MC-seismo-ambient-noise`, `MC-seismo-broadband`

---

## PD-microseism: Secondary microseism and oceanic coupling

**Setting**: global background signal between ~5–10 s period (0.1–0.2 Hz), generated by ocean-wave-wave interactions in deep water. Dominates the ambient seismic field everywhere on Earth. Modulated by storms, seasonal wave climate, and ocean basin geometry.

**Mechanism**:
1. **(Oceanography + atmospheric sciences)** Wind-driven ocean waves; opposing wave groups produce standing-wave components with twice the fundamental wave frequency.
2. **(Atmospheric science → ocean → solid Earth)** The standing-wave component creates a non-attenuating pressure forcing on the seabed (Longuet-Higgins 1950 mechanism).
3. **(Seismology)** Pressure forcing excites compressional and surface waves that propagate globally. Primary microseism (~14–20 s, 0.05–0.07 Hz) is direct coastal coupling.

**Observables per discipline**:
- **Seismology**: continuous broadband; back-projection localizes sources to storm regions (e.g., North Pacific in NH winter, Southern Ocean in SH winter).
- **Atmospheric sciences**: storm tracks correlate with microseism intensity; the seismic record provides an independent climate proxy.
- **Oceanography**: microseism PSD is a continuous proxy for offshore significant wave height; pre-instrumental wave climates have been reconstructed from historic seismograms.
- **Hydrology / glaciology**: oceanic forcing imprinted on local broadband stations modulates noise-correlation Green's-function recovery; tracking this is necessary for hydrology-relevant dv/v measurements.

**Open questions for translator-agent integration**:
- Microseism PSD as a long-term climate change signal: significant-wave-height intensification has been argued from seismic records.
- Use of microseisms (and ocean tides) as the noise field for time-lapse dv/v studies in hydrology; the source distribution affects accuracy and is itself climatic.

**Anchor papers**:
- Longuet-Higgins, M. S. (1950). A theory of the origin of microseisms. *Phil. Trans. R. Soc. Lond. A*, 243(857), 1–35. doi:10.1098/rsta.1950.0012
- Ardhuin, F., Stutzmann, E., Schimmel, M., & Mangeney, A. (2011). Ocean wave sources of seismic noise. *Journal of Geophysical Research: Oceans*, 116(C9), C09004. doi:10.1029/2011JC006952
- McNamara, D. E., & Buland, R. P. (2004). doi:10.1785/012003001

**Related cards**: `CC-seismo-noise`, `MC-seismo-ambient-noise`, `CC-seismo-dvv`
