---
discipline: geomorphology
card_type: concept
schema_version: v3
---

# Geomorphology — concept cards

Each card defines one core geomorphic variable, equation, or measured quantity, with units, numerical ranges, and explicit hooks into the other Gaia disciplines. Format follows `docs/card_format_spec.md`.

---

## CC-geomorph-D: Hillslope sediment-transport diffusivity κ [m²/yr]

**Quantity**: the proportionality constant in the linear hillslope-transport law q_s = −κ ∂z/∂x, where q_s is sediment flux per unit contour length [m²/yr] and z is elevation. Mathematically identical to hydraulic and consolidation diffusion (`TC-01`), but ~10⁸ times slower in dimensional rate. The fundamental conservative-transport model for soil-mantled hillslopes (Culling 1960; Roering et al. 1999).

**Defining relation**: linear ∂z/∂t = κ ∇²z applies for low gradients; for slopes approaching the angle of repose, the nonlinear form q_s = −(κ ∂z/∂x)/(1 − (∂z/∂x / S_c)²) (Roering et al. 1999) captures the rapid runaway as gradients approach the threshold S_c (≈ 0.5–1.2). Soil-production rate from bedrock P(h) sets the steady-state coupling to long-term erosion (Heimsath et al. 1997).

**Typical ranges**:
- κ in soil-mantled humid temperate landscapes: 10⁻³ – 10⁻² m²/yr (Roering et al. 1999 Oregon Coast Range).
- κ in semi-arid landscapes: 10⁻⁴ – 10⁻³ m²/yr.
- Periglacial / cold-climate (frost creep, solifluction): 10⁻² – 10⁻¹ m²/yr.
- S_c critical slope: 0.5–1.2 (≈ 27°–50°) depending on lithology and root reinforcement.

**Cross-discipline equivalents**:
- **Hydrology**: same diffusion equation as `CC-hydro-D` but ~10¹⁰ times slower; the canonical `TC-01` cross-discipline bridge.
- **Geotechnical engineering**: consolidation `CC-geotech-cv` is mechanically the same diffusion equation in soils under load.
- **Heat transfer**: thermal diffusion in soil shares the equation; periglacial coupling uses both.

**When you see this in a paper**: confirm linear vs. nonlinear formulation; the linear model fails wherever local slopes approach S_c, which is most of the steep PNW. Distinguish κ (transport diffusivity) from K (bedrock-incision coefficient in `CC-geomorph-streampower`) — different variables, occasional symbol collision.

**Anchor citations**:
- Culling, W. E. H. (1960). Analytical theory of erosion. *The Journal of Geology*, 68(3), 336–344. doi:10.1086/626663
- Roering, J. J., Kirchner, J. W., & Dietrich, W. E. (1999). Evidence for nonlinear, diffusive sediment transport on hillslopes and implications for landscape morphology. *Water Resources Research*, 35(3), 853–870. doi:10.1029/1998WR900090
- Heimsath, A. M., Dietrich, W. E., Nishiizumi, K., & Finkel, R. C. (1997). The soil production function and landscape equilibrium. *Nature*, 388(6640), 358–361. doi:10.1038/41056

**Related cards**: `CC-hydro-D`, `CC-geotech-cv`, `CC-geomorph-Qs`, `CC-geomorph-erosion-rate`, `TC-01`, `TC-13`, `PD-AR-landslide`

---

## CC-geomorph-streampower: Stream power and bedrock incision [W/m, W/m²]

**Quantity**: total stream power Ω = ρ g Q S [W/m] and unit stream power ω = ρ g (Q/W) S = ρ g R V S [W/m²], where Q is discharge, S is slope, W is width, R is hydraulic radius, V is velocity. The mechanical energy expenditure rate per unit channel length (or area) that drives bed shear, sediment transport, and bedrock incision. Foundation of the detachment-limited bedrock-incision model E = K A^m S^n (Howard 1994; Whipple & Tucker 1999).

**Defining relation**: incision rate E = K A^m S^n combines drainage-area surrogate A^m for discharge with slope S^n for energy gradient. Typical m/n ratios 0.4–0.6 from morphometric inversion; K varies with lithology, climate, and sediment supply. The saltation–abrasion model (Sklar & Dietrich 2004) adds an explicit sediment-tools-and-cover effect: incision peaks at intermediate sediment supply.

