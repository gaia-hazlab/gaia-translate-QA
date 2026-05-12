---
discipline: seismology
card_type: translation
schema_version: v3
---

# Seismology — translation cards

Cross-discipline bridges originating from seismology. Complements `TC-02` (effective stress, hydrology-origin), `TC-03` (dv/v as hydrology proxy), and `TC-04` (power laws across disciplines), all of which already cover seismology. Format follows `docs/card_format_spec.md`.

---

## TC-07: Anisotropy across disciplines (seismic, hydraulic, structural fabric)

**Shared structure**: directional dependence of a measured property arising from fabric — crystal orientation, fracture alignment, layering, or stress-induced micro-crack alignment. Same physical *cause* (aligned anisotropic elements at sub-resolution scale) produces directional signals across multiple geophysical observables.

**Discipline-specific manifestations**:
- **Seismology**: shear-wave splitting (SKS, local-S) yields fast-direction azimuth and delay time δt; surface-wave azimuthal anisotropy from tomography; full elastic tensor inversion in receiver-function work. Causes: olivine LPO in mantle (Silver 1996), aligned cracks in upper crust (Crampin 1981), foliated metamorphic rocks. Typical Vs anisotropy: 1–10%.
- **Hydrology**: hydraulic conductivity anisotropy K_h / K_v = 10–1000 in layered sedimentary basins; fracture-network anisotropy K(θ) in fractured rock. Same fabric (layer-parallel deposition, joint sets) drives both seismic and hydraulic anisotropy. See `CC-hydro-K`.
- **Geomorphology**: jointing patterns in bedrock outcrops; preferential erosion along weak directions; drainage-network orientation often inherits fracture-zone fabric.
- **Geology / petrography**: foliations, lineations, LPO measured directly via EBSD or thin section.

**When the analogy holds**:
- The fabric responsible is shared across observables: e.g., an aligned crack set causes both seismic and hydraulic anisotropy with a predictable ratio (Hudson 1981 framework for cracked-rock elasticity).
- The wavelength of seismic measurement is much larger than the fabric scale (effective-medium regime).
- Stress orientations are stable over the observation period.

**When the analogy breaks**:
- Crack-filling fluid type matters for seismic anisotropy (Hudson framework distinguishes dry vs. fluid-filled) but matters less for hydraulic anisotropy.
- Strong stress-induced anisotropy in seismic data can decouple from hydraulic anisotropy on geologic-fabric scales.
- Joint inversion for both observables must include the petrophysical mixing law explicitly; assumed correspondence is brittle.

**Translator agent move**: when a paper reports anisotropy in any discipline, identify the responsible fabric and ask whether the same fabric should be observable in adjacent disciplines. For fractured-rock aquifers, the same fracture network controls both K(θ) and Vs(θ); joint analysis can constrain the network statistics better than either observable alone.

**Anchor citations**:
- Crampin, S. (1981). A review of wave motion in anisotropic and cracked elastic-media. *Wave Motion*, 3(4), 343–391. doi:10.1016/0165-2125(81)90026-3
- Hudson, J. A. (1981). Wave speeds and attenuation of elastic waves in material containing cracks. *Geophysical Journal International*, 64(1), 133–150. doi:10.1111/j.1365-246X.1981.tb02662.x
- Silver, P. G. (1996). Seismic anisotropy beneath the continents: Probing the depths of geology. *Annual Review of Earth and Planetary Sciences*, 24, 385–432. doi:10.1146/annurev.earth.24.1.385

**Related cards**: `CC-seismo-Vs`, `CC-hydro-K`, `MC-seismo-tomography`

---

## TC-08: Joint geophysical inversion — seismic ↔ ERT ↔ MT ↔ gravity

**Shared structure**: subsurface imaging from disparate physical observables — elastic wave (seismic), electrical resistivity (ERT, MT, AEM), gravity, magnetics — that share a target structure but sample different physical properties. Joint inversion enforces structural similarity or petrophysical coupling between the recovered models.

**Discipline-specific manifestations**:
- **Seismology**: Vp, Vs models from body- and surface-wave tomography or full-waveform inversion (`MC-seismo-tomography`).
- **Near-surface geophysics**: electrical resistivity from ERT, magnetotelluric (MT), or airborne EM (AEM); gravity from ground or airborne gravimeters; magnetics. Resistivity is highly sensitive to water content and fluid chemistry — complementary to seismic sensitivity to rigidity and density.
- **Hydrology**: water content, salinity, and porosity are the petrophysical link between elastic and electrical observables (Archie 1942 for clean sands; Waxman-Smits for clays).
- **Geophysical exploration**: industry has used joint inversion for decades; academic adoption in hydrogeophysics is more recent (Binley et al. 2015).

