---
discipline: geotechnical_engineering
card_type: phenomenon
schema_version: v3
---

# Geotechnical engineering — phenomenon dossiers

Each dossier describes one real-world geotechnical phenomenon with cross-discipline observability. Format follows `docs/card_format_spec.md`. Earthquake-induced liquefaction is *not* duplicated here — it lives in `PD-liquefaction` (seismology file), with geotech cross-references resolved through this corpus.

---

## PD-coseismic-landslide: Earthquake-triggered landslides

**Setting**: hillslopes in seismically active regions subjected to strong shaking. Canonical cases: 1994 Northridge (Mw 6.7) ≈ 11,000 landslides; 2008 Wenchuan (Mw 7.9) ≈ 200,000 landslides killing ≈ 20,000 people (Dai et al. 2011); 2015 Gorkha Nepal; 2018 Hokkaido Eastern Iburi. PNW relevance: a Cascadia Mw 9 event is projected to trigger tens of thousands of landslides in the coastal range and along glaciated valleys.

**Mechanism (4-step chain)**:
1. **(Seismology)** Strong ground motion arrives at the slope; PGA, PGV, and duration scale with Mw and distance via `MC-geotech-GMPE`.
2. **(Geotech)** Cyclic shear stress on a candidate failure surface temporarily exceeds yield: τ > τ_f, equivalent to FS < 1 (`CC-geotech-FS`). Sliding initiates.
3. **(Geotech + hydro)** If saturated, pore-pressure rise (`CC-geotech-PorePressure`) reduces σ' and accelerates motion; coupling to liquefaction (`PD-liquefaction`) generates the largest displacements.
4. **(Geomorphology)** Newmark (1965) sliding block accumulates permanent displacement D_N when a > a_y; empirical D_N(Mw, R) regressions (Jibson 2007) feed regional hazard maps.

**Observables per discipline**:
- **Seismology**: ground-motion intensity maps (ShakeMap); aftershock catalogs (`MC-seismo-ML`); ambient-noise dv/v decreases observed after large events (`CC-seismo-dvv`).
- **Geotechnical engineering**: Newmark displacement maps; FS analyses on critical infrastructure slopes.
- **Geomorphology**: post-event landslide inventories from optical, SAR, and InSAR imagery; long-term sediment-yield change.
- **Hydrology**: post-landslide streamflow and sediment-flux anomalies; transient damming and outburst flood risk.
- **Ecology**: forest cover loss, root cohesion recovery (Sidle & Ochiai 2006), decadal regrowth trajectory.

**Open questions for translator-agent integration**:
- Multi-hazard cascades (earthquake → landslide → dam → flood; the Gaia mountain-to-sea hazard agenda) lack physics-based forecasting frameworks.
- The role of pre-event soil moisture and antecedent rainfall in modulating coseismic landslide susceptibility is empirically clear but poorly parameterized.
- ML landslide-inventory pipelines from satellite imagery (Tanyas et al. 2017) provide rapid post-event ground truth.

**Anchor papers**:
- Newmark, N. M. (1965). Effects of earthquakes on dams and embankments. *Géotechnique*, 15(2), 139–160. doi:10.1680/geot.1965.15.2.139
- Keefer, D. K. (1984). Landslides caused by earthquakes. *Geological Society of America Bulletin*, 95(4), 406–421. doi:10.1130/0016-7606(1984)95<406:LCBE>2.0.CO;2
- Jibson, R. W. (2007). Regression models for estimating coseismic landslide displacement. *Engineering Geology*, 91(2–4), 209–218. doi:10.1016/j.enggeo.2007.01.013
- Tanyas, H., et al. (2017). Presentation and analysis of a worldwide database of earthquake-induced landslide inventories. *J. Geophys. Res. Earth Surface*, 122(10), 1991–2015. doi:10.1002/2017JF004236

**Related cards**: `CC-geotech-FS`, `CC-geotech-MohrCoulomb`, `CC-geotech-PorePressure`, `CC-seismo-magnitude`, `MC-geotech-GMPE`, `PD-AR-landslide`, `PD-liquefaction`, `TC-11`

---

## PD-subsidence-consolidation: Pumping-induced consolidation and land subsidence

**Setting**: aquifer systems with compressible aquitards undergoing groundwater extraction beyond recharge. Canonical: California's San Joaquin Valley (≈ 9 m cumulative subsidence by 2016; Faunt et al. 2016), Mexico City (≈ 14 m), Beijing-Tianjin, Jakarta, Bangkok, the U.S. High Plains, and Houston. Mechanically distinct from the hydrologic storage-loss view in `PD-aquifer-depletion`.