**Typical ranges**:
- Unit stream power in lowland alluvial rivers: 1 – 30 W/m².
- Mountain rivers, bankfull: 50 – 500 W/m².
- Extreme flood events (debris-laden): > 10³ W/m².
- K (m^(1−2m) yr⁻¹) erosion-rate coefficient: 10⁻⁷ – 10⁻⁴ across lithologies and climates.

**Cross-discipline equivalents**:
- **Hydrology**: Q is the same streamflow as `CC-hydro-Q`; W and S from morphometry close the link. Stream power is the geomorphic complement to the hydrologic discharge observable.
- **Seismology**: bedload-driven high-frequency seismic noise (Burtin et al. 2008; `CC-seismo-noise`, `TC-14`) tracks stream-power proxies at the watershed scale.
- **Ecology**: stream power controls channel-bed disturbance regime, central to in-stream habitat and `CC-eco-IHA` indicators.

**When you see this in a paper**: distinguish total Ω from unit ω (factor W between them); confirm whether the work uses peak event power, mean-annual power, or formative-discharge power (Wolman & Miller 1960). The m/n ratio is regression-derived and sensitive to the assumed channel-width scaling.

**Anchor citations**:
- Howard, A. D. (1994). A detachment-limited model of drainage basin evolution. *Water Resources Research*, 30(7), 2261–2285. doi:10.1029/94WR00757
- Whipple, K. X., & Tucker, G. E. (1999). Dynamics of the stream-power river incision model. *Journal of Geophysical Research: Solid Earth*, 104(B8), 17661–17674. doi:10.1029/1999JB900120
- Sklar, L. S., & Dietrich, W. E. (2004). A mechanistic model for river incision into bedrock by saltating bed load. *Water Resources Research*, 40(6), W06301. doi:10.1029/2003WR002496

**Related cards**: `CC-hydro-Q`, `CC-geomorph-tau`, `CC-geomorph-Qs`, `CC-geomorph-ksn`, `CC-seismo-noise`, `TC-14`, `PD-river-floods`

---

## CC-geomorph-tau: Bed shear stress and threshold of motion [Pa, N/m²]

**Quantity**: τ = ρ g R S, the bed-parallel force per unit area exerted by flowing water on the channel bed. The mechanistic driver for sediment entrainment; threshold-of-motion frameworks compare τ to a critical Shields stress τ_c* = τ_c / [(ρ_s − ρ) g D] for grain size D. Meyer-Peter–Müller bedload formula and its derivatives use τ_excess = τ − τ_c.

**Defining relation**: dimensionless Shields stress τ* = τ/[(ρ_s − ρ)gD]; critical τ_c* ≈ 0.03–0.06 for fully turbulent flow over uniform gravel (Buffington & Montgomery 1997). Bedload transport q_b ~ (τ − τ_c)^1.5 (Meyer-Peter & Müller 1948; Wilcock & Crowe 2003 for mixed-size beds).

**Typical ranges**:
- Sand-bed rivers, bankfull: τ ≈ 1–20 Pa.
- Gravel-bed mountain streams, bankfull: 50–300 Pa.
- Extreme floods: > 10³ Pa.
- Shields critical τ_c* for D = 10 mm gravel: ≈ 0.045 → τ_c ≈ 7 Pa.

**Cross-discipline equivalents**:
- **Geotechnical engineering**: Shields-style critical-stress framework parallels the Mohr-Coulomb yield criterion (`CC-geotech-MohrCoulomb`); both compare an applied stress to a material-property threshold.
- **Hydrology**: τ is hydrology's discharge translated into the mechanical-work-on-bed observable; closes the bedload-transport budget that feeds `CC-geomorph-Qs`.
- **Ecology**: bed-shear-stress disturbance regime structures benthic invertebrate community composition.

**When you see this in a paper**: confirm whether τ is reach-averaged (using bulk R and S) or grain-scale; the two can differ by factors of 2–5 in poorly-sorted gravel beds. Critical Shields stress τ_c* is empirical and varies with bed-sediment sorting (Wilcock-Crowe).

