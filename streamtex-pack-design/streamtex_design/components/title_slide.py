"""
# Title slide — Cover slide with title, subtitle, author/date

## Visual

```
                THE FUTURE OF QUANTUM COMPUTING
                ──────────────────────────────────────
                A practitioner's overview

                Dr. Jane Doe — 2026-05-19
```

The opening slide of a presentation or section. Title is large and centered;
subtitle and metadata sit below in muted styles.

## Structure

- Centered slide title (`titles.slide`).
- Optional subtitle (`titles.subtitle`).
- Optional metadata footer (`body.paragraph`, often italic-muted).

## Styling rules

| Element | Style |
|---|---|
| title | titles.slide |
| subtitle | titles.subtitle |
| metadata | body.paragraph |

## Extrapolation rules

### INVARIANTS
- Title is centered, dominant on the slide.
- Author/date is below the subtitle and visually muted.

### PARAMS
- subtitle: optional
- metadata: optional one-liner

### INTERDITS
- No bullets / lists on a title slide.
- No body content beneath — the title slide stands alone.

## When to use

- The first slide of any deck.
- Section transition slides within a long deck.

## When NOT to use

- For in-slide section headings (use `slide_heading`).

## Design system bundles required

- titles.slide
- titles.subtitle
- body.paragraph
"""

from streamtex import st_space, st_write

__component_meta__ = {
    "name": "title_slide",
    "description": "Cover slide: title + subtitle + optional metadata.",
    "tags": ["title", "slide", "cover"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["titles.slide", "titles.subtitle", "body.paragraph"],
    "granularity": "block",
}


def title_slide(*, design_system, title: str = "", subtitle: str = "", metadata: str = "") -> None:
    """Render a cover title slide."""
    st_write(design_system.titles.slide, title)
    if subtitle:
        st_space("v", 1.0)
        st_write(design_system.titles.subtitle, subtitle)
    if metadata:
        st_space("v", 2.0)
        st_write(design_system.body.paragraph, metadata)