**Mechanism (3-step chain)**:
1. **(Hydrology)** Pumping reduces head h in the aquifer (`CC-hydro-h`); the change propagates into adjacent low-permeability aquitards by diffusion (`CC-hydro-D`).
2. **(Geotech)** Pore-pressure drop in the aquitard increases effective stress σ' = σ − p (`CC-geotech-MohrCoulomb`); skeletal grains rearrange. Within the elastic preconsolidation range, deformation is reversible (m_v,e); beyond it, inelastic m_v,v compaction dominates and is permanent (`CC-geotech-cv`).
3. **(Geotech + remote sensing)** Surface subsidence accumulates from the integrated aquitard compaction; rate set by c_v.

**Observables per discipline**:
- **Hydrology**: well-water-level records (`MC-hydro-NWIS`), pumping inventories, GRACE total-water-storage anomalies (`MC-hydro-GRACE`).
- **Geotechnical engineering**: aquitard m_v from oedometer (`MC-geotech-triaxial`); piezometer transients; extensometer compaction at depth intervals.
- **Near-surface geophysics**: InSAR subsidence rates (1–10 cm/yr precision over decades) are the dominant modern observable.
- **Agricultural sciences**: irrigation demand drives the forcing; canal infrastructure damage from subsidence drives economic cost.
- **Seismology**: stress changes from poroelastic loading have modulated regional seismicity in some basins (Wicks et al. 2001).

**Open questions for translator-agent integration**:
- Permanent inelastic compaction is irreversible storage loss — the link to long-term water security is direct but rarely quantified outside USGS reports.
- Joint inversion of InSAR + GRACE + well data for aquitard properties is an active hydrogeophysics frontier (Smith et al. 2017).
- Subsidence rate as a leading indicator for arsenic / fluoride mobilization in compacted clays is poorly constrained.

**Anchor papers**:
- Galloway, D. L., & Burbey, T. J. (2011). Review: Regional land subsidence accompanying groundwater extraction. *Hydrogeology Journal*, 19(8), 1459–1486. doi:10.1007/s10040-011-0775-5
- Faunt, C. C., Sneed, M., Traum, J., & Brandt, J. T. (2016). Water availability and land subsidence in the Central Valley, California, USA. *Hydrogeology Journal*, 24(3), 675–684. doi:10.1007/s10040-015-1339-x
- Smith, R. G., Knight, R., Chen, J., Reeves, J. A., Zebker, H. A., Farr, T., & Liu, Z. (2017). Estimating the permanent loss of groundwater storage in the southern San Joaquin Valley, California. *Water Resources Research*, 53(3), 2133–2148. doi:10.1002/2016WR019861

**Related cards**: `CC-geotech-cv`, `CC-geotech-MohrCoulomb`, `CC-hydro-h`, `CC-hydro-S`, `CC-hydro-D`, `MC-hydro-GRACE`, `MC-geotech-triaxial`, `PD-aquifer-depletion`

---

## PD-dam-levee-safety: Earth dam and levee safety under seismic and hydrologic loading

**Setting**: earth-fill and rockfill dams, levees, and tailings dams subjected to seismic shaking, reservoir loading, rapid drawdown, and overtopping. Critical infrastructure: ≈ 90,000 dams in the U.S. National Inventory of Dams, with median age > 60 yr; Oroville Dam 2017 spillway incident, Edenville/Sanford 2020 failure (Michigan), Brumadinho 2019 tailings dam failure (Brazil, 270 fatalities). Climate-driven extreme precipitation and increasingly recognized aging infrastructure raise the joint hazard.

**Mechanism (failure modes, often coupled)**:
1. **(Geotech)** Seismic instability — slope failure under cyclic loading (`CC-geotech-FS`, Newmark `PD-coseismic-landslide` mechanics scaled to engineered slopes; Bray & Travasarou 2007).
2. **(Geotech + hydro)** Internal erosion / piping — hydraulic gradient through the embankment exceeds the critical gradient; pore-pressure transients (`CC-geotech-PorePressure`) plus seepage initiate progressive failure (Foster et al. 2000 statistical compilation).
3. **(Geotech + seismo)** Liquefaction of embankment fill or foundation (`PD-liquefaction`); the canonical Lower San Fernando Dam 1971 case (Seed et al. 1975).
4. **(Hydro + atmospheric)** Overtopping during extreme inflow events; spillway capacity vs. revised PMF estimates under climate change.

**Observables per discipline**:
- **Geotechnical engineering**: instrumentation — piezometers, inclinometers, settlement plates, fiber-optic strain (DAS-adjacent).
- **Seismology**: site-specific PSHA (`MC-geotech-GMPE`) for design ground motion; aftershock monitoring at instrumented dams.
- **Hydrology / atmospheric**: reservoir inflow forecasts; PMP and PMF; AR-driven inflow extremes (`PD-AR-landslide`).
- **Near-surface geophysics**: ERT and seismic refraction for seepage anomalies; InSAR for dam-crest deformation.
- **Ecology / society**: downstream consequence — population, infrastructure, ecosystem at risk.

