"""
# Narrative transition — Bridge slide between two sections

## Visual

```
                ── PART II ───────────────

                From theory to practice
                _________________________

                We have established the why.
                Now: how.
```

A minimal slide whose only job is to mark a transition: a section label, a
short framing line, and 1-3 lines of bridging prose.

## Structure

- A muted section marker (titles.section, often "PART N").
- A bold framing line (titles.slide).
- 1-3 lines of bridging text (body.paragraph).

## Styling rules

| Element | Style |
|---|---|
| section_marker | titles.section |
| framing | titles.slide |
| bridging | body.paragraph |

## Extrapolation rules

### INVARIANTS
- Always 3 visual zones: marker, frame, prose.
- No content, charts, or lists — pure narrative.

### PARAMS
- marker: optional ("PART II", "II — IMPLEMENTATION", etc.)
- prose lines: 1 to 3

### INTERDITS
- No bullets / lists.
- No data / images / charts.

## When to use

- Between major parts of a deck.
- To shift register from analysis to recommendation.

## When NOT to use

- For content slides (use title_slide + body).
- For chapter summaries (use takeaways).

## Design system bundles required

- titles.section
- titles.slide
- body.paragraph
"""

from streamtex import st_space, st_write

__component_meta__ = {
    "name": "narrative_transition",
    "description": "Minimal transition slide between deck sections.",
    "tags": ["transition", "narrative", "slide"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": ["titles.section", "titles.slide", "body.paragraph"],
    "granularity": "block",
}


def narrative_transition(
    *,
    design_system,
    marker: str = "",
    framing: str = "",
    bridging: str = "",
) -> None:
    """Render a narrative transition slide."""
    if marker:
        st_write(design_system.titles.section, marker)
        st_space("v", 1.0)
    st_write(design_system.titles.slide, framing)
    if bridging:
        st_space("v", 1.0)
        st_write(design_system.body.paragraph, bridging)
