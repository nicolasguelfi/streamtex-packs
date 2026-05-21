# Changelog

All notable changes to streamtex-pack-design are documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/);
versions follow semver pinned to the reuse architecture milestones.

## [0.2.5] — 2026-05-21 — Slide TOC propagation, part_intro, hover docstring fix

### Added

- **`part_intro` component** — a section-opener slide (part label + title +
  objective + role-in-flow). Registers a table-of-contents entry at level
  `"1"` by default, so every part of a deck is reachable from the sidebar and
  the narrative structure is legible. Addresses the GSE-ODOO finding that
  decks had no per-part intro slides.

### Fixed

- **`title_slide` and `slide_heading` now propagate `toc_lvl`** (optional,
  default `None`). Previously these slide components rendered their title via
  `st_write` *without* a TOC level, so the sidebar / table of contents stayed
  empty even on a 50-slide deck (the GSE-ODOO defect). Pass `toc_lvl="1"` to
  register a navigation entry. Backwards-compatible: omitting it preserves the
  prior (no-TOC) behaviour.
- **`slide_heading` docstring** corrected: it claimed the `st_hover_tooltip`
  widget "ships in streamtex if the project depends on it" — the widget did
  not exist. It now ships in the core `streamtex` library; the example imports
  it directly.

## [0.2.4] — 2026-05-20 — Migration to streamtex-packs monorepo

### Changed

- **Pip name renamed**: `streamtex-design` → `streamtex-pack-design`
  to align with the convention `streamtex-pack-{name}` adopted across
  the StreamTeX pack ecosystem.
- **License**: switched from MIT to BUSL-1.1 (same as the streamtex
  library) for consistency across the ecosystem.
