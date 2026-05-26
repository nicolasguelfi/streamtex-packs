---
name: graphic-line
description: GSE visual identity spec (palette, register, vocabulary, contrast, forbidden elements)
rules: []
applies_to: [components, archetypes, projects]
since: 2026-05-05
---

# Graphic line — gse v1.0.0

The single source of truth for the GSE visual identity. All other artifacts in
this package (`assets/*`, `src/gse/*`) are derived from this document.

> **Visual reference**: GSE adopts the visual register of the
> `ai4se6d/modules/ai4se6d_gensem` project (the author's existing tech-talk
> register, validated 2026-05-05 via the method-δ persona pilot). Same
> aesthetic, same palette, same illustration technique.

Scene archetypes are documented separately, one file per archetype, in
[`archetypes/`](archetypes/).

---

## 1. Aesthetic statement

**Minimalist digital illustration on dark navy — clean, modern, dignified.
Knowledge, governance, and digital intelligence are rendered as confident
abstract metaphors with vivid pops of saturated colour against a deep dark
canvas.**

The register speaks through clarity, not through narrative scenes. Every image
reads in two seconds as ONE concept. Figures, when present, are abstract
silhouettes — symbolic markers, not characters.

---

## 2. Illustration register

- **Style**: flat 2D vector with soft inner gradients (just enough gradient to
  give clean depth — never painterly grain, never watercolor wash, never
  hand-painted texture).
- **Reference register**: tech-conference editorial illustration — clean
  confident shapes, abstract symbolic compositions, generous dark negative
  space, vivid pops of colour.
- **Geometry**: clean confident shapes, subtle rounded corners, simple flat
  forms with subtle gradient depth. No ornate decoration, no organic
  irregularity, no painterly noise.
- **Finish**: clean digital — every surface is a simple flat or gradient
  fill. No texture overlays.

---

## 3. Colour palette

The canvas is **deep dark navy**. Accents are saturated and vivid — they
glow against the dark.

| Token             | Hex       | Role |
|---|---|---|
| `bg-navy`         | `#1A1A2E` | base canvas (deep dark navy, slight blue tint, NEVER pure black, NEVER warm cream) |
| `electric-blue`   | `#7AB8F5` | primary; ideological dimension; structure; abstract figures; classical building icon |
| `teal`            | `#2EC4B6` | accent; technical dimension; growth, network lines, modern building icon |
| `amber`           | `#F39C12` | highlight; decisional dimension; focal warmth — **ACCENT ONLY**, never dominant |
| `coral`           | `#E07A6E` | political dimension; recourse, warmth without aggression |
| `white`           | `#FFFFFF` | pure highlight, used sparingly for the brightest focal element |
| `muted-gray`      | `#95A5A6` | caption / source text only (never on visuals) |

**Rule of dominance**:

- `bg-navy` dominates the frame (typically 60–70 % of pixels).
- `electric-blue` and `teal` are the workhorses for shapes, figures,
  primary structure.
- `amber` is reserved for the ONE focal warm accent (a glowing node, a
  bridge of light, a spirit-light, a single highlighted icon). NEVER as a
  building fill, NEVER as a background, NEVER as a major surface.
- `coral` appears only on political-dimension scenes (recourse,
  accommodation).
- `white` appears only as the brightest pin-point highlight.

**Forbidden** in image generation:

- Pure black `#000000`
- Warm cream / sand / yellow-dominant backgrounds
- Pastel washes
- Neon hues outside the palette
- Cold gray fills

---

## 4. Contrast model

The single most important rule. The visual register stands or falls on the
contrast.

- **One luminous focal element per composition** — typically a glowing
  amber accent (a node, a bridge, a spirit-light, a key icon), or a bright
  teal/electric-blue focal shape.
- **Vivid pops on deep dark** — accent colours are used at full saturation
  to glow against the dark canvas.
- **Soft inner gradients** on shapes give just enough depth without being
  painterly.
- **Generous dark negative space** — the dark canvas is the dominant
  visual element; shapes and accents pop within it.
- **NO atmospheric perspective**, NO volumetric beams, NO sun-glow, NO
  warm shadows. Clean minimalism.
- **NO bright daylight scenes** — the canvas stays dark; brightness comes
  from accent shapes, not from the background.

