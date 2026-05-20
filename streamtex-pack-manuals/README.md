# streamtex-pack-manuals

Manual-authoring pack on top of [`streamtex-pack-design`](../streamtex-pack-design).

Part of the [`nicolasguelfi/streamtex-packs`](https://github.com/nicolasguelfi/streamtex-packs)
monorepo.

Provides 3 components for the recurring welcome / overview patterns of
documentation manuals:

| Component | Purpose |
|---|---|
| `level_badge_hero` | Gradient title card + sidebar-left badge box (manual cover page) |
| `column_features` | 2–3 column grid with semantic-colored cells + bulleted lists |
| `pitch_hero` | Centered gradient hero card for opening statements |

## Quick start

```bash
# Inside any StreamTeX project
stx pack add git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-manuals-v0.1.0#subdirectory=streamtex-pack-manuals
stx kit install streamtex-pack-manuals:manuals-default
```

This pulls `streamtex-pack-design` transitively (the components rely on its
design systems for callouts, body, titles bundles).

## Python module

The pip name `streamtex-pack-manuals` provides the Python module `streamtex_manuals`
(decoupled by design):

```python
from streamtex_manuals.components.level_badge_hero import level_badge_hero
from streamtex_manuals.components.column_features import column_features
from streamtex_manuals.components.pitch_hero import pitch_hero
```

## License

[Business Source License 1.1](LICENSE).
