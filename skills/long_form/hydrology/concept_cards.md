---
discipline: hydrology
card_type: concept
schema_version: v3
---

# Hydrology — concept cards

Each card defines one core hydrological variable, equation, or measured quantity, with units, numerical ranges, and explicit hooks into the other Gaia disciplines. Format follows `docs/card_format_spec.md`.

---

## CC-hydro-K: Hydraulic conductivity K [m/s, m/day]

**Quantity**: the proportionality constant in Darcy's law q = −K ∇h, where q is specific discharge [m/s] and h is hydraulic head. K combines intrinsic permeability k [m²] and fluid properties: K = k ρ g / μ. SI units m/s; conventionally m/day in groundwater practice (1 m/day ≈ 1.16 × 10⁻⁵ m/s).

**Defining relation**: Darcy (1856). Valid for low-Reynolds laminar flow (Re < ~10); non-Darcian corrections required in karst conduits and very high gradients.

**Typical ranges** (≈ 14 orders of magnitude):
- Clay / shale aquitards: 10⁻¹¹ – 10⁻⁸ m/s.
- Silt and silty sand: 10⁻⁸ – 10⁻⁵ m/s.
- Clean sand: 10⁻⁵ – 10⁻³ m/s.
- Gravel and karst: 10⁻³ – 10⁰ m/s.
- Matrix K vs. bulk K in fractured rock can differ by 6+ orders of magnitude.

**Cross-discipline equivalents**:
- **Geotechnical engineering**: same k controls c_v = k/(γ_w m_v) in Terzaghi consolidation (`CC-geotech-cv`); the consolidation diffusion equation is mathematically identical to the hydraulic-head diffusion equation (`TC-01`).
- **Seismology**: K-contrast at the water table changes Vs by 5–15% via saturation (`CC-seismo-Vs`); fault-zone K modulates induced-seismicity pressure diffusion (`PD-induced-seismicity`).
- **Near-surface geophysics**: ERT and joint inversion (`TC-08`) recover K-proxies via Archie / Waxman-Smits petrophysics.

**When you see this in a paper**: confirm matrix vs. bulk K (fractures dominate bulk values); single-well slug tests give K uncertain by ~order of magnitude; pumping tests integrate over the radius of influence and are not point measurements. K reported without lithology is uninterpretable.

**Anchor citations**:
- Darcy, H. (1856). *Les Fontaines Publiques de la Ville de Dijon*. Victor Dalmont, Paris.
- Freeze, R. A., & Cherry, J. A. (1979). *Groundwater*. Prentice Hall.
- Hsieh, P. A., & Bredehoeft, J. D. (1981). A reservoir analysis of the Denver earthquakes: A case of induced seismicity. *Journal of Geophysical Research: Solid Earth*, 86(B2), 903–920. doi:10.1029/JB086iB02p00903

**Related cards**: `CC-hydro-T`, `CC-hydro-D`, `CC-geotech-cv`, `CC-seismo-Vs`, `TC-01`, `TC-08`, `PD-induced-seismicity`

---

## CC-hydro-T: Transmissivity T [m²/day, m²/s]

**Quantity**: depth-integrated hydraulic conductivity over the saturated thickness b: T = K × b. The horizontal-flow capacity of an aquifer; the variable that pumping-test analysis (Theis 1935; Cooper & Jacob 1946) actually resolves.

**Defining relation**: in the Theis radial-flow solution, drawdown s = (Q/4πT) W(u) where W is the well function and u = r²S/(4Tt). Estimation of T and S proceeds by curve matching or Cooper-Jacob straight-line analysis.

**Typical ranges**:
- Tight aquitards: 10⁻³ – 10⁻¹ m²/day.
- Fine-sand aquifers: 10¹ – 10² m²/day.
- Coarse-sand / glacial outwash: 10² – 10⁴ m²/day.
- Karst and high-yield alluvium: > 10⁴ m²/day.

