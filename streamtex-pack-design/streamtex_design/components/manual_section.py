"""
# Manual section — Documentation-manual section wrapper with title and intro

## Visual

```
   ── 3. Style System ──────────────────

   Styles are the smallest unit of design in StreamTeX. They live in a
   `Style` object and compose with `+`.

   [child content]
```

The outer wrapper of a manual section: a numbered section header, a short
introduction paragraph, and a body region the user fills with arbitrary
children.

## Structure

- Header: `titles.section`.
- Intro paragraph: `body.paragraph`.
- Body: a `st_block` content slot.

## Styling rules

| Element | Style |
|---|---|
| header | titles.section |
| intro | body.paragraph |
| body slot | none (children style themselves) |

## Extrapolation rules

### INVARIANTS
- Header always carries the section number.
- Intro paragraph is one short paragraph maximum.

### PARAMS
- number: integer section number
- title: section title
- intro: 1-3 sentence intro
- body callable: arbitrary children

### INTERDITS
- No multiple headers per section.
- No empty body (sections must have content).

## When to use

- Top-level sections of a documentation manual.
- Chapter wrappers in long-form material.

## When NOT to use

- Sub-section headings inside a block (use slide_heading).
- Pure title slides (use title_slide).

## Design system bundles required

- titles.section
- body.paragraph
"""

from streamtex import st_space, st_write

__component_meta__ = {
    "name": "manual_section",
    "description": "Documentation-manual section header + intro + body slot.",
    "tags": ["docs", "section", "manual"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["titles.section", "body.paragraph"],
    "granularity": "composition",
}


def manual_section(*, design_system, number: int = 1, title: str = "", intro: str = "", body=None) -> None:
    """Render a manual section header + intro, then call `body()` for children."""
    st_write(design_system.titles.section, f"{number}. {title}")
    if intro:
        st_write(design_system.body.paragraph, intro)
    st_space("v", 1.0)
    if body is not None:
        body()