- **Hosting**: the pack now lives in the
  [`nicolasguelfi/streamtex-packs`](https://github.com/nicolasguelfi/streamtex-packs)
  monorepo at the subdirectory `streamtex-pack-design/`.
  The standalone `nicolasguelfi/streamtex-design` repo is archived.
- **Versioning**: per-pack via prefixed git tags
  (`pack-design-v0.2.4`) on the monorepo.
- **Requires** `streamtex >= 0.7.7`.

### Unchanged

- The Python module name (`streamtex_design`) is **preserved** — all
  `from streamtex_design.components import ...` imports continue to
  work without modification.
- All 3 design systems (default / modern_dark / modern_light) unchanged.
- All components unchanged.
- All kits, project blueprints, cli_templates, samples unchanged.

## [0.2.3] — 2026-05-20 — Track streamtex 0.7.6 relative scale

### Changed

- Requires `streamtex >= 0.7.6`.
- The `var(--stx-scale-K, fallback_pt)` references in all 3 design
  systems remain unchanged: streamtex 0.7.6's WORD_PROCESSOR curve
  desktop values are identical to 0.7.5 (round-trip exact), so
  fallback pt values stay valid. The CSS variable runtime values
  now derive from `base_pt_desktop × ratios` instead of absolute pt
  tables, but consumers see the same desktop pt values.
- Per-document `st_book(scale=ScaleConfig(base_pt_desktop=X))` now
  rescales every DS bundle automatically — design systems require no
  per-base configuration.

## [0.2.2] — 2026-05-20 — Indexed responsive scale integration

### Changed

- All three design systems (default, modern_dark, modern_light) now
  consume the indexed responsive font scale via
  `var(--stx-scale-K, fallback_pt)` instead of hardcoded `px` values.
  Components rendered by streamtex-design now respect the parent
  document's `st_book(scale=...)` config and react automatically to
  the 1024px / 480px responsive breakpoints.
- Requires `streamtex >= 0.7.5`.

### Added

- `tests/test_design_systems.py::test_no_hardcoded_px_in_design_systems`
  — guard that fails CI if any design-system bundle declares a
  hardcoded `Npx` font-size.

## [0.2.1] — 2026-05-19 (Legacy reference module removed)

### Removed
- `styles/styles_consolidated.py` (739 lines) — legacy reference
  module that documented the bundle vocabulary derived from the
  `streamtex-patterns` audit (551 blocks, 2026-05-11). The active
  `streamtex_design.design_systems.default` DS was *derived from*
  this palette and is now standalone — no code imports the
  consolidated file. The `streamtex-design/styles/` directory was
  outside the shipped package (`include = ["streamtex_design*"]`),
  so the deletion has no impact on the pack's distribution.
- `streamtex_design.design_systems.default` docstring updated:
  "derived from the legacy styles_consolidated palette" → "neutral
  palette suitable for documentation and slides".

## [0.2.0] — 2026-05-19

### Added
- New component `transition_gse` (block tier, `extrapolable=false`) —
  ai4se6d-specific specialisation of `narrative_transition` pivoting
  into the GSE-One methodology. Replaces the legacy
  `projects/ai4se6d/ptn_transition_gse.md`.
- New kit `core` (8 components) — covers the legacy `core` preset:
  `slide_heading`, `cite`, `inline_emphasis`, `callout`, `card_grid`,
  `comparison_table`, `takeaways`, `term_definition_list`.
- New kit `minimal` (3 atoms) — replaces the legacy `minimal` preset:
  `slide_heading`, `cite`, `inline_emphasis`.
- Kit `course-default` enriched with `categorized_grid`,
  `exercise_flow` for full coverage of the legacy `slides` preset.
- `slide_heading.py` docstring documents the tooltip + 95/5 grid
  workaround (use `st_grid` + `st_hover_tooltip` inline; not bundled
  here for separation of concerns).
- `.github/workflows/test.yml` — pytest + ruff + `stx validate --strict`
  CI replacing the legacy A2 validator.

### Removed (legacy markdown catalogue)
- Directories `core/`, `slides/`, `docs/`, `presets/` (22 `ptn_*.md`
  files + 5 preset `.toml`). All patterns have Python equivalents in
  `streamtex_design/components/`; presets are superseded by kits.
- `_pattern_library.md` (legacy index).
- `scripts/validate.py` + `scripts/README.md` (legacy A2 validator).
- `.github/workflows/validate.yml` (legacy CI calling the validator).
- `projects/streamtex-docs/` (README-only placeholder, no patterns).
- `projects/ai4se6d/` (replaced by the `transition_gse` Python
  component above).

### Changed
- `pyproject.toml` `dependencies = ["streamtex>=0.7.0"]` (was `>=0.6.41`).
- `_pack_manifest.toml` `streamtex_compat = ">=0.7.0,<1.0"`.

### Migration notes
- Consumers of `ptn_inline_emphasis` variants beyond `strong`/`soft`
  (i.e. `keyword`, `accent`, `highlight`, `label`) should treat these
  as **design system properties**, not function kwargs. Define the
  variant in the design system bundle and select it via the existing
  Python signature.
- Consumers of `ptn_slide_heading` with tooltip + 95/5 grid: see the
  inline composition example in the `slide_heading.py` docstring.

## [0.1.0] — 2026-05-19 (Wave 1)

### Added
- Initial release as a Python pack (was: `streamtex-patterns` A2-markdown
  catalog). Conversion is part of Wave 1 of the StreamTeX reuse architecture
  refonte (see `streamtex/documentation/maintenance/reuse-architecture/PLAN.md`).
- Python package `streamtex_design/` with:
  - `_pack_manifest.toml` declaring `[manifest] format = "0.1"` (Q16 mouvant).
  - Entry point `streamtex.packs:streamtex-design` for runtime discovery.
  - 18 components across primitive / composition / block granularities
    (cf. PLAN §9.2): callout, cite, inline_emphasis, slide_heading,
    term_definition_list, card_grid, comparison_table, takeaways,
    title_slide, stat_hero, evidence_insight, exercise_flow,
    categorized_grid, narrative_transition, api_reference_card,
    composite_block, feature_walkthrough, manual_section.
  - 3 design systems: `default` (derived from styles_consolidated palette),
    `modern_dark`, `modern_light`.
  - 4 kits: `course-default`, `manual-default`, `project-default`,
    `slides-modern-dark`.
- pytest suite — 30 tests covering CV001-CV011 (components), DV001-DV006
  (design systems), KV001-KV005 (kits), PV001-PV010 (pack manifest).

### Renamed
- Repository renamed from `streamtex-patterns` to `streamtex-design`
  (GitHub + local). Old remote URLs auto-redirect.

### Deferred
- Conversion of the 14 block blueprints (cf. PLAN §9.3) is deferred to a
  follow-up commit — the 18 patterns above are sufficient to validate the
  architecture end-to-end.
- CLI templates (`cli_templates/`) and project blueprints
  (`project_blueprints/`) are scaffolded as empty directories; their
  population is planned for Wave 2 (Phase 2b sandbox integration).
