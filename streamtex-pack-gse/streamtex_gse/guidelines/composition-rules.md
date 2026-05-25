---
name: composition-rules
description: Universal composition rules R1-R13 for slide decks
rules: [R1, R10, R11, R12, R13, R2, R3, R4, R5, R6, R7, R8, R9]
applies_to: [components, projects]
since: 2026-05-05
---

# Design guideline — gse v1.0.0

Universal composition rules for slide decks (or any single-frame
visual artifact) that adopt the GSE graphic line. Framework-agnostic.

> **R-numbering note**: rule numbers are preserved from the original
> FC-260507 project where this extract originates, so traceability across
> projects is preserved. Gaps (R3, R4, R5, R6, R8, R9, R10) correspond to
> rules that were FC-specific (typography sizes, tooltip widget config,
> dimension-to-slide mapping) and are intentionally NOT in this universal
> extract — projects re-introduce them locally.

---

## R1 — One idea per slide

Each slide has exactly one focal point. Elaborations go to tooltips, a
caption, or a separate slide. If you find yourself writing more than one
idea, split the slide.

**Why**: matches §4 contrast model — one luminous focal element per
composition. A second idea introduces a second focal point and breaks the
register.

---

## R2 — Visual identity → see `graphic-line.md`

The single source of truth for the visual identity is
[`graphic-line.md`](graphic-line.md). Block files / image prompts MUST:

- Use the palette tokens from §3 — no off-palette colours.
- Use the prompt template from §10 — `PREFIX + scene + SUFFIX`.
- Stay within the vocabulary of §5 — abstract figures, stylised icon
  buildings, network constellations, amber AI accent.
- Avoid every element listed in §9 (forbidden).

When in doubt, defer to §11 (archetypes) for a validated composition.

---

## R7 — Image centring delegated to the parent block

Single hero image: centring is performed by the **parent block**
(`page_fill_center` or equivalent flex container); the image style itself
remains neutral (`s.none` in StreamTeX, `style=""` in HTML).

**Why**: keeps the image atom reusable across templates with different
centring needs (T01 centred, T02 image-left, T03 two-images).

---

## R11 — Use only framework primitives

Use only the host framework's primitives (StreamTeX, React, Vue, etc.).
Force-majeure raw HTML / CSS injection is allowed only when:

- A required behaviour cannot be obtained through any primitive (e.g.,
  CSS `:hover` for true tooltip in vanilla Streamlit).
- The container/page-level needs a one-time global style override (e.g.,
  reducing Streamlit's default top padding).

Each force-majeure exception MUST be documented inline (in the block's
docstring or component's comment) with the reason it cannot be expressed
through a primitive.

---

## R12 — AI image prompts assembled from PREFIX + scene + SUFFIX

All AI-generated images use:

```
<contents of prompts/prefix.txt>            ← canonical PREFIX text
<scene-specific description>                ← 3–6 sentences, drawn from an archetype
<contents of prompts/suffix-landscape.txt>  ← or suffix-portrait.txt / suffix-square.txt
```

The PREFIX locks the register: deep dark navy `#1A1A2E` canvas, flat
vector with soft inner gradients, saturated palette, abstract symbolic
compositions, no detailed faces, no books, no AR overlays. The SUFFIX
enforces orientation, the single-focal-element rule, and the
no-text/no-label/no-number guardrails.

**Never override scene-by-scene** — if a project needs a variant prefix
(e.g., for a sub-deck with a different register), bump GSE major and add
a parallel `prompts/prefix-variant.txt` rather than diverging silently.

For working examples: `example.py` at the root (any image generator) or
`integrations/streamtex/example_block.py` (StreamTeX consumer).

---

## R13 — No numbers in filenames or stable identifiers

Sequence belongs to the **orchestrator** (the slide list, the route
config, the navigation manifest), never to the filesystem.

- Block files: `bck_<slug>.py`, never `bck_01_<slug>.py`.
- AI image cache `name=` keys: `<project>_<slug>_<composition_hint>`,
  never `<project>_01_<slug>`.
- `Style.create("...")` identifiers: drop sequence numbers — use content
  slugs.

**Why**: inserting / removing / reordering an item is then a single-file
edit (the orchestrator) — no rename ripple across the codebase, no broken
git history, no stale cache key collisions.

