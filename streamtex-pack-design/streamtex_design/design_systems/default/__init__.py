"""Default design system — neutral palette suitable for documentation and slides.

Bundles exposed: colors, titles, callouts, body, stat_hero, card_grid,
takeaways, citation, inline_emphasis.

Font sizes use the indexed responsive scale via ``var(--stx-scale-K, fallback)``
references. The fallbacks are pt values that match the WORD_PROCESSOR curve
desktop column. Consumers automatically inherit responsive sizing at 1024px
and 480px breakpoints. To override per-document, pass
``st_book(scale=ScaleConfig(...))`` upstream.
"""

from streamtex.styles import Style


class _Colors:
    primary = Style("color: #7AB8F5;", "primary")
    accent = Style("color: #2EC4B6;", "accent")
    bg = Style("background-color: #0e1117;", "bg")
    surface = Style("background-color: #1c1f26;", "surface")
    text = Style("color: #FAFAFA;", "text")
    muted = Style("color: #95A5A6;", "muted")


class _Titles:
    slide = Style("font-size: var(--stx-scale-13, 36pt); font-weight: 700;", "title_slide")
    section = Style("font-size: var(--stx-scale-11, 28pt); font-weight: 700;", "title_section")
    subtitle = Style("font-size: var(--stx-scale-9, 22pt); font-weight: 600;", "title_subtitle")
    body = Style("font-size: var(--stx-scale-7, 18pt);", "title_body")
    caption = Style("font-size: var(--stx-scale-7, 18pt); color: #95A5A6;", "title_caption")


class _Callouts:
    info = Style(
        "background-color: rgba(122,184,245,0.10); border-left: 4px solid #7AB8F5; padding: 12px 16px;",
        "callout_info",
    )
    warn = Style(
        "background-color: rgba(243,156,18,0.10); border-left: 4px solid #F39C12; padding: 12px 16px;",
        "callout_warn",
    )
    error = Style(
        "background-color: rgba(231,76,60,0.10); border-left: 4px solid #E74C3C; padding: 12px 16px;",
        "callout_error",
    )
    success = Style(
        "background-color: rgba(39,174,96,0.10); border-left: 4px solid #27AE60; padding: 12px 16px;",
        "callout_success",
    )
    icon = Style("font-size: var(--stx-scale-8, 20pt); font-weight: 700;", "callout_icon")
    title = Style("font-weight: 700; font-size: var(--stx-scale-10, 24pt);", "callout_title")
    body = Style("font-size: var(--stx-scale-7, 18pt); line-height: 1.5;", "callout_body")


class _Body:
    paragraph = Style("font-size: var(--stx-scale-8, 20pt); line-height: 1.6;", "body_p")
    emphasis = Style("font-weight: 700; color: #7AB8F5;", "body_em")
    code = Style("font-family: monospace; background: rgba(255,255,255,0.05); padding: 1px 6px;", "body_code")


class _StatHero:
    value = Style("font-size: var(--stx-scale-17, 72pt); font-weight: 700; color: #2EC4B6;", "stat_value")
    body = Style("font-size: var(--stx-scale-7, 18pt); color: #FAFAFA;", "stat_body")


class _CardGrid:
    card = Style(
        "background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);"
        " padding: 16px; border-radius: 8px;",
        "card",
    )
    card_title = Style("font-size: var(--stx-scale-7, 18pt); font-weight: 700;", "card_title")
    card_body = Style("font-size: var(--stx-scale-7, 18pt); line-height: 1.5;", "card_body")


class _Takeaways:
    item = Style(
        "font-size: var(--stx-scale-7, 18pt); padding: 6px 0;"
        " border-bottom: 1px solid rgba(255,255,255,0.05);",
        "ta_item",
    )
    lead = Style("font-size: var(--stx-scale-7, 18pt); font-weight: 700;", "ta_lead")


class _Citation:
    source = Style("font-size: var(--stx-scale-7, 18pt); color: #95A5A6; font-style: italic;", "cite_source")
    author = Style("font-size: var(--stx-scale-7, 18pt); color: #95A5A6;", "cite_author")


class _InlineEmphasis:
    strong = Style("font-weight: 700; color: #7AB8F5;", "ie_strong")
    soft = Style("font-style: italic; color: #FAFAFA;", "ie_soft")


class _ComparisonTable:
    header = Style(
        "font-weight: 700; font-size: var(--stx-scale-7, 18pt); padding: 8px 12px;"
        " background: rgba(255,255,255,0.05);",
        "ct_header",
    )
    row = Style(
        "font-size: var(--stx-scale-7, 18pt); padding: 8px 12px;"
        " border-bottom: 1px solid rgba(255,255,255,0.05);",
        "ct_row",
    )
    accent_row = Style(
        "font-size: var(--stx-scale-7, 18pt); padding: 8px 12px;"
        " background: rgba(46,196,182,0.08);",
        "ct_accent",
    )


class DesignSystem:
    """The default design system shipped with streamtex-design."""

    name = "default"
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