**Anchor citations**:
- Shields, A. (1936). *Anwendung der Aehnlichkeitsmechanik und der Turbulenzforschung auf die Geschiebebewegung*. Mitteilungen der Preußischen Versuchsanstalt für Wasserbau und Schiffbau, Berlin.
- Meyer-Peter, E., & Müller, R. (1948). Formulas for bed-load transport. *Proceedings of the 2nd Meeting of IAHR*, Stockholm, 39–64.
- Buffington, J. M., & Montgomery, D. R. (1997). A systematic analysis of eight decades of incipient motion studies, with special reference to gravel-bedded rivers. *Water Resources Research*, 33(8), 1993–2029. doi:10.1029/96WR03190
- Wilcock, P. R., & Crowe, J. C. (2003). Surface-based transport model for mixed-size sediment. *Journal of Hydraulic Engineering*, 129(2), 120–128. doi:10.1061/(ASCE)0733-9429(2003)129:2(120)

**Related cards**: `CC-geomorph-streampower`, `CC-geomorph-Qs`, `CC-geotech-MohrCoulomb`, `CC-hydro-Q`, `TC-14`

---

## CC-geomorph-Qs: Sediment flux and sediment continuity [kg/s, m³/yr]

**Quantity**: volumetric or mass sediment discharge through a channel cross-section [m³/yr, kg/s, t/yr]. Includes bedload (coarse, near-bed transport) and suspended load (fine, full-depth). Closes the sediment-continuity equation ∂z/∂t = U − ∇·Q_s + (sediment sources/sinks), the geomorphic analog to the watershed water balance (`TC-06`). ⚠️ Symbol collision: Q in hydrology is water discharge (`CC-hydro-Q`); Q_s is sediment discharge — same letter, different physical quantity.

**Defining relation**: Q_s_bedload from Meyer-Peter–Müller or Wilcock-Crowe (functions of τ, `CC-geomorph-tau`); Q_s_suspended via rating curve Q_s = a Q^b from gauge data. Total Q_s spans 10⁻¹–10⁵ t/yr per km² across watersheds; suspended typically dominates by mass.

**Typical ranges**:
- Sediment yield in stable temperate landscapes: 10–100 t/km²/yr.
- Active orogens (Himalaya, Taiwan, New Zealand): 1,000–10,000 t/km²/yr.
- Post-disturbance (wildfire, deforestation, glacial outburst): can increase by 10–100× for years to decades.
- Suspended sediment dominates by mass; bedload 5–20% in temperate, higher in steep mountain streams.

**Cross-discipline equivalents**:
- **Hydrology**: Q_s rating curves derive from USGS suspended-sediment records (`MC-hydro-NWIS`); the joint Q–Q_s observation closes the hydrologic and geomorphic budgets together.
- **Seismology**: high-frequency seismic noise correlates with bedload Q_s (Burtin et al. 2008; Gimbert et al. 2014; `TC-14`); seismic noise is now a continuous bedload monitor.
- **Geotechnical engineering**: sediment yield from post-fire and seismically destabilized hillslopes (`PD-coseismic-landslide`) drives downstream hazard.
- **Ecology**: sediment delivery shapes channel substrate, water clarity, and salmonid habitat quality.

**When you see this in a paper**: confirm bedload vs. suspended partitioning method; bedload rating curves are highly site-specific; one storm can deliver more sediment than years of low-flow background.

**Anchor citations**:
- Hovius, N., Stark, C. P., & Allen, P. A. (1997). Sediment flux from a mountain belt derived by landslide mapping. *Geology*, 25(3), 231–234. doi:10.1130/0091-7613(1997)025<0231:SFFAMB>2.3.CO;2
- Lamb, M. P., Dietrich, W. E., & Venditti, J. G. (2008). Is the critical Shields stress for incipient sediment motion dependent on channel-bed slope? *Journal of Geophysical Research: Earth Surface*, 113(F2), F02008. doi:10.1029/2007JF000831
- Wilcock, P. R., & Crowe, J. C. (2003). Surface-based transport model for mixed-size sediment. *Journal of Hydraulic Engineering*, 129(2), 120–128. doi:10.1061/(ASCE)0733-9429(2003)129:2(120)

