---
discipline: hydrology
card_type: translation
schema_version: v3
---

# Hydrology — translation cards

Cross-discipline bridges originating from hydrology. These are the cross-cutting cards the rest of the corpus already references: `TC-01` (diffusion), `TC-02` (effective stress), `TC-03` (dv/v as hydro proxy), `TC-04` (power laws), `TC-05` (data assimilation), `TC-06` (watershed mass balance). Format follows `docs/card_format_spec.md`.

---

## TC-01: Diffusion equation across disciplines

**Shared structure**: the parabolic PDE ∂φ/∂t = D ∇²φ governs how a scalar field φ (head, pressure, temperature, sediment elevation) spreads under gradient-driven transport. The equation is identical across disciplines; the substrate, the diffusivity D, and the boundary conditions differ. Diffusivity values span ≥ 10 orders of magnitude. Recognizing a problem as "diffusion of X" is the most common single move in cross-discipline translation.

**Discipline-specific manifestations**:
- **Hydrology**: hydraulic head h diffuses with D = T/S; D ≈ 10⁰ – 10² m²/s in confined aquifers (`CC-hydro-D`). The Theis (1935) pumping-test solution is the canonical analytical case.
- **Geotechnical engineering**: pore pressure dissipates under consolidation with c_v = k/(γ_w m_v); c_v ≈ 10⁻⁸ – 10⁻² m²/s (`CC-geotech-cv`). Terzaghi (1925) consolidation theory.
- **Geomorphology**: hillslope sediment transport κ ≈ 10⁻⁴ m²/yr; same equation at vastly slower rates (`CC-geomorph-D`, placeholder).
- **Heat / geothermal**: thermal diffusivity ≈ 10⁻⁶ m²/s; reservoir temperature, permafrost evolution.
- **Seismology**: pore-pressure diffusion through fault zones produces the r²/t cloud expansion of injection-triggered earthquakes (`PD-induced-seismicity`); r ≈ √(4πDt). Aftershock rate decay (Omori 1894) is *not* literally diffusion despite the t⁻¹ form — different physics (Dieterich 1994 rate-state).
- **Atmospheric**: eddy diffusivity in the boundary layer is a parameterization, not a true Fickian diffusion (vocabulary collision; flagged in the agent playbook).

**When the analogy holds**:
- Linear regime, no thresholds.
- Substrate properties (D) approximately constant over the domain.
- Source term, if any, is well-characterized.
- Length and time scales such that the analytical solutions (Theis, error-function fronts, Heaviside step response) are physically meaningful.

**When the analogy breaks**:
- Threshold effects: matrix-fracture exchange, dual-porosity, preferential flow — all violate continuum diffusion.
- Strong nonlinearity (unsaturated zone, large strain, non-Darcian flow) requires a nonlinear PDE.
- Hyperbolic / wave-like regimes (rapid pressure transients, shocks) — the parabolic approximation fails.
- Coupled problems: even when each problem is diffusion, the coupling can produce qualitatively different behavior (poroelasticity, thermo-hydromechanical coupling).

**Translator agent move**: when a paper reports a characteristic timescale τ for a propagating signal, compute D = L²/τ (where L is the relevant length scale) and compare against the table of disciplinary D ranges. If D plausibly lies in another discipline's range, ask: is the underlying physics the same, or is this a numerical coincidence? Surface the cross-discipline analog if the physics supports it.

**Anchor citations**:
- Bear, J. (1972). *Dynamics of Fluids in Porous Media*. Elsevier.
- Roeloffs, E. A. (1996). Poroelastic techniques in the study of earthquake-related hydrologic phenomena. *Advances in Geophysics*, 37, 135–195. doi:10.1016/S0065-2687(08)60270-8
- Carslaw, H. S., & Jaeger, J. C. (1959). *Conduction of Heat in Solids* (2nd ed.). Oxford University Press.
- Shapiro, S. A., & Dinske, C. (2009). Fluid-induced seismicity: Pressure diffusion and hydraulic fracturing. *Geophysical Prospecting*, 57(2), 301–310. doi:10.1111/j.1365-2478.2008.00770.x

