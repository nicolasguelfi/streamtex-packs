# streamtex-packs

Collection of [StreamTeX](https://github.com/nicolasguelfi/streamtex) packs maintained by [@nicolasguelfi](https://github.com/nicolasguelfi).

A **pack** is a Python package that ships reusable visual artefacts —
components, design systems, kits, project blueprints — for consumption
by StreamTeX documents.

## Packs in this monorepo

| Pack | Version | Description |
|------|---------|-------------|
| [streamtex-pack-design](streamtex-pack-design/) | v0.3.0 | Foundations + universal components. 3 design systems (default / modern_dark / modern_light) with extended `Colors` (info/success/warning/critical/highlight), new `Fonts` bundle, 19 components, 6 kits. Public re-exports for `Colors`, `Titles`, `Fonts`, `Callouts`, `Body`. |
| [streamtex-pack-manuals](streamtex-pack-manuals/) | v0.2.0 | Manual-authoring **and** instructor-led training components on top of pack-design: level badges, pitch heroes, FAQ, trainer profile, training header/footer, glossary, references list, changelog card. Two kits: `manuals-default` + `training-default`. |
| [streamtex-pack-gse](streamtex-pack-gse/) | v0.1.0 | Project-specific pack for the AI4SE / GSE training family: `gse` design system (GSE-One brand colors), `transition_gse` slide, `gse_letter` inline component. |

## Which pack for which document?

| You want to build … | Declare these packs in `stx.toml` | Pick design system |
|---|---|---|
| A manual in the family-stx-manuels line | pack-design + pack-manuals | `default` (or `modern_dark` / `modern_light`) |
| A training session / instructor-led deck | pack-design + pack-manuals (+ kit `training-default`) | `default` |
| A module in the family-stx-gse line | pack-design + pack-gse | `gse` |
| A generic slide deck (no project identity) | pack-design only | `default` (or `modern_dark`) |

CLI templates for each scenario ship in
[`streamtex-pack-design/streamtex_design/cli_templates/`](streamtex-pack-design/streamtex_design/cli_templates/)
— `new-manual/`, `new-training/`, `new-gse-module/`.

## Foundation bundles — composable styles for new documents

From `streamtex-pack-design 0.3.0`, the foundation bundles of the `default`
design system are re-exported at the package root so a new document can
write a slim `custom/styles.py`:

```python
from streamtex_design import Colors, Titles, Fonts, Callouts, Body

# Compose new project styles from the pack's bundles
my_section_title = Titles.section + Colors.primary
```

The bundle inventory is:

| Bundle | Slots |
|---|---|
| `Colors` | primary, accent, bg, surface, text, muted, info, success, warning, critical, highlight |
| `Titles` | slide, section, subtitle, body, caption |
| `Fonts`  | body_family, heading_family, code_family |
| `Callouts` | info, warn, error, success, icon, title, body |
| `Body` | paragraph, emphasis, code |

`Fonts` is currently **optional** in the streamtex `DesignSystemProtocol`
— third-party design systems that do not declare it remain conforming.
It will be promoted to required in a future minor.

## Patterns → packs migration

The legacy `streamtex-patterns` system (markdown catalogue of `ptn_*.md`
files) is deprecated. See
[`docs/PATTERNS_MIGRATION.md`](docs/PATTERNS_MIGRATION.md) for the
canonical mapping of `ptn_*` to component import paths. No action is
required for existing documents that still use `[patterns]` in their
`stx.toml`.

## How to reference a pack from a StreamTeX consumer

Add to your project's `pyproject.toml`:

```toml
dependencies = [
    "streamtex-pack-design @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-design-v0.3.0#subdirectory=streamtex-pack-design",
    "streamtex-pack-manuals @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-manuals-v0.2.0#subdirectory=streamtex-pack-manuals",
    "streamtex-pack-gse @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-gse-v0.1.0#subdirectory=streamtex-pack-gse",
]
```

For local development with editable installs, override via `[tool.uv.sources]`:

```toml
[tool.uv.sources]
streamtex-pack-design  = { path = "../streamtex-packs/streamtex-pack-design",  editable = true }
streamtex-pack-manuals = { path = "../streamtex-packs/streamtex-pack-manuals", editable = true }
streamtex-pack-gse     = { path = "../streamtex-packs/streamtex-pack-gse",     editable = true }
```

The Dockerfile-side `uv sync --no-sources` ignores the local override and
falls back to the `git+https...#subdirectory=` URL, fetching each pack
from this monorepo via a single shared clone.

## Python module naming

The pip package name (`streamtex-pack-{name}`) is **decoupled** from the
Python module name:

| Pip package | Python module |
|-------------|---------------|
| `streamtex-pack-design` | `streamtex_design` |
| `streamtex-pack-manuals` | `streamtex_manuals` |
| `streamtex-pack-gse` | `streamtex_gse` |

This decoupling means renaming the pip package does NOT affect existing
`from streamtex_design.components import callout` imports.

## Versioning

Each pack has its own version, released via **prefixed git tags** on the
monorepo:

- `pack-design-v0.3.0` → release of `streamtex-pack-design v0.3.0`
- `pack-manuals-v0.2.0` → release of `streamtex-pack-manuals v0.2.0`
- `pack-gse-v0.1.0` → release of `streamtex-pack-gse v0.1.0`
- `pack-{name}-vX.Y.Z` → release of `streamtex-pack-{name} vX.Y.Z`

To consume, reference the prefixed tag in the `@` clause of the dep URL.

## License

[Business Source License 1.1](LICENSE) (same as `streamtex` itself).