**Joint inversion architectures**:
- **Cross-gradient** (Gallardo & Meju 2003): minimize ∇m1 × ∇m2 to enforce structural similarity without prescribing a petrophysical relation.
- **Petrophysical coupling**: explicit empirical model linking m1 and m2 (e.g., Archie's law for ρ↔θ).
- **Structurally constrained**: use one model as a reference framework for inverting the other.

**When the analogy holds**:
- Targets are at comparable scales and depths.
- Petrophysical mixing models are calibrated to the specific lithology.
- Both datasets have well-characterized noise and resolution structure.

**When the analogy breaks**:
- One observable is much higher resolution than the other; joint inversion can introduce artifacts in the lower-resolution model.
- Conflicting structural information (a real feature in one observable that is not present in the other) is unhandled by cross-gradient.
- Petrophysical relations are site-specific; using a textbook curve out-of-region introduces bias.

**Translator agent move**: when a paper uses one geophysical method to characterize the subsurface, ask: is there a complementary observable? What does Archie's law (or equivalent petrophysical link) predict the joint signature should look like? For the hydrogeophysics community, ERT + ambient-noise seismic + DAS form a dense imaging suite that the Denolle Group's near-surface work increasingly exploits.

**Anchor citations**:
- Archie, G. E. (1942). The electrical resistivity log as an aid in determining some reservoir characteristics. *Transactions of the AIME*, 146(1), 54–62. doi:10.2118/942054-G
- Gallardo, L. A., & Meju, M. A. (2003). Characterization of heterogeneous near-surface materials by joint 2D inversion of dc resistivity and seismic data. *Geophysical Research Letters*, 30(13), 1658. doi:10.1029/2003GL017370
- Binley, A., Hubbard, S. S., Huisman, J. A., Revil, A., Robinson, D. A., Singha, K., & Slater, L. D. (2015). The emergence of hydrogeophysics for improved understanding of subsurface processes over multiple scales. *Water Resources Research*, 51(6), 3837–3866. doi:10.1002/2015WR017016

**Related cards**: `MC-seismo-tomography`, `MC-seismo-MASW`, `CC-seismo-Vs`, `CC-hydro-K`, `MC-nsg-ERT`

---

## TC-09: Source-identification inverse problems (seismology ↔ isotope hydrology ↔ ecology eDNA ↔ atmospheric attribution)

**Shared structure**: given a set of observations downstream of an unknown source, identify the source's location, magnitude, and/or composition. The mathematical structure is Bayesian inverse-problem theory (Tarantola 2005): p(source | observations) ∝ p(observations | source) p(source). The specific observation operator H varies by discipline; the inference machinery is identical.

**Discipline-specific manifestations**:
- **Seismology**: earthquake source inversion. Focal mechanism from first-motion polarities or waveform inversion; centroid moment tensor (`CC-seismo-source`). For nuclear and industrial events: discrimination via amplitude ratios, depth, mechanism.
- **Hydrology**: water-source attribution via stable isotopes (δ¹⁸O, δD); groundwater contamination forensics via chemical fingerprinting; tritium/CFC source dating (`MC-hydro-isotopes`).
- **Ecology**: environmental DNA (eDNA) source identification from water or sediment samples (Deiner et al. 2017); pollen provenance; isotopic tracking of food webs.
- **Atmospheric sciences**: emission-source attribution via inverse modeling (e.g., methane emissions from CH₄ flux observations + atmospheric transport modeling — Maasakkers et al. 2021). Bayesian back-trajectories from CO₂ concentration anomalies.
- **Geomorphology**: sediment provenance from heavy minerals, geochronology (detrital zircon), cosmogenic isotopes; debris-flow source delineation.

**Shared inference structure**:
- Forward model M maps source → observations: M(source) = observations + noise.
- Observation operator H: for seismology, propagation Green's functions; for atmosphere, transport (LPDM, GEOS-Chem adjoint); for hydrology, mixing model.
- Prior on source: spatial/compositional plausibility constraints.
- Posterior characterizes both the most-likely source and its uncertainty.

**When the analogy holds** (transfer of methodology across disciplines):
- Non-uniqueness of inversion is a shared challenge; tools (regularization, ensemble methods, Bayesian sampling) port across.
- Software stacks share a Bayesian inverse-problems core (PyMC, emcee, Stan; for seismology, Cubit/SPECFEM); cross-discipline collaboration is natural.

**When the analogy breaks**:
- Physical mixing in source attribution (e.g., end-member mixing in isotope hydrology) has very different structure from propagation in seismology — different non-uniqueness modes.
- Source space dimensionality varies widely: a seismic source is parameterized by ~6–10 numbers; an emissions source map is millions of pixels with regularization-dominated inversion.

**Translator agent move**: when a paper formulates a "where did this signal come from" question, retrieve this card and `TC-05` (data assimilation). Ask: what's M? What's H? What's the noise? What prior makes physical sense? These four questions are portable across disciplines.

**Anchor citations**:
- Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter Estimation*. SIAM. doi:10.1137/1.9780898717921
- Deiner, K., et al. (2017). Environmental DNA metabarcoding: Transforming how we survey animal and plant communities. *Molecular Ecology*, 26(21), 5872–5895. doi:10.1111/mec.14350
- Maasakkers, J. D., et al. (2021). 2010–2015 North American methane emissions, sectoral contributions, and trends: A high-resolution inversion of GOSAT observations of atmospheric methane. *Atmospheric Chemistry and Physics*, 21(6), 4339–4356. doi:10.5194/acp-21-4339-2021

**Related cards**: `CC-seismo-source`, `MC-hydro-isotopes`, `TC-05`
