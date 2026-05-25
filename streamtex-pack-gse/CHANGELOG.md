# Changelog

All notable changes to streamtex-pack-gse are documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/);
versions follow semver pinned to the reuse architecture milestones.

## [2.0.0] — 2026-05-23 — Manifest 0.2: palette + AI prompts as first-class artifacts

### Added

- **Palette artifact** ``palettes/main.json`` — canonical GSE palette (7 colors
  + 4 semantic dimensions: ideological / political / technical / decisional).
  Multi-runtime by design: readable by Python (Style atoms via the engine),
  Figma export, Midjourney prompts, any tool that reads JSON. Migrated from
  ``streamtex-shared/graphic-designs/gse/palette/colors.json``.
- **AI prompt artifact** ``ai_prompts/scene_generation/`` — prefix.txt + 3
  orientation-specific suffix files (landscape/portrait/square). Migrated from
  ``streamtex-shared/graphic-designs/gse/prompts/``.
- ``[pack.data]`` section in ``_pack_manifest.toml`` declaring the two new
  artifact categories (manifest format 0.2).
- Design system ``gse`` is now **generated at import time** from
  ``palettes/main.json`` via ``streamtex.core.artifacts.palette``. Hex values
  fall back to hardcoded canonical constants when the palette file is missing
  (degraded test environments).
- ``setuptools.package-data`` extended to ship ``palettes/*.json`` and
  ``ai_prompts/**/*.txt``.

### Changed

- Bumped manifest format from ``0.1`` to ``0.2``.
- Bumped version from ``0.1.0`` to ``2.0.0`` (major: jumps to align with the
  ``streamtex-shared/gse`` v1.0.0 that this pack supersedes; subsequent
  ``streamtex-shared/`` will be removed entirely once this pack is published).
- Bumped ``streamtex`` compat to ``>=0.7.16`` (the engine requires the
  ``streamtex.core.artifacts`` module added in 0.7.16's siblings).
- The ``_Colors`` bundle now exposes the 4 semantic dimensions
  (``ideological``, ``political``, ``technical``, ``decisional``) in addition
  to the existing letter accents (``g_letter``, ``s_letter``, ``e_letter``).
  Letter accents are mapped via convention: G → amber, S → teal, E →
  electric-blue.

### Migration

- ``streamtex-shared/graphic-designs/gse/`` is **fully superseded** by this
  pack. The data files (palette JSON + prompts) are now distributed via the
  pip/git pack pipeline rather than file-copy.
- Existing consumers using the previous ``g_letter = #F5A623`` mapping are
  silently corrected to the canonical ``amber = #F39C12``. The new value is
  the one documented in ``graphic-line.md §3``.

## [0.1.0] — 2026-05-23 — First public release

### Added

- Initial release as a separate pack inside the
  [`nicolasguelfi/streamtex-packs`](https://github.com/nicolasguelfi/streamtex-packs)
  monorepo at subdirectory `streamtex-pack-gse/`.
- **`gse` design system** — extends `streamtex-pack-design` defaults with
  GSE-One brand colors: amber `highlight` for the pivot prose, and three
  letter colors (`g_letter`, `s_letter`, `e_letter`) used by the
  `gse_letter` component to colorise the GSE initials.
- **`transition_gse` component** — relocated from `streamtex-pack-design`
  (where it lived since v0.2.0 — see streamtex-pack-design `CHANGELOG.md`).
  Behaviour unchanged. The pack-design copy was removed in
  `streamtex-pack-design 0.3.0`.
- **`gse_letter` component** — new inline helper that takes a phrase and
  highlights the GSE initials (Generative / Software / Engineering by
  default) in their three brand colors. Composable in any inline context.
- **`gse-default` kit** — design system `gse` + the two components above.

### Conventions

- **Pip name**: `streamtex-pack-gse` (aligned with the
  `streamtex-pack-{name}` ecosystem convention).
- **Python module name**: `streamtex_gse` (decoupled from the pip name).
- **License**: BUSL-1.1 (same as the streamtex library).
- **Versioning**: per-pack via prefixed git tags
  (`pack-gse-v0.1.0`) on the monorepo.
- **Requires** `streamtex >= 0.7.7` and `streamtex-pack-design >= 0.3.0`.
