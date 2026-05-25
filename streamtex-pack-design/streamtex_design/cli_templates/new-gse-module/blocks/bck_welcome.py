"""Welcome block — uses gse_letter to render the GSE brand phrase."""

from streamtex import st_space, st_write
from streamtex_gse.components.gse_letter import gse_letter
from streamtex_gse.design_systems.gse import DesignSystem

DS = DesignSystem()


def build() -> None:
    st_write(DS.titles.slide, "GSE_MODULE_NAME", toc_lvl="1")
    st_space("v", 2)
    gse_letter(
        design_system=DS,
        text="Generative Software Engineering",
    )
