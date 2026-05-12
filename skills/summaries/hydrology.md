---
discipline: hydrology
purpose: system-prompt summary, ~350 words
schema_version: v3
---

# Hydrology — summary

Hydrology studies the storage, transport, and transformation of water in the Earth system, spanning groundwater flow, vadose-zone moisture, surface runoff, evapotranspiration, atmospheric coupling, and the biogeochemistry of water-rock and water-vegetation interactions. The discipline is the structural integrator of the Gaia translator's cross-cutting bridges: hydrology supplies the pore-pressure term that couples to geotech and seismology (`TC-02`), the diffusion equation shared with consolidation and hillslope transport (`TC-01`), and the watershed mass balance that closes onto atmospheric and ecosystem branches (`TC-06`).

**Core governing equations**:
- Darcy's law: q = −K ∇h.
- Continuity in porous media: ∂h/∂t = (1/S) ∇·(T ∇h).
- Hydraulic diffusivity D = T/S; pressure-diffusion equation ∂h/∂t = D ∇²h (the equation shared across `TC-01`).
- Effective stress σ' = σ − p (Terzaghi-Biot), the basis of `TC-02`.
- Penman-Monteith reference ET₀ (Allen et al. 1998 FAO-56).
- Watershed mass balance P = ET + Q + ΔS (`TC-06`).

**Core observables**: hydraulic conductivity K [m/s] and transmissivity T [m²/day]; storativity / specific storage S, Sₛ and specific yield Sy; hydraulic diffusivity D [m²/s]; hydraulic head h [m] and pore pressure p [Pa]; evapotranspiration ET [mm/day]; streamflow Q [m³/s] (⚠️ vocabulary collision with seismic attenuation Q dimensionless; `CC-seismo-Q`); recharge R [mm/yr]; soil moisture θ [m³/m³].

**Core measurement infrastructure**: USGS NWIS (streamflow, well levels, water quality); GRACE / GRACE-FO satellite gravimetry for total water storage; SMAP / SMOS L-band radiometer for surface soil moisture; cosmic-ray neutron sensing (COSMOS) for intermediate-scale soil moisture; FLUXNET / AmeriFlux / ICOS eddy-covariance towers for ET, GPP, H, LE; stable and radioactive water isotopes for source attribution and age dating; process-based models MODFLOW, ParFlow, CLM, SWAT, WRF-Hydro.

**Cross-discipline hooks the chatbot should be alert for**:
- *Hydrology ↔ geotechnical engineering*: effective stress (`TC-02`), consolidation as hydraulic diffusion (`TC-01`), pumping-induced subsidence (`PD-aquifer-depletion`, `PD-subsidence-consolidation`), embankment seepage and pore-pressure transients (`PD-dam-levee-safety`).
- *Hydrology ↔ seismology*: effective stress (`TC-02`), dv/v as hydrology proxy (`TC-03`), injection-induced seismicity (`PD-induced-seismicity`), earthquake-triggered hydrologic responses (`PD-eq-hydro-coupling`), high-frequency seismic noise from streamflow (`CC-hydro-Q` ↔ `CC-seismo-noise`).
- *Hydrology ↔ geomorphology*: AR-driven shallow landslides (`PD-AR-landslide`), flood-frequency power-law statistics (`TC-04`), sediment-transport stream power.
- *Hydrology ↔ atmospheric sciences*: watershed mass balance vs. atmospheric branch (`TC-06`), data assimilation (`TC-05`), AR moisture-source attribution, drought cascades (`PD-drought`).
- *Hydrology ↔ ecology*: ET–GPP coupling at the leaf scale, IHA hydrologic-alteration indicators, plant-water-source isotopes.
- *Hydrology ↔ agricultural sciences*: irrigation-driven aquifer depletion (`PD-aquifer-depletion`), reference ET₀ for irrigation scheduling.
- *Hydrology ↔ near-surface geophysics*: hydrogeophysics joint inversion (`TC-08`), petrophysical Archie/Waxman-Smits link to seismic Vs and electrical resistivity.

**Foundational anchor citations**: Darcy (1856) for the constitutive law; Theis (1935) and Cooper & Jacob (1946) for pumping-test analysis; Terzaghi (1925, 1943) for effective stress; Hubbert (1940) for head as energy potential; Bear (1972) for the porous-media reference; Penman (1948) and Monteith (1965) for ET; Wang & Manga (2010) for earthquake-hydrology coupling; Beven (2006) for equifinality; Famiglietti (2014) for the global-groundwater-crisis framing.

For full details, retrieve from `skills/long_form/hydrology/` (concept cards, method cards, phenomenon dossiers, translation cards).