**Cross-discipline equivalents**:
- **Seismology**: T controls hydraulic-diffusivity-driven pressure migration in `PD-induced-seismicity`; r²/t cloud expansion from a fluid-injection well measures T (via D = T/S; Shapiro & Dinske 2009).
- **Geotechnical engineering**: T is rarely used directly; the equivalent quantity is the integrated drainage capacity of an aquitard during consolidation.

**When you see this in a paper**: confirm units (m²/day vs. m²/s, factor of 86,400). Single-well pumping tests have a radius of influence < 100 m typically and integrate over only that region; basin-scale T from numerical models is regularization-dominated. T reported from specific capacity Q/s alone is a lower bound.

**Anchor citations**:
- Theis, C. V. (1935). The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well using ground-water storage. *Eos, Transactions American Geophysical Union*, 16(2), 519–524. doi:10.1029/TR016i002p00519
- Cooper, H. H., & Jacob, C. E. (1946). A generalized graphical method for evaluating formation constants and summarizing well-field history. *Transactions, American Geophysical Union*, 27(4), 526–534. doi:10.1029/TR027i004p00526
- Hantush, M. S. (1956). Analysis of data from pumping tests in leaky aquifers. *Transactions, American Geophysical Union*, 37(6), 702–714. doi:10.1029/TR037i006p00702

**Related cards**: `CC-hydro-K`, `CC-hydro-S`, `CC-hydro-D`, `MC-hydro-modeling`, `PD-induced-seismicity`

---

## CC-hydro-S: Storativity S, specific storage Sₛ, specific yield Sy [dimensionless, 1/m]

**Quantity**: storage coefficients quantifying the volume of water released per unit area per unit head decline (confined: S, dimensionless) or per unit volume per unit head (specific storage Sₛ, 1/m). For unconfined aquifers, the dominant term is specific yield Sy (drainable porosity, dimensionless). Confined S vs. unconfined Sy differ by 2–4 orders of magnitude and are not interchangeable.

**Defining relation**: Sₛ = ρ g (α_s + n β_w), where α_s is aquifer-skeleton compressibility, n is porosity, β_w is water compressibility. S = Sₛ × b for a confined aquifer. The compressibility link makes Sₛ the hydrologic side of the same mechanical compressibility geotech writes as m_v in consolidation (`CC-geotech-cv`).

**Typical ranges**:
- Confined S: 10⁻⁵ – 10⁻³ (dimensionless).
- Sₛ: 10⁻⁷ – 10⁻⁵ /m.
- Unconfined Sy: 0.05 – 0.30 (dimensionless).
- Karst: variable; effective porosity can be 0.001 – 0.05.

**Cross-discipline equivalents**:
- **Geotechnical engineering**: aquifer compressibility α_s is mechanically the same quantity as m_v in oedometer testing; pumping-induced consolidation (`PD-subsidence-consolidation`) couples through this link.
- **Seismology**: dv/v from ambient noise is sensitive to changes in S × Δh (storage anomaly); the cleanest dv/v ↔ hydrology bridge (`TC-03`).
- **Remote sensing**: GRACE total-water-storage anomalies (`MC-hydro-GRACE`) integrate vertical S × Δh over the satellite footprint.

**When you see this in a paper**: confirm confined vs. unconfined framework; inelastic Sy associated with permanent compaction is distinct from elastic Sₛ. Single-well S estimates are uncertain by an order of magnitude.

**Anchor citations**:
- Jacob, C. E. (1940). On the flow of water in an elastic artesian aquifer. *Eos, Transactions American Geophysical Union*, 21(2), 574–586. doi:10.1029/TR021i002p00574
- Konikow, L. F., & Neuzil, C. E. (2007). A method to estimate groundwater depletion from confining layers. *Water Resources Research*, 43(7), W07417. doi:10.1029/2006WR005597

**Related cards**: `CC-hydro-T`, `CC-hydro-D`, `CC-geotech-cv`, `MC-hydro-GRACE`, `TC-02`, `TC-03`, `PD-subsidence-consolidation`

---

## CC-hydro-D: Hydraulic diffusivity D [m²/s]

