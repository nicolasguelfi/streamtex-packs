"""Project palette for GSE_MODULE_NAME — built on the `gse` design system.

Imports pack-design foundations and the GSE design system from
streamtex-pack-gse. Custom project styles are minimal.
"""

from streamtex.styles import Style, StxStyles

from streamtex_design import Body, Callouts, Fonts, Titles
from streamtex_gse.design_systems.gse import DesignSystem as GseDS


class ProjectColors:
    """Project accents on top of the GSE palette."""
    brand = Style("color: #F5A623;", "gse_brand")  # amber highlight


class Styles:
    Large = StxStyles.Large
    bold = StxStyles.bold
    center_txt = StxStyles.center_align
    none = StxStyles.none

    # `colors` here is the GSE design system's color bundle — includes
    # g_letter / s_letter / e_letter and the amber `highlight`.
    colors = GseDS.colors
    titles = Titles
    fonts = Fonts
    callouts = Callouts
    body = Body

    class project:
        colors = ProjectColors
