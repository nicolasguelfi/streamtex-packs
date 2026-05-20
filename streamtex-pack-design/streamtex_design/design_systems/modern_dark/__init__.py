"""Modern dark design system — vibrant accents on a deeply-dark surface.

Inherits non-callout bundles from the default DS. All font sizes use
``var(--stx-scale-K, fallback)`` to integrate with the indexed responsive
scale.
"""

from streamtex.styles import Style

from streamtex_design.design_systems.default import (
    _Body,
    _CardGrid,
    _Citation,
    _ComparisonTable,
    _InlineEmphasis,
    _StatHero,
    _Takeaways,
    _Titles,
)


class _Colors:
    primary = Style("color: #5dade2;", "primary")
    accent = Style("color: #a78bfa;", "accent")
    bg = Style("background-color: #050608;", "bg")
    surface = Style("background-color: #11141b;", "surface")
    text = Style("color: #f5f7fa;", "text")
    muted = Style("color: #8e9aaa;", "muted")


class _Callouts:
    info = Style(
        "background-color: rgba(93,173,226,0.12); border-left: 4px solid #5dade2; padding: 14px 18px;",
        "md_callout_info",
    )
    warn = Style(
        "background-color: rgba(243,156,18,0.12); border-left: 4px solid #F39C12; padding: 14px 18px;",
        "md_callout_warn",
    )
    error = Style(
        "background-color: rgba(231,76,60,0.14); border-left: 4px solid #E74C3C; padding: 14px 18px;",
        "md_callout_error",
    )
    success = Style(
        "background-color: rgba(39,174,96,0.12); border-left: 4px solid #27AE60; padding: 14px 18px;",
        "md_callout_success",
    )
    icon = Style("font-size: var(--stx-scale-9, 22pt); font-weight: 700; color: #a78bfa;", "md_callout_icon")
    title = Style("font-weight: 700; font-size: var(--stx-scale-10, 24pt);", "md_callout_title")
    body = Style("font-size: var(--stx-scale-7, 18pt); line-height: 1.55;", "md_callout_body")


class DesignSystem:
    """Modern dark design system."""

    name = "modern_dark"
    colors = _Colors
    titles = _Titles
    callouts = _Callouts
    body = _Body
    stat_hero = _StatHero
    card_grid = _CardGrid
    takeaways = _Takeaways
    citation = _Citation
    inline_emphasis = _InlineEmphasis
    comparison_table = _ComparisonTable
