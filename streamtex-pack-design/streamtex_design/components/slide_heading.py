"""
# Slide heading — Centered title at the top of a slide block

## Visual

```
                THE THREE PILLARS OF GREEN CHEMISTRY
                ─────────────────────────────────────
```

A bold, centered title that announces a slide. Optionally accompanied by an
underline rule or subtitle.

## Structure

- A `st_write(titles.slide, text)` line, centered.
- Optional thin underline or subtitle via `titles.subtitle`.

## Styling rules

| Element | Style |
|---|---|
| title | titles.slide |
| subtitle | titles.subtitle |

## Extrapolation rules

### INVARIANTS
- One title per slide; never two.
- Always at the visual top of the slide.

### PARAMS
- subtitle: optional secondary line
- align: center | left
- toc_lvl: optional TOC level (e.g. "1") so the heading registers a sidebar /
  navigation entry — slide components do not register the TOC on their own.

### INTERDITS
- No inline emphasis inside the heading.
- No multi-line wraps for the main title.

## When to use

- The first content block of every slide.
- Section transition slides.

## When NOT to use

- Inside a callout (use callouts.title).
- For sub-section headings within a slide (use titles.section).

## Design system bundles required

- titles.slide
- titles.subtitle

## Extended layouts (tooltip + 95/5 grid)

The simple `slide_heading(title=..., subtitle=...)` covers the canonical
case. If a slide needs a **section-recap tooltip on hover**, compose it
inline instead of using this component — for separation of concerns the
heading itself stays tooltip-free. The `st_hover_tooltip` widget ships in
the core `streamtex` library (palette-neutral); import it directly.
Pattern:

```python
from streamtex import st_block, st_grid, st_hover_tooltip, st_write, st_zoom

with st_grid(cols="95% 5%", gap="0px") as g:
    with g.cell():
        with st_zoom(90):
            st_write(ds.titles.slide, "<title>")
    with g.cell():
        st_hover_tooltip(
            title="<section recap>",
            entries=[("<point>", "<one-line summary>")],
            scale="2vw", width="70vw", position="left",
        )
```
"""

from streamtex import st_write

__component_meta__ = {
    "name": "slide_heading",
    "description": "Centered slide title (one per slide).",
    "tags": ["title", "heading", "slide"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["titles.slide", "titles.subtitle"],
    "granularity": "primitive",
}


def slide_heading(
    *, design_system, title: str = "", subtitle: str = "",
    toc_lvl: str | None = None,
) -> None:
    """Render a slide-top heading + optional subtitle.

    Pass ``toc_lvl`` (e.g. ``"1"``) to register this heading in the table of
    contents / sidebar navigation; defaults to ``None`` (no TOC entry).
    """
    st_write(design_system.titles.slide, title, toc_lvl=toc_lvl)
    if subtitle:
        st_write(design_system.titles.subtitle, subtitle)
