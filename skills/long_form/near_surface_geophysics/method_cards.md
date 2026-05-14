---
discipline: near_surface_geophysics
card_type: method
schema_version: v3
---

# Near-surface geophysics — method cards

Each card describes one measurement technique, instrument, or dataset relevant to near-surface geophysics. Format follows `docs/card_format_spec.md`. MASW and HVSR are owned by seismology (`MC-seismo-MASW`) and geotechnical engineering (`MC-geotech-HVSR`); cross-referenced here rather than duplicated.

---

## MC-nsg-ERT: Electrical resistivity tomography

**What it is**: 2D / 3D imaging of subsurface resistivity ρ_e from arrays of surface (or borehole) electrodes injecting current and measuring voltage. Various electrode arrays (Wenner, Schlumberger, dipole-dipole) sample the subsurface at depths set by electrode spacing. Inversion converts apparent-resistivity pseudosections to true resistivity images via regularized optimization (Loke & Barker 1996; Günther & Rücker 2015 pyGIMLI). The workhorse hydrogeophysical method for water-table mapping, plume tracking, and time-lapse infiltration monitoring.

**What you can retrieve**:
- 2D resistivity tomograms along survey lines; 3D tomograms with crossing arrays.
- Time-lapse images for monitoring water-content change, contaminant migration, salt-water intrusion.
- Depth of investigation: 5–10× minimum electrode spacing (typical: 10–100 m for surface; 100–500 m with borehole arrays).
- Cross-borehole ERT for high-resolution imaging between wells.
- Software: pyGIMLI (open-source), RES2DINV, BERT.

**Failure modes**:
- Inversion is non-unique; regularization choices control feature amplitude and continuity.
- Smooth inversion smears sharp interfaces; block-inversion or structurally-constrained inversion needed for sharp targets.
- Sensitivity drops rapidly with depth and electrode spacing; deep features need long arrays.
- Surface electrodes have galvanic-contact requirements; dry surface conditions degrade data quality.
- Galvanic vs. capacitive vs. induced-polarization data have distinct calibration concerns.

**Cross-discipline uses**:
- **Hydrology**: the dominant geophysical method for water-table mapping, plume tracking, and time-lapse infiltration; foundational for hydrogeophysics (`PD-aquifer-architecture`).
- **Agricultural sciences**: in-field σ maps for salinity, drainage, soil-texture zoning at precision-agriculture scale (Romero-Ruiz et al. 2018).
- **Geotechnical engineering**: ERT identifies clay-rich zones, seepage paths in earth dams, void detection.
- **Geomorphology**: regolith-bedrock interface depth complements lidar (`MC-geomorph-lidar`).
- **Environmental forensics**: contaminant-plume tracking (`PD-contaminant-plume`).

**When you see this in a paper**: confirm array configuration, electrode spacing, depth of investigation, and inversion-regularization parameters; resolution tests should accompany interpretation.

**Anchor citations**:
- Loke, M. H., & Barker, R. D. (1996). Rapid least-squares inversion of apparent resistivity pseudosections by a quasi-Newton method. *Geophysical Prospecting*, 44(1), 131–152. doi:10.1111/j.1365-2478.1996.tb00142.x
- Binley, A., & Slater, L. (2020). *Resistivity and Induced Polarization: Theory and Applications to the Near-Surface Earth*. Cambridge University Press. doi:10.1017/9781108685955

**Related cards**: `CC-nsg-resistivity`, `MC-nsg-GPR`, `MC-nsg-AEM`, `PD-aquifer-architecture`, `PD-contaminant-plume`, `TC-08`, `TC-19`

---

## MC-nsg-GPR: Ground-penetrating radar

