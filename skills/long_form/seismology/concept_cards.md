---
discipline: seismology
card_type: concept
schema_version: v3
---

# Seismology — concept cards

Each card defines one core seismological variable, equation, or measured quantity, with units, numerical ranges, and explicit hooks into the other Gaia disciplines. Format follows `docs/card_format_spec.md`.

---

## CC-seismo-stress: Fault stress σ_n, τ, and stress drop Δσ [Pa, MPa]

**Quantity**: stress is a second-order tensor (9 components, 6 independent). On a fault plane, the resolved normal stress σ_n and shear stress τ control failure. Stress drop Δσ = τ_initial − τ_final is the change during slip. SI units Pa; conventionally MPa for crustal-fault quantities (1 MPa = 10 bar).

**Defining relation**: Coulomb failure criterion τ ≥ μ(σ_n − p) + c (where p is pore pressure, c is cohesion). Static stress changes from neighboring earthquakes propagate via the ΔCFS = Δτ + μ' Δσ_n field (King, Stein & Lin 1994).

**Typical ranges**:
- Lithostatic σ_v ≈ 25 MPa/km depth.
- Effective σ'_v on saturated rock ≈ 15 MPa/km (hydrostatic).
- Tectonic stress drop Δσ for crustal earthquakes: 1–10 MPa (Allmann & Shearer 2009); essentially scale-invariant from M3 to M8.
- Subduction interface Δσ: typically 1–5 MPa.
- b-value-inferred differential stress varies regionally.

**Cross-discipline equivalents**:
- **Hydrology**: pore pressure p modifies σ_n via Terzaghi-Biot effective stress. See `CC-hydro-p`, `TC-02`.
- **Geotechnical engineering**: Mohr-Coulomb on a fault plane is the same equation as on a soil slip surface. See `CC-geotech-MohrCoulomb`.
- **Geomorphology**: stress-field orientation governs fault scarp orientation and joint patterns; controls Iverson (2000) hillslope FS via σ'.

**When you see this in a paper**: confirm static vs. dynamic, ambient vs. coseismic, and whether σ' or σ (total) is being used. "Stress" without qualifier means total stress; "effective stress" is unambiguous.

**Anchor citations**:
- Byerlee, J. (1978). Friction of rocks. *Pure and Applied Geophysics*, 116(4), 615–626. doi:10.1007/BF00876528
- King, G. C. P., Stein, R. S., & Lin, J. (1994). Static stress changes and the triggering of earthquakes. *Bull. Seismol. Soc. Am.*, 84(3), 935–953.
- Allmann, B. P., & Shearer, P. M. (2009). Global variations of stress drop for moderate to large earthquakes. *Journal of Geophysical Research: Solid Earth*, 114(B1), B01310. doi:10.1029/2008JB005821

**Related cards**: `CC-hydro-p`, `CC-geotech-MohrCoulomb`, `TC-02`, `PD-induced-seismicity`

---

## CC-seismo-Vs: Shear-wave velocity Vs and Vs30 [m/s]

**Quantity**: shear-wave (S-wave) propagation velocity — one physical field, sampled by four geoscience subfields at incompatible depth and resolution regimes (see `TC-12`). Vs30 is the time-averaged Vs in the upper 30 m, the canonical site-response parameter; it is a derived top-of-stack quantity over the geotechnical / shallow-NSG depth window, not a separate physical concept. Vs depends strongly on rigidity, density, water saturation, and fracture state.

**Defining relation**: Vs = √(μ/ρ), where μ is shear modulus and ρ is density. From the seismic-wave equation; first-order quantity for elastic-wave propagation. The relation is linear-elastic and small-strain (γ < ≈ 10⁻⁴); at engineering ground-motion strains, the effective shear modulus degrades along `CC-geotech-G-Gmax`(γ) and the linear Vs ↔ Gmax map no longer governs response (`TC-10`).

**Typical ranges**:
- Hard rock (granite, basalt): 2,500–3,500 m/s
- Sedimentary rock: 1,500–2,500 m/s
- Stiff soil/saprolite: 360–1,500 m/s
- Soft soil/alluvium: 180–360 m/s
- Very soft soil/peat: < 180 m/s
- NEHRP site classes A (>1500), B (760–1500), C (360–760), D (180–360), E (<180).

