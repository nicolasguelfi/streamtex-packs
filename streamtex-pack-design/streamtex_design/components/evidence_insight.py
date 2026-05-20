"""
# Evidence insight — Slide combining a stat hero with a takeaway and a source

## Visual

```
                         72%
              of CO2 emissions are from
                energy production

         1. Coal still dominates baseload
         2. Renewables grow but lag behind
         3. Storage is the next bottleneck

         — IPCC AR6 WG3, 2022
```

A slide template that frames a statistic with derived takeaways and a source
citation. Composed from stat_hero + takeaways + cite.

## Structure

- A `stat_hero` block.
- A `takeaways` list of 2-4 items.
- A `cite` source attribution.

## Styling rules

| Element | Style |
|---|---|
| value | stat_hero.value |
| takeaways | takeaways.item |
| citation | citation.source |

## Extrapolation rules

### INVARIANTS
- Always exactly one stat_hero and one cite.
- Takeaways count is 2-4 items.

### PARAMS
- stat value / caption
- takeaway items (2-4)
- source attribution

### INTERDITS
- No multi-value stat (use a card_grid of stats instead).
- No takeaways longer than one short sentence each.

## When to use

- Evidence slides supporting a claim.
- Closing slides of a research section.

## When NOT to use

- Pure narrative slides — use slide_heading + body paragraph.
- Comparison slides — use comparison_table.

## Design system bundles required

- stat_hero.value
- stat_hero.body
- takeaways.lead
- takeaways.item
- citation.source
- citation.author
"""

from streamtex import st_space

from streamtex_design.components.cite import cite
from streamtex_design.components.stat_hero import stat_hero
from streamtex_design.components.takeaways import takeaways

__component_meta__ = {
    "name": "evidence_insight",
    "description": "Slide combining stat_hero + takeaways + cite.",
    "tags": ["evidence", "slide", "composite"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": [
        "stat_hero.value",
        "stat_hero.body",
        "takeaways.lead",
        "takeaways.item",
        "citation.source",
        "citation.author",
    ],
    "granularity": "block",
    "uses_components": ["stat_hero", "takeaways", "cite"],
}


def evidence_insight(
    *,
    design_system,
    value: str = "",
    caption: str = "",
    insights: list = None,
    source: str = "",
) -> None:
    """Render the composite evidence_insight slide."""
    stat_hero(design_system=design_system, value=value, body=caption)
    st_space("v", 2.0)
    takeaways(design_system=design_system, items=insights or [])
    st_space("v", 1.5)
    cite(design_system=design_system, source=source)
