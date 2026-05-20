"""
# API reference card — Compact card for a single API function

## Visual

```
   ┌────────────────────────────────────┐
   │ st_block(style, *content)          │
   │                                    │
   │ Group children under a styled box. │
   │                                    │
   │ Returns: None                      │
   └────────────────────────────────────┘
```

A documentation-oriented card that documents one API function: signature,
short description, return value.

## Structure

- A `card_grid.card` container.
- Signature line: `body.code`.
- Description: `body.paragraph`.
- Returns line: `body.paragraph` italic-muted.

## Styling rules

| Element | Style |
|---|---|
| signature | body.code |
| description | body.paragraph |
| returns | body.paragraph |

## Extrapolation rules

### INVARIANTS
- One function per card — never two.
- Signature is on a single visual line (wrap at param boundaries if needed).

### PARAMS
- signature: full call signature including params
- description: 1-3 sentences
- returns: optional return summary

### INTERDITS
- No detailed parameter table (use term_definition_list outside the card).
- No syntax examples inside (use a separate code block).

## When to use

- API reference manuals.
- Quick-lookup slides for a workshop.

## When NOT to use

- Tutorial pages (use feature_walkthrough).
- High-level overviews (use card_grid of concept cards).

## Design system bundles required

- card_grid.card
- body.code
- body.paragraph
"""

from streamtex import st_block, st_write

__component_meta__ = {
    "name": "api_reference_card",
    "description": "Compact card documenting one API function.",
    "tags": ["api", "reference", "card"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["card_grid.card", "body.code", "body.paragraph"],
    "granularity": "composition",
}


def api_reference_card(*, design_system, signature: str = "", description: str = "", returns: str = "") -> None:
    """Render a single API function reference card."""
    with st_block(design_system.card_grid.card):
        st_write(design_system.body.code, signature)
        if description:
            st_write(design_system.body.paragraph, description)
        if returns:
            st_write(design_system.body.paragraph, f"Returns: {returns}")
