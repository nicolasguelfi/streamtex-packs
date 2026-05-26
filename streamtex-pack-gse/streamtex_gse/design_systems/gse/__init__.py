"""GSE design system — generated at import from the canonical palette JSON.

Source of truth: ``streamtex_gse/palettes/main.json`` (loaded at import time
via the ``streamtex.core.artifacts.palette`` engine).

The class structure mirrors the conventions of ``streamtex_design``:
- ``_Colors`` exposes the 7 canonical tokens + 4 semantic dimensions + 3 GSE
  letter accents (``g_letter``, ``s_letter``, ``e_letter``) mapped onto the
  canonical palette (G → amber, S → teal, E → electric-blue).
- Every other bundle (``titles``, ``callouts``, ``body``, ``fonts``, …) is
  inherited unchanged from ``streamtex_design.design_systems.default``.

If the palette JSON cannot be loaded (e.g. running tests without the file
present), the module falls back to the historical hex values so downstream
tests still pass.
"""

from pathlib import Path

from streamtex.core.artifacts.palette import load_palette_from_path
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

_PALETTE_PATH = Path(__file__).resolve().parents[2] / "palettes" / "main.json"

# Fallback hex values (used if palette JSON cannot be read). Match the
# canonical palette at the time of writing — kept in sync by the
# `test_gse_design_system` test in the pack-gse suite.
_FALLBACK_HEX: dict[str, str] = {
    "bg-navy":       "#1A1A2E",
    "electric-blue": "#7AB8F5",
    "teal":          "#2EC4B6",
    "amber":         "#F39C12",
    "coral":         "#E07A6E",
    "white":         "#FFFFFF",
    "muted-gray":    "#95A5A6",
}


def _hex_for(token: str) -> str:
    if _PALETTE.is_loaded:
        return _PALETTE.palette.hex_for(token)
    return _FALLBACK_HEX[token]


class _PaletteState:
    """Lazy holder for the loaded palette; falls back to hardcoded values."""

    def __init__(self) -> None:
        self.palette = None
        self.is_loaded = False
        try:
            self.palette = load_palette_from_path(_PALETTE_PATH, pack="streamtex-pack-gse")
            self.is_loaded = True
        except Exception:
            # Tolerate missing palette in degraded environments (e.g. tests
            # running without the data file). Fallback constants kick in.
            pass


_PALETTE = _PaletteState()


class _Colors:
    """GSE colors — palette canonical + GSE letter mappings + semantic aliases."""

    # Canonical 7 tokens (kebab-case in JSON → snake_case attributes)
    bg_navy        = Style(f"color: {_hex_for('bg-navy')};",       "gse_bg_navy")
    bg             = Style(f"background-color: {_hex_for('bg-navy')};", "bg")
    electric_blue  = Style(f"color: {_hex_for('electric-blue')};", "gse_electric_blue")
    teal           = Style(f"color: {_hex_for('teal')};",          "gse_teal")
    amber          = Style(f"color: {_hex_for('amber')};",         "gse_amber")
    coral          = Style(f"color: {_hex_for('coral')};",         "gse_coral")
    white          = Style(f"color: {_hex_for('white')};",         "gse_white")
    muted_gray     = Style(f"color: {_hex_for('muted-gray')};",    "gse_muted_gray")

    # Required-bundle aliases (ColorsBundle Protocol minimum)
    primary    = electric_blue
    accent     = teal
    surface    = Style("background-color: #1c1f26;", "surface")  # neutral surface
    text       = white
    muted      = muted_gray

    # Semantic colors (additive set introduced in pack-design v0.3.0)
    info       = electric_blue
    success    = Style("color: #27AE60;", "color_success")
    warning    = amber
    critical   = Style("color: #E74C3C;", "color_critical")
    highlight  = amber  # GSE: amber is the decisional accent — focal warmth

    # GSE letter mappings — G → amber, S → teal, E → electric-blue
    g_letter   = amber
    s_letter   = teal
    e_letter   = electric_blue

    # GSE semantic dimensions (from palette JSON)
    ideological = electric_blue
    political   = coral
    technical   = teal
    decisional  = amber


class DesignSystem:
    """GSE design system — pack-design `default` + GSE-One brand palette."""

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
