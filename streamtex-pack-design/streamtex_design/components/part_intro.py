"""
# Part intro — Section-opener slide that announces a part and its role

## Visual

```
                PART 3
                ──────────────────────────────────────
                The cost of friction

                Objective: make the pain measurable
                Where it fits: sets up why a tool is needed
```

The slide that opens a part of a presentation. It states the part number, its
title, its objective, and how it fits in the flow — so the audience always
knows where they are and why. Registers a table-of-contents entry by default
(the spine of the deck's navigation).

## Structure

- An eyebrow line with the part label (`titles.caption`).
- The part title (`titles.slide`), which registers the TOC entry.
- An objective line (`titles.subtitle`).
- A one-line "where it fits in the flow" rationale (`body.paragraph`).

## Styling rules

| Element | Style |
|---|---|
| eyebrow | titles.caption |
| title | titles.slide |
| objective | titles.subtitle |
| logic | body.paragraph |

## Extrapolation rules

### INVARIANTS
- Exactly one part-intro per part; it is the part's first slide.
- The title registers a TOC entry (so every part is reachable in the sidebar).

### PARAMS
- eyebrow: the part label (e.g. "Part 3"); optional.
- objective: one line stating what the part achieves; optional.
- logic: one line on how the part fits the overall flow; optional.
- toc_lvl: TOC level for the title (default "1"; pass None to suppress).

### INTERDITS
- No dense bullet lists — the part-intro is a signpost, not a content slide.
- No detailed body text — push detail to the part's content slides or hovers.

## When to use

- The opening slide of every part / major section of a deck.
- Whenever the audience needs to be re-oriented in the narrative.

## When NOT to use

- For the deck's cover (use `title_slide`).
- For an in-slide heading (use `slide_heading`).

## Design system bundles required

- titles.caption
- titles.slide
- titles.subtitle
- body.paragraph
"""

from streamtex import st_space, st_write

__component_meta__ = {
    "name": "part_intro",
    "description": "Section-opener slide: part label + title + objective + role in flow.",
    "tags": ["title", "slide", "section", "part", "transition"],
    "extrapolable": True,
    "since": "2026-05-21",
    "bundles_required": [
        "titles.caption", "titles.slide", "titles.subtitle", "body.paragraph",
    ],
    "granularity": "block",
}


def part_intro(
    *, design_system, eyebrow: str = "", title: str = "",
    objective: str = "", logic: str = "", toc_lvl: str | None = "1",
) -> None:
    """Render a part-opener slide.

    The ``title`` registers a table-of-contents entry at ``toc_lvl`` (default
    ``"1"``) so each part is reachable from the sidebar; pass ``toc_lvl=None``
    to suppress the entry.
    """
    if eyebrow:
        st_write(design_system.titles.caption, eyebrow)
    st_write(design_system.titles.slide, title, toc_lvl=toc_lvl)
    if objective:
        st_space("v", 1.5)
        st_write(design_system.titles.subtitle, objective)
    if logic:
        st_space("v", 0.5)
        st_write(design_system.body.paragraph, logic)
