"""
# Training footer — Closing credits strip

## Visual

```
┌─────────────────────────────────────────────────────┐
│  © 2026 Author · License: CC BY-SA       v1.2.3    │
└─────────────────────────────────────────────────────┘
```

A thin, full-width strip used at the end of a training session or
manual to surface attribution, license, and version. Pairs with
`training_header` for top/bottom framing.

## Structure

- `st_grid(cols="1fr auto")` — credits on the left, version label on
  the right.
- Both cells use the `citation` bundle style (smaller, muted).

## Styling rules

- Container: `surface` background, 8px vertical padding, top border
  using `colors.muted` at 20% alpha.
- Text style: `citation.source` (small + italic + muted).

## Extrapolation rules

### INVARIANTS
- One line, no wrapping (truncate upstream if needed).
- License string format is free (the component does not validate SPDX).

### PARAMS
- `author`: e.g. "Nicolas Guelfi".
- `year`: int (defaults to current year if omitted).
- `license_label`: e.g. "CC BY-SA 4.0", "All rights reserved".
- `version`: e.g. "v1.2.3" — appears on the right cell.
- `version` can be `None` to omit.

### INTERDITS
- No clickable links — keep this strip pure-text for clean PDF export.
- No multi-line content — the footer is always one row; if the credits
  line is too long, abbreviate the license label upstream.

## When to use

- Last page of a training session.
- Bottom of every page in a manual when a per-page footer is desired
  (rendered via `BannerConfig.full(footer=...)` in book.py).

## When NOT to use

- For licensing the entire manual at the cover page (use `level_badge_hero`).

## Design system bundles required

- `citation.source`
- `colors.surface`
- `colors.muted`
"""

from datetime import datetime

from streamtex import st_block, st_grid, st_write
from streamtex.enums import Tags as t
from streamtex.styles import StxStyles, Style

__component_meta__ = {
    "name": "training_footer",
    "description": "Thin closing strip with author + license on the left and version on the right.",
    "tags": ["footer", "training", "credits"],
    "extrapolable": True,
    "since": "2026-05-23",
    "bundles_required": [
        "citation.source",
        "colors.surface",
        "colors.muted",
    ],
    "granularity": "primitive",
}


def training_footer(
    *,
    design_system,
    author: str,
    license_label: str,
    year: int | None = None,
    version: str | None = None,
) -> None:
    """Render a thin closing footer strip with credits + version."""
    container_style = Style.create(
        design_system.colors.surface
        + "padding: 8px 16px; "
        + "border-top: 1px solid rgba(255,255,255,0.08); ",
        "tf_container",
    )
    effective_year = year if year is not None else datetime.now().year
    credits_line = f"© {effective_year} {author} · License: {license_label}"

    with st_block(container_style):
        with st_grid(cols="1fr auto") as g:
            with g.cell():
                st_write(design_system.citation.source, credits_line, tag=t.div)
            with g.cell():
                if version:
                    st_write(design_system.citation.source, version, tag=t.div)
                else:
                    st_write(StxStyles.none, "", tag=t.div)
