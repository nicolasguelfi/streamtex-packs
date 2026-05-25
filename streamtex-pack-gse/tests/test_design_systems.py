"""Validate the GSE design system extends pack-design correctly."""

from __future__ import annotations

import pytest
from streamtex.core import validation

import streamtex_gse.design_systems.gse as gse_mod


def test_gse_design_system_validates():
    issues = validation.validate_design_system(gse_mod)
    errors = [i for i in issues if i.is_error()]
    assert errors == [], f"errors: {errors}"


def test_gse_has_letter_colors():
    """The `gse` DS must expose g_letter / s_letter / e_letter so
    gse_letter can read them without falling through BV001."""
    DS = gse_mod.DesignSystem
    for slot in ("g_letter", "s_letter", "e_letter", "highlight"):
        assert hasattr(DS.colors, slot), f"Missing colors.{slot}"


def test_gse_inherits_optional_bundles():
    """Non-overridden bundles are inherited from pack-design default."""
    DS = gse_mod.DesignSystem
    for bundle in ("titles", "callouts", "body", "fonts", "stat_hero",
                   "card_grid", "takeaways", "citation",
                   "inline_emphasis", "comparison_table"):
        assert hasattr(DS, bundle), f"Missing bundle {bundle}"
