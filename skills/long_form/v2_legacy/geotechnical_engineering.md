# Geotechnical engineering — Gaia translator skill file

Companion discipline file. Citation policy as in `atmospheric_sciences.md`.

## Core variables and equations

- Effective stress: σ' = σ − p (Terzaghi 1925). The single most important equation in geotechnical engineering and the cleanest bridge to seismology (induced seismicity, fault stability) and hydrology (poroelastic coupling).
- Mohr-Coulomb shear strength: τ_f = c' + σ' tan φ'. φ' friction angle, c' cohesion (often ≈ 0 for cohesionless soils).
- Undrained shear strength: Sᵤ (saturated clays, short-term).
- Pore pressure ratio rᵤ = Δp / σ'_v0; key liquefaction observable.
- Cyclic stress ratio CSR = 0.65 (a_max/g)(σ_v0/σ'_v0) r_d, cyclic resistance ratio CRR (functions of N₁,60, q_c1N, or Vs1 per Seed-Idriss family methods).
- Consolidation: Terzaghi 1D consolidation ∂u/∂t = c_v ∂²u/∂z² (a diffusion equation, with c_v = k/(γ_w m_v) — same mathematical form as hydraulic and hillslope diffusion).
- Site characterization variables: Vs30 (time-averaged shear-wave velocity in upper 30 m), shared verbatim with seismology and near-surface geophysics.
- Factor of safety against slope failure: FS = τ_f / τ_d.

## Methods

- In-situ tests: Standard Penetration Test (SPT, N₆₀), Cone Penetration Test (CPT with q_c, f_s, u₂), seismic CPT (combines q_c with Vs profile), Pressuremeter, Vane Shear.
- Geophysical site characterization: MASW, ReMi, downhole/crosshole seismic, HVSR (Nakamura 1989). All shared with near-surface geophysics.
- Laboratory: triaxial (CU, CD), direct shear, resonant column, cyclic simple shear, oedometer, Atterberg limits, grain-size analysis.
- Numerical: finite-element/finite-difference codes (FLAC, PLAXIS), nonlinear site response (DEEPSOIL, OpenSees).
- Liquefaction triggering analysis: Seed–Idriss "simplified procedure" and descendants (Idriss & Boulanger 2008; Boulanger & Idriss 2014; Robertson & Wride 1998 CPT-based).
- NGA-West/East ground motion models couple to engineering via site amplification factors keyed on Vs30 (Boore et al. 2014).

## Phenomena studied

- Soil liquefaction during earthquakes — directly relevant to the Gaia Nisqually digital-twin prototype. Mechanism: cyclic shear in saturated loose sand → pore pressure buildup → effective stress → 0 → loss of strength.
- Lateral spreading and ground deformation during shaking.
- Foundation settlement (immediate, primary consolidation, secondary creep).
- Slope stability and earthquake-triggered landslides (Newmark 1965 sliding block; Jibson 2007).
- Earth dam, levee, and tailings dam safety.
- Ground improvement (compaction, stone columns, deep mixing, jet grouting).
- Tunnel and excavation support.

## Translation hooks

- **→ Seismology**: site response is the bilingual problem. Both fields use Vs30 and HVSR; geotech adds nonlinear stress-strain and pore-pressure feedback that linear seismic site response models miss. Liquefaction is a coupled geotech-seismology-hydrology problem.
- **→ Hydrology**: Terzaghi effective stress is mathematically identical to the poroelastic effective stress in Wang & Manga 2010 earthquake hydrology. Consolidation theory is a hydraulic diffusion problem with mechanical coupling.
- **→ Geomorphology**: factor-of-safety analysis underlies the Iverson 2000 transient pore pressure landslide model. φ', c', and Sᵤ are the same variables the hillslope hydrology community uses.
- **→ Near-surface geophysics**: MASW-derived Vs profiles are the input to site classification (ASCE 7, Eurocode 8) and liquefaction-triggering Vs-based methods (Andrus & Stokoe 2000).
- **→ Atmospheric sciences**: extreme precipitation forecasts feed embankment pore-pressure rise models.
- **→ Agricultural sciences**: pumping-induced subsidence in Central Valley (1-10 m cumulative) is a consolidation problem driven by an agricultural process.

## Foundational references

- Terzaghi, K. (1925). *Erdbaumechanik auf bodenphysikalischer Grundlage*. Vienna: Franz Deuticke. (English: Theoretical Soil Mechanics, Wiley, 1943.) — origin of effective stress.
- Newmark, N. M. (1965). Effects of earthquakes on dams and embankments. *Géotechnique*, 15(2), 139–160. doi:10.1680/geot.1965.15.2.139
- Seed, H. B., & Idriss, I. M. (1971). Simplified procedure for evaluating soil liquefaction potential. *J. Soil Mech. Found. Div., ASCE*, 97(SM9), 1249–1273.
- Nakamura, Y. (1989). A method for dynamic characteristics estimation of subsurface using microtremor on the ground surface. *QR RTRI*, 30(1), 25–33.
- Robertson, P. K., & Wride, C. E. (1998). Evaluating cyclic liquefaction potential using the cone penetration test. *Canadian Geotechnical Journal*, 35(3), 442–459. doi:10.1139/t98-017
- Andrus, R. D., & Stokoe, K. H. (2000). Liquefaction resistance of soils from shear-wave velocity. *J. Geotech. Geoenviron. Eng.*, 126(11), 1015–1025. doi:10.1061/(ASCE)1090-0241(2000)126:11(1015)
- Idriss, I. M., & Boulanger, R. W. (2008). *Soil Liquefaction During Earthquakes*. EERI Monograph MNO-12.
- Jibson, R. W. (2007). Regression models for estimating coseismic landslide displacement. *Engineering Geology*, 91(2–4), 209–218. doi:10.1016/j.enggeo.2007.01.013
- Boore, D. M., et al. (2014). NGA-West2 equations for predicting PGA, PGV, and 5%-damped PSA. *Earthquake Spectra*, 30(3), 1057–1085. doi:10.1193/070113EQS184M
- Boulanger, R. W., & Idriss, I. M. (2014). CPT and SPT-based liquefaction triggering procedures. *Report UCD/CGM-14/01*, UC Davis.
