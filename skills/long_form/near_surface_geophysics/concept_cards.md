---
discipline: near_surface_geophysics
card_type: concept
schema_version: v3
---

# Near-surface geophysics — concept cards

Each card defines one core near-surface-geophysics variable, equation, or measured quantity, with units, numerical ranges, and explicit hooks into the other Gaia disciplines. Format follows `docs/card_format_spec.md`.

Near-surface geophysics is the connective tissue between the deep-Earth and surface-Earth disciplines: it images the substrate that hydrology, geomorphology, geotechnical engineering, ecology, and agriculture all care about, using physics shared with seismology (elastic waves), electromagnetics, and gravity / magnetics.

---

## CC-nsg-resistivity: Electrical resistivity and Archie's law [Ω·m, S/m]

**Quantity**: bulk electrical resistivity ρ_e [Ω·m] (or its inverse, electrical conductivity σ = 1/ρ_e [S/m]). The dominant subsurface property recovered by ERT (`MC-nsg-ERT`), EM methods, and electrical logging. In water-bearing porous media, resistivity is controlled by porosity, water saturation, water-pore-fluid conductivity, and clay content, with Archie's law (Archie 1942) as the foundational petrophysical link.

**Defining relation**: Archie's law (clean sands, no clay): σ_bulk = (σ_w × φ^m × S_w^n), where σ_w is pore-water conductivity, φ is porosity, S_w is water saturation, and m (cementation exponent ≈ 1.3–2.5) and n (saturation exponent ≈ 1.5–2.5) are material parameters. Waxman-Smits (1968) extends to clay-bearing rocks by adding a surface-conduction term. Mostly empirical; the bridge from geophysical observation to hydrology, agriculture, and contaminant transport.

**Typical ranges**:
- Clay-bearing sediments: 1–30 Ω·m.
- Fresh-water-saturated sand and silt: 10–100 Ω·m.
- Saline / contaminated groundwater: 0.1–5 Ω·m.
- Crystalline bedrock: 100–10,000 Ω·m.
- Air-filled (above water table): 1,000–100,000 Ω·m.

**Cross-discipline equivalents**:
- **Hydrology**: bulk σ ↔ water saturation S_w (`CC-hydro-h` water-table depth, `CC-hydro-S` storage) via Archie's law; the foundational petrophysical link for hydrogeophysics (Binley et al. 2015).
- **Seismology**: joint with `CC-seismo-Vs` via shared substrate (`TC-08`); resistivity and seismic Vs respond differently to saturation and lithology, providing complementary information.
- **Geotechnical engineering**: high conductivity in saturated, low-strength soils helps liquefaction-susceptibility mapping; clay-content estimation feeds `CC-geotech-MohrCoulomb` characterization.
- **Agricultural sciences**: in-field σ maps used for soil-texture / salinity / drainage zoning at the precision-agriculture scale; same Archie's-law machinery.

**When you see this in a paper**: confirm Archie's m and n values used (often defaults are misapplied to clay-bearing settings); whether Waxman-Smits surface-conduction is included; whether the inversion is a 1D, 2D, or 3D recovery. Resistivity is highly non-unique without independent constraints on porosity or fluid chemistry.

**Anchor citations**:
- Archie, G. E. (1942). The electrical resistivity log as an aid in determining some reservoir characteristics. *Transactions of the AIME*, 146(1), 54–62. doi:10.2118/942054-G
- Waxman, M. H., & Smits, L. J. M. (1968). Electrical conductivities in oil-bearing shaly sands. *Society of Petroleum Engineers Journal*, 8(2), 107–122. doi:10.2118/1863-A
- Binley, A., Hubbard, S. S., Huisman, J. A., Revil, A., Robinson, D. A., Singha, K., & Slater, L. D. (2015). The emergence of hydrogeophysics for improved understanding of subsurface processes over multiple scales. *Water Resources Research*, 51(6), 3837–3866. doi:10.1002/2015WR017016

**Related cards**: `CC-nsg-permittivity`, `CC-nsg-EM-conductivity`, `CC-hydro-h`, `CC-seismo-Vs`, `MC-nsg-ERT`, `MC-nsg-AEM`, `TC-08`, `TC-19`

---

## CC-nsg-permittivity: Relative dielectric permittivity for GPR and water content [dimensionless]

