---
discipline: atmospheric_sciences
card_type: translation
schema_version: v3
---

# Atmospheric sciences — translation cards

Cross-discipline bridges originating from atmospheric sciences. Complements `TC-05` (data assimilation across atm-hydro-seismo) and `TC-06` (watershed mass balance ↔ atmospheric branch), both already touching atmospheric sciences. Format follows `docs/card_format_spec.md`.

---

## TC-15: Clausius-Clapeyron and the intensification cascade across atmospheric, hydrologic, and geomorphic extremes

**Shared structure**: a warmer atmosphere holds more water vapor (~7%/K via Clausius-Clapeyron); the additional moisture is available for precipitation. The thermodynamic scaling sets a baseline rate of extreme-precipitation intensification; dynamical changes (storm organization, AR strengthening, MCS updraft intensification) can amplify or reduce this. The intensified precipitation extreme then cascades through hydrologic, geomorphic, geotechnical, and ecological systems, each amplifying or transforming the signal in its own way. This is the canonical climate-extremes cross-discipline bridge.

**Discipline-specific manifestations**:
- **Atmospheric**: column-integrated water vapor (`CC-atm-q`) follows Clausius-Clapeyron at fixed RH; sub-daily precipitation extremes show super-CC scaling 10–15%/K (Lenderink & van Meijgaard 2008); ARs in CMIP6 intensify faster than CC (Espinoza et al. 2018).
- **Hydrology**: nonstationary flood-frequency curves (`CC-geomorph-flood-frequency`); shifts in the relationship between precipitation extremes and streamflow extremes; rain-on-snow vs. snow vs. rain regime shifts at intermediate elevations.
- **Geomorphology**: shallow-landslide and debris-flow triggering thresholds (`PD-AR-landslide`, `PD-debris-flow`); post-fire windows with reduced thresholds (`PD-post-fire-erosion`); channel-forming flood intensification (`PD-river-floods`).
- **Geotechnical engineering**: revision of design-event rainfall (PMP) and design-flood (PMF) under nonstationary climate; revised dam-safety hazard assessments (`PD-dam-levee-safety`).
- **Ecology / agriculture**: extreme-precipitation flooding alters ecosystem and crop production; downstream sediment delivery alters habitat (`PD-salmon-habitat`).

**When the analogy holds**:
- Thermodynamic Clausius-Clapeyron scaling is well-validated at synoptic to climatological scales; ~7%/K applies to column-integrated moisture.
- Cascading impacts share the same underlying intensification driver, so the framework provides a unified narrative.
- High-resolution convection-permitting models reproduce the super-CC scaling at sub-daily timescales.

**When the analogy breaks**:
- Mean-precipitation changes do *not* follow CC (constrained by global energy balance to ~1–3%/K), only extremes.
- Dynamical contributions are regime- and region-dependent; tropical-cyclone, MCS, and AR intensification have different mechanisms and rates.
- Compound extremes (heat + precip, drought-then-flood) involve interactions that single-variable CC scaling misses (Zscheischler et al. 2018).
- The cascade is not monotonic: drier antecedent conditions can change hillslope response to a given precipitation event in either direction.

**Translator agent move**: when a paper reports extreme-precipitation or extreme-flood trends, identify (a) the scaling rate (% per K), (b) whether thermodynamic vs. dynamical decomposition is attempted, (c) the assumed stationarity. For impact studies in geomorph / geotech / hydro, the intensification cascade is the through-line — cross-retrieve `PD-atmospheric-river`, `PD-AR-landslide`, `PD-debris-flow`, and `PD-river-floods` together when this bridge is invoked.

**Anchor citations**:
- Held, I. M., & Soden, B. J. (2006). Robust responses of the hydrological cycle to global warming. *Journal of Climate*, 19(21), 5686–5699. doi:10.1175/JCLI3990.1
- Westra, S., Fowler, H. J., Evans, J. P., Alexander, L. V., Berg, P., Johnson, F., Kendon, E. J., Lenderink, G., & Roberts, N. M. (2014). Future changes to the intensity and frequency of short-duration extreme rainfall. *Reviews of Geophysics*, 52(3), 522–555. doi:10.1002/2014RG000464
- Lenderink, G., & van Meijgaard, E. (2008). Increase in hourly precipitation extremes beyond expectations from temperature changes. *Nature Geoscience*, 1(8), 511–514. doi:10.1038/ngeo262
- Milly, P. C. D., et al. (2008). Stationarity is dead: Whither water management? *Science*, 319(5863), 573–574. doi:10.1126/science.1151915

**Related cards**: `CC-atm-q`, `CC-atm-precip`, `CC-atm-IVT`, `CC-geomorph-flood-frequency`, `CC-hydro-Q`, `PD-atmospheric-river`, `PD-AR-landslide`, `PD-river-floods`, `PD-debris-flow`, `PD-extreme-precip-intensification`, `PD-dam-levee-safety`, `TC-04`, `TC-06`
