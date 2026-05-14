---
discipline: geomorphology
card_type: translation
schema_version: v3
---

# Geomorphology — translation cards

Cross-discipline bridges originating from geomorphology. Complements `TC-01` (diffusion, where hillslope κ is one of the diffusivities), `TC-02` (effective stress, in hillslope and channel-bed mechanics), `TC-04` (power laws across landslide-size, flood-frequency, and Gutenberg-Richter), `TC-06` (mass balance), and `TC-11` (engineered FS ↔ natural hillslope FS), all of which already involve geomorphology. Format follows `docs/card_format_spec.md`.

---

## TC-13: Sediment continuity ↔ watershed water balance ↔ critical-zone carbon balance

**Shared structure**: the geomorphic, hydrologic, and ecosystem-carbon budgets all take the conservation-law form ∂φ/∂t + ∇·F_φ = sources − sinks. The same skeleton governs:

- *Geomorphology*: ∂z/∂t = U − ∇·Q_s + incision − landslides.
- *Hydrology*: ∂S/∂t = P − ET − Q (`TC-06`).
- *Ecology / critical zone*: ∂C_soil/∂t = NPP − R_eco − leaching − erosional POC export.

Treated as a coupled hydro-geomorphic-ecosystem unit, these budgets share variables (Q, Q_s, ET) and must close jointly. The critical-zone framework (NRC 2001) is the institutional articulation of this coupling.

**Discipline-specific manifestations**:
- **Geomorphology**: sediment continuity drives `CC-geomorph-Qs` and the long-profile evolution; landscape-evolution models (`MC-geomorph-landlab`) integrate the equation forward over 10⁵–10⁷ yr.
- **Hydrology**: P = ET + Q + ΔS is the working water balance (`TC-06`); residual recharge couples to groundwater storage (`CC-hydro-S`).
- **Ecology / biogeochemistry**: erosional sediment carries particulate organic carbon (POC); Hilton et al. (2008) estimated mountain-belt POC export as a significant term in global C cycling; ecosystem NEE and erosional POC export are coupled through the soil-carbon pool.
- **Agricultural sciences**: tillage and land-use changes alter sediment yield and soil carbon stock simultaneously; CRP-style soil-erosion conservation programs intersect agriculture and geomorphology directly.

**When the analogy holds**:
- Conservation is exact within a well-defined control volume; the closure error is a diagnostic of unobserved fluxes (interbasin transfers, anthropogenic withdrawals, inelastic storage changes).
- Co-located observations (eddy covariance for ET and NEE, gauging for Q and Q_s, lidar for ΔZ) close all three budgets at the same scale.
- Steady-state assumptions hold over the appropriate averaging timescale (centuries for sediment; seasonal for water; decadal for carbon).

**When the analogy breaks**:
- Non-stationary forcing (climate change, land-use change) breaks steady-state closure on the timescales we care about for prediction.
- Cross-budget coupling through plant physiology (stomatal conductance links ET and GPP at the leaf) is a *coupling*, not a shared equation; both budgets must be solved jointly.
- Footprint mismatches between observation types (eddy covariance ≈ 1 km²; suspended sediment integrates the upstream basin; lidar DoD captures whatever the survey covered) create aliasing.

**Translator agent move**: when a paper formulates a watershed or critical-zone budget, identify which terms are observed vs. assumed; the closure error is the meaningful diagnostic, not the absolute fluxes. Surface the cross-discipline analogs: a hydrologic budget paper that doesn't address sediment is incomplete for the same basin; a sediment-budget paper that doesn't address water is also incomplete.

**Anchor citations**:
- NRC. (2001). *Basic Research Opportunities in Earth Science*. National Academies Press. doi:10.17226/9981
- Hilton, R. G., Galy, A., Hovius, N., Chen, M.-C., Horng, M.-J., & Chen, H. (2008). Tropical-cyclone-driven erosion of the terrestrial biosphere from mountains. *Nature Geoscience*, 1(11), 759–762. doi:10.1038/ngeo333
- Brantley, S. L., Goldhaber, M. B., & Ragnarsdottir, K. V. (2007). Crossing disciplines and scales to understand the Critical Zone. *Elements*, 3(5), 307–314. doi:10.2113/gselements.3.5.307
- Larsen, I. J., Almond, P. C., Eger, A., Stone, J. O., Montgomery, D. R., & Malcolm, B. (2014). Rapid soil production and weathering in the Southern Alps, New Zealand. *Science*, 343(6171), 637–640. doi:10.1126/science.1244908