**Quantity**: relative dielectric permittivity ε_r (also written ε' or just ε) [dimensionless], the ratio of the medium's permittivity to vacuum permittivity ε_0. Critical for ground-penetrating radar (GPR; `MC-nsg-GPR`) because radar velocity v = c/√(ε_r μ_r) and reflection coefficients depend on ε contrast. Tightly coupled to volumetric water content θ via Topp's equation (Topp, Davis & Annan 1980): ε_r ≈ 3 + 9.3θ + 146θ² − 76.7θ³. This is the petrophysical link from GPR observation to soil moisture.

**Defining relation**: Topp (1980) for soil θ → ε_r; Hilhorst (2000) for inverse θ from ε_r in TDR/FDR sensors. GPR two-way travel time t = 2d/v relates reflector depth d to ε_r-derived velocity. Frequency-dependent ε_r in clay-rich and highly conductive soils requires complex-permittivity treatment.

**Typical ranges**:
- Air: ε_r = 1; velocity ≈ 0.3 m/ns.
- Dry sand and rock: ε_r = 3–6; v ≈ 0.13 m/ns.
- Moist sand: ε_r = 10–25; v ≈ 0.06–0.10 m/ns.
- Saturated sand: ε_r ≈ 25; v ≈ 0.06 m/ns.
- Water: ε_r ≈ 80; v ≈ 0.033 m/ns.
- Clay-rich soils: ε_r highly variable, often > 30 due to clay-water interactions.

**Cross-discipline equivalents**:
- **Hydrology**: GPR-derived θ from ε_r is a direct soil-moisture method (Huisman et al. 2003) at the m-scale resolution; complementary to point sensors (`MC-ag-soil-moisture`) and footprint-scale COSMOS (`MC-hydro-COSMOS`).
- **Agricultural sciences**: precision-agriculture soil-moisture mapping in real time; root-zone characterization.
- **Geomorphology**: GPR images soil-bedrock interface (regolith depth) for soil-production rate inversions (Heimsath 1997 framework); complements lidar topography (`MC-geomorph-lidar`).

**When you see this in a paper**: confirm GPR frequency (typically 100 MHz – 1 GHz), the ε_r → θ conversion (Topp vs. site-specific), and antenna geometry. GPR is highly attenuating in saline / conductive ground; penetration depth varies by ~10× across PNW soil types.

**Anchor citations**:
- Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content: Measurements in coaxial transmission lines. *Water Resources Research*, 16(3), 574–582. doi:10.1029/WR016i003p00574
- Huisman, J. A., Hubbard, S. S., Redman, J. D., & Annan, A. P. (2003). Measuring soil water content with ground penetrating radar: A review. *Vadose Zone Journal*, 2(4), 476–491. doi:10.2136/vzj2003.4760

**Related cards**: `CC-nsg-resistivity`, `MC-nsg-GPR`, `MC-hydro-COSMOS`, `MC-ag-soil-moisture`, `MC-geomorph-lidar`

---

## CC-nsg-impedance: Acoustic impedance and reflection coefficient [Pa·s/m, kg/(m²·s)]

**Quantity**: acoustic impedance Z = ρ V [kg/(m²·s)], the product of bulk density and elastic-wave velocity (P-wave Vp or S-wave Vs). Reflection coefficient at a layer interface R = (Z₂ − Z₁)/(Z₂ + Z₁) determines the amplitude of reflected energy in seismic reflection surveys. The mechanism by which seismic methods image subsurface structure; foundational for reflection seismology at all scales from cm (engineering site investigation) to km (deep-Earth tomography).

**Defining relation**: P-wave impedance Z_P = ρ V_p; S-wave impedance Z_S = ρ V_s; reflectivity ∝ ΔZ/Z. In porous media: Gassmann (1951) couples bulk modulus changes to fluid saturation, the petrophysical link for hydrocarbon and water-saturation discrimination.

**Typical ranges**:
- Air: Z = 414 Pa·s/m.
- Water: Z = 1.5 × 10⁶ Pa·s/m.
- Soft saturated sediments: Z = 1–3 × 10⁶ Pa·s/m.
- Crystalline bedrock: Z = 10–20 × 10⁶ Pa·s/m.
- Reflection coefficient at typical sediment-bedrock interface: R = 0.3–0.5.

**Cross-discipline equivalents**:
- **Seismology**: same impedance physics across all scales; the reflection coefficient in near-surface refraction and reflection surveys is the same equation as in crustal reflection seismology.
- **Geotechnical engineering**: V_s and density together give the impedance contrast that controls site amplification (`PD-site-response`, `MC-geotech-numerical`); the engineering bridge.
- **Hydrology**: water saturation modifies V_p via Gassmann; time-lapse seismic methods can monitor saturation changes (`TC-03` dv/v and related).

**When you see this in a paper**: confirm whether the work is reflection-based (R from impedance contrasts) or refraction-based (velocity contrasts); for hydrology applications, the Gassmann assumption requires fluid-saturated porous-media validation.

**Anchor citations**:
- Gassmann, F. (1951). Über die Elastizität poröser Medien. *Vierteljahrsschrift der Naturforschenden Gesellschaft in Zürich*, 96, 1–23.
- Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.). University Science Books.