---

## 5. Visual vocabulary

What may appear in the images, organised by family.

### 5.1 Abstract figures (when present)

- Figures are **abstract symbolic icons**, not characters.
- Shape: simple silhouette of head + shoulders/body; back-view by default;
  electric-blue or teal flat fill with subtle inner gradient.
- **NO faces, NO facial detail, NO eyes, NO expressions.** A figure is
  always a symbolic marker of community/individual, never a portrait.
- One figure (decision/individual semantic), small group of 3–4 (community
  semantic), or circle of 5–7 (federation/cohort semantic).
- Used SPARINGLY — many compositions have no figures at all, just metaphor.

### 5.2 Architecture (when present)

- Stylised **single-shape ICONS**, not buildings:
  - Classical academic = small pediment + two columns (electric-blue fill).
  - Modern academic = simple rectangle + soft rounded corners + a few small
    lit windows (teal fill).
  - Generic institution = clean geometric block with soft gradient.
- Always small, symbolic, never narrative.
- Two building icons together = transition / comparison metaphor.

### 5.3 Network / digital vocabulary

- **Constellation of nodes**: small circular nodes (electric-blue + teal,
  with one or two amber accent nodes), connected by thin teal lines.
  Used for federation, network, governance flow, ambient digital intelligence.
- **Glowing arc / bridge**: a single luminous amber arc connecting two
  elements across dark space — the transition / connection metaphor.
- **Floating panel**: a translucent rectangular shape with subtle gradient
  fill, holding a simple chart shape (a curve, three bar shapes, an icon).
  Used for digital interface / knowledge surface.
- **Light traces**: thin glowing lines tracing along edges of icons or as
  decorative flow.
- **Woven ribbons**: parallel coloured ribbons twisting along a path — the
  "thread of commitments" metaphor.
- **No pixel motes, no holograms, no AR-style overlays** — keep it
  abstract, not skeuomorphic-future.

### 5.4 AI vocabulary

AI is rendered as **a single small amber accent node** OR **an amber
glowing orb / spirit-light** — never as a robot, never as a face, never as
anything anthropomorphic.

- The amber accent is the universal AI signature. When AI is symbolised
  in a composition, one or more nodes / icons / accents are amber.
- A small amber glowing sphere can hover near a figure or icon to indicate
  "ambient AI assistance".

---

## 6. Metaphors and symbols

| Concept | Visual symbol |
|---|---|
| Decision / fork | Single back-view figure + two diverging paths (one dark, one teal) |
| Transition / 30-year horizon | Two building icons (classical + modern) on opposite cliffs + amber arc bridge |
| Federation / community | Central institution icon + circle of 5–7 figure-icons connected by teal lines |
| Knowledge mission | Central glowing teal+amber node + figures arranged inward facing it |
| Governance / deliberation | Round table top-view with nodes around the circumference |
| Digital infrastructure | Constellation of nodes + thin teal lines |
| Ambient AI | Single amber node or amber glowing orb in the composition |
| Path forward / future | Ascending diagonal of light from lower-left to upper-right |
| Three commitments | Three woven ribbons (electric-blue + teal + amber) along a path or bridge |
| Risk / lesson learned | A single small amber pulse next to a calmer pattern (never violent crack) |
| Status quo as dead-end | A path that fades into the dark + a brighter alternative path adjacent |
| Recourse | Open doorway icon with light spilling (coral accent) |
| Vote / decision act | Hand icon over a glowing box / single amber accent |

---

## 7. Composition rules

- **One focal point** — exactly one bright element per scene.
- **Asymmetric** — focal element off-centre (rule of thirds).
- **Diagonal energy preferred** — lower-left → upper-right ascending
  composition for "future" / "growth" semantics; flat horizontal for
  "balance" / "comparison" semantics; symmetric for "federation" /
  "knowledge mission" semantics.
- **Layered depth via opacity** — subtle gradient depth, NOT atmospheric
  perspective.
- **Generous dark negative space** — the dark canvas dominates; shapes pop.
- **NO hard frame, NO black border** (the dark canvas IS the frame).
- **High contrast** — vivid accents glow against deep dark.

---

## 8. Emotional tone

Each composition reads on a 2-second glance as one of:

