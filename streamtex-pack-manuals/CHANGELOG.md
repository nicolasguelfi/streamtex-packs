# Changelog

All notable changes to streamtex-pack-manuals are documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/);
versions follow semver pinned to the reuse architecture milestones.

## [0.1.0] — 2026-05-20 — First public release in streamtex-packs monorepo

### Added

- Initial public release. Previously the pack lived as a local-only
  workspace folder; it is now formalized as part of the
  [`nicolasguelfi/streamtex-packs`](https://github.com/nicolasguelfi/streamtex-packs)
  monorepo, at subdirectory `streamtex-pack-manuals/`.

### Components shipped

- `level_badge_hero` — hero with gradient background + level badge
  (BEGINNER / ADVANCED / EXPERT) for manual welcome pages.
- `column_features` — 2-column semantic grid (green/blue tints) for
  "what changed at a glance" overview blocks.
- `pitch_hero` — opening hero with bold pitch and supporting subtitle.

### Conventions

- **Pip name**: `streamtex-pack-manuals` (aligned with the
  `streamtex-pack-{name}` ecosystem convention).
- **Python module name**: `streamtex_manuals` (decoupled from the pip
  name; preserved for backward-compatible imports).
- **License**: BUSL-1.1 (same as the streamtex library).
- **Versioning**: per-pack via prefixed git tags
  (`pack-manuals-v0.1.0`) on the monorepo.
- **Requires** `streamtex >= 0.7.7` and `streamtex-pack-design >= 0.2.4`.

### Consumer reference

```toml
dependencies = [
    "streamtex-pack-manuals @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-manuals-v0.1.0#subdirectory=streamtex-pack-manuals",
]
```