**Related cards**: `CC-hydro-Q`, `CC-geomorph-streampower`, `CC-geomorph-tau`, `CC-seismo-noise`, `MC-geomorph-sediment-monitoring`, `MC-hydro-NWIS`, `TC-13`, `TC-14`

---

## CC-geomorph-erosion-rate: Long-term erosion / denudation rate E [mm/kyr]

**Quantity**: time-integrated rate of mass removal from a surface, expressed as vertical lowering [mm/kyr, m/Myr] or area-normalized denudation flux [t/km²/yr]. Distinct from instantaneous sediment yield (`CC-geomorph-Qs`) by the averaging timescale: cosmogenic ¹⁰Be catchment-mean rates integrate over 10³–10⁵ yr; thermochronology over 10⁶–10⁸ yr.

**Defining relation**: cosmogenic-isotope-derived rate E = P_0 / (N λ + ρ Λ E / Λ), where P_0 is the surface production rate, N is the measured nuclide concentration, λ is decay constant, ρ is rock density, Λ is attenuation length (Lal 1991; Granger et al. 1996). The CRONUS-Earth online calculator (Balco et al. 2008) is the community standard.

**Typical ranges**:
- Stable cratons: 1–10 mm/kyr.
- Tectonically inactive low-relief: 10–100 mm/kyr.
- Active orogens (Himalaya, Andes, Alps): 1,000–10,000 mm/kyr.
- Pacific Northwest Coast Range: ≈ 100–300 mm/kyr (Reneau & Dietrich 1991; Heimsath et al. 2001).
- Global mean denudation: ≈ 50 mm/kyr (Willenbring & von Blanckenburg 2010).

**Cross-discipline equivalents**:
- **Seismology / tectonics**: long-term denudation rates from cosmogenics are compared with rock-uplift rates (`PD-megathrust`, `PD-fault-scarp`) to test landscape steady-state assumptions.
- **Climate**: orographic precipitation patterns coupled to denudation give "tectonic aneurysm" feedbacks (Zeitler et al. 2001 Nanga Parbat); cosmogenic rates anchor climate-erosion attribution.
- **Hydrology**: long-term sediment yield must close with E on the appropriate averaging timescale; instantaneous yield from `CC-geomorph-Qs` is event-dominated and routinely diverges from the long-term mean.

**When you see this in a paper**: confirm the integration timescale of the method (cosmogenic vs. thermochronology vs. modern sediment yield); these often disagree at the same site, reflecting non-steady-state landscapes (e.g., post-glacial sediment slugs).

**Anchor citations**:
- Lal, D. (1991). Cosmic ray labeling of erosion surfaces: in situ nuclide production rates and erosion models. *Earth and Planetary Science Letters*, 104(2–4), 424–439. doi:10.1016/0012-821X(91)90220-C
- Granger, D. E., Kirchner, J. W., & Finkel, R. (1996). Spatially averaged long-term erosion rates measured from in situ–produced cosmogenic nuclides in alluvial sediment. *The Journal of Geology*, 104(3), 249–257. doi:10.1086/629823
- Portenga, E. W., & Bierman, P. R. (2011). Understanding Earth's eroding surface with ¹⁰Be. *GSA Today*, 21(8), 4–10. doi:10.1130/G111A.1

**Related cards**: `CC-geomorph-D`, `CC-geomorph-Qs`, `MC-geomorph-cosmogenic`, `PD-landscape-evolution`, `TC-13`

---

## CC-geomorph-ksn: Channel steepness index and chi analysis [dimensionless ksn]

**Quantity**: normalized channel steepness ksn = k_s × A^(θ_ref) where k_s is the steepness coefficient in the slope-area relation S = k_s A^(−θ) and θ_ref is a reference concavity (typically 0.45). The chi-method transforms long profiles into a steady-state coordinate χ = ∫(A_0/A)^θ dx, in which steady-state profiles plot as straight lines (Perron & Royden 2013).

**Defining relation**: under detachment-limited incision E = K A^m S^n at steady state with uniform U, slope S = (U/K)^(1/n) A^(−m/n). Concavity θ = m/n; steepness k_s = (U/K)^(1/n) packages the tectonic and lithologic forcing. Chi-elevation plots reveal knickpoints (transient signals from base-level changes or differential uplift).

