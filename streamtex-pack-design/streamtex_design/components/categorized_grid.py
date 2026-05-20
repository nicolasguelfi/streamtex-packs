"""
# Categorized grid — Card grid grouped under category headers

## Visual

```
   ── Backend ───────────────────
   ┌─────┐ ┌─────┐ ┌─────┐
   │ DB  │ │ API │ │ Q   │
   └─────┘ └─────┘ └─────┘

   ── Frontend ──────────────────
   ┌─────┐ ┌─────┐
   │ UI  │ │ Map │
   └─────┘ └─────┘
```

A two-level layout: section dividers (categories) each followed by a small
card_grid scoped to that category.

## Structure

- For each category: a `titles.section` divider line, then a `card_grid`.

## Styling rules

| Element | Style |
|---|---|
| category | titles.section |
| card | card_grid.card |

## Extrapolation rules

### INVARIANTS
- Each category contains ≥ 1 card.
- All categories use the same card width.

### PARAMS
- max categories: 4 (more becomes visually overwhelming)
- min_card_width: same as card_grid

### INTERDITS
- No empty categories.
- No mixed component types per category — all cards or all callouts, not both.

## When to use

- A taxonomy presentation.
- "Stack overview" slides (backend / frontend / data).

## When NOT to use

- A flat list of N items → use `card_grid` directly.
- A comparison across criteria → use `comparison_table`.

## Design system bundles required

- titles.section
- card_grid.card
- card_grid.card_title
- card_grid.card_body
"""

from streamtex import st_block, st_grid, st_space, st_write

__component_meta__ = {
    "name": "categorized_grid",
    "description": "Card grid grouped under category dividers.",
    "tags": ["grid", "categorized", "taxonomy"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": [
        "titles.section",
        "card_grid.card",
        "card_grid.card_title",
        "card_grid.card_body",
    ],
    "granularity": "composition",
}


def categorized_grid(*, design_system, categories: dict = None) -> None:
    """Render a card grid grouped by category. `categories` = {label: [(title, body), ...]}."""
    categories = categories or {}
    for category, items in categories.items():
        st_write(design_system.titles.section, category)
        with st_grid(cols="repeat(auto-fit, minmax(240px, 1fr))", gap="16px") as g:
            for ctitle, cbody in items:
                with g.cell():
                    with st_block(design_system.card_grid.card):
                        st_write(design_system.card_grid.card_title, ctitle)
                        st_write(design_system.card_grid.card_body, cbody)
        st_space("v", 1.5)