**Related cards**: `CC-hydro-D`, `CC-hydro-K`, `CC-hydro-T`, `CC-hydro-S`, `CC-geotech-cv`, `PD-induced-seismicity`, `PD-aquifer-depletion`

---

## TC-02: Effective stress unifies hydrology, geotechnical engineering, and seismology

**Shared structure**: σ' = σ − p (Terzaghi 1925); generalized to σ' = σ − αp (Biot 1941) where α is the Biot-Willis coefficient. Mechanical strength of porous geological materials is determined by effective stress, not total stress; the pore-pressure term p couples mechanics to hydrology. This is the single most-cited bridge in the corpus and the deepest hydrology-geotech-seismology integration.

**Discipline-specific manifestations**:
- **Hydrology**: p is hydraulic head expressed as pressure (`CC-hydro-p`); rainfall infiltration, pumping, injection, and post-seismic redistribution all modulate p. Hubbert & Rubey (1959) demonstrated that effective stress explains long-debated overthrust mechanics, anchoring the framework's interdisciplinary status.
- **Geotechnical engineering**: τ_f = c' + σ' tan φ' (`CC-geotech-MohrCoulomb`) — failure depends on σ'. Liquefaction (`PD-liquefaction`) is the limit case where p rises to σ_n and σ' → 0. Skempton (1954) parameters A and B (`CC-geotech-PorePressure`) describe how undrained loading generates Δp.
- **Seismology**: Coulomb failure criterion τ = μ(σ_n − p) + c (`CC-seismo-stress`); injection-induced seismicity (`PD-induced-seismicity`) is the textbook case (Healy et al. 1968 Denver, Ellsworth 2013 review). Fault static-stress changes after earthquakes propagate via the ΔCFS framework.
- **Geomorphology**: Iverson (2000) shows that rainfall-triggered shallow landsliding (`PD-AR-landslide`) is a transient effective-stress problem on a hillslope; the same equation, different boundary conditions and forcing.

**When the analogy holds**:
- Fully saturated medium with isotropic Biot coefficient α (most subsurface applications).
- Linear-elastic response with well-defined preconsolidation history.
- Pore-pressure measurement is co-located in space (or close enough) with the stress measurement.

**When the analogy breaks**:
- Unsaturated conditions require Bishop's effective stress σ' = σ − χ p_w − (1−χ) p_a, where χ is a saturation-dependent factor; the generalization is essential for shallow-landslide forecasting.
- Anisotropic α (transversely isotropic shale, fractured rock) breaks the scalar formulation.
- Large strain and inelastic deformation — the elastic framework no longer applies, even though σ' still governs failure (`CC-geotech-G-Gmax`, `TC-10`).
- Dynamic loading at very high strain rate (impact, ultra-high-frequency seismic): not enough time for pore-pressure equilibration on the relevant timescale; "undrained" total-stress analysis takes over.

**Translator agent move**: when a paper invokes "stress" in any geomechanical / hydrologic context, identify whether it means total or effective; if effective, identify the assumed Biot coefficient and saturation state. For paper interpretation in hazard contexts (induced seismicity, slope failure, dam safety), `TC-02` is almost always the deep bridge. Surface the discipline-specific cards (`CC-hydro-p`, `CC-geotech-MohrCoulomb`, `CC-seismo-stress`) together.

**Anchor citations**:
- Terzaghi, K. (1943). *Theoretical Soil Mechanics*. Wiley.
- Biot, M. A. (1941). General theory of three-dimensional consolidation. *Journal of Applied Physics*, 12(2), 155–164. doi:10.1063/1.1712886
- Hubbert, M. K., & Rubey, W. W. (1959). Role of fluid pressure in mechanics of overthrust faulting. *Geological Society of America Bulletin*, 70(2), 115–166. doi:10.1130/0016-7606(1959)70[115:ROFPIM]2.0.CO;2
- Healy, J. H., Rubey, W. W., Griggs, D. T., & Raleigh, C. B. (1968). The Denver earthquakes. *Science*, 161(3848), 1301–1310. doi:10.1126/science.161.3848.1301

