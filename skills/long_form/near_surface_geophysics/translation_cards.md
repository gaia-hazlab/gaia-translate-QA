---
discipline: near_surface_geophysics
card_type: translation
schema_version: v3
---

# Near-surface geophysics — translation cards

Cross-discipline bridges originating from near-surface geophysics. Complements `TC-08` (joint geophysical inversion — seismic ↔ ERT ↔ MT ↔ gravity), already touching NSG explicitly. Format follows `docs/card_format_spec.md`.

---

## TC-19: Critical-zone observability — the multi-method imaging stack

**Shared structure**: the critical zone (CZ) — the surface and near-surface region where rock, soil, water, air, and living organisms interact — is the operational substrate for hydrology, geomorphology, ecology, geotechnical engineering, and agriculture. No single geophysical method captures all the physical contrasts at all depths in the CZ; recovery of a useful subsurface model requires a multi-method stack and joint interpretation. This translation card frames the operational practice of CZ characterization, which has matured into a distinct sub-discipline of hydrogeophysics-plus-environmental-seismology since the early 2000s (Brantley et al. 2007; Parsekian et al. 2015).

**Discipline-specific manifestations**:
- **Near-surface geophysics**: the integrated method stack — ERT (`MC-nsg-ERT`), GPR (`MC-nsg-GPR`), MASW (`MC-seismo-MASW`), HVSR (`MC-geotech-HVSR`), gravity (`MC-nsg-gravity`), AEM (`MC-nsg-AEM`) — used at instrumented CZ sites for substrate characterization (`PD-critical-zone-imaging`).
- **Hydrology**: water-content and saturation mapping from ρ_e, ε_r via Archie's and Topp's relations; integrated with isotope-based recharge work (`MC-hydro-isotopes`) for full ecohydrologic characterization.
- **Geomorphology**: regolith depth, bedrock topography (`CC-geomorph-D`, `MC-geomorph-lidar`) revealed by seismic refraction and ERT; soil-production-function inputs (Heimsath et al. 1997).
- **Ecology**: rooting-zone characterization; coupled vegetation-water-substrate dynamics; integration with `MC-eco-FIA-NEON-LTER` plot data.
- **Geotechnical engineering**: subsurface stratigraphy and stiffness profiles for site characterization; the urban-NSG → geotechnical-engineering bridge.
- **Agricultural sciences**: in-field σ maps for precision agriculture; the agricultural side of hydrogeophysics (Romero-Ruiz et al. 2018).

**When the analogy holds**:
- At dedicated CZ sites with multi-method deployments, joint inversion or co-located interpretation produces subsurface models more robust than any single method.
- Petrophysical relations are calibrated at the site, or transferred carefully from analog sites.
- The CZ-imaged substrate feeds downstream process-based models (Landlab, ParFlow-CLM, CLM/ELM) that close the cross-discipline modeling chain.

**When the analogy breaks**:
- Single-method deployments at non-CZ sites can't recover the full substrate; the bridge collapses to whatever the single method can resolve.
- Petrophysical relations are non-unique; multiple subsurface configurations can fit the same multi-method observations.
- The frontier of 3D, time-lapse, multi-method CZ characterization is computationally and operationally expensive; most CZ work remains 2D or sparse-3D.

**Translator agent move**: when a paper reports a CZ characterization, identify which methods were used, what petrophysical relations link them, and what downstream process model uses the result. Single-method CZ work is incomplete by definition; cross-retrieve method cards (`MC-nsg-*`) and the CZ-relevant geomorph and hydrology cards to suggest the missing complementary observations.

**Anchor citations**:
- Brantley, S. L., Goldhaber, M. B., & Ragnarsdottir, K. V. (2007). Crossing disciplines and scales to understand the Critical Zone. *Elements*, 3(5), 307–314. doi:10.2113/gselements.3.5.307
- Parsekian, A. D., Singha, K., Minsley, B. J., Holbrook, W. S., & Slater, L. D. (2015). Multiscale geophysical imaging of the critical zone. *Reviews of Geophysics*, 53(1), 1–26. doi:10.1002/2014RG000465
- Binley, A., Hubbard, S. S., Huisman, J. A., Revil, A., Robinson, D. A., Singha, K., & Slater, L. D. (2015). The emergence of hydrogeophysics for improved understanding of subsurface processes over multiple scales. *Water Resources Research*, 51(6), 3837–3866. doi:10.1002/2015WR017016
- Holbrook, W. S., et al. (2019). Links between physical and chemical weathering inferred from a 65-m-deep borehole through Earth's critical zone. *Scientific Reports*, 9, 4495. doi:10.1038/s41598-019-40819-9

**Related cards**: `MC-nsg-ERT`, `MC-nsg-GPR`, `MC-nsg-AEM`, `MC-nsg-refraction`, `MC-nsg-joint-inversion`, `MC-seismo-MASW`, `MC-geotech-HVSR`, `CC-nsg-resistivity`, `CC-nsg-permittivity`, `CC-geomorph-D`, `CC-hydro-K`, `PD-critical-zone-imaging`, `PD-aquifer-architecture`, `TC-08`, `TC-13`
