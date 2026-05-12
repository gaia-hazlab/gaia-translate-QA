---
discipline: seismology
purpose: system-prompt summary, ~350 words
schema_version: v3
---

# Seismology — summary

Seismology studies the generation and propagation of elastic waves in the Earth and other planetary bodies, with applications spanning earthquake science, deep Earth structure, near-surface imaging, and environmental monitoring. The discipline straddles two complementary directions: **source** (what makes earthquakes and tremor happen) and **structure / monitoring** (what waves reveal about the medium they pass through).

**Core governing equations**:
- Elastic wave equation ρ ∂²u/∂t² = ∇·σ, with constitutive law σ = C : ε for elastic media.
- Coulomb failure criterion τ ≥ μ(σ_n − p) + c for fault slip.
- Moment magnitude Mw = (2/3) log₁₀(M0) − 6.0 (Hanks & Kanamori 1979), where M0 = μ A D̄.
- Brune (1970) source spectrum with corner frequency f_c ∝ Δσ^(1/3) M0^(−1/3).
- Gutenberg-Richter log N(≥M) = a − bM, with b ~ 1 globally.

**Core observables**: stress on faults σ_n, τ, Δσ [MPa]; shear-wave velocity Vs [m/s] and the site-classification parameter Vs30; attenuation Q (dimensionless — ⚠️ collision with hydrology Q for streamflow); moment magnitude Mw and seismic moment M0; b-value of magnitude-frequency relation; relative velocity change dv/v from coda-wave or ambient-noise monitoring; ambient seismic noise PSD; focal mechanism / centroid moment tensor.

**Core measurement infrastructure**: broadband seismometers (GSN, USArray, ANSS, PNSN); DAS fiber-optic arrays; ambient-noise cross-correlation; MASW for site characterization; body- and surface-wave tomography; ML-based earthquake catalogs (PhaseNet, EQTransformer); EarthScope (formerly IRIS) data services via FDSN web services and ObsPy.

**Cross-discipline hooks the chatbot should be alert for**:
- *Seismology ↔ hydrology*: effective stress (`TC-02`), dv/v as groundwater proxy (`TC-03`), induced seismicity from injection (`PD-induced-seismicity`), earthquake-triggered hydrologic change (`PD-eq-hydro-coupling`), high-frequency noise from streamflow (`CC-seismo-noise`).
- *Seismology ↔ geotechnical engineering*: Vs30 and site amplification (`CC-seismo-Vs`), liquefaction (`PD-liquefaction`), ground motion → embankment stability (`TC-02`).
- *Seismology ↔ geomorphology*: surface displacement from large earthquakes (`PD-megathrust`), landslide and debris-flow seismic signatures, fault-scarp accumulation.
- *Seismology ↔ atmospheric sciences*: microseism intensity as climate proxy (`PD-microseism`), ionospheric coupling at largest magnitudes (`PD-megathrust`), volcanic plume monitoring.
- *Seismology ↔ ecology*: ocean-bottom seismometer biological signals; ambient-soundscape collisions (vocabulary).
- *Seismology ↔ near-surface geophysics*: joint imaging (`TC-08`), shared MASW methodology, hydrogeophysics.

**Foundational anchor citations**: Aki & Richards (2002) *Quantitative Seismology*; Wang & Manga (2010) earthquake hydrology; Kanamori (1977) and Hanks & Kanamori (1979) for moment magnitude; Brune (1970) for source spectrum; Shapiro et al. (2005) for ambient-noise tomography; Ellsworth (2013) for induced seismicity; Beroza & Ide (2011) for slow slip.

For full details, retrieve from `skills/long_form/seismology/` (concept cards, method cards, phenomenon dossiers, translation cards).
