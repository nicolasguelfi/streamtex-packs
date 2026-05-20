"""
# Takeaways — Numbered or bulleted list of key points

## Visual

```
   1. RuBisCO catalyses CO₂ fixation
   2. Photorespiration competes with carboxylation
   3. C4 plants pre-concentrate CO₂ to suppress this
```

A tight, vertical list of 3-6 key statements emphasised by a lead style on
each item.

## Structure

- Optional lead line: `takeaways.lead`.
- N items, each `st_write(takeaways.item, …)`.

## Styling rules

| Element | Style |
|---|---|
| lead | takeaways.lead |
| item | takeaways.item |

## Extrapolation rules

### INVARIANTS
- Each item is one short sentence.
- 3 ≤ N ≤ 6 items.

### PARAMS
- numbered: True | False
- lead: optional headline above the list

### INTERDITS
- No paragraph-length items.
- No nested lists.

## When to use

- The "key takeaways" closing slide.
- A summary of a previous section.

## When NOT to use

- A heterogeneous list (use `card_grid`).
- A glossary (use `term_definition_list`).

## Design system bundles required

- takeaways.lead
- takeaways.item
"""

from streamtex import st_write

__component_meta__ = {
    "name": "takeaways",
    "description": "Vertical list of 3-6 key takeaways.",
    "tags": ["list", "takeaways", "summary"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["takeaways.lead", "takeaways.item"],
    "granularity": "composition",
}


def takeaways(*, design_system, items: list = None, lead: str = "", numbered: bool = True) -> None:
    """Render a list of takeaway items."""
    items = items or []
    if lead:
        st_write(design_system.takeaways.lead, lead)
    for idx, item in enumerate(items, start=1):
        prefix = f"{idx}. " if numbered else "• "
        st_write(design_system.takeaways.item, f"{prefix}{item}")
