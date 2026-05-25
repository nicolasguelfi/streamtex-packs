"""Welcome block — manual cover using level_badge_hero from pack-manuals."""

from streamtex_design.design_systems.default import DesignSystem
from streamtex_manuals.components.level_badge_hero import level_badge_hero

DS = DesignSystem()


def build() -> None:
    level_badge_hero(
        design_system=DS,
        manual_title="MANUAL_NAME",
        manual_subtitle="Short tagline describing what the manual covers",
        level_label="REUSE LEVEL",
        level_headline="One-sentence headline (≤ 80 chars).",
        level_body="One short paragraph framing the manual's scope and the value it brings to the reader.",
        accent_color="#7AB8F5",
        gradient_start="#1c3d5a",
        gradient_end="#0e1117",
        bullets=["Item 1", "Item 2", "Item 3"],
    )