**Quantity**: ratio governing the rate of pressure/head propagation: D = T/S = K/Sₛ. The fundamental diffusion coefficient in the pressure-diffusion equation ∂h/∂t = D ∇²h. Spans the same orders of magnitude across substrates as K does.

**Defining relation**: identical mathematical form to the heat equation, to Terzaghi 1D consolidation (`CC-geotech-cv`), and to hillslope sediment-transport diffusion (`CC-geomorph-D`). The shared structure is documented in `TC-01`. In induced seismicity, hydraulic diffusivity is estimated from the r²/t cloud expansion of injection-triggered events (Shapiro & Dinske 2009): r ≈ √(4πDt).

**Typical ranges**:
- Confined aquifer (high T, low S): 10⁰ – 10² m²/s.
- Unconfined aquifer (high T, large Sy): 10⁻² – 10⁰ m²/s.
- Aquitards: 10⁻⁶ – 10⁻³ m²/s.
- Crustal fault zones (from r²/t induced seismicity): 10⁻² – 10¹ m²/s.

**Cross-discipline equivalents**:
- **Geotechnical engineering**: c_v is hydraulic diffusivity under mechanical loading (`CC-geotech-cv`); same equation, different driver.
- **Seismology**: pressure-diffusion drives induced-seismicity cloud expansion (`PD-induced-seismicity`); inversion of r²/t recovers fault-zone D directly.
- **Geomorphology**: hillslope-sediment diffusion κ ≈ 10⁻⁴ m²/yr (much slower; same equation; `CC-geomorph-D`).

**When you see this in a paper**: confirm which D — hydraulic, pressure (poroelastic), thermal, sediment? Time-scale and length-scale span ≥10 orders of magnitude across disciplines. Always state numerator (T or K) and denominator (S or Sₛ) explicitly.

**Anchor citations**:
- Bear, J. (1972). *Dynamics of Fluids in Porous Media*. Elsevier.
- Roeloffs, E. A. (1996). Poroelastic techniques in the study of earthquake-related hydrologic phenomena. *Advances in Geophysics*, 37, 135–195. doi:10.1016/S0065-2687(08)60270-8
- Shapiro, S. A., & Dinske, C. (2009). Fluid-induced seismicity: Pressure diffusion and hydraulic fracturing. *Geophysical Prospecting*, 57(2), 301–310. doi:10.1111/j.1365-2478.2008.00770.x

**Related cards**: `CC-hydro-K`, `CC-hydro-T`, `CC-hydro-S`, `CC-geotech-cv`, `TC-01`, `TC-02`, `PD-induced-seismicity`

---

## CC-hydro-h: Hydraulic head h [m]

**Quantity**: the mechanical energy of groundwater per unit weight: h = z + p/(ρg), where z is elevation head and p/(ρg) is pressure head. In a flowing system the kinetic-energy term v²/(2g) is added but is negligible in slow porous-media flow. h is the scalar potential whose gradient drives Darcy flow: q = −K ∇h.

**Defining relation**: Hubbert's (1940) reformulation of Bernoulli for groundwater. Water flows from high to low h, regardless of relative depth. In a vertical column under hydrostatic conditions, dh/dz = 0; under flow, dh/dz ≠ 0 (downward flow if dh/dz > 0).

**Typical ranges**: regional water-table elevations span from -10 m below sea level (Death Valley, Netherlands polder) to >4,000 m (Tibetan Plateau). Within a watershed, head gradients dh/dx are typically 10⁻⁴ – 10⁻². Confined-aquifer artesian head can exceed land surface (flowing wells).

**Cross-discipline equivalents**:
- **Geotechnical engineering**: h is the same scalar potential whose gradient produces seepage forces in slope-stability analysis (`CC-geotech-FS`); pore pressure p = ρg(h−z) couples to effective stress (`CC-geotech-MohrCoulomb`, `CC-geotech-PorePressure`).
- **Seismology**: head perturbations from earthquake static and dynamic stresses produce well-level oscillations (`PD-eq-hydro-coupling`); dv/v tracks head changes in some settings (`TC-03`).
- **Atmospheric sciences**: atmospheric-pressure loading (barometric efficiency) directly perturbs confined-aquifer head; instructive analog for assessing pore-pressure response times.

