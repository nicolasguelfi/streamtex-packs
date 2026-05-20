# streamtex-pack-design

Official StreamTeX **design pack**: components, design systems, kits, and
CLI templates, distributed as a standard Python package per the reuse
architecture spec.

Part of the [`nicolasguelfi/streamtex-packs`](https://github.com/nicolasguelfi/streamtex-packs)
monorepo.

---

## Quick start

```bash
# Inside any StreamTeX project
stx pack add git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-design-v0.2.4#subdirectory=streamtex-pack-design
stx kit install streamtex-pack-design:course-default
```

This declares the pack in `stx.toml`, installs the Python package, sets the
active design system (`default`), and exposes the kit's selected
components.

## What's inside

| Layer | Count | Notes |
|---|---|---|
| Design systems | 3 | `default`, `modern_dark`, `modern_light` |
| Components | 19 | mix of primitive / composition / block (PLAN §9.2) |
| Kits | 6 | core, course-default, manual-default, minimal, project-default, slides-modern-dark |
| Entry point | 1 | `streamtex.packs:streamtex-design` |

Every component validates against the contracts in
`streamtex.core.validation.validate_component` (CV001–CV011). Every
design system validates against `validate_design_system` (DV001–DV006).
Every kit validates against `validate_kit` (KV001–KV005). The pack
manifest validates against `validate_pack` (PV001–PV010).

## Using a component

```python
from streamtex_design.components.callout import callout
from streamtex_design.design_systems.default import DesignSystem as DS

callout(design_system=DS, title="Note", body="Watch the units.", variant="info")
```

Components consume the active design system via keyword argument so a
project can swap systems by changing one import.

## Bundles consumed (`Design system bundles required`)

Each component lists the design-system bundle attributes it depends on
(format `<bundle>.<attr>`). The lib's runtime helper
`streamtex.core.discovery.get_bundle_attr` enriches the error message when
a bundle is missing — pointing the user at `stx validate`.

## Authoring your own pack

Use `streamtex-design` as a working reference, or follow the workflow in
`stx_manual_reuse` (chapter "Pack authoring") and the dedicated
`cookiecutter-streamtex-pack` template (forthcoming).

## License

MIT — see [`LICENSE`](LICENSE).
