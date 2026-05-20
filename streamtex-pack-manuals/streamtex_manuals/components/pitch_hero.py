"""
# Pitch hero — Opening statement card with subtle gradient background

## Visual

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│      Creating rich documents should not require     │
│      choosing between power and simplicity.         │
│                                                     │
│      Traditional tools force a compromise: visual   │
│      editors are easy but limited, while LaTeX is   │
│      powerful but hard to learn. StreamTeX removes  │
│      this trade-off — you write in Python.          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

A centered card with a subtle two-color gradient background. Used as
the opening statement of a section: a bold lead paragraph stating a
problem or thesis, followed by a regular paragraph framing the
solution.

## Structure

- Outer `st_block` with `linear-gradient(135deg, rgba1, rgba2)` background,
  rounded corners, generous padding.
- Inside: large bold center-aligned lead, optional spacer, regular
  paragraph in muted color.

## Styling rules

- Gradient endpoints use 8% rgba alpha — very subtle, never dominant.
- Border radius: 8px. Padding: 24px.
- Lead: `LARGE`, bold, center-aligned, design-system primary text color.
- Body: `large`, center-aligned, design-system muted color.

## Extrapolation rules

### INVARIANTS
- The card is always centered and full-width within its grid cell.
- Gradient angle is always 135°.
- The lead is bold and larger than the body.

### PARAMS
- `lead`: the bold thesis statement (1–2 sentences).
- `body`: a follow-up paragraph (2–4 sentences).
- `gradient_start_rgba` / `gradient_end_rgba`: optional rgba tuples
  (e.g. `(79, 172, 254)`). Default uses design-system primary accents.

### INTERDITS
- Multiple pitch_hero per section — used as an opener, not a divider.
- Lead longer than 2 sentences.
- Embedded links or buttons (use a follow-up callout or a feature_walkthrough).

## When to use

- The first content card of a section, framing the "why" before the "how".
- Opening of a chapter or part introduction.

## When NOT to use

- For inline emphasis → use `callout`.
- For a manual's cover page → use `level_badge_hero`.
- For a quote or citation → use `cite`.

## Design system bundles required

- `body.paragraph`
- `inline_emphasis.strong` (used for the lead's bold styling)
- `colors.muted` (used for the body color, if available)
"""

from streamtex import st_block, st_space, st_write
from streamtex.enums import Tags as t
from streamtex.styles import StxStyles, Style

__component_meta__ = {
    "name": "pitch_hero",
    "description": "Centered gradient card for opening section statements (lead + body).",
    "tags": ["hero", "pitch", "opening", "gradient"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": [
        "body.paragraph",
        "inline_emphasis.strong",
    ],
    "granularity": "primitive",
}


def pitch_hero(
    *,
    design_system,
    lead: str,
    body: str = "",
    gradient_start_rgba: tuple[int, int, int] = (79, 172, 254),
    gradient_end_rgba: tuple[int, int, int] = (0, 242, 254),
) -> None:
    """Render a centered gradient pitch card with a bold lead + optional body.

    Args:
        design_system: Provides ``body.paragraph`` and ``inline_emphasis.strong``
            bundles.
        lead: Bold thesis statement (1-2 sentences).
        body: Optional follow-up paragraph (2-4 sentences).
        gradient_start_rgba: ``(r, g, b)`` for the gradient start colour
            (alpha 0.08 applied).
        gradient_end_rgba: ``(r, g, b)`` for the gradient end colour
            (alpha 0.08 applied).
    """
    r1, g1, b1 = gradient_start_rgba
    r2, g2, b2 = gradient_end_rgba
    pitch = Style(
        f"background: linear-gradient(135deg, rgba({r1},{g1},{b1},0.08) 0%, "
        f"rgba({r2},{g2},{b2},0.08) 100%); border-radius: 8px; padding: 24px;",
        "ph_pitch",
    )

    with st_block(pitch):
        st_write(
            StxStyles.LARGE + StxStyles.bold + StxStyles.center_txt,
            lead, tag=t.div,
        )
        if body:
            st_space("v", 1)
            muted = _muted_or_paragraph(design_system)
            st_write(
                StxStyles.large + StxStyles.center_txt + muted,
                body, tag=t.div,
            )


def _muted_or_paragraph(design_system):
    """Return a muted-color style if the DS exposes one, else the body paragraph."""
    colors = getattr(design_system, "colors", None)
    if colors is not None and hasattr(colors, "muted"):
        return colors.muted
    return design_system.body.paragraph
