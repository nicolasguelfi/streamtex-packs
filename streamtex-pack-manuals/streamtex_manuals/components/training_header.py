"""
# Training header — Per-page header strip for training material

## Visual

```
┌─────────────────────────────────────────────────────┐
│  AI4SE · GenAI Intro          Module 1 · 2026-05    │
└─────────────────────────────────────────────────────┘
```

A thin, full-width strip rendered at the top of each training slide /
chapter. Left side: program + module name. Right side: module index +
date (or session identifier). Provides constant visual anchoring across
a long training deck.

## Structure

- `st_grid(cols="1fr auto")` so the right cell shrinks to content while
  the left fills the rest.
- Left cell: program name + module title joined by `·`.
- Right cell: module index + date (or any short identifier).

## Styling rules

- Container: thin (8px vertical padding), `surface` background, small
  bottom border using `colors.muted` at 20% alpha.
- Both cells use `body.paragraph` size, slightly muted color.
- The separator `·` between program and module is rendered with extra
  horizontal spacing.

## Extrapolation rules

### INVARIANTS
- The header is always one line; if text overflows, it must be truncated
  upstream (no automatic wrap inside this component).
- The right cell is `auto`-sized — anything that should grow goes on the
  left.

### PARAMS
- `program`: e.g. "AI4SE", "StreamTeX Trainings".
- `module`: e.g. "GenAI Intro", "VibeCoding".
- `right_label`: free text for the right cell (e.g. "Module 1 · 2026-05").
- `right_label` can be `None` to omit.

### INTERDITS
- No logo / icon inline — that goes in `training_footer` or in a hero
  block at the start of the session.
- No interactive elements (links, buttons).

## When to use

- At the top of every page of a long training deck.
- Above a "manual section" page in a multi-chapter manual.

## When NOT to use

- For a cover / title page (use `level_badge_hero` or `pitch_hero`).
- For inline navigation (use `slide_heading` with a TOC entry).

## Design system bundles required

- `body.paragraph`
- `colors.muted`
- `colors.surface`
"""

from streamtex import st_block, st_grid, st_write
from streamtex.enums import Tags as t
from streamtex.styles import StxStyles, Style

__component_meta__ = {
    "name": "training_header",
    "description": "Thin per-page header strip with program/module on the left and a short label on the right.",
    "tags": ["header", "training", "navigation"],
    "extrapolable": True,
    "since": "2026-05-23",
    "bundles_required": [
        "body.paragraph",
        "colors.muted",
        "colors.surface",
    ],
    "granularity": "primitive",
}


def training_header(
    *,
    design_system,
    program: str,
    module: str,
    right_label: str | None = None,
) -> None:
    """Render a thin training-deck header strip."""
    container_style = Style.create(
        design_system.colors.surface
        + "padding: 8px 16px; "
        + "border-bottom: 1px solid rgba(255,255,255,0.08); ",
        "th_container",
    )
    text_style = Style.create(
        design_system.body.paragraph + design_system.colors.muted,
        "th_text",
    )
    label_text = f"{program} · {module}"

    with st_block(container_style):
        with st_grid(cols="1fr auto") as g:
            with g.cell():
                st_write(text_style, label_text, tag=t.div)
            with g.cell():
                if right_label:
                    st_write(text_style, right_label, tag=t.div)
                else:
                    st_write(StxStyles.none, "", tag=t.div)
