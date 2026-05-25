"""Validate every kit TOML in streamtex-pack-gse."""

from __future__ import annotations

from pathlib import Path

import pytest
from streamtex.core import validation

KITS_DIR = Path(__file__).resolve().parent.parent / "streamtex_gse" / "kits"

KIT_FILES = sorted(KITS_DIR.glob("*.toml"))


@pytest.mark.parametrize("kit_path", KIT_FILES, ids=lambda p: p.stem)
def test_kit_validates(kit_path: Path):
    issues = validation.validate_kit(kit_path)
    errors = [i for i in issues if i.is_error()]
    assert errors == [], f"{kit_path.name} errors: {errors}"


def test_at_least_one_kit():
    """v0.1.0 ships gse-default."""
    names = {p.stem for p in KIT_FILES}
    assert "gse-default" in names, f"Got {names}"
