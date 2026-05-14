---
discipline: atmospheric_sciences
card_type: concept
schema_version: v3
---

# Atmospheric sciences — concept cards

Each card defines one core atmospheric variable, equation, or measured quantity, with units, numerical ranges, and explicit hooks into the other Gaia disciplines. Format follows `docs/card_format_spec.md`.

---

## CC-atm-T: Temperature, potential temperature, and atmospheric stability [K, °C]

**Quantity**: air temperature T [K, °C]; potential temperature θ = T (p₀/p)^(R/cₚ) is T mapped to a reference pressure (typically 1000 hPa) and is conserved under adiabatic motion. Equivalent potential temperature θ_e includes latent-heat content and is conserved under both dry and moist-adiabatic motion. Buoyancy frequency N² = (g/θ)(∂θ/∂z) sets atmospheric static stability.

**Defining relation**: ideal gas p = ρ R T; first law cₚ dT − (1/ρ) dp = δq drives adiabatic and diabatic temperature changes. Lapse rate Γ = −∂T/∂z; dry-adiabatic Γ_d ≈ 9.8 K/km; moist-adiabatic Γ_m ≈ 4–6 K/km depending on q.

**Typical ranges**:
- Surface T globally: 220–320 K (−50° to +50 °C).
- Tropopause T: 200–220 K mid-latitudes, 190 K equatorial.
- Stratosphere: increases with height to ~270 K at stratopause.
- Conditional instability: ∂θ_e/∂z < 0 in unstable cloud-bearing layers.

**Cross-discipline equivalents**:
- **Hydrology**: T controls saturation vapor pressure via Clausius-Clapeyron; sets ET demand (`CC-hydro-ET`).
- **Ecology**: T drives phenology, growing-season length, stomatal conductance; the dominant climate-control variable on GPP.
- **Geomorphology**: long-term T sets weathering rates and freeze-thaw cycles; permafrost thaw `PD-permafrost-thaw`.
- **Seismology**: thermoelastic forcing of dv/v at near-surface depths (Hillers et al. 2015); seasonal T cycle creates a 10⁻⁴-scale dv/v signal that must be separated from hydrologic signals (`TC-03`).

**When you see this in a paper**: distinguish T (instantaneous), θ (adiabatically conserved), θ_e (moist-adiabatic conserved). Stability discussions require θ or θ_e, not T. Surface-T trends vs. tropospheric-mean T trends are different observables under climate change.

**Anchor citations**:
- Wallace, J. M., & Hobbs, P. V. (2006). *Atmospheric Science: An Introductory Survey* (2nd ed.). Academic Press.
- Held, I. M., & Soden, B. J. (2006). Robust responses of the hydrological cycle to global warming. *Journal of Climate*, 19(21), 5686–5699. doi:10.1175/JCLI3990.1

**Related cards**: `CC-atm-q`, `CC-atm-PBL`, `CC-hydro-ET`, `CC-eco-GPP`, `TC-03`, `PD-heat-dome`, `PD-permafrost-thaw`

---

## CC-atm-q: Specific humidity, vapor pressure deficit, Clausius-Clapeyron [kg/kg, Pa]

**Quantity**: specific humidity q [kg water / kg moist air]; mixing ratio r ≈ q for q ≪ 1; vapor pressure e [Pa] and saturation e_sat(T) [Pa]; relative humidity RH = e/e_sat; vapor pressure deficit VPD = e_sat − e. Clausius-Clapeyron sets e_sat(T) and thus the thermodynamic ceiling on atmospheric water content.

**Defining relation**: Clausius-Clapeyron de_sat/dT ≈ L_v e_sat / (R_v T²); roughly 7%/K increase in saturation vapor pressure (Held & Soden 2006). At fixed RH, q increases ~7%/K with warming — the anchor of intensifying precipitation extremes. Total column water vapor TCWV (also called integrated water vapor IWV) is the depth-integrated q ρ.

**Typical ranges**:
- Surface q in cold dry air: ≈ 1 g/kg.
- Surface q tropical maritime: ≈ 20 g/kg.
- TCWV / IWV: 5–70 mm; atmospheric rivers exceed 30 mm (Ralph et al. 2019).
- VPD over moist canopies: 0.5–2 kPa typical; > 4 kPa during heat-dome events.

**Cross-discipline equivalents**:
- **Hydrology**: q sets ET demand through VPD; Penman-Monteith ET₀ (`CC-hydro-ET`) reduces to a VPD-and-radiation function.
- **Ecology**: VPD drives stomatal closure; the proximate mechanism for drought-induced GPP reduction and forest mortality (Williams et al. 2013; `PD-forest-mortality`).
- **Agricultural sciences**: VPD controls crop water demand; `CC-ag-ET0` Penman-Monteith uses the same e_sat − e term.