**Cross-discipline equivalents**:
- **Geotechnical engineering**: Vs in the upper 30 m is sampled by borehole methods — downhole, crosshole, seismic CPT (`MC-geotech-CPT`); the design-code derived parameter Vs30 enters ASCE 7 / Eurocode 8 / NEHRP site coefficients F_a, F_v. The geotech borehole regime and the seismology tomography regime sample the same Vs field at different depths — `TC-12` is the depth-regime bridge.
- **Near-surface geophysics**: MASW (`MC-seismo-MASW`) and SASW measure Vs at the 5–50 m surface-wave regime, between the geotech borehole and the deeper ambient-noise tomography regime.
- **Hydrology**: Vs is sensitive to water saturation (~5–15% change across the water table); time-lapse Vs from ambient-noise dv/v gives a hydrology proxy. See `TC-03`.

**When you see this in a paper**: identify which depth regime the paper samples (`TC-12`) and whether the deeper structure was independently constrained. Vs30 reported without method (MASW, downhole, ReMi, CPT-Vs) is hard to interpret — methods can disagree by 20–30%. Site-amplification factors derived from Vs30 alone miss depth-to-bedrock effects and basin geometry (`PD-site-response`).

**Anchor citations**:
- Boore, D. M. (2004). Estimating Vs30 (or NEHRP site classes) from shallow velocity models (depths < 30 m). *Bull. Seismol. Soc. Am.*, 94(2), 591–597. doi:10.1785/0120030105
- Wills, C. J., Gutierrez, C. I., Perez, F. G., & Branum, D. M. (2015). A next generation Vs30 map for California. *Bull. Seismol. Soc. Am.*, 105(6), 3083–3091. doi:10.1785/0120150164
- Foti, S., et al. (2018). Guidelines for the good practice of surface wave analysis: a product of the InterPACIFIC project. *Bulletin of Earthquake Engineering*, 16(6), 2367–2420. doi:10.1007/s10518-017-0206-7

**Related cards**: `MC-seismo-MASW`, `MC-seismo-ambient-noise`, `MC-geotech-CPT`, `CC-geotech-MohrCoulomb`, `CC-geotech-G-Gmax`, `PD-liquefaction`, `PD-site-response`, `TC-03`, `TC-10`, `TC-12`

---

## CC-seismo-Q: Seismic attenuation quality factor Q [dimensionless]

**Quantity**: dimensionless quality factor 1/Q = ΔE/(2π E) — the fraction of elastic energy dissipated per oscillation cycle. Separately defined for P-waves (Qp), S-waves (Qs), and as intrinsic vs. scattering components. ⚠️ **Vocabulary collision**: Q in hydrology denotes streamflow [m³/s] (`CC-hydro-Q`); the two are unrelated.

**Defining relation**: amplitude decay A(x) = A₀ exp(−πfx/(Qv)), where f is frequency, x distance, v wave velocity. Intrinsic Q (anelastic dissipation) and scattering Q (loss of coherent energy to heterogeneity) combine as 1/Q_total = 1/Q_intrinsic + 1/Q_scattering.

**Typical ranges**:
- Qs continental crust: 50–300 at 1 Hz.
- Qs stable cratons: 500–1500.
- Qs sediments / fault zones: 10–100; near-surface < 50.
- Qp typically 1.5–2× Qs in rock.

**Cross-discipline equivalents**:
- **Geotechnical engineering**: low Q in soft sediments produces strong site amplification and ground-motion duration extension; canonical for the Mexico City lake-bed effect in the 1985 earthquake.
- **Material science**: Q is the same parameter used for any damped harmonic oscillator (mechanical Q of a tuning fork, electrical Q of a circuit).
- **Hydrology — explicit non-equivalent**: streamflow Q [m³/s] and attenuation Q [dimensionless] are unrelated despite the shared symbol.

**When you see this in a paper**: check the frequency band (Q is frequency-dependent: Q = Q₀ f^η typically reported), intrinsic vs. scattering decomposition method (multiple-lapse-time window analysis), and the reference path length.

**Anchor citations**:
- Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.). University Science Books.
- Sato, H., Fehler, M. C., & Maeda, T. (2012). *Seismic Wave Propagation and Scattering in the Heterogeneous Earth* (2nd ed.). Springer. doi:10.1007/978-3-642-23029-5

**Related cards**: `CC-seismo-Vs`, `CC-seismo-noise`, `MC-seismo-tomography`

---

## CC-seismo-magnitude: Moment magnitude Mw and seismic moment M0 [N m]

