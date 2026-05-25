# Patterns → Packs migration

The legacy `streamtex-patterns` system (a markdown catalogue of `ptn_*.md`
files installed per-project via `stx.toml [patterns]`) is **deprecated**.
Every reusable visual artefact now ships as a Python component inside a
pack (`streamtex-pack-design`, `streamtex-pack-manuals`, or
`streamtex-pack-gse`).

This document is the single canonical mapping a new document author should
consult when wondering "where did pattern X go?".

## Status

- **`streamtex-patterns/`** — frozen, no further evolution.
- **Pre-pack projects** that declare `[patterns]` in their `stx.toml` keep
  working — their local `.claude/custom/streamtex-patterns/` copy is
  untouched. **No migration is required for existing documents.**
- **New documents** should NOT use `[patterns]` in their `stx.toml`. They
  should declare the relevant packs in `[[packs]]` and import components
  directly from the pack modules.

## Mapping table

| Legacy pattern              | Pack                       | Python import path                                                   | Notes                                |
|-----------------------------|----------------------------|----------------------------------------------------------------------|--------------------------------------|
| `ptn_slide_heading`         | streamtex-pack-design      | `streamtex_design.components.slide_heading.slide_heading`            |                                      |
| `ptn_callout`               | streamtex-pack-design      | `streamtex_design.components.callout.callout`                        |                                      |
| `ptn_inline_emphasis`       | streamtex-pack-design      | `streamtex_design.components.inline_emphasis.inline_emphasis`        |                                      |
| `ptn_cite`                  | streamtex-pack-design      | `streamtex_design.components.cite.cite`                              |                                      |
| `ptn_card_grid`             | streamtex-pack-design      | `streamtex_design.components.card_grid.card_grid`                    |                                      |
| `ptn_comparison_table`      | streamtex-pack-design      | `streamtex_design.components.comparison_table.comparison_table`      |                                      |
| `ptn_categorized_grid`      | streamtex-pack-design      | `streamtex_design.components.categorized_grid.categorized_grid`      |                                      |
| `ptn_takeaways`             | streamtex-pack-design      | `streamtex_design.components.takeaways.takeaways`                    |                                      |
| `ptn_term_definition_list`  | streamtex-pack-design      | `streamtex_design.components.term_definition_list.term_definition_list` |                                   |
| `ptn_title_slide`           | streamtex-pack-design      | `streamtex_design.components.title_slide.title_slide`                |                                      |
| `ptn_stat_hero`             | streamtex-pack-design      | `streamtex_design.components.stat_hero.stat_hero`                    |                                      |
| `ptn_evidence_insight`      | streamtex-pack-design      | `streamtex_design.components.evidence_insight.evidence_insight`      |                                      |
| `ptn_exercise_flow`         | streamtex-pack-design      | `streamtex_design.components.exercise_flow.exercise_flow`            |                                      |
| `ptn_narrative_transition`  | streamtex-pack-design      | `streamtex_design.components.narrative_transition.narrative_transition` |                                   |
| `ptn_transition_gse`        | **streamtex-pack-gse**     | `streamtex_gse.components.transition_gse.transition_gse`             | Relocated from pack-design v0.3.0    |

## Adopting packs in a new document

Add to your project `stx.toml`:

```toml
[[packs]]
type = "git"
name = "streamtex-pack-design"
ref = "github.com/nicolasguelfi/streamtex-packs#streamtex-pack-design"
rev = "pack-design-v0.3.0"

# Optional, depending on the document family:
[[packs]]
type = "git"
name = "streamtex-pack-manuals"
ref = "github.com/nicolasguelfi/streamtex-packs#streamtex-pack-manuals"
rev = "pack-manuals-v0.2.0"

[[packs]]
type = "git"
name = "streamtex-pack-gse"
ref = "github.com/nicolasguelfi/streamtex-packs#streamtex-pack-gse"
rev = "pack-gse-v0.1.0"

[design_system]
use = "default"   # or "modern_dark", "modern_light", "gse"

[resolution]
prefer = ["streamtex-pack-gse", "streamtex-pack-manuals", "streamtex-pack-design"]
```

Add to your project `pyproject.toml`:

```toml
dependencies = [
    "streamtex>=0.7.7",
    "streamtex-pack-design @ git+https://github.com/nicolasguelfi/streamtex-packs.git@pack-design-v0.3.0#subdirectory=streamtex-pack-design",
    # plus pack-manuals / pack-gse if applicable
]
```

In a block:

```python
from streamtex_design.components.callout import callout
from streamtex_design.design_systems.default import DesignSystem

DS = DesignSystem()

def build():
    callout(design_system=DS, title="Note", body="Replaces ptn_callout.", variant="info")
```

## Styles composables — the easy import

From `streamtex-pack-design 0.3.0` onwards, the foundation bundles of the
`default` design system are re-exported at the package root for direct use
in your own custom styles:

```python
from streamtex_design import Colors, Titles, Fonts, Callouts, Body

class MyStyles:
    callout_title = Colors.primary + Titles.subtitle  # composable Style
```

This lets a new document keep a slim `custom/styles.py` (project palette
only) while leaning on the pack for typography, semantic colors, callouts,
and body styles. Use the alternative design systems by importing them
directly: `from streamtex_design.design_systems.modern_dark import
DesignSystem`.

## Why this is just a documentation move

14 of the 15 generic patterns of the legacy catalogue had already been
re-implemented as Python components in `streamtex-pack-design` between
v0.1.0 and v0.2.5 (see `streamtex-pack-design/CHANGELOG.md`). The
remaining project-specific `ptn_transition_gse` was hosted in pack-design
between v0.2.0 and v0.2.5 and was moved to the new `streamtex-pack-gse`
in v0.3.0 to keep the generic pack free of project artefacts. This
document formalises a state that already existed in code.
