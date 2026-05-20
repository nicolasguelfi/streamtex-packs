"""
# Stat hero — Centerpiece statistic in big numerals

## Visual

```
                          72%
                of CO2 emissions are
                from energy production
```

A slide centerpiece: a single large numeric value with a short caption
underneath. Captures attention immediately and frames the slide's argument.

## Structure

- `st_write(stat_hero.value, …)` for the big number.
- `st_write(stat_hero.body, …)` for the caption beneath.

## Styling rules

| Element | Style |
|---|---|
| value | stat_hero.value |
| body | stat_hero.body |

## Extrapolation rules

### INVARIANTS
- One value per stat_hero — never multiple.
- The value is rendered visually huge (font-size 60-90px).

### PARAMS
- value: numeric or short string (e.g. "72%", "3.4×")
- body: 1-2 line explanation

### INTERDITS
- No surrounding container — the stat_hero takes the visual stage.
- No bullets in the body.

## When to use

- The hook slide of a section.
- Evidence supporting a paragraph in a longer block.

## When NOT to use

- For multiple stats side-by-side (use a card_grid of stat_hero instances).
- For a non-numeric headline (use slide_heading).

## Design system bundles required

- stat_hero.value
- stat_hero.body
"""

from streamtex import st_write

__component_meta__ = {
    "name": "stat_hero",
    "description": "Big-number centerpiece with one-line caption.",
    "tags": ["stat", "hero", "evidence"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["stat_hero.value", "stat_hero.body"],
    "granularity": "block",
}


def stat_hero(*, design_system, value: str = "", body: str = "") -> None:
    """Render a stat hero (big number + caption)."""
    st_write(design_system.stat_hero.value, value)
    if body:
        st_write(design_system.stat_hero.body, body)
