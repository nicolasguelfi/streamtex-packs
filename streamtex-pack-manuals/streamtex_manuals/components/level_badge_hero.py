"""
# Level badge hero — Manual cover page

## Visual

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  ╔═════════════╗   STREAMTEX MANUAL TITLE          │
│  ║    LOGO     ║   Subtitle line — short tagline   │
│  ║   25% col   ║                                   │
│  ╚═════════════╝                                   │
│                                                     │
└─────────────────────────────────────────────────────┘
   ▌ LEVEL LABEL (uppercase, accent color)
   ▌ Headline — what the manual covers, end-to-end
   ▌
   ▌ Body paragraph framing the manual's scope and
   ▌ value to the reader.
```

A two-tier hero block: a full-width gradient title card followed by a
sidebar-left badge box. Used on the first page of every manual to
identify its level, scope, and audience.

## Structure

- Outer `st_block(gradient_header_style)` — full-width gradient container
- Inside: `st_grid(cols="25% 1fr")` with logo cell + title cell
- Below: `st_block(level_box_style)` — left-bordered tinted box with
  uppercase label, headline, and body paragraph

## Styling rules

- Gradient header uses 135° linear gradient between `gradient_start` and
  `gradient_end`. Title text is always WHITE for contrast.
- Level box: `rgba(accent_color, 0.08)` background + 4px solid left border
  in `accent_color`. Rounded right corners only.
- Level label is uppercase, bold, letter-spaced; same color as accent.

## Extrapolation rules

### INVARIANTS
- Title text inside the gradient header is always WHITE.
- The badge box has only a LEFT border (not all 4 sides).
- Gradient direction is always 135°.

### PARAMS
- `manual_title`: the H1 of the manual (also the TOC entry).
- `manual_subtitle`: short tagline, secondary to the title.
- `level_label`: e.g. "REUSE LEVEL", "INTRO LEVEL". Rendered uppercase
  regardless of input casing.
- `level_headline`: short sentence (≤ 80 chars).
- `level_body`: 1–3 short paragraphs framing the manual's scope.
- `bullets`: optional list of short scope items rendered as a bulleted list
  inside the badge box (e.g. "Concepts", "Authoring", "Self-demo").
- `accent_color`: hex `#RRGGBB`, used for the badge box border + label.
- `gradient_start` / `gradient_end`: hex, header gradient endpoints.
- `logo_uri`: optional URI for the logo image (recommended).
- `support_url`: optional URL for a sponsor / support button.

### INTERDITS
- No additional content inside the gradient header beyond logo + title.
- No icons or emojis embedded in the title (the gradient + level badge
  already convey identity).

## When to use

- The very first page of any manual that has a "level" identity (intro,
  reuse, advanced, deploy, etc.).

## When NOT to use

- Inside a manual's body — use `slide_heading` for section titles.
- For a single statement of value — use `pitch_hero`.

## Design system bundles required

- `body.paragraph` (level body text)
- `inline_emphasis.strong` (optional, if level_body contains inline emphasis)
"""

import streamlit as st
from streamtex import st_block, st_grid, st_image, st_list, st_space, st_write
from streamtex.enums import Tags as t
from streamtex.styles import StxStyles, Style

__component_meta__ = {
    "name": "level_badge_hero",
    "description": "Manual cover page: gradient title card + sidebar-left level badge box.",
    "tags": ["hero", "cover", "level-badge", "manual"],
    "extrapolable": True,
    "since": "2026-05-19",
    "bundles_required": [
        "body.paragraph",
    ],
    "granularity": "block",
}


def level_badge_hero(
    *,
    design_system,
    manual_title: str,
    manual_subtitle: str,
    level_label: str,
    level_headline: str,
    level_body: str,
    accent_color: str,
    gradient_start: str,
    gradient_end: str,
    bullets: list[str] | None = None,
    logo_uri: str | None = None,
    support_url: str | None = None,
) -> None:
    """Render a manual's cover hero: gradient header + level badge box."""
    header_style = Style(
        f"background: linear-gradient(135deg, {gradient_start} 0%, "
        f"{gradient_end} 100%); padding: 40px 20px; border-radius: 8px;",
        "lbh_header",
    )
    level_box = Style(
        f"background: rgba({_hex_to_rgb(accent_color)}, 0.08); "
        f"border-left: 4px solid {accent_color}; padding: 20px 24px; "
        "border-radius: 0 8px 8px 0;",
        "lbh_level_box",
    )
    level_label_style = Style(
        f"color: {accent_color}; font-weight: bold; font-size: 14pt; "
        "text-transform: uppercase; letter-spacing: 2px;",
        "lbh_level_label",
    )
    logo_style = Style("width: 100%; height: auto;", "lbh_logo")
    logo_cell = Style(
        "display: flex; flex-direction: column; align-items: center; "
        "justify-content: center; gap: 4px;",
        "lbh_logo_cell",
    )

    st_space("v", 1)
    with st_block(header_style):
        if logo_uri:
            with st_grid(
                cols="25% 1fr", breakpoint="600px",
                cell_styles=[logo_cell, None],
            ) as g:
                with g.cell():
                    st_image(logo_style, uri=logo_uri)
                    if support_url:
                        st.link_button(
                            "❤️ Support us!", support_url,
                            use_container_width=True,
                        )
                with g.cell():
                    _hero_title(manual_title, manual_subtitle)
        else:
            _hero_title(manual_title, manual_subtitle)
    st_space("v", 1)

    with st_block(level_box):
        st_write(level_label_style, level_label)
        st_space("v", 0.5)
        st_write(
            StxStyles.LARGE + StxStyles.bold,
            level_headline,
            tag=t.div,
        )
        st_space("v", 1)
        st_write(design_system.body.paragraph, level_body, tag=t.div)
        if bullets:
            st_space("v", 1)
            with st_list(list_type="ul") as l:
                for item in bullets:
                    with l.item():
                        st_write(StxStyles.medium, item)


def _hero_title(title: str, subtitle: str) -> None:
    st_write(
        StxStyles.LARGE + StxStyles.bold + "color:white;",
        title, tag=t.div, toc_lvl="1",
    )
    st_write(
        StxStyles.large + "color:white;",
        subtitle, tag=t.div,
    )


def _hex_to_rgb(hex_color: str) -> str:
    """Convert #RRGGBB → 'r, g, b' string for use in rgba()."""
    h = hex_color.lstrip("#")
    return f"{int(h[0:2], 16)}, {int(h[2:4], 16)}, {int(h[4:6], 16)}"
