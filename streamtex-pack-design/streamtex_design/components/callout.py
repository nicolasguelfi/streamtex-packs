"""
# Callout — Framed box that lifts emphasised content out of the surrounding flow

## Visual

```
┌──────────────────────────────────────┐
│  Knowledge Capitalization            │
│                                      │
│  No compound phase                   │
└──────────────────────────────────────┘
```

A small framed container with an accent label on the first line and a short
body underneath. Variants (info/warn/error/success) differ by inline label
color, never by container background — this keeps the visual surface uniform.

## Structure

- A `with st_block(callouts.info)` (or warn/error/success) container.
- First line: accent label using `inline_emphasis.strong`.
- Optional `st_space("v", 0.5)` separator.
- Body: 1-3 lines of `body.paragraph`.

## Styling rules

| Variant | Container | Label color |
|---|---|---|
| info | callouts.info | inline_emphasis.strong (primary) |
| warn | callouts.warn | inline_emphasis.strong (highlight) |
| error | callouts.error | inline_emphasis.strong (critical) |
| success | callouts.success | inline_emphasis.strong (success) |

## Extrapolation rules

### INVARIANTS
- Container background is set by the design system, never inline-overridden.
- Body is 1-3 short lines; longer text belongs in a paragraph.

### PARAMS
- variant: info | warn | error | success
- label may be omitted for purely visual emphasis (rare)

### INTERDITS
- No nesting callouts inside callouts.
- No 4+ line bodies — use a paragraph instead.

## When to use

- Definitions or key insights inside an explanatory slide.
- "Watch out" / "Note" / "Did you know" emphasised statements.

## When NOT to use

- Slide titles → use `title_slide` / `slide_heading`.
- Hero statistics → use `stat_hero`.

## Design system bundles required

- callouts.info
- callouts.warn
- callouts.error
- callouts.success
- callouts.title
- callouts.body
- inline_emphasis.strong
- body.paragraph
"""

from streamtex import st_block, st_space, st_write
from streamtex.core.discovery import get_bundle_attr

__component_meta__ = {
    "name": "callout",
    "description": "Framed box that emphasises content (info/warn/error/success variants).",
    "tags": ["callout", "container", "emphasis"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": [
        "callouts.info",
        "callouts.warn",
        "callouts.error",
        "callouts.success",
        "callouts.title",
        "callouts.body",
        "inline_emphasis.strong",
        "body.paragraph",
    ],
    "granularity": "primitive",
}


def callout(*, design_system, title: str = "", body: str = "", variant: str = "info") -> None:
    """Render a callout box. `variant` ∈ {info, warn, error, success}."""
    container = get_bundle_attr(design_system.callouts, variant, "callout")
    title_style = design_system.callouts.title
    body_style = design_system.callouts.body
    with st_block(container):
        if title:
            st_write(title_style, title)
            st_space("v", 0.5)
        if body:
            st_write(body_style, body)
