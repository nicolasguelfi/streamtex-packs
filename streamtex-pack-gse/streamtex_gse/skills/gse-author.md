---
name: gse-author
description: Author content in the GSE visual register — pick the right archetype, apply palette tokens correctly, compose AI prompts that respect the GSE guardrails.
---

# GSE author — quick reference

This skill helps you (or an agent) write content that respects the
**GSE Graphic Style Editorial** visual identity. It pulls together the
palette, archetypes, prompts and composition rules shipped by
`streamtex-pack-gse`.

## When to invoke

- Drafting a new slide or block that should fit the GSE register
  (deep dark navy canvas, saturated palette, abstract symbolic figures).
- Composing an AI image prompt that should produce GSE-style imagery
  (use `stx artifact show scene_generation --kind ai_prompt`).
- Picking the right archetype for a given narrative beat — list
  available archetypes with `stx archetype list` (or
  `stx artifact list --kind archetype`).

## Workflow

1. **Identify the intent** of the slide (transition? evidence? decision?
   federation? recourse? …).
2. **Pick the matching archetype**:
   - transition between two states → `bridge`, `horizon`
   - decision / fork in the road → `forking-path`, `ballot`
   - balance / proportionality → `balance`
   - federation / network → `federation`, `cycle`
   - arrival of the new → `panel-spires`, `doorway`
   - institutional procession → `path-of-arrows`, `closing`
3. **Apply the palette**: read the canonical hexes via
   `stx artifact show main --kind palette`. NEVER hardcode a hex
   outside this palette.
4. **For AI image generation**: compose `PREFIX + scene + SUFFIX-<orientation>`.
   The pack ships the prefix and the three orientation suffixes ready
   to concatenate.
5. **Check the rules**: `stx artifact show graphic-line --kind guideline`
   for the full spec, `composition-rules` for the R1-R13 composition
   rules that apply to slide decks.

## Common pitfalls

- Using **yellow** outside of `amber` — breaks the contrast model.
- Showing **multiple amber accents** in one composition — there should
  always be exactly one focal warmth.
- Adding **text or numbers** inside generated images — explicitly
  forbidden by the `suffix-*` constraints.
- Rendering **realistic faces** — figures must remain abstract back-view
  silhouettes.

## Quick links to artifacts shipped by this pack

- Palette: `streamtex-pack-gse:main`
- AI prompts: `streamtex-pack-gse:scene_generation`
- Archetypes (11): balance, ballot, bridge, closing, cycle, doorway,
  federation, forking-path, horizon, panel-spires, path-of-arrows
- Guidelines: `graphic-line`, `composition-rules`
