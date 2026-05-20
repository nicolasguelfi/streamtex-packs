"""
# Inline emphasis — Bold-color word or phrase inside a sentence

## Visual

```
   The reaction is **catalysed** by the enzyme RuBisCO.
```

A single word or short phrase rendered in bold with a semantic colour
(primary, accent, success, warn, error). Used to draw the eye to the
critical noun or verb in a paragraph.

## Structure

- A `st_write` call inside another component (body, callout, card body).
- Style: `inline_emphasis.strong` for high emphasis or `.soft` for italic.

## Styling rules

| Variant | Style |
|---|---|
| strong | inline_emphasis.strong |
| soft | inline_emphasis.soft |

## Extrapolation rules

### INVARIANTS
- Always inline — never broken across paragraphs.
- One-to-three words at most.

### PARAMS
- variant: strong | soft
- color is delegated to the design system

### INTERDITS
- No emphasis on whole sentences — defeats the purpose.
- No nested emphasis.

## When to use

- The "keyword" of a paragraph.
- A definition's defining word.

## When NOT to use

- Slide titles (use titles bundle).
- Inline citations (use cite).

## Design system bundles required

- inline_emphasis.strong
- inline_emphasis.soft
"""

from streamtex import st_write

__component_meta__ = {
    "name": "inline_emphasis",
    "description": "Bold-color inline emphasis (1-3 words).",
    "tags": ["emphasis", "inline", "keyword"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["inline_emphasis.strong", "inline_emphasis.soft"],
    "granularity": "primitive",
}


def inline_emphasis(*, design_system, text: str = "", variant: str = "strong") -> None:
    """Render a 1-3 word inline emphasis."""
    style = design_system.inline_emphasis.strong if variant == "strong" else design_system.inline_emphasis.soft
    st_write(style, text)
