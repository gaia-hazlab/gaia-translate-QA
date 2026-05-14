---
discipline: near_surface_geophysics
card_type: phenomenon
schema_version: v3
---

# Near-surface geophysics — phenomenon dossiers

Each dossier describes one real-world near-surface-geophysics phenomenon with cross-discipline observability. Format follows `docs/card_format_spec.md`.

---

## PD-critical-zone-imaging: Multi-method imaging of the critical zone

**Setting**: the critical zone (CZ) — the surface and near-surface region where rock, soil, water, air, and living organisms interact — is the substrate where hydrology, geomorphology, ecology, geotechnical engineering, and agriculture all operate. Imaging the CZ requires multiple geophysical methods because no single method captures all the physical contrasts at all depths. The NSF Critical Zone Observatory (CZO) network (active 2007–2020) and its successor Critical Zone Collaborative Network (CZCN, 2020–) institutionalized this multi-method approach. Canonical case studies: Calhoun CZO (South Carolina); Boulder Creek CZO (Colorado); Eel River CZO (California); CRC Engineering Texas Engineering Experiment Station's subsurface laboratory.

**Mechanism (4-step chain — observational, not physical)**:
1. **(Geophysics)** Multiple methods deployed at the same site sample different subsurface contrasts: seismic refraction and surface-wave for V_p / V_s and bedrock depth; ERT for water content and clay; GPR for shallow stratigraphy; EM for deep conductivity; gravity for density structure.
2. **(Methodological)** Joint inversion or co-located interpretation reduces non-uniqueness in any single observable; petrophysical relations (Archie, Topp, Gassmann) link the methods.
3. **(Critical-zone integration)** The recovered subsurface model — bedrock topography, regolith thickness, hydraulic-property variability, root-zone characterization — becomes the substrate for cross-discipline modeling.
4. **(Forecasting)** Hydrologic, ecological, and geomorphic processes simulated on the CZ-imaged substrate make process-based predictions about how the landscape will respond to disturbance.

**Observables per discipline**:
- **Near-surface geophysics**: ERT, GPR, MASW, refraction, gravity, EM, magnetics; the integrated method stack.
- **Hydrology**: water-content time series at instrumented wells; recharge estimates anchored by isotope methods.
- **Geomorphology**: regolith-thickness, bedrock-topography from joint inversion; topography from `MC-geomorph-lidar`.
- **Ecology**: rooting-depth distributions; vegetation structure from GEDI lidar.
- **Geotechnical engineering**: in-situ tests (CPT, MASW) at instrumented sites for calibration.

**Open questions for translator-agent integration**:
- Standardization of CZ characterization protocols across sites remains elusive; reduces cross-site synthesis power.
- 3D imaging at meaningful resolutions remains computationally expensive; most CZ work is 2D or sparse-3D.
- Coupling CZ-imaged substrate to process-based models (Landlab, CLM, ParFlow) is the operational frontier.

**Anchor papers**:
- Brantley, S. L., Goldhaber, M. B., & Ragnarsdottir, K. V. (2007). Crossing disciplines and scales to understand the Critical Zone. *Elements*, 3(5), 307–314. doi:10.2113/gselements.3.5.307
- Parsekian, A. D., Singha, K., Minsley, B. J., Holbrook, W. S., & Slater, L. D. (2015). Multiscale geophysical imaging of the critical zone. *Reviews of Geophysics*, 53(1), 1–26. doi:10.1002/2014RG000465
- Holbrook, W. S., Marcon, V., Bacon, A. R., Brantley, S. L., Carr, B. J., Flinchum, B. A., Richter, D. D., & Riebe, C. S. (2019). Links between physical and chemical weathering inferred from a 65-m-deep borehole through Earth's critical zone. *Scientific Reports*, 9, 4495. doi:10.1038/s41598-019-40819-9

**Related cards**: `MC-nsg-ERT`, `MC-nsg-GPR`, `MC-nsg-AEM`, `MC-nsg-refraction`, `MC-nsg-joint-inversion`, `MC-geomorph-lidar`, `MC-geomorph-cosmogenic`, `TC-08`, `TC-13`, `TC-19`

---

## PD-aquifer-architecture: Hydrogeophysical aquifer-architecture mapping

**Setting**: large-scale (regional to basin) imaging of aquifer architecture — confining layers, paleochannels, brackish-fresh-water boundaries, fault-controlled compartments — using multi-method geophysical surveys. The dominant operational application of hydrogeophysics. Canonical surveys: USGS Mississippi Embayment AEM survey (2018; Minsley et al. 2021); California DWR statewide AEM (ongoing); Lake Saskatchewan saline-intrusion mapping. Critical input to operational groundwater management under U.S. Sustainable Groundwater Management Act (California SGMA), and analogous frameworks globally.