**Related cards**: `CC-seismo-Vs`, `CC-nsg-permittivity`, `MC-seismo-MASW`, `MC-geotech-HVSR`, `MC-nsg-refraction`, `TC-08`

---

## CC-nsg-EM-conductivity: Electromagnetic conductivity from TEM, FEM, AEM [S/m]

**Quantity**: bulk conductivity σ [S/m] measured by electromagnetic induction. Time-domain electromagnetic methods (TEM) inject a current pulse and measure the decay of induced secondary fields; frequency-domain (FEM) measure phase and amplitude at multiple frequencies; airborne EM (AEM) flies these systems from helicopter or fixed-wing aircraft. The dominant tool for mapping aquifer architecture, brackish-fresh water interfaces, and contaminant plumes at regional scale.

**Defining relation**: Maxwell's equations propagate induced fields through a conductive subsurface; inversion of decay curves or phase-amplitude curves recovers σ(z) profiles. AEM provides km-scale coverage at airborne-altitude speed (~100 km/hr); ground EM (e.g., Geonics EM31, EM34, EM38) provides high spatial density at field-scale.

**Typical ranges**:
- Same as `CC-nsg-resistivity` range (σ = 1/ρ_e); 0.001–10 S/m typical for sediments and aquifers.
- AEM depth of investigation: 100–400 m typical, deeper at lower frequencies.
- TEM depth: 100–600 m typical; longer pulses for deeper.
- Sea-water salinity gives σ ≈ 4–5 S/m; useful for salt-water-intrusion mapping.

**Cross-discipline equivalents**:
- **Hydrology**: AEM is the dominant regional-scale aquifer-mapping method; Mississippi Embayment AEM survey (USGS, 2018); Central Valley AEM (DWR, ongoing) (`PD-aquifer-architecture`).
- **Agricultural sciences**: in-field σ maps for salinity, drainage, soil-texture zoning (Romero-Ruiz et al. 2018); same petrophysics as `MC-nsg-ERT` but different platform.
- **Geotechnical engineering**: AEM can identify low-resistivity clay-rich zones for engineering investigations.

**When you see this in a paper**: confirm system (TEM vs. FEM vs. AEM), frequency range, inversion method, and depth of investigation. AEM has poorer near-surface (< 10 m) resolution than ground methods; complementary stack.

**Anchor citations**:
- Auken, E., et al. (2017). The Aarhus Workbench user guide. *HydroGeophysics Group, Aarhus University*.
- Reynolds, J. M. (2011). *An Introduction to Applied and Environmental Geophysics* (2nd ed.). Wiley-Blackwell.

**Related cards**: `CC-nsg-resistivity`, `MC-nsg-ERT`, `MC-nsg-AEM`, `PD-aquifer-architecture`, `PD-contaminant-plume`

---

## CC-nsg-gravity: Gravity anomalies and density variations [mGal, m/s²]

**Quantity**: deviation of measured gravitational acceleration from a reference model. Surface gravimetry measures absolute g or relative gravity differences in mGal (1 mGal = 10⁻⁵ m/s²). After corrections (latitude, free-air, Bouguer, terrain, isostatic), the residual anomaly reflects subsurface density variations. The Bouguer anomaly is the standard product for subsurface mapping; free-air anomaly for tectonic-scale or oceanographic interpretation.

