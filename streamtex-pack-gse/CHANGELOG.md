# Changelog

All notable changes to streamtex-pack-gse are documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/);
versions follow semver pinned to the reuse architecture milestones.

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