**Related cards**: `CC-hydro-p`, `CC-geotech-MohrCoulomb`, `CC-geotech-PorePressure`, `CC-seismo-stress`, `PD-induced-seismicity`, `PD-AR-landslide`, `PD-liquefaction`, `PD-eq-hydro-coupling`

---

## TC-03: Ambient seismic noise as hydrology proxy (dv/v)

**Shared structure**: relative seismic velocity change dv/v measured from coda-wave interferometry of repeating sources or from time-lapse cross-correlation of ambient seismic noise (`CC-seismo-dvv`) is sensitive to subsurface property changes including water content, pore pressure, and effective stress. The bridge converts a continuous seismological observable into a continuous proxy for hydrologic state variables: groundwater storage, soil moisture, water-table position. Sensitivity is small (typical dv/v at the 10⁻⁴ level for ~10 m water-table changes) but the spatial and temporal coverage of seismic networks gives information unavailable to any single well or in-situ sensor.

**Discipline-specific manifestations**:
- **Seismology**: dv/v from `MC-seismo-ambient-noise` cross-correlation; frequency-band selection determines depth sensitivity (low frequency = deeper).
- **Hydrology**: storage anomalies (`CC-hydro-S`), water-table fluctuation (`CC-hydro-h`), soil moisture (`MC-hydro-COSMOS`); calibration of dv/v signal to storage requires site-specific information.
- **Geotechnical engineering**: dv/v can detect transient soil-stiffness damage and post-earthquake site-property changes; promising for structural-health monitoring.
- **Atmospheric sciences**: thermoelastic forcing of dv/v from temperature must be removed (Hillers et al. 2015) before hydrologic interpretation; the correction itself constrains shallow thermal diffusivity.

**When the analogy holds**:
- Site-specific calibration to local water-table data or piezometric records exists.
- Frequency band has been chosen to match the depth of interest.
- Thermoelastic and barometric contributions have been separated.
- Source-distribution effects on the noise field are not changing.

**When the analogy breaks**:
- Without calibration, dv/v is a relative signal — the conversion to physical units requires assumption-loaded petrophysics.
- Source-distribution non-stationarity (storm seasonality, anthropogenic noise) can mimic hydrologic signals.
- Frequency-band mismatch: a dv/v derived from 0.5–1 Hz noise samples 1–10 km; not the same as a wellhead measurement at 30 m.
- Coupling can be opposite-sign in different settings (Lecocq et al. 2017 30-year record): unsaturated-zone wetting tends to *decrease* Vs; below the water table, dv/v can *increase* with pressure. The sign of the response is site-dependent.

**Translator agent move**: when a paper reports a dv/v time series, ask: what is the calibration target? what hydrologic state variable does the work claim to measure? what's the frequency band? has the thermal correction been done? For hydrology papers using seismic data, retrieve `CC-seismo-dvv` and `MC-seismo-ambient-noise`; for seismology papers reporting dv/v in a region with known aquifer activity, retrieve `CC-hydro-S` and `CC-hydro-h`.

**Anchor citations**:
- Sens-Schönfelder, C., & Wegler, U. (2006). Passive image interferometry and seasonal variations of seismic velocities at Merapi Volcano, Indonesia. *Geophysical Research Letters*, 33(21), L21302. doi:10.1029/2006GL027797
- Clements, T., & Denolle, M. A. (2018). Tracking groundwater levels using the ambient seismic field. *Geophysical Research Letters*, 45(13), 6459–6465. doi:10.1029/2018GL077706
- Lecocq, T., Longuevergne, L., Pedersen, H. A., Brenguier, F., & Stammler, K. (2017). Monitoring ground water storage at mesoscale using seismic noise: 30 years of continuous observation and thermo-elastic and hydrological modeling. *Scientific Reports*, 7, 14241. doi:10.1038/s41598-017-14468-9
- Hillers, G., Ben-Zion, Y., Campillo, M., & Zigone, D. (2015). Seasonal variations of seismic velocities in the San Jacinto fault area observed with ambient seismic noise. *Geophysical Journal International*, 202(2), 920–932. doi:10.1093/gji/ggv151