**When you see this in a paper**: confirm datum (mean sea level vs. local arbitrary), measurement context (static well vs. flowing, equilibrated vs. transient), and whether the well screens a confined or unconfined unit (h means different things in each).

**Anchor citations**:
- Hubbert, M. K. (1940). The theory of ground-water motion. *The Journal of Geology*, 48(8, Part 1), 785–944. doi:10.1086/624930
- Bear, J. (1972). *Dynamics of Fluids in Porous Media*. Elsevier.

**Related cards**: `CC-hydro-p`, `CC-hydro-K`, `CC-geotech-PorePressure`, `TC-02`, `PD-eq-hydro-coupling`

---

## CC-hydro-p: Pore pressure p [Pa, kPa, MPa]

**Quantity**: fluid pressure in interconnected pore space. Under hydrostatic conditions, p = ρ_w g d where d is depth below the water table; overpressure (p > hydrostatic) is common in sedimentary basins (sealed compartments), subduction zones, and injection scenarios. p is the variable that couples hydrology to the mechanical strength of soil and rock through Terzaghi-Biot effective stress σ' = σ − p.

**Defining relation**: hydrostatic gradient ≈ 9.8 kPa/m (10 MPa/km). Effective stress reduction: σ' = σ − αp (Biot α coefficient; α ≈ 1 for soft soils, 0.6–0.9 for stiff rock). The single most-cited bridge in this corpus is `TC-02`.

**Typical ranges**:
- Hydrostatic gradient: 9.8 kPa/m.
- Crustal lithostatic gradient: ~25 kPa/m (factor 2.5 over hydrostatic).
- Sedimentary-basin overpressures: 10s of MPa above hydrostatic at depth.
- Wastewater-injection wellhead pressures: 1–20 MPa; pressures propagate kilometers along permeable units.
- Earthquake-induced transient pressure changes: 10s of kPa observed in monitoring wells (Hsieh et al. 2006 for 2002 Denali far-field response).

**Cross-discipline equivalents**:
- **Geotechnical engineering**: same p, same Terzaghi σ' (`CC-geotech-MohrCoulomb`); pore-pressure response to undrained loading parameterized by Skempton A, B (`CC-geotech-PorePressure`).
- **Seismology**: pore-pressure modulation of fault strength produces induced seismicity (`PD-induced-seismicity`); post-seismic pore-pressure redistribution drives hydrologic anomalies (`PD-eq-hydro-coupling`).
- **Geomorphology**: rainfall-triggered transient pore pressure is the trigger in Iverson 2000 hillslope landslide mechanics (`PD-AR-landslide`).

**When you see this in a paper**: confirm static vs. transient, hydrostatic vs. overpressured, and the framework: "stress" without qualifier means total stress; "effective stress" is unambiguous.

**Anchor citations**:
- Terzaghi, K. (1943). *Theoretical Soil Mechanics*. Wiley.
- Hubbert, M. K., & Rubey, W. W. (1959). Role of fluid pressure in mechanics of overthrust faulting. *Geological Society of America Bulletin*, 70(2), 115–166. doi:10.1130/0016-7606(1959)70[115:ROFPIM]2.0.CO;2
- Hsieh, P. A., Townend, J., Becker, T. W., & Reichow, M. K. (2006). Hydraulic response of an alluvial aquifer to the 2002 Mw 7.9 Denali fault, Alaska, earthquake. *Bulletin of the Seismological Society of America*, 96(6S), S367–S381. doi:10.1785/0120050823

**Related cards**: `CC-hydro-h`, `CC-geotech-MohrCoulomb`, `CC-geotech-PorePressure`, `CC-seismo-stress`, `TC-02`, `PD-induced-seismicity`, `PD-AR-landslide`, `PD-eq-hydro-coupling`

---

## CC-hydro-ET: Evapotranspiration [mm/day, mm/yr]

