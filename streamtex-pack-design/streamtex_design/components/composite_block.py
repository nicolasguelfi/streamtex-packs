"""
# Composite block — Documentation block that interleaves explanation and demo

## Visual

```
   ┌─── Explanation ─────────┐
   │ Use st_block to group   │
   │ children under a style. │
   └─────────────────────────┘

   ┌─── Demo ────────────────┐
   │ [live demo renders here] │
   └─────────────────────────┘

   ┌─── Code ────────────────┐
   │ with st_block(s):       │
   │   st_write("hi")        │
   └─────────────────────────┘
```

A documentation-manual primitive: alternates explanation, live demo, and
the underlying code so the reader sees behaviour and source side by side.

## Structure

- Header: `titles.section`.
- Three subsections, each in its own `card_grid.card` container.

## Styling rules

| Element | Style |
|---|---|
| header | titles.section |
| section_title | titles.subtitle |
| body | body.paragraph |
| code | body.code |

## Extrapolation rules

### INVARIANTS
- Three subsections in fixed order: explanation, demo, code.
- Each subsection is short — half a slide each maximum.

### PARAMS
- explanation: 1-3 sentences
- demo callable (the actual rendering)
- code string (shown verbatim)

### INTERDITS
- No interleaving of subsections.
- No long prose in the explanation (link out instead).

## When to use

- StreamTeX-style documentation manuals.
- Tutorial-style workshop materials.

## When NOT to use

- Pure code references (use api_reference_card).
- Pure narrative slides (use slide_heading + body).

## Design system bundles required

- titles.section
- titles.subtitle
- body.paragraph
- body.code
- card_grid.card
"""

from streamtex import st_block, st_write

__component_meta__ = {
    "name": "composite_block",
    "description": "Doc-manual block: explanation + demo + code subsections.",
    "tags": ["docs", "composite", "tutorial"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": [
        "titles.section",
        "titles.subtitle",
        "body.paragraph",
        "body.code",
        "card_grid.card",
    ],
    "granularity": "composition",
}


def composite_block(
    *,
    design_system,
    title: str = "",
    explanation: str = "",
    demo=None,
    code: str = "",
) -> None:
    """Render a composite documentation block."""
    st_write(design_system.titles.section, title)
    with st_block(design_system.card_grid.card):
        st_write(design_system.titles.subtitle, "Explanation")
        st_write(design_system.body.paragraph, explanation)
    if demo is not None:
        with st_block(design_system.card_grid.card):
            st_write(design_system.titles.subtitle, "Demo")
            demo()
    if code:
        with st_block(design_system.card_grid.card):
            st_write(design_system.titles.subtitle, "Code")
            st_write(design_system.body.code, code)