**When you see this in a paper**: confirm RH vs. q vs. VPD reporting — they convey different information. Clausius-Clapeyron-scaled changes in q are robust across models; precipitation-extreme scaling can exceed 7%/K when convective dynamics intensify (Trenberth 2011).

**Anchor citations**:
- Held, I. M., & Soden, B. J. (2006). Robust responses of the hydrological cycle to global warming. *Journal of Climate*, 19(21), 5686–5699. doi:10.1175/JCLI3990.1
- Trenberth, K. E. (2011). Changes in precipitation with climate change. *Climate Research*, 47(1–2), 123–138. doi:10.3354/cr00953
- Williams, A. P., et al. (2013). Temperature as a potent driver of regional forest drought stress and tree mortality. *Nature Climate Change*, 3(3), 292–297. doi:10.1038/nclimate1693

**Related cards**: `CC-atm-T`, `CC-atm-precip`, `CC-hydro-ET`, `CC-eco-GPP`, `CC-ag-ET0`, `PD-flash-drought`, `PD-heat-dome`, `TC-15`

---

## CC-atm-precip: Precipitation [mm/day, mm/h, kg/m²/s]

**Quantity**: rate of liquid + frozen water arrival at the surface. SI: kg/m²/s; conventionally mm/day or mm/h (1 mm = 1 kg/m² ≈ 1 L/m²). Includes rainfall, snowfall (snow water equivalent SWE), graupel, hail. Time- and space-integrated: returns from satellite (GPM/IMERG), gauge (NWS COOP, SNOTEL), radar (NEXRAD), and reanalysis (`MC-atm-ERA5`).

**Defining relation**: Clausius-Clapeyron sets a thermodynamic ceiling on column moisture; precipitation rate scales with column moisture × residence time × convergence. Extreme-precipitation intensification under warming exceeds the 7%/K thermodynamic rate when convective dynamics also intensify (Lenderink & van Meijgaard 2008; Westra et al. 2014). AR-driven precipitation in the U.S. West delivers 30–50% of annual P in a handful of multi-day events (Ralph et al. 2019).

**Typical ranges**:
- Global mean: ≈ 2.7 mm/day (≈ 1,000 mm/yr).
- Wet temperate (PNW windward Cascades): 2,000–5,000 mm/yr.
- Arid: < 250 mm/yr.
- Extreme rates: ARs deliver 100–500 mm in 24 h; mesoscale convective systems exceed 100 mm/h at thunderstorm cores.

**Cross-discipline equivalents**:
- **Hydrology**: P is the forcing for the watershed water balance P = ET + Q + ΔS (`TC-06`); USGS NWIS streamflow is the immediate downstream observable.
- **Geomorphology**: extreme P drives landslide and debris-flow triggering (`PD-AR-landslide`, `PD-debris-flow`) and channel-forming floods (`PD-river-floods`).
- **Ecology / agriculture**: P timing controls phenology and crop water-stress windows; flash drought develops on weeks-to-months timescales when P deficit + high VPD coincide (`PD-flash-drought`).
- **Seismology**: P-induced soil-moisture loading produces a measurable dv/v signal (`TC-03`); microseisms intensify with storm activity (`PD-microseism`).

**When you see this in a paper**: confirm gauge vs. radar QPE vs. satellite product; the three can differ by factor 2 in mountainous terrain. Extreme-event return periods are sensitive to record length and nonstationarity assumption.

**Anchor citations**:
- Ralph, F. M., Rutz, J. J., Cordeira, J. M., Dettinger, M., Anderson, M., Reynolds, D., Schick, L. J., & Smallcomb, C. (2019). A scale to characterize the strength and impacts of atmospheric rivers. *Bulletin of the American Meteorological Society*, 100(2), 269–289. doi:10.1175/BAMS-D-18-0023.1
- Westra, S., et al. (2014). Future changes to the intensity and frequency of short-duration extreme rainfall. *Reviews of Geophysics*, 52(3), 522–555. doi:10.1002/2014RG000464

**Related cards**: `CC-atm-q`, `CC-atm-IVT`, `CC-hydro-Q`, `CC-hydro-ET`, `CC-hydro-recharge`, `PD-atmospheric-river`, `PD-AR-landslide`, `PD-river-floods`, `TC-06`, `TC-15`

---