**Quantity**: combined water flux from surface evaporation and plant transpiration to the atmosphere. Three nested concepts: reference ET₀ (Penman-Monteith for a standardized grass surface; Allen et al. 1998 FAO-56), potential ET (atmospheric demand limit), and actual ET (constrained by soil-moisture, vegetation, energy balance). Routinely 40–70% of annual P in temperate watersheds; > 90% in arid regions.

**Defining relation**: Penman (1948) combined the surface-energy balance with aerodynamic mass-transfer; Monteith (1965) added canopy resistance r_c. The combination equation gives ET in terms of net radiation R_n, vapor pressure deficit, wind, and r_c. Priestley & Taylor (1972) is the radiation-driven simplification used widely in remote sensing.

**Typical ranges**:
- Reference ET₀: 1 – 8 mm/day depending on climate and season.
- Annual ET in temperate forests: 400 – 800 mm/yr.
- Arid-shrubland actual ET: 100 – 300 mm/yr.
- Tropical rainforest: > 1,500 mm/yr.

**Cross-discipline equivalents**:
- **Ecology**: ET is mechanistically the integrated stomatal conductance × atmospheric demand × leaf area; the same physiological process that fixes carbon (GPP). Eddy-covariance towers (`MC-hydro-eddycov`) measure both fluxes jointly.
- **Atmospheric sciences**: ET is the land-surface boundary condition for atmospheric humidity and the latent-heat term in the surface energy balance; ERA5 (`MC-atm-ERA5`) prescribes / assimilates it.
- **Agricultural sciences**: irrigation scheduling uses crop-coefficient-modified ET₀ to estimate water demand.

**When you see this in a paper**: confirm definition (potential vs. actual vs. reference); the FAO-56 ET₀ in particular is a specific calculation that should not be confused with PET from energy balance. Energy-balance closure error (10–30%) bounds confidence in eddy-covariance ET.

**Anchor citations**:
- Penman, H. L. (1948). Natural evaporation from open water, bare soil and grass. *Proceedings of the Royal Society A*, 193(1032), 120–145. doi:10.1098/rspa.1948.0037
- Monteith, J. L. (1965). Evaporation and environment. *Symposia of the Society for Experimental Biology*, 19, 205–234.
- Priestley, C. H. B., & Taylor, R. J. (1972). On the assessment of surface heat flux and evaporation using large-scale parameters. *Monthly Weather Review*, 100(2), 81–92. doi:10.1175/1520-0493(1972)100<0081:OTAOSH>2.3.CO;2
- Allen, R. G., Pereira, L. S., Raes, D., & Smith, M. (1998). *Crop Evapotranspiration — Guidelines for Computing Crop Water Requirements*. FAO Irrigation and Drainage Paper 56.

**Related cards**: `MC-hydro-eddycov`, `CC-eco-GPP`, `CC-ag-ET0`, `MC-atm-ERA5`, `TC-06`, `PD-drought`

---

## CC-hydro-Q: Streamflow Q and baseflow Q_b [m³/s, ft³/s]

**Quantity**: volumetric water discharge through a stream cross-section. Computed at gauging stations from continuous stage measurement and a stage-discharge rating curve. Baseflow Q_b is the slow, groundwater-fed component obtained by hydrograph separation; the fast component is stormflow/overland flow. ⚠️ **Vocabulary collision**: Q in seismology denotes attenuation (dimensionless; `CC-seismo-Q`); the two are unrelated despite the shared symbol.

**Defining relation**: Q = A × v̄ (cross-sectional area times depth-averaged velocity); rating curve Q = a (H − H_0)^b from gauging campaigns. Annual flow-duration curves, partial-duration extreme-value statistics (`TC-04`), and baseflow recession constants are the standard derived quantities.

**Typical ranges**:
- Headwater streams: 10⁻³ – 10⁰ m³/s.
- Mid-size rivers: 10⁰ – 10² m³/s.
- Major rivers (Mississippi, Amazon): 10⁴ – 10⁵ m³/s.
- Baseflow index BFI: 0.2 – 0.8 depending on basin geology.

