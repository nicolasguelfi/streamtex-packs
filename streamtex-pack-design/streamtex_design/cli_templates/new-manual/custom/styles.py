"""Project palette for MANUAL_NAME.

Imports the pack-provided foundations (Colors, Titles, Fonts) and only
re-declares what's project-specific. Keep this file slim — never copy the
entire pack palette into here; reuse via the imports below.
"""

from streamtex.styles import Style, StxStyles

# Foundations from streamtex-pack-design 0.3.0+ — re-exports of the
# `default` design system bundles. Override per-document if needed.
from streamtex_design import Body, Callouts, Colors, Fonts, Titles


class ProjectColors:
    """Project-specific accents on top of the pack's Colors."""
    brand = Style("color: #7AB8F5;", "manual_brand")


class ProjectTitles:
    """Project-specific title styles composed from the pack's Titles."""
    section = Style.create(Titles.section + ProjectColors.brand, "manual_section")


class Styles:
    """Single entry point used by blocks via `from custom.styles import Styles as s`."""
    Large = StxStyles.Large
    bold = StxStyles.bold
    center_txt = StxStyles.center_align
    none = StxStyles.none

    # Re-export pack foundations under a single namespace
    colors = Colors
    titles = Titles
    fonts = Fonts
    callouts = Callouts
    body = Body

    class project:
        colors = ProjectColors
        titles = ProjectTitles
