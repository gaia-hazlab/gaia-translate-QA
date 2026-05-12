# Card format specification — Gaia translator skill files

This spec codifies the schema that the v3 hydrology and seismology long-form cards already follow. Cards live at `skills/long_form/<discipline>/<card_type_plural>.md`. Each file is a single Markdown document containing multiple cards of one type for one discipline.

Schema version: **v3**.

## Front-matter (required)

Every long-form card file starts with a YAML front-matter block:

```yaml
---
discipline: <hydrology|seismology|geotechnical_engineering|geomorphology|atmospheric_sciences|ecology|agricultural_sciences|near_surface_geophysics>
card_type: <concept|method|phenomenon|translation>
schema_version: v3
---
```

The four `card_type` values name the four card flavors. Translation cards are the only flavor where `discipline` may be arguable; use the discipline of the file in which the card is *authored*, not the disciplines it bridges. The same translation card ID (e.g., `TC-02`) is referenced from all bridged disciplines but lives in exactly one file.

## Card IDs

- Concept cards: `CC-<disc>-<short>` — e.g., `CC-hydro-K`, `CC-seismo-Vs`, `CC-geotech-MohrCoulomb`.
- Method cards: `MC-<disc>-<short>` — e.g., `MC-seismo-DAS`, `MC-geotech-CPT`.
- Phenomenon dossiers: `PD-<short>` (no discipline prefix; phenomena are cross-discipline by design) — e.g., `PD-liquefaction`, `PD-AR-landslide`.
- Translation cards: `TC-<NN>` zero-padded if helpful, but two digits is fine — e.g., `TC-02`, `TC-12`. Numeric order = order of authoring; semantics are not encoded in the number.

Every card ID must be globally unique across the corpus.

## Card structure

Each card is a level-2 heading (`## CC-...`, `## MC-...`, `## PD-...`, `## TC-...`) followed by the card body. Cards within a file are separated by `---` horizontal rules.

### Concept card sections (in order)

1. `## CC-<disc>-<short>: <Quantity name and primary symbol> [units]`
2. **Quantity** — one paragraph: physical meaning, tensorial rank if relevant, units (SI and any conventional non-SI like MPa, bar, m²/day).
3. **Defining relation** — the equation(s) that define it. Inline LaTeX or plain ASCII; consistent across cards.
4. **Typical ranges** — bulleted list of representative numerical ranges with units. Order: smallest → largest, or by setting. Use real numbers, not handwave like "varies."
5. **Cross-discipline equivalents** — for each adjacent discipline where an equivalent exists, name the equivalent variable, link the target card, and give the bridge in one phrase. If no equivalent, omit the discipline rather than write "n/a."
6. **When you see this in a paper** — one paragraph hook: what to verify, common reporting traps, what the unqualified term usually means.
7. **Anchor citations** — 2–4 full citations with DOI. Primary references only; reviews if no primary exists.
8. **Related cards** — backlinks to other cards in the corpus.

### Method card sections (in order)

1. `## MC-<disc>-<short>: <Method name>`
2. **What it is** — one paragraph: what the method measures and how.
3. **What you can retrieve** — bullets: data products, output formats, standard software, data centers.
4. **Failure modes** — bullets: known biases, common pitfalls, scale limits.
5. **Cross-discipline uses** — bullets: how the method is used outside its home discipline.
6. **When you see this in a paper** — paragraph: what to verify (response correction, parameter choices, software version).
7. **Anchor citations** — 2–4 with DOI.
8. **Related cards**.

### Phenomenon dossier sections (in order)

1. `## PD-<short>: <Phenomenon name>`
2. **Setting** — geographic / tectonic / climatic / temporal scope; canonical case studies.
3. **Mechanism (N-step chain)** — numbered steps, each labeled with the discipline(s) that own the step: `**(seismology + hydrology)** ...`. This makes cross-discipline structure legible at a glance.
4. **Observables per discipline** — bullets, one per discipline that contributes.
5. **Open questions for translator-agent integration** — bullets: what's not yet resolved and where the agent should surface this as a research opportunity.
6. **Anchor papers** — full citations with DOI; cite primary works that established the mechanism plus 1 modern review.
7. **Related cards**.

Phenomenon dossiers may run slightly longer than 200 words because the mechanism chain has many steps. Target 250 words; hard cap 350.

### Translation card sections (in order)

1. `## TC-<NN>: <One-line bridge name>`
2. **Shared structure** — one paragraph: the abstract bridge (governing equation, measurement principle, statistical machinery).
3. **Discipline-specific manifestations** — bullets, one per discipline, naming the discipline-specific variable / observable / method.
4. **When the analogy holds** — bullets: conditions under which the bridge is physically valid.
5. **When the analogy breaks** — bullets: regimes where the verbal similarity outruns the physics.
6. **Translator agent move** — one paragraph: what concrete retrieval/response action the chatbot should take when it sees this bridge in a query.
7. **Anchor citations** — 2–4 with DOI.
8. **Related cards**.

## Hard rules

- **Length** (calibrated to the seismology + geotech + hydrology reference standard):
  - Concept cards: target ~280 words, hard cap 450.
  - Method cards: target ~330 words, hard cap 450.
  - Phenomenon dossiers: target ~400 words, hard cap 500.
  - Translation cards: target ~450 words, hard cap 550.
  - These targets replace the earlier ≤200-word aspiration, which the actual reference cards (seismology: 265–442; geotech: 234–468; hydrology: 273–500) did not honor. The bar is "match the density of the existing v3 corpus." A linter (Phase 3) will flag outliers above hard caps for review rather than reject them; the targets are advisory.
- **Citations**: every factual claim must trace to either an in-card citation or a `Related cards` pointer that itself carries the citation. Anchor citations carry full DOI or, if no DOI exists, full bibliographic information including publisher and year.
- **Cross-discipline equivalents**: every concept and method card must have at least one explicit cross-discipline equivalent (named, linked, and with a one-phrase bridge), unless the card explicitly documents a "this is unique to this discipline" finding.
- **"When you see this in a paper" hook**: required on every concept and method card. Not a stylistic option — it's load-bearing for the agent's paper-interpretation flow.
- **Vocabulary collisions**: when a card uses a term that collides across disciplines (e.g., "noise," "Q," "permeability," "diffusivity"), flag the collision in the card body and ensure the term appears in `skills/agent_playbook.md` vocabulary table.

## Co-retrieval index

Every card must have an entry in `skills/co_retrieval_index.yaml` declaring:

- `always_retrieve_with`: cards that must be co-retrieved.
- `cross_discipline_anchors`: per-discipline anchors (cards or papers) to surface.
- `caveats`: mandatory caveats to apply when this card is hit.

A card without a co-retrieval entry is invisible to the retrieval layer. Authoring a card and the entry are a single atomic deliverable.

## Filing

- Long-form cards go in `skills/long_form/<discipline>/<card_type_plural>.md`. Translation cards live with their authoring discipline.
- Short summaries go in `skills/summaries/<discipline>.md`. Target 350 words; system-prompt-grade.
- The cross-cutting concepts file `skills/cross_cutting_concepts.md` holds *principles*, not cards. When a principle has been crystallized into a translation card (e.g., effective stress → `TC-02`), the principle still lives in the cross-cutting file but should point to its translation card.

## Citation discipline (mirrored from `agent_playbook.md`)

DOIs are mandatory where they exist. Use the canonical form `doi:10.xxxx/yyyy` in card bodies. Do not abbreviate journal names beyond standard ISO 4 abbreviations. Pre-2000 papers with no DOI cite full publisher and city.
