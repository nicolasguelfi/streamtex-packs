# streamtex-pack-gse

Project-specific StreamTeX pack for the **AI4SE / GSE training family**.
Sits on top of [`streamtex-pack-design`](../streamtex-pack-design/) (which
ships the generic design systems and components) and adds:

- a **GSE design system** (`gse`) — extends the `default` palette with the
  GSE-One brand colors (G/S/E letter colors, amber highlight);
- a **`transition_gse` component** — pivot slide into the GSE-One methodology
  (logo on the left, pivot prose on the right);
- a **`gse_letter` component** — inline highlight of the G/S/E initials in a
  multi-word phrase (e.g. **G**enerative **S**oftware **E**ngineering).

## Consume

In your project `stx.toml`:

```toml
[[packs]]
type = "git"
name = "streamtex-pack-design"
ref = "github.com/nicolasguelfi/streamtex-packs#streamtex-pack-design"
rev = "pack-design-v0.3.0"

[[packs]]
type = "git"
name = "streamtex-pack-gse"
ref = "github.com/nicolasguelfi/streamtex-packs#streamtex-pack-gse"
rev = "pack-gse-v0.1.0"

[design_system]
use = "gse"

[resolution]
prefer = ["streamtex-pack-gse", "streamtex-pack-design"]
```

In `pyproject.toml`:

```toml
dependencies = [
    "streamtex-pack-gse @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-gse-v0.1.0#subdirectory=streamtex-pack-gse",
]
```

## Why a dedicated pack

`transition_gse` was historically shipped from `streamtex-pack-design` while
it is, by design, project-specific (`extrapolable: false`). Moving it into a
GSE-scoped pack keeps `pack-design` free of project artefacts and gives the
GSE family a stable home for further specialisations.