## CC-atm-wind: Wind, geostrophic balance, jets [m/s]

**Quantity**: three-dimensional wind vector (u, v, w) [m/s]. Surface wind (10 m) is the conventional engineering reference. Geostrophic wind u_g = (1/fρ) k × ∇p balances pressure gradient against Coriolis at synoptic scales (Rossby number Ro = U/(fL) ≪ 1). Jets — subtropical, polar, low-level — concentrate horizontal momentum in narrow bands.

**Defining relation**: primitive equations (rotating Navier-Stokes + continuity + thermodynamic energy + moisture). Surface stress τ = ρ C_D U² couples wind to ocean and land-surface; drives ocean swell (the source of microseisms via `PD-microseism`) and aeolian sediment transport.

**Typical ranges**:
- Surface 10-m wind: 0–30 m/s globally; gusts exceed 50 m/s in extreme storms.
- Jet stream cores at ~10 km altitude: 50–100 m/s, exceeding 150 m/s in winter.
- AR low-level jets: 20–40 m/s at 1–2 km altitude.

**Cross-discipline equivalents**:
- **Seismology**: wind-driven ocean swell generates microseisms (Longuet-Higgins 1950, `PD-microseism`); near-surface wind couples directly to seismic noise at high frequencies (`CC-seismo-noise`).
- **Geomorphology**: surface wind drives aeolian erosion and dust transport (Dust Bowl historical; modern Sahara-Atlantic dust). Strong winds amplify post-fire erosion (`PD-post-fire-erosion`).
- **Ecology**: tree-sway wind biases ambient seismic noise PSD; storm wind drives blowdown disturbance.
- **Atmospheric → hydrology**: wind enters Penman-Monteith ET through the aerodynamic-resistance term.

**When you see this in a paper**: confirm reference height (10 m vs. boundary-layer mean vs. jet-level); surface winds underestimate jet intensity by factors of 3–10. Wind-energy site characterization uses 50- to 100-m reference heights and Weibull statistics.

**Anchor citations**:
- Holton, J. R. (2004). *An Introduction to Dynamic Meteorology* (4th ed.). Academic Press.
- Longuet-Higgins, M. S. (1950). A theory of the origin of microseisms. *Phil. Trans. R. Soc. Lond. A*, 243(857), 1–35. doi:10.1098/rsta.1950.0012

**Related cards**: `CC-atm-pressure`, `CC-atm-PBL`, `CC-seismo-noise`, `PD-microseism`, `PD-atmospheric-river`, `PD-post-fire-erosion`

---

## CC-atm-pressure: Surface pressure, geopotential height, microseism forcing [Pa, hPa, m]

**Quantity**: atmospheric pressure p [Pa, hPa]; surface pressure ≈ 1013 hPa global mean. Geopotential height Z [m] is the pressure-level altitude in a constant-gravity sense. Pressure gradients drive wind; pressure loading is also the direct mechanism by which atmospheric mass transfer drives microseisms (`PD-microseism`) and barometric perturbations of confined-aquifer head.

**Defining relation**: hydrostatic balance ∂p/∂z = −ρg. Geopotential thickness Z_top − Z_bottom = R T̄ / g × ln(p_bot/p_top): thicker layers indicate warmer columns. Surface-pressure loading propagates into the solid Earth as a real, measurable load.

**Typical ranges**:
- Surface p: 870 hPa (deep tropical cyclones; Typhoon Tip 1979) to 1080 hPa (Siberian winter highs).
- Diurnal solar tide amplitude: ~2 hPa.
- Storm passing a station: 10–50 hPa drop over hours.
- 500 hPa height (mid-troposphere): 5,400–5,900 m typical; climate-change-driven thickening.

