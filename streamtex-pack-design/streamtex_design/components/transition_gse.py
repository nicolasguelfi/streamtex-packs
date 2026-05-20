"""
# Transition GSE — ai4se6d-specific transition into GSE-One

## Visual

```
   <slide_heading: "The Methodological Gap" or similar>

   ┌──────────────┐ ┌──────────────────────────────────────┐
   │              │ │  Today: beyond VibeEngineering →     │
   │  GSE-One     │ │  Generative SE practiced through     │
   │  logo        │ │  GSE-One                             │
   │              │ │                                      │
   └──────────────┘ └──────────────────────────────────────┘
```

A project-specific specialisation of `narrative_transition` used in
the GenSEM module of the `ai4se6d` training collection. The pattern
fixes the *destination* of the pivot to the GSE-One methodology and
the visual anchor to the GSE-One logo.

## Structure

1. `slide_heading` — title varies per slide but always names a gap or
   a "beyond X" framing.
2. 2-column grid (cols="1fr 2fr") with logo on the left and pivot
   prose on the right.

## Styling rules

| Element | Style |
|---|---|
| heading | titles.slide |
| pivot prose | inline_emphasis.strong |
| logo | image, width fixed at 50 % of cell |

## Extrapolation rules

### INVARIANTS

- The destination concept is always "GSE-One".
- The visual anchor is always the GSE-One logo.
- Layout is 2-column 1fr/2fr.

### PARAMS

- title: str — the gap framing (e.g. "The Methodological Gap").
- pivot: str — the bridging line ("Today: ... → GSE-One").

### INTERDITS

- Do not use for transitions to other methodologies (use generic
  `narrative_transition` instead).
- Do not use for transitions *out of* GSE-One (towards limitations or
  open questions).
- Do not use outside the `ai4se6d` collection — the logo URI is
  project-local.

## When to use

- Closing slide of a GenSEM section that introduces or re-introduces
  GSE-One.
- Pivot from a problem state to GSE-One as the answer.

## When NOT to use

- Transitions to other methodologies — use `narrative_transition`.
- Transitions out of GSE-One.
- Outside the `ai4se6d` collection.

## Design system bundles required

- titles.slide
- inline_emphasis.strong
"""

from streamtex import st_grid, st_image, st_space, st_write

__component_meta__ = {
    "name": "transition_gse",
    "description": (
        "ai4se6d-specific transition slide pivoting a section into "
        "the GSE-One methodology."
    ),
    "tags": ["transition", "narrative", "slide", "ai4se6d", "gse-one"],
    "extrapolable": False,
    "since": "2026-05-19",
    "bundles_required": ["titles.slide", "inline_emphasis.strong"],
    "granularity": "block",
    "uses_components": ["narrative_transition"],
}

_GSE_LOGO_URI = "images/managed/GSE/images/logo-gse-geni-with-shield.webp"


def transition_gse(
    *,
    design_system,
    title: str = "",
    pivot: str = (
        "Today: beyond VibeEngineering → Generative SE practiced "
        "through GSE-One"
    ),
    logo_uri: str = _GSE_LOGO_URI,
) -> None:
    """Render a GSE-One transition slide (ai4se6d-specific)."""
    if title:
        st_write(design_system.titles.slide, title)
        st_space("v", 1.5)

    with st_grid(cols="1fr 2fr", gap="24px") as g:
        with g.cell():
            st_image(uri=logo_uri, width="50%")
        with g.cell():
            st_write(design_system.inline_emphasis.strong, pivot)