**Quantity**: M0 = μ A D̄ is seismic moment [N m], where μ is shear modulus, A is rupture area, D̄ is average slip. Moment magnitude Mw = (2/3) log₁₀(M0) − 6.0 (Hanks & Kanamori 1979). M0 spans ~16 orders of magnitude across observed earthquakes; Mw is the standard catalog magnitude.

**Defining relation**: each unit of Mw corresponds to a factor of ~31.6 in radiated energy and ~10^1.5 in M0. Empirical scaling relations link M0 to rupture area, slip, and corner frequency (Wells & Coppersmith 1994; Hanks & Bakun 2002).

**Typical ranges**:
- Microearthquakes (Mw < 2): millions per year globally.
- Moderate (Mw 5–6): ~1500/yr globally.
- Major (Mw 7–7.9): ~15/yr.
- Great (Mw ≥ 8): ~1/yr.
- Largest recorded: Mw 9.5 (Chile 1960).
- Detection completeness in well-instrumented regions: Mw ~1.5–2.5; ML catalogs push 0.5–1.0.

**Cross-discipline equivalents**:
- **Geomorphology**: M0 controls coseismic surface displacement (D̄ scales with rupture length); fault scarp height accumulates over multiple seismic cycles.
- **Hydrology**: M0-distance scaling controls earthquake-triggered hydrologic responses (Wang & Manga 2010: streamflow responses observed up to M0^(1/2) × distance threshold).
- **Geotechnical engineering**: ground motion amplitude (PGA, PGV) scales with Mw via empirical GMPEs (Boore et al. 2014 NGA-West2).
- **Atmospheric sciences**: large M ≥ 8 earthquakes excite atmospheric infrasound and ionospheric waves.

**When you see this in a paper**: distinguish Mw (moment, preferred) from ML (local Richter, saturates above ~6.5), mb (body wave, used by USGS for routine reporting), and Ms (surface wave). Different magnitudes for the same event can differ by 0.3–0.5 units.

**Anchor citations**:
- Kanamori, H. (1977). The energy release in great earthquakes. *Journal of Geophysical Research*, 82(20), 2981–2987. doi:10.1029/JB082i020p02981
- Hanks, T. C., & Kanamori, H. (1979). A moment magnitude scale. *Journal of Geophysical Research: Solid Earth*, 84(B5), 2348–2350. doi:10.1029/JB084iB05p02348
- Wells, D. L., & Coppersmith, K. J. (1994). New empirical relationships among magnitude, rupture length, rupture width, rupture area, and surface displacement. *Bull. Seismol. Soc. Am.*, 84(4), 974–1002.

**Related cards**: `CC-seismo-stress`, `CC-seismo-GR`, `PD-megathrust`, `PD-induced-seismicity`

---

## CC-seismo-GR: Gutenberg-Richter and b-value [dimensionless]

**Quantity**: empirical relation log₁₀ N(≥M) = a − bM, where N is the number of earthquakes of magnitude ≥ M per unit time. The b-value characterizes the slope of the magnitude-frequency distribution; a-value is overall seismicity rate.

**Defining relation**: Gutenberg & Richter (1944). Equivalently in terms of seismic moment: log₁₀ N(≥M0) = a' − (2b/3) log₁₀ M0. b-value is robust to catalog magnitude conventions when fit above the magnitude of completeness Mc.

**Typical ranges**:
- Global average b ≈ 1.0.
- Mid-ocean ridges: b ≈ 1.0–1.5.
- Subduction zones: b ≈ 0.7–1.0.
- Volcanic regions: b ≈ 1.5–2.5 (small-event-dominated).
- Induced seismicity (Oklahoma, geothermal): b often elevated, 1.2–2.0.
- Aftershock sequences: b similar to background; Omori temporal decay separately.

**Cross-discipline equivalents**:
- **Hydrology**: flood-frequency analysis fits log-Pearson III or GEV to annual peak Q; same statistical machinery (extreme-value theory) but distinct mechanism. See `TC-04` for the analogy-and-its-limits.
- **Geomorphology**: landslide-size distributions show power-law tails with α ~ 1.0–2.5 (Malamud et al. 2004); again, shared statistics, distinct physics.

**When you see this in a paper**: confirm (1) the magnitude of completeness Mc — fits below Mc are dominated by detection bias, not real seismicity, (2) the fitting method (maximum likelihood preferred over least-squares; Aki 1965 framework), (3) spatiotemporal sample size (b-value uncertainty σ_b ≈ b/√N). Spatial b-value mapping is informative but requires N > 50–100 events per cell.

