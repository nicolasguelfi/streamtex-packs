"""Welcome block — trainer profile + training header."""

from streamtex import st_space
from streamtex_design.design_systems.default import DesignSystem
from streamtex_manuals.components.trainer_profile import trainer_profile
from streamtex_manuals.components.training_header import training_header

DS = DesignSystem()


def build() -> None:
    training_header(
        design_system=DS,
        program="PROGRAM_NAME",
        module="TRAINING_NAME",
        right_label="Module 1 · YYYY-MM",
    )
    st_space("v", 2)
    trainer_profile(
        design_system=DS,
        name="Trainer Name",
        role="Trainer",
        affiliation="Affiliation",
        bio="One short paragraph framing the trainer's expertise and the angle they bring to this session.",
        photo_uri=None,
    )
