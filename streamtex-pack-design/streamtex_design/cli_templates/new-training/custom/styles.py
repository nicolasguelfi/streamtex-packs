"""Project palette for TRAINING_NAME — same shape as new-manual, kept slim
by importing from the pack."""

from streamtex.styles import Style, StxStyles

from streamtex_design import Body, Callouts, Colors, Fonts, Titles


class ProjectColors:
    brand = Style("color: #2EC4B6;", "training_brand")


class Styles:
    Large = StxStyles.Large
    bold = StxStyles.bold
    center_txt = StxStyles.center_align
    none = StxStyles.none

    colors = Colors
    titles = Titles
    fonts = Fonts
    callouts = Callouts
    body = Body

    class project:
        colors = ProjectColors