**Anchor citations**:
- Gutenberg, B., & Richter, C. F. (1944). Frequency of earthquakes in California. *Bull. Seismol. Soc. Am.*, 34(4), 185–188.
- Aki, K. (1965). Maximum likelihood estimate of b in the formula log N = a − bM and its confidence limits. *Bull. Earthquake Res. Inst. Tokyo Univ.*, 43, 237–239.
- Wiemer, S., & Wyss, M. (2002). Mapping spatial variability of the frequency-magnitude distribution of earthquakes. *Advances in Geophysics*, 45, 259–302. doi:10.1016/S0065-2687(02)80007-3

**Related cards**: `CC-seismo-magnitude`, `PD-induced-seismicity`, `TC-04`

---

## CC-seismo-dvv: Relative velocity change dv/v [dimensionless, often 10⁻⁴]

**Quantity**: fractional change in seismic wave velocity over time, (v(t) − v_ref)/v_ref. Measured from coda-wave interferometry of repeating sources (Poupinet et al. 1984) or from time-lapse cross-correlation of ambient seismic noise (Sens-Schönfelder & Wegler 2006).

**Defining relation**: extracted from temporal stretching of cross-correlation functions (stretching method) or from spectrally-weighted phase delays (moving window cross-spectrum). Typical sensitivity: detectable dv/v ≥ 1 × 10⁻⁴ over a multi-day stack.

**Typical ranges**:
- Volcanic, pre-eruption: 10⁻⁴ to 10⁻³ (Brenguier et al. 2008b).
- Postseismic relaxation (Parkfield): 10⁻⁴ over months (Brenguier et al. 2008a).
- Seasonal thermoelastic: 10⁻⁴ peak-to-peak (Hillers et al. 2015).
- Groundwater storage: 10⁻⁴ to 10⁻³ for ~10-m water-table changes (Clements & Denolle 2018).

**Cross-discipline equivalents**:
- **Hydrology**: dv/v ↔ groundwater storage is one of the most actively researched cross-discipline bridges. See `TC-03`; canonical reference Lecocq et al. (2017) for 30-year aquifer record.
- **Geotechnical engineering**: dv/v can detect soil-stiffness damage; promising for structural health monitoring and post-earthquake site characterization.
- **Near-surface geophysics**: complementary to time-lapse ERT for water content monitoring.

**When you see this in a paper**: confirm (1) the frequency band (different bands sample different depths), (2) corrections for thermal forcing (Hillers et al. 2015 framework), (3) whether scattering or direct waves are used, (4) the reference period and stack length. Calibration to physical observables (storage, stress) is site-specific.

**Anchor citations**:
- Poupinet, G., Ellsworth, W. L., & Frechet, J. (1984). Monitoring velocity variations in the crust using earthquake doublets: An application to the Calaveras Fault, California. *Journal of Geophysical Research*, 89(B7), 5719–5731. doi:10.1029/JB089iB07p05719
- Sens-Schönfelder, C., & Wegler, U. (2006). doi:10.1029/2006GL027797
- Brenguier, F., et al. (2008). Postseismic relaxation along the San Andreas fault at Parkfield from continuous seismological observations. *Science*, 321(5895), 1478–1481. doi:10.1126/science.1160944
- Clements, T., & Denolle, M. A. (2018). doi:10.1029/2018GL077706

**Related cards**: `CC-seismo-Vs`, `CC-seismo-noise`, `MC-seismo-ambient-noise`, `TC-03`

---

## CC-seismo-noise: Ambient seismic field [m/s, m/s² PSD]

**Quantity**: the continuous, ubiquitous seismic ground motion present in the absence of identifiable earthquakes. Reported as power spectral density (PSD) of velocity or acceleration. Spans 0.001–100 Hz; dominated by different source physics at different frequencies.

**Defining structure** (by frequency band):
- **Primary microseism (~10–20 s, 0.05–0.1 Hz)**: ocean swell interacting directly with coast.
- **Secondary microseism (~5–10 s, 0.1–0.2 Hz)**: pressure forcing from opposing wave-wave interactions in deep water (Longuet-Higgins 1950 mechanism). Globally the dominant ambient signal.
- **Earth's hum (0.002–0.02 Hz)**: continuous excitation of normal modes, sourced by atmospheric and oceanic forcing.
- **High-frequency (1–100 Hz)**: anthropogenic (vehicles, machinery), rivers and bedload transport (Burtin et al. 2008), wind, biological.