**Open questions for translator-agent integration**:
- Climate-driven revision of design hydrology (PMP, PMF, AR-frequency) is uneven across jurisdictions.
- Tailings dams have a distinct failure-statistics record (Robertson et al. 2019, post-Brumadinho); cross-disciplinary integration with mining hydrology is uneven.
- Real-time multi-hazard digital-twin models for high-consequence dams (a Gaia mountain-to-sea relevance) are not yet operational.

**Anchor papers**:
- Seed, H. B., et al. (1975). The slides in the San Fernando dams during the earthquake of February 9, 1971. *J. Geotech. Eng. Div. (ASCE)*, 101(7), 651–688. doi:10.1061/AJGEB6.0000175
- Foster, M., Fell, R., & Spannagle, M. (2000). The statistics of embankment dam failures and accidents. *Canadian Geotechnical Journal*, 37(5), 1000–1024. doi:10.1139/t00-030
- Bray, J. D., & Travasarou, T. (2007). Simplified procedure for estimating earthquake-induced deviatoric slope displacements. *J. Geotech. Geoenviron. Eng.*, 133(4), 381–392. doi:10.1061/(ASCE)1090-0241(2007)133:4(381)

**Related cards**: `CC-geotech-FS`, `CC-geotech-PorePressure`, `CC-geotech-CSR-CRR`, `MC-geotech-GMPE`, `PD-liquefaction`, `PD-AR-landslide`, `PD-coseismic-landslide`

---

## PD-site-response: Nonlinear site response and basin effects

**Setting**: soft-sediment sites — alluvial valleys, lake-bed deposits, sedimentary basins — that amplify ground motion through impedance contrast, resonance, and basin-edge focusing. The Mexico City 1985 (Mw 8.0 Michoacán) lake-bed amplification reached factors of 10–50 at site fundamental periods of 2–3 s, killing ≈ 10,000 people; Loma Prieta 1989 Marina District; 1995 Kobe; Tokyo, Seattle, and Los Angeles basins are all subject to large-basin amplification.

**Mechanism (3-step chain)**:
1. **(Seismology + geotech)** Impedance contrast at the sediment-bedrock interface amplifies vertically incident SH waves; first peak at f_0 = V_s,avg/(4H) for a single layer (`MC-geotech-HVSR`).
2. **(Geotech)** At large input motion, soil stiffness degrades along G/Gmax(γ) (`CC-geotech-G-Gmax`); damping ξ(γ) increases; effective resonance shifts to longer period; nonlinear effects reduce peak amplification at f_0 but extend duration.
3. **(Seismology + applied geophysics)** Basin-edge focusing and 2D/3D resonances (Bard & Bouchon 1985) produce amplification not captured by 1D analysis; surface-wave generation at basin edges adds late-arriving energy.

**Observables per discipline**:
- **Seismology**: dense urban accelerometer networks (e.g., NetQuakes, CIESMIC for L.A. and Seattle); spectral ratios (HVSR, SSR, GIT) over reference rock sites.
- **Geotechnical engineering**: nonlinear 1D/2D site-response simulations (`MC-geotech-numerical`); G/Gmax curves from `MC-geotech-cyclic-labs`.
- **Near-surface geophysics**: Vs profiles from MASW, ambient-noise tomography, gravity for basin depth Z_1.0, Z_2.5.
- **Engineering / society**: building-code site-class amplification factors F_a, F_v keyed on V_s30 underpredict large-basin amplification.

**Open questions for translator-agent integration**:
- Linear seismic (`MC-seismo-ambient-noise`) and nonlinear engineering (`MC-geotech-numerical`) site-response pictures converge only in the small-strain limit; the integrated framework is `TC-10`.
- Urban-scale 3D ground-motion simulations (SW4, SCEC BBP) require simultaneous geotechnical, seismological, and geophysical inputs — a classic Gaia integration target.
- Real-time dv/v in cities (e.g., from urban DAS, Spica et al. 2020) potentially gives time-varying site-response calibration.

**Anchor papers**:
- Borcherdt, R. D. (1970). Effects of local geology on ground motion near San Francisco Bay. *Bull. Seismol. Soc. Am.*, 60(1), 29–61.
- Bard, P.-Y., & Bouchon, M. (1985). The two-dimensional resonance of sediment-filled valleys. *Bull. Seismol. Soc. Am.*, 75(2), 519–541. doi:10.1785/BSSA0750020519
- Stewart, J. P., et al. (2014). Amplification factors for spectral acceleration in active regions. *Bull. Seismol. Soc. Am.*, 104(6), 3019–3036. doi:10.1785/0120130319

**Related cards**: `CC-geotech-G-Gmax`, `CC-seismo-Vs`, `MC-geotech-HVSR`, `MC-geotech-numerical`, `MC-seismo-MASW`, `TC-10`, `TC-12`