**Related cards**: `CC-geomorph-Qs`, `CC-geomorph-erosion-rate`, `CC-hydro-Q`, `CC-hydro-ET`, `CC-hydro-recharge`, `CC-eco-GPP`, `MC-geomorph-landlab`, `MC-hydro-eddycov`, `TC-06`, `PD-landscape-evolution`

---

## TC-14: Bedload transport ↔ high-frequency seismic noise

**Shared structure**: river bedload — the coarse fraction of `CC-geomorph-Qs` — produces a measurable broadband (1–100 Hz) seismic signal as moving grains impact the bed and channel walls. The signal is locally generated and roughly proportional to bedload-power expenditure, linking fluvial geomorphology (sparse, biased sampling) and environmental seismology (continuous passive monitoring of the ambient field, `CC-seismo-noise`). The bridge has matured from empirical correlation (Burtin et al. 2008) to quantitative inversion theory (Tsai et al. 2012; Gimbert et al. 2014) and field validation across diverse rivers (Roth et al. 2016).

**Discipline-specific manifestations**:
- **Geomorphology**: bedload flux Q_s_bedload from Helley-Smith samplers or trap structures; intermittent, expensive, and biased toward calm conditions (`MC-geomorph-sediment-monitoring`).
- **Seismology**: ambient PSD at 5–100 Hz at near-channel broadband stations; the bedload-induced contribution is a meaningful signal, not a nuisance to be filtered (`CC-seismo-noise`, `MC-seismo-broadband`).
- **Hydrology**: discharge Q is the forcing; the seismic-bedload signal envelopes the storm hydrograph but with a different lag than suspended sediment, providing complementary information.
- **Engineering / monitoring**: continuous, non-intrusive monitoring at remote rivers; key for high-flow events when sampling is impossible.

**When the analogy holds**:
- Inversion is most reliable when the bed-material grain size is known and approximately uniform; Gimbert et al. (2014) framework explicitly parameterizes by grain size.
- Stations close to the channel (≤ 100 m) capture the signal cleanly; distant stations dilute the source and are confounded by other noise.
- Suitable for episodic monitoring of bedload pulses (post-fire sediment slugs, dam-removal sediment release).

**When the analogy breaks**:
- Steady-state inversion fails for very high or very low flows where assumed channel and grain conditions don't apply.
- Cultural noise (traffic, machinery) at urban stations swamps the channel signal in the same frequency band; rural deployments needed.
- Multiple co-located processes (rain, wind, debris flows, ice, hyporheic-flow tremor) confound attribution; signal partitioning is the current frontier.

**Translator agent move**: when a paper reports a passive-seismic-based bedload estimate, retrieve the validation against a co-located sampling campaign if available; the inversion framework's assumptions (grain size, station-to-channel distance, frequency band) must be stated. Conversely, when a paper reports a sediment-yield record at a sampling-based gauge, ask whether seismic instrumentation is available — the seismic record can fill the high-flow sampling gap and recover events the gauge missed.

**Anchor citations**:
- Burtin, A., Bollinger, L., Vergne, J., Cattin, R., & Nábělek, J. L. (2008). Spectral analysis of seismic noise induced by rivers: A new tool to monitor spatiotemporal changes in stream hydrodynamics. *Journal of Geophysical Research: Solid Earth*, 113(B5), B05301. doi:10.1029/2007JB005034
- Tsai, V. C., Minchew, B., Lamb, M. P., & Ampuero, J.-P. (2012). A physical model for seismic noise generation from sediment transport in rivers. *Geophysical Research Letters*, 39(2), L02404. doi:10.1029/2011GL050255
- Gimbert, F., Tsai, V. C., & Lamb, M. P. (2014). A physical model for seismic noise generation by turbulent flow in rivers. *Journal of Geophysical Research: Earth Surface*, 119(10), 2209–2238. doi:10.1002/2014JF003201
- Roth, D. L., Brodsky, E. E., Finnegan, N. J., Rickenmann, D., Turowski, J. M., & Badoux, A. (2016). Bed load sediment transport inferred from seismic signals near a river. *Journal of Geophysical Research: Earth Surface*, 121(4), 725–747. doi:10.1002/2015JF003782

**Related cards**: `CC-geomorph-Qs`, `CC-geomorph-streampower`, `CC-geomorph-tau`, `CC-seismo-noise`, `MC-seismo-broadband`, `MC-geomorph-sediment-monitoring`, `MC-hydro-NWIS`, `PD-river-floods`, `PD-debris-flow`
