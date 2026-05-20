"""
# Card grid — Responsive grid of compact cards

## Visual

```
   ┌───────────┐ ┌───────────┐ ┌───────────┐
   │ Title 1   │ │ Title 2   │ │ Title 3   │
   │ Body...   │ │ Body...   │ │ Body...   │
   └───────────┘ └───────────┘ └───────────┘
```

A responsive grid that lays out N homogeneous cards in a `repeat(auto-fit,
minmax(280px, 1fr))` template. Each card has an optional title and a short
body.

## Structure

- `st_grid` with auto-fit columns.
- Per card: a `with st_block(card_grid.card)` container.
- Card body: `st_write(card_grid.card_title, …)` + `st_write(card_grid.card_body, …)`.

## Styling rules

| Element | Style |
|---|---|
| card | card_grid.card |
| card_title | card_grid.card_title |
| card_body | card_grid.card_body |

## Extrapolation rules

### INVARIANTS
- All cards share the same visual height ambition (`align-items: stretch`).
- Each card has at most one title and a 1-3 line body.

### PARAMS
- min_card_width: 240px - 320px (defaults to 280px)
- gap: tight (16) | regular (24) | loose (32)
- columns: auto (fit) | fixed N

### INTERDITS
- No mixed card sizes within one grid.
- No deep nested content (≤ 2 visual levels per card).

## When to use

- Feature lists with parallel structure.
- "What's missing" / "Key takeaways" grids of callouts.

## When NOT to use

- A list of N items with a single column → use `takeaways`.
- Comparing 2 options across 5 criteria → use `comparison_table`.

## Design system bundles required

- card_grid.card
- card_grid.card_title
- card_grid.card_body
"""

from streamtex import st_block, st_grid, st_write

__component_meta__ = {
    "name": "card_grid",
    "description": "Responsive grid of homogeneous compact cards.",
    "tags": ["grid", "cards", "layout"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["card_grid.card", "card_grid.card_title", "card_grid.card_body"],
    "granularity": "composition",
}


def card_grid(*, design_system, items: list = None, min_card_width: str = "280px", gap: str = "24px") -> None:
    """Render a responsive card grid. `items` is a list of (title, body) pairs."""
    items = items or []
    with st_grid(cols=f"repeat(auto-fit, minmax({min_card_width}, 1fr))", gap=gap) as g:
        for title, body in items:
            with g.cell():
                with st_block(design_system.card_grid.card):
                    if title:
                        st_write(design_system.card_grid.card_title, title)
                    if body:
                        st_write(design_system.card_grid.card_body, body)