**Cross-discipline equivalents**:
- **Seismology**: high-frequency seismic noise PSD correlates with stream discharge through bedload transport (Burtin et al. 2008; `CC-seismo-noise`).
- **Geomorphology**: Q controls sediment-transport stream power; flood-frequency power-law statistics share machinery with Gutenberg-Richter (`TC-04`).
- **Ecology**: indicators of hydrologic alteration (IHA, `CC-eco-IHA`) translate Q regimes into ecologically meaningful metrics (timing, duration, frequency of floods and droughts).

**When you see this in a paper**: confirm daily mean vs. instantaneous peak vs. annual statistic; rating-curve uncertainty grows toward extremes (≥50% uncertainty for return periods beyond the calibration range); regulated vs. natural status determines whether Q can be compared across watersheds.

**Anchor citations**:
- Hewlett, J. D., & Hibbert, A. R. (1967). Factors affecting the response of small watersheds to precipitation in humid areas. *Forest Hydrology*, 275–290.
- Tasker, G. D., & Stedinger, J. R. (1989). An operational GLS model for hydrologic regression. *Journal of Hydrology*, 111(1–4), 361–375. doi:10.1016/0022-1694(89)90268-0
- Burtin, A., Bollinger, L., Vergne, J., Cattin, R., & Nábělek, J. L. (2008). Spectral analysis of seismic noise induced by rivers: A new tool to monitor spatiotemporal changes in stream hydrodynamics. *Journal of Geophysical Research: Solid Earth*, 113(B5), B05301. doi:10.1029/2007JB005034

**Related cards**: `MC-hydro-NWIS`, `CC-seismo-noise`, `CC-geomorph-streampower`, `CC-eco-IHA`, `TC-04`, `TC-06`, `PD-AR-landslide`, `PD-drought`

---

## CC-hydro-recharge: Groundwater recharge R [mm/yr]

**Quantity**: vertical flux of water across the water table into the saturated zone. Diffuse recharge (areal infiltration through the vadose zone) and focused recharge (through losing streams, ponds, fractures) are mechanistically distinct and rarely partitioned cleanly. The single most uncertain term in basin water balances.

**Defining relation**: estimation methods include water-table fluctuation R = Sy × Δh/Δt; chloride mass balance R = (P × Cl_P)/Cl_gw; tritium and CFC age-dating (`MC-hydro-isotopes`); soil-water-budget modeling. Estimates from different methods at the same site routinely differ by factors of 2–10 (Healy & Cook 2002; Scanlon et al. 2002).

**Typical ranges**:
- Arid and semi-arid (P < 250 mm/yr): 1 – 10 mm/yr.
- Mediterranean and humid temperate: 50 – 300 mm/yr.
- Tropical wet: 200 – 1,000 mm/yr.
- Urban infiltration through leaking infrastructure: highly variable, often > natural rates.

**Cross-discipline equivalents**:
- **Atmospheric sciences**: recharge is the residual P − ET − Q − ΔS in the watershed mass balance (`TC-06`); atmospheric forcing controls long-term mean recharge.
- **Ecology**: deep-rooted vegetation can intercept and transpire would-be-recharge water; ecosystem changes (afforestation, deforestation) alter R substantially.
- **Agricultural sciences**: irrigation return flow is anthropogenic recharge; overdraft when extraction > recharge (`PD-aquifer-depletion`).

**When you see this in a paper**: identify the method; tritium and CFC age-dating measures mean transit time, not instantaneous flux; chloride mass balance requires steady-state assumptions that climate change increasingly violates.

**Anchor citations**:
- Healy, R. W., & Cook, P. G. (2002). Using groundwater levels to estimate recharge. *Hydrogeology Journal*, 10(1), 91–109. doi:10.1007/s10040-001-0178-0
- Scanlon, B. R., Healy, R. W., & Cook, P. G. (2002). Choosing appropriate techniques for quantifying groundwater recharge. *Hydrogeology Journal*, 10(1), 18–39. doi:10.1007/s10040-001-0176-2

**Related cards**: `CC-hydro-ET`, `MC-hydro-isotopes`, `MC-hydro-modeling`, `TC-06`, `PD-aquifer-depletion`, `PD-drought`