**Typical ranges**:
- ksn in tectonically quiescent landscapes: 10–50 m^0.9.
- Moderate uplift (e.g., Sierra Nevada): 50–200 m^0.9.
- Active orogens (Taiwan, Himalaya): 200–1,000 m^0.9.
- Concavity θ: 0.3–0.6 typical; 0.45 is the default reference.

**Cross-discipline equivalents**:
- **Seismology / tectonics**: ksn maps document spatial uplift-rate variations; complement to fault-slip-rate observations and `PD-fault-scarp` records.
- **Hydrology**: A^m is a drainage-area proxy for discharge, so ksn implicitly assumes the hydrologic-climatic regime is uniform across the analysis area; non-uniform precipitation (orographic gradients) confounds.
- **Geomorphology**: ksn is paired with `CC-geomorph-erosion-rate` cosmogenic data for joint tectonic-erosion inversions (Kirby & Whipple 2012 review).

**When you see this in a paper**: confirm the reference concavity used and the regression method; ksn is sensitive to noisy DEM-derived slopes — chi-elevation plots are more robust. Knickpoints can be tectonic, lithologic, or autogenic; attribution requires independent evidence.

**Anchor citations**:
- Wobus, C., Whipple, K. X., Kirby, E., Snyder, N., Johnson, J., Spyropolou, K., Crosby, B., & Sheehan, D. (2006). Tectonics from topography: Procedures, promise, and pitfalls. *GSA Special Paper*, 398, 55–74. doi:10.1130/2006.2398(04)
- Perron, J. T., & Royden, L. (2013). An integral approach to bedrock river profile analysis. *Earth Surface Processes and Landforms*, 38(6), 570–576. doi:10.1002/esp.3302
- Mudd, S. M., Clubb, F. J., Gailleton, B., & Hurst, M. D. (2018). How concave are river channels? *Earth Surface Dynamics*, 6(2), 505–523. doi:10.5194/esurf-6-505-2018

**Related cards**: `CC-geomorph-streampower`, `CC-geomorph-erosion-rate`, `MC-geomorph-DEM-analysis`, `PD-fault-scarp`, `PD-landscape-evolution`

---

## CC-geomorph-flood-frequency: Flood-frequency analysis [m³/s at recurrence interval]

**Quantity**: peak-discharge magnitude associated with a specified annual exceedance probability (or recurrence interval RI). Standard outputs: Q_100 (100-yr flood, 1% annual exceedance), Q_500 (0.2%). Estimated by fitting an extreme-value distribution (log-Pearson III in the USGS framework; GEV elsewhere) to a partial-duration or annual-maximum series of gauge records (`MC-hydro-NWIS`).

**Defining relation**: log-Pearson III on log Q: log Q_T = μ + K_T σ, with K_T from the Pearson type-III tables for skew g. USGS Bulletin 17C (England et al. 2018) is the current U.S. operational standard. Regional regression equations (StreamStats) transfer estimates to ungauged sites. ⚠️ Vocabulary collision warning: flood-frequency power-law-like tails share statistical machinery with `CC-seismo-GR` but not mechanism (see `TC-04`).

**Typical ranges**:
- Q_2 (mean annual peak) on a small temperate-headwater stream: 1–10 m³/s.
- Q_100 / Q_2 ratio: 3–10× depending on basin response (flashier in arid/semi-arid).
- Largest U.S. historical flows: Mississippi 1927 ≈ 76,500 m³/s at Memphis; Columbia 1894 ≈ 35,000 m³/s at The Dalles.

**Cross-discipline equivalents**:
- **Hydrology**: extreme-value statistics machinery shared with all return-period analyses; `MC-hydro-NWIS` provides the gauge records.
- **Seismology**: Gutenberg-Richter `CC-seismo-GR` and flood-frequency are both heavy-tailed but mechanistically distinct (`TC-04`); the chatbot must refuse the "shared statistics → shared physics" inference.
- **Geotechnical engineering**: design floods drive dam-safety analysis (`PD-dam-levee-safety`); revisions of PMF/PMP under climate change are an active concern.
- **Atmospheric sciences**: stationarity assumption increasingly violated under climate change (Milly et al. 2008 "stationarity is dead").