**Cross-discipline equivalents**:
- **Seismology**: large-amplitude pressure systems load the surface; pressure perturbations contribute to the seismic noise PSD at long periods (Earth's hum mechanism; `CC-seismo-noise`). The same coupling generates microseisms via ocean-wave-wave interaction (`PD-microseism`).
- **Hydrology**: barometric pressure changes perturb confined-aquifer head; barometric efficiency = Δh/Δp_atm, a diagnostic of aquifer confinement (`CC-hydro-h`).
- **Geotechnical engineering**: large-pressure-system passage produces 10s of kPa transient stress changes — generally small for engineering structures but measurable on instrumented dams.

**When you see this in a paper**: confirm whether p is at the station, at sea level (mean-sea-level-corrected), or at a constant pressure level; the three are different. Barometric-pressure corrections for groundwater hydrology are routine but easily misapplied.

**Anchor citations**:
- Holton, J. R. (2004). *An Introduction to Dynamic Meteorology* (4th ed.). Academic Press.
- Tanimoto, T. (2005). The oceanic excitation hypothesis for the continuous oscillations of the Earth. *Geophysical Journal International*, 160(1), 276–288. doi:10.1111/j.1365-246X.2005.02484.x

**Related cards**: `CC-atm-wind`, `CC-atm-T`, `CC-seismo-noise`, `CC-hydro-h`, `PD-microseism`, `PD-atmospheric-river`

---

## CC-atm-radiation: Radiative fluxes and surface energy balance [W/m²]

**Quantity**: shortwave (SW, 0.3–4 µm) and longwave (LW, 4–100 µm) radiative fluxes [W/m²]. Net radiation R_n = SW_↓(1−α) + LW_↓ − LW_↑, where α is surface albedo. R_n drives the surface energy balance R_n = H + LE + G (sensible heat H + latent heat LE = ρ λ ET + ground heat G), the boundary condition for ET and atmospheric boundary-layer dynamics.

**Defining relation**: Stefan-Boltzmann LW_↑ = εσT⁴ (ε emissivity, σ Stefan-Boltzmann constant); two-stream radiative transfer approximations propagate SW and LW through cloudy atmospheres. Beer's law SW(z) = SW_0 exp(−τ) attenuates through optical depth τ. Earth's radiation budget at top-of-atmosphere now imbalanced by +0.5 to +1.0 W/m² (Loeb et al. 2021), driving the present rate of climate change.

**Typical ranges**:
- Solar constant SW_TOA: ≈ 1,361 W/m² (incident on perpendicular face).
- Global-mean SW_↓ at surface: ≈ 185 W/m²; LW_↓: ≈ 340 W/m².
- Surface albedo: 0.05 (dark ocean) to 0.85 (fresh snow).
- Net R_n at midday clear: 600–800 W/m² over vegetation.

**Cross-discipline equivalents**:
- **Hydrology**: R_n is the energy source for ET (`CC-hydro-ET`); eddy covariance closes the energy balance (`MC-hydro-eddycov`).
- **Ecology**: PAR (photosynthetically active radiation, 0.4–0.7 µm) drives GPP through photosynthesis; vegetation albedo and LAI couple back to radiation (`CC-eco-GPP`, `CC-eco-LAI`).
- **Geomorphology**: insolation drives weathering rates; aspect-dependent radiation produces north-south slope asymmetry in some landscapes.
- **Agricultural sciences**: PAR + temperature + water = the proximate drivers of crop yield in light- and water-limited regimes.

**When you see this in a paper**: confirm whether SW is shortwave-down, net SW (down − up), or PAR; whether LW is up, down, or net; whether R_n is computed or directly measured (4-component radiometer). Albedo varies seasonally and after disturbance (post-fire albedo drops for years).

**Anchor citations**:
- Trenberth, K. E., Fasullo, J. T., & Kiehl, J. (2009). Earth's global energy budget. *Bulletin of the American Meteorological Society*, 90(3), 311–323. doi:10.1175/2008BAMS2634.1
- Loeb, N. G., Johnson, G. C., Thorsen, T. J., Lyman, J. M., Rose, F. G., & Kato, S. (2021). Satellite and ocean data reveal marked increase in Earth's heating rate. *Geophysical Research Letters*, 48(13), e2021GL093047. doi:10.1029/2021GL093047

**Related cards**: `CC-atm-T`, `CC-hydro-ET`, `CC-eco-GPP`, `CC-eco-LAI`, `CC-ag-ET0`, `MC-hydro-eddycov`

---

## CC-atm-PBL: Atmospheric boundary layer [m, dimensionless]

**Quantity**: the lowest layer of the troposphere directly coupled to the surface through turbulent fluxes. Depth h_PBL [m] ranges 100 m (stable nocturnal) to 3,000 m (deep convective). The layer where surface-atmosphere exchange occurs; the conduit between Earth-system surface fluxes (ET, NEE, sensible heat) and the free troposphere.

**Defining relation**: bulk Richardson number Ri_b = (g/θ) Δθ Δz / (Δu)² discriminates stable (Ri_b > 0.25), neutral, and unstable layers. Turbulent fluxes parameterized via Monin-Obukhov similarity theory (Monin & Obukhov 1954); friction velocity u* = (τ/ρ)^(1/2) sets the scaling.

**Typical ranges**:
- Stable nocturnal PBL depth: 50–500 m.
- Daytime convective PBL: 500–3,000 m, deepest over hot dry surfaces.
- Marine PBL: 500–1,500 m, capped by trade-wind inversion.
- Friction velocity u*: 0.05–1.0 m/s typical.

**Cross-discipline equivalents**:
- **Hydrology / ecology**: eddy-covariance towers (`MC-hydro-eddycov`) measure H, LE, F_C in the surface layer of the PBL; u* filtering is required for nighttime stable conditions where turbulence breaks down.
- **Atmospheric forecasting**: PBL parameterizations are a leading source of NWP and reanalysis error; ERA5 PBL height has known biases over heterogeneous land.
- **Air quality**: PBL height sets ground-level pollutant concentrations; shallow PBL = high concentrations.

**When you see this in a paper**: confirm PBL-height definition (parcel method, Ri-based, bulk Ri threshold, virtual θ gradient); methods can differ by 30–50%. Nighttime fluxes from eddy covariance during stable conditions are unreliable without proper u* filtering.

**Anchor citations**:
- Stull, R. B. (1988). *An Introduction to Boundary Layer Meteorology*. Springer. doi:10.1007/978-94-009-3027-8
- Monin, A. S., & Obukhov, A. M. (1954). Basic laws of turbulent mixing in the surface layer of the atmosphere. *Trudy Geofizicheskogo Instituta AN SSSR*, 24(151), 163–187.

**Related cards**: `CC-atm-T`, `CC-atm-wind`, `MC-hydro-eddycov`, `CC-hydro-ET`, `CC-eco-GPP`

---

## CC-atm-IVT: Integrated vapor transport and atmospheric river characterization [kg/(m·s)]

**Quantity**: vertically integrated horizontal water-vapor transport IVT = ∫(q V) dp/g over the atmospheric column [kg/(m·s)]. The canonical characterization of atmospheric rivers — ARs are typically defined as IVT > 250 kg/(m·s) sustained over > 2,000 km × < 1,000 km filamentary structures. Ralph et al. (2019) AR Scale (1–5) is set by peak IVT and event duration.

**Defining relation**: AR identification algorithms (ARDT, Guan & Waliser 2015) threshold reanalysis IVT fields temporally and spatially to extract AR objects. AR Scale: AR-1 (weak, IVT 250–500), AR-3 (strong, 750–1,000), AR-5 (exceptional, > 1,250), with secondary axis for duration. Two AR-5 events struck California in January 2017 and January 2023 with major impacts (Ralph et al. 2019; State of California DWR reports).

**Typical ranges**:
- Background mid-latitude IVT: 100–250 kg/(m·s).
- Weak AR (AR-1): 250–500 kg/(m·s).
- Strong AR (AR-3): 750–1,000 kg/(m·s).
- Exceptional AR (AR-5): > 1,250 kg/(m·s); record events approach 2,000.

**Cross-discipline equivalents**:
- **Hydrology**: AR landfall is the primary trigger for PNW and California winter floods (`PD-river-floods`); orographic enhancement multiplies precipitation rates 2–5× on windward slopes (`CC-atm-precip`).
- **Geomorphology**: ARs drive shallow landslides (`PD-AR-landslide`), debris flows (`PD-debris-flow`), and channel-forming floods (`PD-river-floods`).
- **Geotechnical engineering**: AR-driven precipitation drives embankment pore-pressure rise (`PD-dam-levee-safety`).
- **Ecology**: AR-delivered moisture replenishes mountain snowpack and groundwater that supports late-summer ecological flows.

**When you see this in a paper**: confirm AR-identification algorithm (Guan-Waliser vs. Rutz vs. Mundhenk); different algorithms classify the same event differently at the margins. AR Scale reporting is increasingly standard for impact attribution.

**Anchor citations**:
- Ralph, F. M., Rutz, J. J., Cordeira, J. M., Dettinger, M., Anderson, M., Reynolds, D., Schick, L. J., & Smallcomb, C. (2019). A scale to characterize the strength and impacts of atmospheric rivers. *Bulletin of the American Meteorological Society*, 100(2), 269–289. doi:10.1175/BAMS-D-18-0023.1
- Guan, B., & Waliser, D. E. (2015). Detection of atmospheric rivers: Evaluation and application of an algorithm for global studies. *Journal of Geophysical Research: Atmospheres*, 120(24), 12514–12535. doi:10.1002/2015JD024257

**Related cards**: `CC-atm-q`, `CC-atm-precip`, `CC-hydro-Q`, `PD-atmospheric-river`, `PD-AR-landslide`, `PD-river-floods`, `PD-dam-levee-safety`, `TC-15`
