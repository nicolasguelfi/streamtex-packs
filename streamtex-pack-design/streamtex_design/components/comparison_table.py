"""
# Comparison table — Tabular comparison of N options across M criteria

## Visual

```
   Criterion    | Option A | Option B
   -------------|----------|---------
   Speed        | fast     | medium
   Cost         | $$$      | $
   Reliability  | high     | medium
```

A simple, regular grid that lines up rows (criteria) against columns
(options). Header row uses `comparison_table.header`; data rows alternate
between `comparison_table.row` and `comparison_table.accent_row` for
readability.

## Structure

- `st_grid` with explicit column count.
- Header row: M `st_write(comparison_table.header, …)` cells.
- Body rows: criterion label + per-option values.

## Styling rules

| Element | Style |
|---|---|
| header | comparison_table.header |
| row | comparison_table.row |
| accent_row | comparison_table.accent_row |

## Extrapolation rules

### INVARIANTS
- All rows have the same number of columns.
- The first column is the criterion label; the rest are options.

### PARAMS
- alternating: zebra-stripe accent_row every other row
- header_color: optional override

### INTERDITS
- No row spans / col spans — grid stays rigid.
- No more than ~6 columns or ~10 rows; otherwise the table stops fitting on a slide.

## When to use

- "Option A vs Option B" decision slides.
- Side-by-side spec comparison.

## When NOT to use

- For a long key/value list (use `term_definition_list`).
- For freeform highlights (use `card_grid`).

## Design system bundles required

- comparison_table.header
- comparison_table.row
- comparison_table.accent_row
"""

from streamtex import st_grid, st_write

__component_meta__ = {
    "name": "comparison_table",
    "description": "Tabular comparison of options across criteria.",
    "tags": ["table", "comparison", "grid"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": [
        "comparison_table.header",
        "comparison_table.row",
        "comparison_table.accent_row",
    ],
    "granularity": "composition",
}


def comparison_table(
    *,
    design_system,
    columns: list = None,
    rows: list = None,
    alternating: bool = True,
) -> None:
    """Render a comparison table. `columns` is header labels; `rows` are tuples of values."""
    columns = columns or []
    rows = rows or []
    template = " ".join(["1fr"] * len(columns))
    with st_grid(cols=template, gap="0") as g:
        for h in columns:
            with g.cell():
                st_write(design_system.comparison_table.header, h)
        for i, row in enumerate(rows):
            row_style = (
                design_system.comparison_table.accent_row
                if alternating and (i % 2 == 0)
                else design_system.comparison_table.row
            )
            for cell in row:
                with g.cell():
                    st_write(row_style, str(cell))
