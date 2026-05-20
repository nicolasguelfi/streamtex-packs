"""
# Column features — Semantic feature grid with bulleted lists

## Visual

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ CREATE      │  │ STYLE       │  │ PUBLISH     │
│             │  │             │  │             │
│ • Item 1    │  │ • Item 1    │  │ • Item 1    │
│ • Item 2    │  │ • Item 2    │  │ • Item 2    │
│ • Item 3    │  │ • Item 3    │  │ • Item 3    │
└─────────────┘  └─────────────┘  └─────────────┘
   (success)        (info)           (warn)
```

A horizontal grid of 2 to 4 columns, each rendered as a callout-style
cell with a colored section header and a bulleted item list. Used to
showcase parallel categories: "Create / Style / Publish", "Reusable
artefacts / Distribution model", etc.

## Structure

- Outer `st_grid` with responsive `repeat(auto-fit, minmax(...))` columns
- Each cell is a `with st_block(callouts.<variant>)` callout container
- Inside each cell: header (`bold, big, accent color`) + bulleted `st_list`

## Styling rules

- Cell background and left border come from the design system's
  `callouts.<variant>` style (info / warn / success / error).
- Header color uses the design system's callout title styling.
- Bullet list items use the design system's body.paragraph.

## Extrapolation rules

### INVARIANTS
- All cells render at the same width via `repeat(auto-fit, minmax(...))`.
- Each variant maps deterministically to a `callouts.<variant>` bundle —
  no ad-hoc color overrides.
- Bulleted lists are unordered (use `takeaways` if numbered order matters).

### PARAMS
- `columns`: list of `(label, variant, items)` triples.
  - `label`: section header (e.g. "Create", "Style", "Publish").
  - `variant`: one of `success`, `info`, `warn`, `error`.
  - `items`: list of strings (bullet items).
- `min_col_width`: minimum cell width before wrapping (default `"280px"`).
- `gap`: gap between cells (default `24`).

### INTERDITS
- More than 4 columns — the cells become too narrow on standard viewports.
- Mixing variants per cell (e.g. green border + amber background).
- Nested column_features inside column_features.

## When to use

- 2–4 parallel categories that a reader should scan side-by-side
  (capabilities, audience segments, before/after summaries).

## When NOT to use

- For 5+ items with no category structure → use `takeaways`.
- For dense data with multiple attributes per item → use `comparison_table`.
- For a single emphasized statement → use `callout`.

## Design system bundles required

- `callouts.info`, `callouts.warn`, `callouts.success`, `callouts.error`
- `callouts.title`
- `body.paragraph`
"""

import streamtex as stx
from streamtex import st_block, st_grid, st_list, st_space, st_write
from streamtex.core.discovery import get_bundle_attr

__component_meta__ = {
    "name": "column_features",
    "description": "N-column semantic grid with colored cells + bulleted item lists.",
    "tags": ["grid", "callout", "features", "overview"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": [
        "callouts.info",
        "callouts.warn",
        "callouts.success",
        "callouts.error",
        "callouts.title",
        "body.paragraph",
    ],
    "granularity": "composition",
}


def column_features(
    *,
    design_system,
    columns: list[tuple[str, str, list[str]]],
    min_col_width: str = "280px",
    gap: int = 24,
) -> None:
    """Render N callout-style cells side-by-side, each with a header + bullet list.

    Args:
        design_system: An instance providing ``callouts.<variant>``, ``callouts.title``,
            and ``body.paragraph`` bundles.
        columns: List of ``(label, variant, items)`` triples. ``variant`` is one of
            ``"info"``, ``"warn"``, ``"success"``, ``"error"``.
        min_col_width: CSS min-width for each cell before grid wraps.
        gap: Gap in pixels between cells.
    """
    grid_gap = stx.StxStyles.container.grid.gap_24 if gap == 24 else _gap_style(gap)
    with st_grid(
        cols=f"repeat(auto-fit, minmax({min_col_width}, 1fr))",
        grid_style=grid_gap,
    ):
        for label, variant, items in columns:
            container = get_bundle_attr(
                design_system.callouts, variant, "column_features",
            )
            with st_block(container):
                st_write(design_system.callouts.title, label)
                st_space("v", 0.5)
                with st_list(
                    list_type="ul", li_style=design_system.body.paragraph,
                ) as l:
                    for item in items:
                        with l.item():
                            st_write(item)


def _gap_style(gap: int):
    """Build a grid gap style for non-default gap values."""
    from streamtex.styles import Style
    return Style(f"gap: {gap}px;", f"cf_gap_{gap}")