- **clear** — single readable concept, no ornament
- **modern** — clean digital aesthetic, tech-talk register
- **dignified** — restrained, serious, suitable for academic projection
- **forward-looking** — ascending diagonal, glowing focal accent
- **balanced** — symmetric where the concept is symmetric

Forbidden tones:

- joyful Pixar / playful animated
- anxiety / dread / dystopian
- ornate / decorative / busy
- warm-and-cuddly / sentimental
- corporate-clean (over-polished, sterile)

---

## 9. Forbidden elements

- Photorealism, 3D rendering, anime, cartoon, watercolor, painterly grain.
- Detailed human faces, expressive features, realistic figures.
- Stock-illustration tropes: handshakes, gears, generic light bulbs,
  rocket ships, generic puzzle pieces.
- Books, paper sheets, scrolls, parchments, lecterns, traditional wooden
  desks (paper-era objects feel anachronistic in this digital register).
- Anthropomorphic AI: robots, glowing humanoid AI, anything resembling a
  science-fiction android. The amber accent / glowing orb is the only AI
  presence permitted.
- Brand logos, recognisable real persons, recognisable real places.
- National / religious / cultural markers. *Single ambient exception*: a
  faint EU-stars circle on regulation-themed scenes, low opacity, never
  literal.
- Readable text, words, labels, numbers, captions, watermarks inside the
  image.
- Pure black `#000000`. Use `#1A1A2E` deep navy.
- Cream / sand / yellow-dominant backgrounds.
- Pastel washes, neon hues outside the palette, cold gray fills.
- Cracks, ruins, broken structures.

---

## 10. Prompt templates

The PREFIX establishes the register, palette, contrast model, figure
abstraction, and AI vocabulary. The SUFFIX enforces composition
(orientation, focal element, dark negative space) and the no-text guardrails.
Block files / prompt authors only need to write the **composition-specific
scene description** between these two anchors.

The verbatim text of these templates lives at the package root:

- `prompts/prefix.txt`
- `prompts/suffix-landscape.txt` — 16:10 landscape
- `prompts/suffix-portrait.txt` — 2:3 portrait
- `prompts/suffix-square.txt` — 1:1 square

**Composition pattern**:

```
<contents of prompts/prefix.txt> <scene description, 3–6 sentences, drawn from an archetype> <contents of prompts/suffix-{landscape|portrait|square}.txt>
```

See `archetypes/` for validated scene templates and `example.py` at the
package root for a working stdlib demo.

---

## 11. Scene archetypes

Documented one per file in [`archetypes/`](archetypes/). All 11 archetypes
below are validated and ready to use. Pick one as the starting skeleton
when authoring a new image prompt; full per-archetype recipes (composition,
palette assignment, variation rules, forbidden variations) live in the
individual archetype files.

| Archetype          | File                                              | Concept                                       | Orientation |
|---|---|---|---|
| The bridge         | [`bridge.md`](archetypes/bridge.md)               | Transition / 30-year horizon                  | landscape |
| The horizon        | [`horizon.md`](archetypes/horizon.md)             | Problem statement / future-facing commitment  | landscape |
| The arrival        | [`panel-spires.md`](archetypes/panel-spires.md)   | Arrival of the new; data → built environment  | square    |
| The community      | [`federation.md`](archetypes/federation.md)       | Community of knowledge / federation           | square    |
| The fork           | [`forking-path.md`](archetypes/forking-path.md)   | Decision; status quo vs alternative path      | landscape |
| The cycle          | [`cycle.md`](archetypes/cycle.md)                 | Continuous improvement / process              | square    |
| The balance        | [`balance.md`](archetypes/balance.md)             | Regulation / proportionality                  | landscape |
| The doorway        | [`doorway.md`](archetypes/doorway.md)             | Recourse / accommodation                      | square    |
| The ballot         | [`ballot.md`](archetypes/ballot.md)               | Vote / decision act                           | landscape |
| The path-of-arrows | [`path-of-arrows.md`](archetypes/path-of-arrows.md) | Institutional decision procession           | landscape |
| The closing        | [`closing.md`](archetypes/closing.md)             | Institution alive in the digital age          | landscape |

To add a new archetype: see [`archetypes/README.md`](archetypes/README.md)
for the file template and the convention.

---

*End of graphic-line v1.0.0 specification.*

