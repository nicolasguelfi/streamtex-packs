"""Modern light design system — calm tones on a paper-bright surface.

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
    primary = Style("color: #1f4e79;", "primary")
    accent = Style("color: #2e7d32;", "accent")
    bg = Style("background-color: #fafafa;", "bg")
    surface = Style("background-color: #ffffff;", "surface")
    text = Style("color: #1c1f26;", "text")
    muted = Style("color: #5a6470;", "muted")


class _Callouts:
    info = Style(
        "background-color: rgba(31,78,121,0.06); border-left: 4px solid #1f4e79; padding: 14px 18px;",
        "ml_callout_info",
    )
    warn = Style(
        "background-color: rgba(243,156,18,0.10); border-left: 4px solid #e69100; padding: 14px 18px;",
        "ml_callout_warn",
    )
    error = Style(
        "background-color: rgba(231,76,60,0.10); border-left: 4px solid #c0392b; padding: 14px 18px;",
        "ml_callout_error",
    )
    success = Style(
        "background-color: rgba(46,125,50,0.10); border-left: 4px solid #2e7d32; padding: 14px 18px;",
        "ml_callout_success",
    )
    icon = Style("font-size: var(--stx-scale-8, 20pt); font-weight: 700; color: #1f4e79;", "ml_callout_icon")
    title = Style("font-weight: 700; font-size: var(--stx-scale-10, 24pt);", "ml_callout_title")
    body = Style("font-size: var(--stx-scale-7, 18pt); line-height: 1.5;", "ml_callout_body")


class DesignSystem:
    """Modern light design system."""

    name = "modern_light"
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