**Related cards**: `CC-seismo-dvv`, `CC-seismo-noise`, `MC-seismo-ambient-noise`, `CC-hydro-S`, `CC-hydro-h`, `MC-hydro-COSMOS`

---

## TC-04: Power-law / heavy-tailed distributions across disciplines

**Shared structure**: many geoscience size-frequency distributions exhibit power-law tails N(≥X) ~ X^−α or heavy-tailed forms (GEV, log-Pearson III, log-normal) in their extremes. The *statistical machinery* — extreme-value theory, return periods, completeness corrections, maximum-likelihood fitting — is portable across disciplines. The *mechanisms* that produce the power law are not. Treating surface statistical similarity as physical equivalence is the corpus's canonical refusal pattern (`agent_playbook.md`).

**Discipline-specific manifestations**:
- **Seismology**: Gutenberg-Richter log N(≥M) = a − bM with b ≈ 1 globally (`CC-seismo-GR`). Mechanism: self-organized criticality on a population of faults; Omori law t^−p for aftershock decay.
- **Hydrology**: flood-frequency analysis fits log-Pearson III or GEV to annual peak streamflow Q (`CC-hydro-Q`). Mechanism: extreme-precipitation distribution × hydrologic response. Hosking & Wallis (1997) regional flood frequency framework.
- **Geomorphology**: landslide size-frequency distributions show power-law tails with α ≈ 1.0–2.5 (Malamud et al. 2004); inverse-gamma roll-over at small sizes. Hack's law L ~ A^h for stream networks (Hack 1957). Mechanism: branching channel networks; soil-strength heterogeneity.
- **Atmospheric sciences**: rainfall extreme statistics (Bunde et al. 2005), tropical-cyclone size and intensity tails.
- **Ecology**: species-abundance distributions; biomass-size spectra.

**When the analogy holds** (transfer of methodology):
- Extreme-value statistical tools (block-maxima, peaks-over-threshold, regional regression) port directly across disciplines.
- Completeness corrections (lower-cutoff truncation) are mechanically the same for earthquake catalogs and landslide inventories.
- Uncertainty quantification of return-period estimates is mathematically identical.

**When the analogy breaks** (mechanism is *not* shared):
- Gutenberg-Richter, Hack's law, landslide size, and flood frequency are all power laws but have entirely different physical origins; sharing statistics does not imply shared physics.
- Stationarity assumption: hydrologic extreme statistics calibrated to historical records are increasingly unreliable under climate change (Milly et al. 2008 "stationarity is dead"). Earthquake catalogs are stationary on much longer timescales; the analogy breaks at the climate-attribution level.
- Power-law slopes ≠ physical constants; they encode different things in different disciplines.

**Translator agent move**: when a paper invokes a power law in one discipline and gestures at "similar behavior" in another, retrieve this card and apply the refusal pattern: shared statistical machinery is portable; shared mechanism is not. Compute return periods and uncertainties using the field-appropriate framework but resist the temptation to claim deep equivalence.

**Anchor citations**:
- Gutenberg, B., & Richter, C. F. (1944). Frequency of earthquakes in California. *Bulletin of the Seismological Society of America*, 34(4), 185–188.
- Malamud, B. D., Turcotte, D. L., Guzzetti, F., & Reichenbach, P. (2004). Landslide inventories and their statistical properties. *Earth Surface Processes and Landforms*, 29(6), 687–711. doi:10.1002/esp.1064
- Hosking, J. R. M., & Wallis, J. R. (1997). *Regional Frequency Analysis: An Approach Based on L-Moments*. Cambridge University Press.
- Milly, P. C. D., et al. (2008). Stationarity is dead: Whither water management? *Science*, 319(5863), 573–574. doi:10.1126/science.1151915

**Related cards**: `CC-seismo-GR`, `CC-hydro-Q`, `CC-geomorph-landslide-size`, `CC-geomorph-flood-frequency`, `MC-hydro-NWIS`

---

## TC-05: Data assimilation across atmosphere, hydrology, and seismology