**What it is**: high-frequency (typically 100 MHz – 1 GHz) electromagnetic-pulse transmission from a surface antenna, reception of reflections from subsurface dielectric contrasts, and inference of subsurface structure from two-way travel times. Resolution and penetration trade off: higher frequencies give better resolution but shallower depth. Standard tool for shallow stratigraphy, infrastructure mapping, archaeology, and (with Topp's equation) soil-moisture mapping.

**What you can retrieve**:
- Subsurface reflectors at 1–10 m depth (1 GHz) to 30 m (100 MHz) in dry / freshwater settings.
- 2D radargrams and 3D radar-cube volumes for shallow stratigraphy.
- Soil water content via Topp's equation (`CC-nsg-permittivity`).
- Buried-infrastructure mapping (utility location); archaeological subsurface features.
- Software: RadEx, Reflexw, GPRpy.

**Failure modes**:
- Conductive (clay-rich, saline) ground attenuates GPR signals to negligible depths within meters.
- Surface roughness creates ringing; coupling artifacts confuse interpretation.
- Reflector identification requires velocity calibration; default ε_r = 9 (water-saturated soil) is often a poor assumption.
- 3D imaging requires dense survey grids; offline processing is time-consuming for production work.

**Cross-discipline uses**:
- **Hydrology**: GPR is a direct probe of soil water content via Topp's equation; complementary to point-scale sensors and remote-sensing soil moisture (`MC-hydro-SMAP`).
- **Agricultural sciences**: in-field root-zone water-content mapping; precision-agriculture decision support.
- **Geomorphology**: shallow stratigraphy in fluvial / aeolian / glacial deposits; depth-to-bedrock for soil-production studies.
- **Archaeology**: non-destructive subsurface feature detection.
- **Engineering**: utility location; permafrost-active-layer mapping in cold regions.

**When you see this in a paper**: confirm antenna frequency, survey configuration (single antenna vs. common offset vs. CMP), velocity calibration approach, and processing chain. Depth conversion from time without velocity calibration is unreliable.

**Anchor citations**:
- Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic determination of soil water content. *Water Resources Research*, 16(3), 574–582. doi:10.1029/WR016i003p00574
- Annan, A. P. (2002). GPR — History, trends, and future developments. *Subsurface Sensing Technologies and Applications*, 3(4), 253–270. doi:10.1023/A:1020657129590

**Related cards**: `CC-nsg-permittivity`, `MC-nsg-ERT`, `MC-hydro-COSMOS`, `MC-ag-soil-moisture`, `PD-aquifer-architecture`, `PD-permafrost-thaw`

---

## MC-nsg-AEM: Airborne electromagnetic survey

**What it is**: helicopter- or fixed-wing-platform-mounted EM systems that fly over terrain, transmitting EM pulses and measuring secondary-field decay or phase-amplitude response. Provides regional-scale (100s–1000s of km²) mapping of subsurface conductivity at 100–400 m depth of investigation. Commercial systems: VTEM, RESOLVE, SkyTEM, TEMPEST. The dominant tool for regional aquifer mapping and salinity monitoring at landscape-to-watershed scales.

**What you can retrieve**:
- Regional σ(z) maps at flight-line resolution (typically 50–200 m line spacing).
- 1D σ(z) profiles below each measurement point; 2D / 3D inversion when line spacing permits.
- Aquifer-architecture mapping: brackish-fresh water interfaces, paleochannel detection, clay layer continuity.
- Recent landmark surveys: USGS Mississippi Embayment AEM (2018, Minsley et al. 2021); California DWR statewide AEM (ongoing); Australia AEM and groundwater initiatives.

**Failure modes**:
- Cultural-noise interference (powerlines, pipelines) corrupts large patches of survey data.
- Near-surface resolution (top 10 m) is poor compared to ground methods (`MC-nsg-ERT`); complementary.
- 1D inversion under-resolves laterally heterogeneous geology; 3D inversion is computationally expensive.
- Vegetation, topography, and flight-altitude variations require careful processing.

**Cross-discipline uses**:
- **Hydrology**: aquifer-architecture mapping at unprecedented scale; foundational for state-scale groundwater management (California SGMA, Mississippi Embayment groundwater sustainability planning).
- **Agricultural sciences**: AEM maps inform irrigation-management at the regional scale; salinity mapping in irrigated arid regions.
- **Geomorphology**: paleochannel detection in alluvial systems; regional regolith mapping.

**When you see this in a paper**: confirm system (VTEM vs. SkyTEM vs. TEMPEST etc.), frequency range, depth of investigation, inversion method, and cultural-noise removal. AEM data quality has improved markedly over the 2010s; older surveys may have higher noise floors.

**Anchor citations**:
- Christensen, N. B., & Auken, E. (2014). Optimizing the geophysical method for resource exploration and groundwater modeling. *Geophysics*, 79(3), B175–B183. doi:10.1190/geo2013-0339.1
- Minsley, B. J., et al. (2021). Airborne geophysical surveys of the lower Mississippi Valley demonstrate broad applicability of high-resolution AEM. *Scientific Reports*, 11, 17856. doi:10.1038/s41598-021-97193-8

**Related cards**: `CC-nsg-resistivity`, `CC-nsg-EM-conductivity`, `MC-nsg-ERT`, `MC-hydro-GRACE`, `PD-aquifer-architecture`, `PD-aquifer-depletion`

---

## MC-nsg-refraction: Seismic refraction tomography

**What it is**: active-source seismic method using surface or near-surface shots and geophone arrays to record first-arrival travel times from refracted P-waves. Inverts travel times for V_p(z) profile or 2D / 3D V_p models. Distinct from refraction microtremor and MASW (`MC-seismo-MASW`); refraction tomography focuses on body-wave first arrivals through layered or heterogeneous subsurface.

**What you can retrieve**:
- V_p(z) profiles to 10–100 m depth; 2D V_p sections along survey lines.
- Bedrock topography under regolith; weathering-thickness mapping.
- Tomographic inversion (PStomo, PEST) handles laterally variable velocity structure.
- Software: PStomo, PEST, REFLEX.

**Failure modes**:
- Hidden-layer problem: low-velocity layers below high-velocity layers are not detected from first arrivals alone.
- Resolution decreases with depth; near-surface heterogeneity affects deep models.
- Inversion assumes 2D structure; out-of-plane heterogeneity produces artifacts.
- Refraction requires monotonically-increasing velocity with depth at most useful array geometries.

**Cross-discipline uses**:
- **Geotechnical engineering**: foundational for bedrock-depth and weathering-thickness characterization; informs `CC-geotech-FS` and infrastructure-design.
- **Geomorphology**: bedrock-regolith interface in soil-production studies; complements `MC-geomorph-lidar` topography.
- **Hydrology**: aquifer-confining-layer geometry for `MC-hydro-modeling` configurations.
- **Seismology**: same physics as deep-Earth refraction tomography; near-surface velocity model informs site-amplification studies (`PD-site-response`).

**When you see this in a paper**: confirm source type (sledgehammer, weight drop, vibroseis), geophone spacing, array length, and inversion method. Hidden-layer assumption should be tested with synthetic-noise resolution test.

**Anchor citations**:
- Sheehan, J. R., Doll, W. E., & Mandell, W. A. (2005). An evaluation of methods and available software for seismic refraction tomography analysis. *Journal of Environmental and Engineering Geophysics*, 10(1), 21–34. doi:10.2113/JEEG10.1.21
- Reynolds, J. M. (2011). *An Introduction to Applied and Environmental Geophysics* (2nd ed.). Wiley-Blackwell.

**Related cards**: `MC-seismo-MASW`, `MC-geotech-HVSR`, `CC-nsg-impedance`, `CC-seismo-Vs`, `MC-nsg-ERT`, `TC-08`

---

## MC-nsg-gravity: Ground and airborne gravimetry for subsurface mapping

**What it is**: precise measurement of gravitational acceleration g at the surface (or by airborne or marine platforms) to recover subsurface density variations. Distinct from satellite gravimetry (GRACE; `MC-hydro-GRACE`) — at near-surface scale, ground gravimeters (LaCoste-Romberg, A-10 absolute gravimeters, FG5) and airborne gravimetry resolve features at 10s of meters to kilometers. Microgravity time-lapse monitoring tracks subsurface mass changes including groundwater (Pool 2008).

**What you can retrieve**:
- Bouguer-corrected gravity anomalies revealing density variations in the upper crust.
- Microgravity time-lapse (precision 1–10 µGal) tracks subsurface mass changes — water storage, soil moisture, snow.
- Cavity / void detection at depth precision related to anomaly size; void detection routinely demonstrated for tunnels and caves.
- Airborne gravimetry over inaccessible terrain.

**Failure modes**:
- Depth ambiguity: the same anomaly can be produced by a near-surface high-contrast body or a deep low-contrast body.
- Terrain corrections at high relief require precise topography (lidar-derived); inadequate correction creates terrain artifacts.
- Instrument drift in continuous monitoring requires routine reference-station checks.
- Survey design is the primary control on what can be resolved; iso-line spacing and station-spacing must match target scale.

**Cross-discipline uses**:
- **Hydrology**: time-lapse microgravity for groundwater storage monitoring at the well-field scale (Pool 2008); complementary to GRACE at smaller scales.
- **Volcanology**: edifice density changes preceding eruptions; gravity-deformation joint analyses.
- **Geotechnical engineering**: cavity and karst feature detection beneath infrastructure.
- **Geophysics joint inversion**: gravity + seismic for basin-geometry imaging (`TC-08`).

**When you see this in a paper**: confirm correction stack (latitude, free-air, Bouguer, terrain), reference density assumption, instrument-drift correction. Microgravity for hydrology requires careful network design and station stability.

**Anchor citations**:
- Pool, D. R. (2008). The utility of gravity and water-level monitoring at alluvial aquifer wells in southern Arizona. *Geophysics*, 73(6), WA49–WA59. doi:10.1190/1.2980395
- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics* (2nd ed.). Cambridge University Press.

**Related cards**: `CC-nsg-gravity`, `MC-hydro-GRACE`, `MC-nsg-magnetics`, `TC-08`

---

## MC-nsg-magnetics: Ground and airborne magnetic surveys

**What it is**: measurement of total magnetic field intensity F [nT] at the surface or from airborne platforms (helicopter, fixed-wing, UAV) to map magnetic-susceptibility variations. Standard instruments: proton-precession and Overhauser magnetometers for ground survey; cesium vapor magnetometers for high-precision airborne work. Aeromagnetic surveys provide regional-scale coverage; ground surveys give meter-scale resolution for archaeology and infrastructure work.

**What you can retrieve**:
- Total-field anomaly maps; vertical-gradient and analytic-signal-derived data products.
- Detection of buried ferromagnetic objects (rebar, pipes, USTs, UXO).
- Structural geological mapping: dike orientations, fault traces, ore-body extents.
- Geological-survey aeromagnetic data (USGS, USGS-USGS) covering large fractions of conterminous U.S.

**Failure modes**:
- IGRF correction required to remove regional field; geomagnetic-storm transients can mimic anomalies.
- Diurnal-variation correction needed for high-precision work.
- Non-uniqueness in inversion: many subsurface configurations produce the same surface anomaly.
- Limited utility for non-magnetic-mineral targets; water content per se has no magnetic signal.

**Cross-discipline uses**:
- **Geotechnical engineering**: buried-infrastructure detection in urban surveys; rebar mapping in concrete.
- **Archaeology**: non-destructive identification of buried features (kilns, hearths).
- **Geology / mineral exploration**: structural mapping and ore exploration.
- **Geomorphology**: paleomagnetic stratigraphy in sediment cores; magnetic susceptibility as paleoclimate proxy in loess records.

**When you see this in a paper**: confirm IGRF correction date and version; diurnal correction; whether the analysis uses raw total field, vertical gradient, or analytic-signal-derived products.

**Anchor citations**:
- Reynolds, J. M. (2011). *An Introduction to Applied and Environmental Geophysics* (2nd ed.). Wiley-Blackwell.

**Related cards**: `CC-nsg-magnetics`, `MC-nsg-gravity`, `MC-nsg-ERT`

---

## MC-nsg-joint-inversion: Joint geophysical inversion in the critical zone

**What it is**: a methodological approach (rather than a single instrument) that combines two or more geophysical observables in a single inversion framework. Cross-gradient (Gallardo & Meju 2003) enforces structural similarity without prescribing a petrophysical link; explicit petrophysical coupling (Archie's law `CC-nsg-resistivity` for ρ_e ↔ S_w, Gassmann for V_p ↔ saturation, ROSETTA for σ ↔ θ) links observables through physical relationships. Defining methodology of hydrogeophysics; the technique behind `TC-08` and the central operational approach for critical-zone imaging (`TC-19`).

**What you can retrieve**:
- Coupled images of multiple subsurface properties (V_p, V_s, ρ_e, ε_r, density) with reduced individual-method non-uniqueness.
- Petrophysically-informed estimates of hydrologic state variables (porosity, water content, salinity).
- Improved imaging of structures observed similarly by multiple methods.
- Software: pyGIMLI (open-source, supports cross-gradient ERT-MT-gravity), PEST, PEST++, Stochastic Engine for cross-discipline.

**Failure modes**:
- Cross-gradient assumes structural alignment of subsurface contrasts; failure modes occur when contrasts in different observables don't align.
- Petrophysical coupling requires site-specific calibration; textbook values produce biased coupled inversions.
- Resolution mismatch: joint inversion can introduce artifacts in the lower-resolution model.
- Computationally expensive; 3D joint inversion of large datasets is rare in operational practice.

**Cross-discipline uses**:
- **Hydrology**: hydrogeophysics is essentially joint inversion (Linde et al. 2006; Binley et al. 2015); foundational for `PD-aquifer-architecture` and `PD-critical-zone-imaging`.
- **Geotechnical engineering**: seismic + ERT joint inversion for site characterization improves Vs profile recovery beneath the upper-30 m surface-wave-resolution limit.
- **Geomorphology / ecology / agriculture**: joint imaging of soil-bedrock interface, regolith depth, root-zone water content.
- **Seismology**: same methodology as crustal joint inversion (`TC-08`).

**When you see this in a paper**: confirm the joint-inversion architecture (cross-gradient vs. petrophysical vs. structurally-constrained), the calibration of coupling parameters, and the explicit uncertainty quantification. Single-method inversions report less but at least don't add coupling-model assumptions.

**Anchor citations**:
- Gallardo, L. A., & Meju, M. A. (2003). Characterization of heterogeneous near-surface materials by joint 2D inversion of dc resistivity and seismic data. *Geophysical Research Letters*, 30(13), 1658. doi:10.1029/2003GL017370
- Linde, N., Binley, A., Tryggvason, A., Pedersen, L. B., & Revil, A. (2006). Improved hydrogeophysical characterization using joint inversion of cross-hole electrical resistance and ground-penetrating radar traveltime data. *Water Resources Research*, 42(12), W12404. doi:10.1029/2006WR005131
- Parsekian, A. D., Singha, K., Minsley, B. J., Holbrook, W. S., & Slater, L. D. (2015). Multiscale geophysical imaging of the critical zone. *Reviews of Geophysics*, 53(1), 1–26. doi:10.1002/2014RG000465

**Related cards**: `MC-nsg-ERT`, `MC-nsg-GPR`, `MC-nsg-AEM`, `MC-nsg-refraction`, `MC-seismo-tomography`, `MC-seismo-MASW`, `CC-nsg-resistivity`, `CC-nsg-permittivity`, `TC-08`, `TC-19`, `PD-critical-zone-imaging`, `PD-aquifer-architecture`