**Mechanism (4-step chain)**:
1. **(Geology / geomorph)** Aquifer geometry inherits from depositional and tectonic history — paleochannels, fault-bounded compartments, regional dip on regional aquifers.
2. **(Hydrology)** Water-bearing units have distinctive σ from clay-bearing aquitards (Archie's law, `CC-nsg-resistivity`); brackish water has very low resistivity contrast with fresh water.
3. **(Geophysics)** AEM, ERT, EM ground methods map σ at regional, watershed, and field scales; resistivity contrasts identify aquifer architecture.
4. **(Hydrology + management)** Aquifer-architecture maps feed `MC-hydro-modeling` grid configurations; identify recharge zones, compartmentalization, and groundwater-management vulnerabilities.

**Observables per discipline**:
- **Near-surface geophysics**: AEM (`MC-nsg-AEM`) regional; ERT (`MC-nsg-ERT`) site-scale; GPR (`MC-nsg-GPR`) shallow.
- **Hydrology**: wellhead head and chemistry; pumping tests for hydraulic-property characterization; isotope dating of groundwater (`MC-hydro-isotopes`).
- **Geomorphology**: paleochannel geomorphic features visible in lidar and DEM analysis.
- **Geology**: stratigraphic mapping, structural geology, well-log compilations.
- **Agricultural sciences**: aquifer-mapping informs irrigation-management planning (especially in California Central Valley, High Plains).

**Open questions for translator-agent integration**:
- Quantitative link from geophysical-property maps to operationally-relevant hydraulic properties (K, T, S) requires petrophysical calibration; the calibration is site-specific.
- 3D-coupled hydrogeophysical inversion (geophysics + well data + pumping-test results) is a frontier.
- Climate-change-driven shifts in aquifer compartmentalization (over-pumping closing fast-flow paths permanently) are operationally important but poorly mapped.

**Anchor papers**:
- Binley, A., Hubbard, S. S., Huisman, J. A., Revil, A., Robinson, D. A., Singha, K., & Slater, L. D. (2015). The emergence of hydrogeophysics for improved understanding of subsurface processes over multiple scales. *Water Resources Research*, 51(6), 3837–3866. doi:10.1002/2015WR017016
- Minsley, B. J., et al. (2021). Airborne geophysical surveys of the lower Mississippi Valley demonstrate broad applicability of high-resolution AEM. *Scientific Reports*, 11, 17856. doi:10.1038/s41598-021-97193-8
- Sherson, L. R., Van Trump, J. J., & Reichard, J. (2024). California's airborne electromagnetic survey program: A statewide approach to mapping groundwater resources. *Hydrogeology Journal* (regional case studies). doi:10.1007/s10040-024-02740-9

**Related cards**: `MC-nsg-ERT`, `MC-nsg-AEM`, `MC-nsg-joint-inversion`, `CC-nsg-resistivity`, `CC-hydro-h`, `CC-hydro-S`, `MC-hydro-isotopes`, `PD-aquifer-depletion`, `PD-subsidence-consolidation`, `TC-08`

---

## PD-contaminant-plume: Tracking groundwater contaminant plumes

**Setting**: subsurface migration of contaminants (organic solvents, fuel hydrocarbons, leached pesticides and herbicides, salt-water intrusion, mine-tailings effluent) through groundwater systems. Geophysical methods (`MC-nsg-ERT` time-lapse) are widely used because contaminant-modified groundwater has distinctive electrical signatures (lower σ for hydrocarbon plumes due to insulating non-aqueous phase; higher σ for ionic-contaminant plumes). Canonical: DOE Hanford Site (Washington); LLNL Site 300 (California); Borden Aquifer (Canada) controlled experiments.

**Mechanism (4-step chain)**:
1. **(Source)** Contaminant release from leaking USTs, landfills, manufacturing facilities, mining operations, agricultural NUE inefficiency (`PD-nutrient-runoff`).
2. **(Hydrology + transport)** Advection and dispersion in groundwater; characteristic plume shape elongated in flow direction; retardation by sorption for many organics.
3. **(Geochemistry)** Reactive transport: biological degradation, chemical reaction with aquifer minerals, redox changes that modify both contaminant and aquifer geochemistry.
4. **(Geophysics)** ERT and EM time-lapse track plume migration through changing σ; mass-balance closure between geophysics-derived plume volume and source records.

**Observables per discipline**:
- **Near-surface geophysics**: time-lapse ERT (`MC-nsg-ERT`); cross-borehole ERT for high-resolution monitoring; complementary CSEM and IP (induced polarization).
- **Hydrology**: monitoring-well sampling (legally-mandated at many contaminated sites); chemical analysis (organics by GC-MS, ions by IC); isotope tracing (`MC-hydro-isotopes`) for source attribution.
- **Atmospheric sciences**: not direct, but airborne plumes (post-disturbance) parallel.
- **Ecology**: biotic responses to subsurface contamination; bioremediation as restoration approach.
- **Agricultural sciences**: nitrate plumes from agricultural sources (`PD-nutrient-runoff`).

**Open questions for translator-agent integration**:
- Quantitative plume-volume estimation from ERT requires careful background-σ characterization; uncertainty quantification is non-trivial.
- 3D plume migration is rarely fully characterized; 1D-2D approaches dominate.
- Bioremediation and natural-attenuation monitoring: geophysics can track but not directly attribute mechanism.

**Anchor papers**:
- Slater, L., Versteeg, R., Cassiani, G., Pellerin, F., Comas, X., Knight, R., & Slater, M. (2008). Electrical geophysics for environmental and hydrological monitoring: An overview. *Surveys in Geophysics*, 29(3), 169–197. doi:10.1007/s10712-008-9036-0
- Kemna, A., Vanderborght, J., Kulessa, B., & Vereecken, H. (2002). Imaging and characterisation of subsurface solute transport using electrical resistivity tomography (ERT) and equivalent transport models. *Journal of Hydrology*, 267(3–4), 125–146. doi:10.1016/S0022-1694(02)00145-2

**Related cards**: `CC-nsg-resistivity`, `MC-nsg-ERT`, `MC-nsg-AEM`, `CC-hydro-h`, `CC-hydro-K`, `MC-hydro-isotopes`, `PD-aquifer-architecture`, `PD-nutrient-runoff`

---

## PD-permafrost-thaw: Geophysical monitoring of permafrost and active-layer dynamics

**Setting**: permafrost (perennially-frozen ground) and the seasonally-thawing active layer above. Permafrost stores ~1,300 Gt soil organic carbon — twice the atmospheric C pool; thaw releases CO₂ and CH₄, the major climate-change positive feedback in high-latitude carbon cycling. Geophysical monitoring is essential because direct sampling is destructive and limited in spatial extent. PNW relevance is limited to high-elevation Olympic and North Cascade marginal permafrost; the bigger PNW analog is glacier loss and post-glacial landform dynamics (overlap with `PD-debris-flow` mechanisms).

**Mechanism (4-step chain)**:
1. **(Atmospheric)** Air-temperature warming accelerates permafrost thaw; thresholds depend on latitude, snow cover, vegetation, and soil organic matter.
2. **(Hydrology + thermal)** Active-layer thickness increases; the talik (unfrozen ground beneath water bodies) expands; subsurface drainage patterns reorganize.
3. **(Ecology + geochemistry)** Microbial decomposition of organic matter releases CO₂ and CH₄ (the methane release is the higher-warming-impact term per molecule); ecosystem state shifts.
4. **(Geomorphology)** Thaw-induced slumping (retrogressive thaw slumps), thermokarst, coastal erosion in Arctic; permafrost-controlled infrastructure failure.

**Observables per discipline**:
- **Near-surface geophysics**: ERT (`MC-nsg-ERT`) maps frozen-unfrozen interface via dramatic σ contrast (ice has σ ~ 10⁻⁹ S/m); time-lapse ERT tracks active-layer dynamics; GPR (`MC-nsg-GPR`) images ice content via reflection coefficients.
- **Hydrology**: subsurface drainage reorganization; expanded talik beneath water bodies enables new groundwater pathways.
- **Atmospheric**: greenhouse-gas flux measurements at thaw sites (eddy covariance `MC-eco-eddycov`); regional atmospheric inverse modeling.
- **Ecology**: vegetation shifts (greening or browning depending on drainage); shrubification of formerly tundra ecosystems.
- **Geomorphology**: thaw slumps and thermokarst mapped from lidar and satellite imagery.

**Open questions for translator-agent integration**:
- Magnitude of permafrost-carbon feedback under different climate scenarios is the dominant uncertainty in century-scale climate projections.
- Localized vs. regional thaw drivers: snow cover, vegetation, soil heterogeneity all matter at site scales.
- Operational permafrost monitoring at landscape scales is incipient; lidar + ERT + remote sensing combinations are the path forward.

**Anchor papers**:
- Schuur, E. A. G., et al. (2015). Climate change and the permafrost carbon feedback. *Nature*, 520(7546), 171–179. doi:10.1038/nature14338
- Hauck, C., Böttcher, M., & Maurer, H. (2011). A new model for estimating subsurface ice content based on combined electrical and seismic data sets. *The Cryosphere*, 5(2), 453–468. doi:10.5194/tc-5-453-2011
- Doetsch, J., Ingeman-Nielsen, T., Christiansen, A. V., Fiandaca, G., Auken, E., & Elberling, B. (2015). Direct current (DC) resistivity and induced polarization (IP) monitoring of active layer dynamics at high temporal resolution. *Cold Regions Science and Technology*, 119, 16–28. doi:10.1016/j.coldregions.2015.07.002

**Related cards**: `MC-nsg-ERT`, `MC-nsg-GPR`, `CC-nsg-resistivity`, `CC-nsg-permittivity`, `CC-atm-T`, `MC-atm-ERA5`, `CC-eco-GPP`, `MC-eco-eddycov`, `PD-debris-flow`