**Shared structure**: Bayesian state estimation combining a forward model M and observations y to update the posterior distribution of the state vector x. The mathematical core (Bayes' theorem applied to high-dimensional state spaces) is identical across disciplines. The discipline-specific differences are: dimensionality of x (atmospheric DA: 10⁸–10⁹; hydrologic DA: 10⁵–10⁷; seismic source: 10⁰–10²), nonlinearity of M, observation density, and the choice of linearization (4D-Var, EnKF, particle filter, hybrid).

**Discipline-specific manifestations**:
- **Atmospheric sciences**: operational numerical weather prediction (ECMWF IFS, NOAA GFS) assimilates 10⁹ observations daily; 4D-Var (Lorenc 1986; Courtier 1997) and EnKF / hybrid (Houtekamer & Mitchell 2005) are the workhorses. ERA5 (Hersbach et al. 2020) is the reanalysis product.
- **Hydrology**: snow / soil moisture / streamflow assimilation in operational land-surface modeling; SMAP L4 Level-4 product (`MC-hydro-SMAP`) is an EnKF assimilation into the NASA Catchment model (Reichle et al. 2017). National Water Model assimilates USGS NWIS streamflow into WRF-Hydro.
- **Seismology**: earthquake source inversion (Tarantola 2005) is small-dimensional Bayesian inverse problem; full-waveform inversion (Virieux & Operto 2009) is the high-dimensional analog with 10⁷–10⁸ model parameters and strong nonlinearity. Linearized iterative inversion borrows ideas (preconditioning, regularization) from the atmospheric community.
- **Reservoir engineering / hydrogeophysics**: history matching reservoir models against production data; joint hydrogeophysical inversion (Linde et al. 2006; `TC-08`).

**Shared inference structure**: prior p(x), likelihood p(y|x), posterior p(x|y) ∝ p(y|x) p(x); forward model M(x) maps state to observations; observation operator H linearizes for incremental updates; innovation y − H(x_b) drives the analysis. Software cores port: PyMC / emcee / Stan (small problems), DART (atmospheric / hydrologic ensembles), SPECFEM (seismic FWI), PEST++ (hydrologic calibration).

**When the analogy holds**: the Bayesian framework is universally applicable; intuition about priors, likelihoods, and ensembles is transferable; diagnostic tools (innovation statistics, posterior predictive checks, spread/error ratio) port across disciplines.

**When the analogy breaks**:
- 4D-Var assumes near-linearity over the assimilation window (≈ 12 h for NWP); seismic FWI is intrinsically nonlinear over the whole inversion.
- Hydrologic DA struggles with mass conservation and bias correction (model bias rarely meets the zero-mean assumption); atmospheric DA has more mature bias-correction machinery.
- Ensemble sizes feasible for atmospheric DA (≈ 100) are inadequate for high-dimensional multimodal seismic inverse problems; alternative samplers (HMC, parallel tempering) needed.

**Translator agent move**: when a paper formulates a state-estimation problem in one discipline, retrieve the analogous structure in adjacent disciplines. For Gaia digital-twin work, multi-physics DA is the technical core — the same machinery does atmospheric forcing, hydrologic state estimation, and seismic monitoring.

**Anchor citations**:
- Evensen, G. (1994). Sequential data assimilation with a nonlinear quasi-geostrophic model using Monte Carlo methods to forecast error statistics. *Journal of Geophysical Research: Oceans*, 99(C5), 10143–10162. doi:10.1029/94JC00572
- Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999–2049. doi:10.1002/qj.3803
- Reichle, R. H. (2008). Data assimilation methods in the Earth sciences. *Advances in Water Resources*, 31(11), 1411–1418. doi:10.1016/j.advwatres.2008.01.001
- Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter Estimation*. SIAM. doi:10.1137/1.9780898717921
- Virieux, J., & Operto, S. (2009). An overview of full-waveform inversion in exploration geophysics. *Geophysics*, 74(6), WCC1–WCC26. doi:10.1190/1.3238367

**Related cards**: `MC-hydro-modeling`, `MC-hydro-SMAP`, `MC-atm-ERA5`, `MC-seismo-tomography`, `TC-08`, `TC-09`

---

## TC-06: Watershed mass balance ↔ atmospheric branch ↔ ecosystem branch

**Shared structure**: P = ET + Q + ΔS — precipitation balances evapotranspiration, streamflow, and storage change. Same skeleton appears in the atmospheric branch (E − P over land returns to the atmosphere as water vapor; E − P over ocean closes the global hydrologic cycle), in the ecosystem-carbon branch (NEE = GPP − R_eco; NPP = GPP − R_a; carbon and water are coupled at the leaf through stomatal conductance), and in the surface-energy balance (R_n = H + LE + G; LE couples to ET). The four budgets share variables, are mechanistically linked through plant physiology and turbulent exchange, and must close jointly under the same observations.

**Discipline-specific manifestations**:
- **Hydrology**: watershed water balance from precipitation gauges, NWIS streamflow (`CC-hydro-Q`, `MC-hydro-NWIS`), ET from eddy covariance (`MC-hydro-eddycov`), and storage from GRACE (`MC-hydro-GRACE`). The residual term is recharge or unobserved storage change.
- **Atmospheric sciences**: vertically integrated moisture-flux convergence ∇·(qv) = E − P from reanalysis; atmospheric water-vapor budget closes the cycle on regional to global scales.
- **Ecology**: ecosystem GPP, R_eco, and NEE from eddy covariance F_C decomposition (`CC-eco-GPP`); coupling to ET via stomatal conductance — both fluxes share the leaf-scale physiology.
- **Agricultural sciences**: crop water balance using FAO-56 ET₀ and crop coefficients (`CC-ag-ET0`); ET partitioning between transpiration (productive) and evaporation (non-productive) is a key irrigation-efficiency question.

**When the analogy holds**:
- Closed watershed boundary (no inter-basin transfer, well-characterized recharge from outside).
- All four terms measured or modeled with consistent timescales and footprints.
- ET measurement at a site representative of the watershed; or distributed observations integrate properly.
- Storage change term ΔS observable (GRACE for large basins; in-situ for small).

**When the analogy breaks**:
- Closure error 10–30% is endemic: P from gauges underestimates by 5–15% (undercatch); ET from eddy covariance underestimates by 10–30% (energy-balance closure); Q has rating-curve uncertainty; ΔS is hardest to constrain. The residuals are small differences of large numbers.
- Inter-basin water transfer (California State Water Project, NYC water supply) breaks the balance.
- Anthropogenic withdrawals — irrigation, municipal pumping, reservoir storage — must be accounted for separately.
- Inhomogeneous footprints — eddy covariance samples ~1 km²; GRACE samples > 300 km²; watershed-mean Q reflects the full integrated area — combining them risks aliasing.

**Translator agent move**: when a paper closes (or claims to close) a water balance, identify each term's measurement and the assumed footprint; flag closure error as a target rather than an inconvenience (a "perfectly closed" balance is suspicious). For cross-discipline integration, the leaf-scale coupling of ET and GPP is the deep bridge between hydrology and ecology, and the basin-scale watershed mass balance is the canonical integration test.

**Anchor citations**:
- Brutsaert, W. (2005). *Hydrology: An Introduction*. Cambridge University Press.
- Trenberth, K. E., Smith, L., Qian, T., Dai, A., & Fasullo, J. (2007). Estimates of the global water budget and its annual cycle using observational and model data. *Journal of Hydrometeorology*, 8(4), 758–769. doi:10.1175/JHM600.1
- Pan, M., Sahoo, A. K., Troy, T. J., Vinukollu, R. K., Sheffield, J., & Wood, E. F. (2012). Multisource estimation of long-term terrestrial water budget for major global river basins. *Journal of Climate*, 25(9), 3191–3206. doi:10.1175/JCLI-D-11-00300.1

**Related cards**: `CC-hydro-Q`, `CC-hydro-ET`, `CC-hydro-recharge`, `MC-hydro-eddycov`, `MC-hydro-GRACE`, `MC-hydro-NWIS`, `CC-eco-GPP`, `CC-ag-ET0`, `MC-atm-ERA5`, `PD-drought`