**Defining relation**: gravity anomaly Δg ≈ G ∫ Δρ(z) f(geom) dV, where Δρ is density contrast and f captures geometric weighting; classic inversion problem with depth-trade-off non-uniqueness. Bouguer correction Δg_B = 2π G ρ h removes the gravitational effect of the surface mass above the reference datum.

**Typical ranges**:
- Bouguer anomaly basin-scale variations: 10–100 mGal.
- High-precision microgravity for hydrology / volcanology: 0.01–1 mGal precision.
- Density contrast water-bearing sand vs. dry sand: ~0.05 g/cm³ → small gravity signal.
- Cave / void detection: 0.1–1 mGal signals at the surface depending on depth.

**Cross-discipline equivalents**:
- **Hydrology**: time-lapse microgravity tracks subsurface mass changes — water storage, snowmelt, soil moisture (Pool 2008); shared physics with GRACE satellite gravimetry (`MC-hydro-GRACE`) but at much higher spatial resolution.
- **Seismology**: shared subsurface-imaging substrate; gravity-seismic joint inversion (`TC-08`) handles the bedrock-basin geometry.
- **Geotechnical engineering**: cavity / void detection beneath dams and infrastructure.
- **Volcanology**: edifice density changes track magma movement; pre-eruption gravity signals at some volcanoes.

**When you see this in a paper**: confirm correction stack (latitude, free-air, Bouguer, terrain) and reference density assumption (typically 2.67 g/cm³ for Bouguer). Time-lapse microgravity for hydrology requires careful station stability and instrument-drift correction.

**Anchor citations**:
- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics* (2nd ed.). Cambridge University Press.
- Pool, D. R. (2008). The utility of gravity and water-level monitoring at alluvial aquifer wells in southern Arizona. *Geophysics*, 73(6), WA49–WA59. doi:10.1190/1.2980395

**Related cards**: `MC-nsg-gravity`, `MC-hydro-GRACE`, `CC-nsg-impedance`, `PD-aquifer-architecture`, `TC-08`

---

## CC-nsg-magnetics: Total-field magnetic anomalies [nT]

**Quantity**: total magnetic field intensity F [nT, nanotesla] or its anomaly ΔF after removal of the regional geomagnetic reference field (IGRF — International Geomagnetic Reference Field). Magnetic anomalies reflect spatial variations in subsurface magnetic susceptibility, dominantly from magnetite, hematite, and magnetic-iron-bearing minerals. Less hydrology- and ecology-relevant than other NSG methods but central for archaeology, ore exploration, fault-zone characterization, and identification of buried infrastructure (UXO, pipelines).

**Defining relation**: induced magnetization M = χ_m H (where H is geomagnetic field, χ_m magnetic susceptibility); total measured F = F_reference + ΔF (anomaly). Forward modeling uses Poisson's relation between magnetic and gravitational potentials. Inversion suffers from non-uniqueness similar to gravity.

**Typical ranges**:
- Earth's main field: 25,000–65,000 nT depending on latitude.
- Crustal magnetic anomalies: 1–10,000 nT scale.
- Magnetic susceptibility of sediments: < 10⁻⁴ (weakly magnetic).
- Magnetic susceptibility of magnetite-bearing rocks: 10⁻¹–10⁰ (strongly magnetic).
- High-precision aeromagnetic surveys: 0.01–1 nT precision.

**Cross-discipline equivalents**:
- **Geotechnical engineering**: ferrous-infrastructure detection (pipelines, USTs, rebar reinforcement).
- **Geomorphology**: paleomagnetic stratigraphy in fluvial / lacustrine deposits; magnetic susceptibility in loess records as paleoclimate proxy.
- **Geology**: structural mapping of dikes, faults, ore bodies.

**When you see this in a paper**: confirm IGRF correction date and version; diurnal-variation correction (geomagnetic storms can mimic anomalies); whether the work uses total field, vertical gradient, or analytic-signal-derived data products.

**Anchor citations**:
- Reynolds, J. M. (2011). *An Introduction to Applied and Environmental Geophysics* (2nd ed.). Wiley-Blackwell.
- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics* (2nd ed.). Cambridge University Press.

**Related cards**: `MC-nsg-magnetics`, `CC-nsg-gravity`, `CC-nsg-resistivity`
