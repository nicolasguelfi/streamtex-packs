# streamtex-packs

Collection of [StreamTeX](https://github.com/nicolasguelfi/streamtex) packs maintained by [@nicolasguelfi](https://github.com/nicolasguelfi).

A **pack** is a Python package that ships reusable visual artefacts —
components, design systems, kits, project blueprints — for consumption
by StreamTeX documents.

## Packs in this monorepo

| Pack | Version | Description |
|------|---------|-------------|
| [streamtex-pack-design](streamtex-pack-design/) | v0.2.4 | Official StreamTeX design pack: 3 design systems (default / modern_dark / modern_light), 20+ components, kits, project blueprints. |
| [streamtex-pack-manuals](streamtex-pack-manuals/) | v0.1.0 | Manual-authoring components on top of streamtex-pack-design (level badges, semantic feature grids, pitch heroes). |

## How to reference a pack from a StreamTeX consumer

Add to your project's `pyproject.toml`:

```toml
dependencies = [
    "streamtex-pack-design @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-design-v0.2.4#subdirectory=streamtex-pack-design",
    "streamtex-pack-manuals @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-manuals-v0.1.0#subdirectory=streamtex-pack-manuals",
]
```

For local development with editable installs, override via `[tool.uv.sources]`:

```toml
[tool.uv.sources]
streamtex-pack-design  = { path = "../streamtex-packs/streamtex-pack-design",  editable = true }
streamtex-pack-manuals = { path = "../streamtex-packs/streamtex-pack-manuals", editable = true }
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

This decoupling means renaming the pip package does NOT affect existing
`from streamtex_design.components import callout` imports.

## Versioning

Each pack has its own version, released via **prefixed git tags** on the
monorepo:

- `pack-design-v0.2.4` → release of `streamtex-pack-design v0.2.4`
- `pack-manuals-v0.1.0` → release of `streamtex-pack-manuals v0.1.0`
- `pack-{name}-vX.Y.Z` → release of `streamtex-pack-{name} vX.Y.Z`

To consume, reference the prefixed tag in the `@` clause of the dep URL.

## Migration note

This monorepo supersedes the standalone repos:

- `nicolasguelfi/streamtex-design` (archived; see [streamtex-pack-design](streamtex-pack-design/))
- `nicolasguelfi/streamtex-manuals` (was local-only; now formalized as [streamtex-pack-manuals](streamtex-pack-manuals/))

The full migration is documented in
[streamtex/documentation/maintenance/pack_monorepo/PLAN.md](https://github.com/nicolasguelfi/streamtex/blob/main/documentation/maintenance/pack_monorepo/PLAN.md).

## License

[Business Source License 1.1](LICENSE) (same as `streamtex` itself).