**Cross-discipline equivalents** (vocabulary collisions, since "noise" is field-specific):
- **Hydrology**: high-frequency seismic noise PSD correlates with stream discharge Q (`CC-hydro-Q`; Burtin et al. 2008); also captures glacier dynamics.
- **Atmospheric sciences**: pressure/wind coupling at long periods (Earth's hum mechanism, microseism intensity modulation by storms).
- **Ecology / "soundscape ecology"**: a similar term referring to acoustic ambient field — entirely different physics; see playbook disambiguation table.
- **Near-surface geophysics**: ambient noise is the *signal* for noise-correlation tomography (`MC-seismo-ambient-noise`); also exploited in DAS.

**When you see this in a paper**: confirm (1) frequency band, (2) source characterization (oceanic, anthropogenic, environmental), (3) whether the work treats noise as signal or as nuisance. Modern noise-correlation methods recast "noise" as the dominant illuminating wavefield.

**Anchor citations**:
- Longuet-Higgins, M. S. (1950). A theory of the origin of microseisms. *Phil. Trans. R. Soc. Lond. A*, 243(857), 1–35. doi:10.1098/rsta.1950.0012
- Burtin, A., Bollinger, L., Vergne, J., Cattin, R., & Nábělek, J. L. (2008). doi:10.1029/2007JB005034
- McNamara, D. E., & Buland, R. P. (2004). Ambient noise levels in the continental United States. *Bull. Seismol. Soc. Am.*, 94(4), 1517–1527. doi:10.1785/012003001

**Related cards**: `MC-seismo-ambient-noise`, `MC-seismo-DAS`, `CC-seismo-dvv`, `CC-hydro-Q`

---

## CC-seismo-source: Earthquake source parameters (focal mechanism, source spectrum)

**Quantity**: kinematic and dynamic descriptors of an earthquake rupture: focal mechanism (strike, dip, rake), centroid moment tensor (CMT), corner frequency f_c, stress drop, rupture velocity, slip distribution.

**Defining relations**: focal mechanism from first-motion polarities or waveform inversion. CMT (Dziewonski, Chou & Woodhouse 1981) decomposes the source into isotropic, double-couple, and compensated-linear-vector-dipole parts. Corner frequency f_c relates to source dimension via Brune (1970): f_c ≈ 0.49 v_s / r for circular crack, where r is rupture radius.

**Typical relations**:
- Stress drop Δσ = (7/16) M0/r³ for circular rupture.
- Self-similar earthquakes obey M0 ∝ f_c⁻³, giving constant Δσ across magnitudes.
- Rupture velocities typically 0.7–0.9 v_s; supershear (v_r > v_s) observed in ~10% of large strike-slip events.

**Cross-discipline equivalents**:
- **Hydrology** (forensic): for injection-induced events (`PD-induced-seismicity`), focal mechanism orientations help discriminate between fluid-driven slip on pre-existing faults vs. fresh fracturing.
- **Geomorphology**: surface rupture pattern and slip distribution feed coseismic landscape change models.
- **Geotechnical engineering**: source rupture parameters seed broadband ground-motion simulations and physics-based hazard models.

**When you see this in a paper**: distinguish point-source vs. finite-fault treatments; CMT solutions from W-phase or surface-wave inversion are reliable down to ~Mw 5; below that, regional moment tensors require care. Stress-drop estimates carry ~factor-of-3 uncertainty even at favorable distance ranges.

**Anchor citations**:
- Brune, J. N. (1970). Tectonic stress and the spectra of seismic shear waves from earthquakes. *Journal of Geophysical Research*, 75(26), 4997–5009. doi:10.1029/JB075i026p04997
- Dziewonski, A. M., Chou, T.-A., & Woodhouse, J. H. (1981). Determination of earthquake source parameters from waveform data for studies of global and regional seismicity. *Journal of Geophysical Research: Solid Earth*, 86(B4), 2825–2852. doi:10.1029/JB086iB04p02825
- Allmann, B. P., & Shearer, P. M. (2009). doi:10.1029/2008JB005821

**Related cards**: `CC-seismo-magnitude`, `CC-seismo-stress`, `PD-megathrust`, `PD-induced-seismicity`, `TC-09`