**When you see this in a paper**: confirm sample length (short records give factor-2+ uncertainty at Q_100); regulation status of the gauge; whether nonstationarity has been addressed (covariate flood-frequency, IDF curves with climate scaling).

**Anchor citations**:
- Stedinger, J. R., Vogel, R. M., & Foufoula-Georgiou, E. (1993). Frequency analysis of extreme events. In *Handbook of Hydrology* (D. R. Maidment, ed.), Ch. 18. McGraw-Hill.
- England, J. F., Cohn, T. A., Faber, B. A., Stedinger, J. R., Thomas, W. O., Veilleux, A. G., Kiang, J. E., & Mason, R. R. (2018). *Guidelines for determining flood flow frequency — Bulletin 17C*. USGS Techniques and Methods 4-B5. doi:10.3133/tm4B5
- Milly, P. C. D., et al. (2008). Stationarity is dead: Whither water management? *Science*, 319(5863), 573–574. doi:10.1126/science.1151915

**Related cards**: `CC-hydro-Q`, `MC-hydro-NWIS`, `CC-seismo-GR`, `TC-04`, `PD-river-floods`, `PD-dam-levee-safety`

---

## CC-geomorph-landslide-size: Landslide size-frequency distribution [number-area]

**Quantity**: empirical distribution of landslide areas (or volumes) in an inventory. Universally well-described by an inverse-gamma roll-over at small sizes plus a power-law tail at large sizes (Malamud et al. 2004): N(≥A) ∝ A^(−α) for A above the roll-over scale, with α ≈ 1.4–2.5 globally. Used for hazard assessment, sediment-flux budgets, and as a probe of landscape state.

**Defining relation**: the Malamud et al. (2004) double-Pareto / inverse-gamma functional form has three parameters (roll-over location, tail exponent, overall amplitude). Inventory-completeness corrections at small sizes are essential — apparent shallow exponents may reflect detection cutoff rather than physics. ⚠️ Same vocabulary collision as flood frequency (`TC-04`): shared statistics, distinct mechanism from Gutenberg-Richter.

**Typical ranges**:
- α (tail exponent on cumulative area): 1.4–1.7 for shallow soil landslides.
- α: 2.0–2.5 for deep-seated rock failures (more truncated tails).
- Roll-over scale: typically 10³–10⁴ m² (varies with detection technology and triggering process).
- Volume estimates from area via V = ε A^γ scaling (Larsen et al. 2010); γ ≈ 1.3 typical.

**Cross-discipline equivalents**:
- **Seismology**: power-law statistics shared with Gutenberg-Richter `CC-seismo-GR` (same TC-04); mechanism is distinct (slope-stability threshold dynamics vs. fault-system self-organized criticality).
- **Hydrology**: rainfall-triggered landslide inventories follow the same Malamud form regardless of trigger; trigger-specific data (`PD-AR-landslide`, `PD-coseismic-landslide`) splits into sub-inventories with different parameters.
- **Geotechnical engineering**: integrated tail mass is the geomorphic input to `PD-dam-levee-safety` sediment-delivery and reservoir-design calculations.

**When you see this in a paper**: check inventory-completeness at small sizes; check whether the fit is to incremental N(A) or cumulative N(≥A) (differ by 1 in exponent); confirm whether area or volume is the statistic.

**Anchor citations**:
- Malamud, B. D., Turcotte, D. L., Guzzetti, F., & Reichenbach, P. (2004). Landslide inventories and their statistical properties. *Earth Surface Processes and Landforms*, 29(6), 687–711. doi:10.1002/esp.1064
- Stark, C. P., & Hovius, N. (2001). The characterization of landslide size distributions. *Geophysical Research Letters*, 28(6), 1091–1094. doi:10.1029/2000GL008527
- Larsen, I. J., Montgomery, D. R., & Korup, O. (2010). Landslide erosion controlled by hillslope material. *Nature Geoscience*, 3(4), 247–251. doi:10.1038/ngeo776

**Related cards**: `CC-seismo-GR`, `CC-geomorph-Qs`, `TC-04`, `PD-AR-landslide`, `PD-coseismic-landslide`, `PD-debris-flow`
