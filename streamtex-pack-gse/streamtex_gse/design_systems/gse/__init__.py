"""GSE design system — extends pack-design `default` with GSE-One brand palette.

Overrides only the `colors` bundle to introduce:

- `highlight` — amber (used by `transition_gse` for pivot prose);
- `g_letter`, `s_letter`, `e_letter` — the three brand colors used by
  `gse_letter` to colorise the GSE initials of a phrase.

Every other bundle (titles, callouts, body, fonts, stat_hero, card_grid,
takeaways, citation, inline_emphasis, comparison_table) is inherited
unchanged from the default design system.
"""

from streamtex.styles import Style
from streamtex_design.design_systems.default import (
    _Body,
    _Callouts,
    _CardGrid,
    _Citation,
    _ComparisonTable,
    _Fonts,
    _InlineEmphasis,
    _StatHero,
    _Takeaways,
    _Titles,
)


class _Colors:
    primary = Style("color: #7AB8F5;", "primary")
    accent = Style("color: #2EC4B6;", "accent")
    bg = Style("background-color: #0e1117;", "bg")
    surface = Style("background-color: #1c1f26;", "surface")
    text = Style("color: #FAFAFA;", "text")
    muted = Style("color: #95A5A6;", "muted")
    info = Style("color: #7AB8F5;", "color_info")
    success = Style("color: #27AE60;", "color_success")
    warning = Style("color: #F39C12;", "color_warning")
    critical = Style("color: #E74C3C;", "color_critical")
    # GSE-One brand: amber pivot accent + three letter colors used by gse_letter.
    highlight = Style("color: #F5A623;", "gse_highlight")
    g_letter = Style("color: #F5A623;", "gse_g")  # amber — Generative
    s_letter = Style("color: #2EC4B6;", "gse_s")  # teal  — Software
    e_letter = Style("color: #7AB8F5;", "gse_e")  # blue  — Engineering


class DesignSystem:
    """GSE design system — pack-design `default` + GSE-One brand colors."""

    name = "gse"
    colors = _Colors
    titles = _Titles
    callouts = _Callouts
    body = _Body
    fonts = _Fonts
    stat_hero = _StatHero
    card_grid = _CardGrid
    takeaways = _Takeaways
    citation = _Citation
    inline_emphasis = _InlineEmphasis
    comparison_table = _ComparisonTable
