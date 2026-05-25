"""Validate the streamtex-pack-manuals manifest + structure."""

from pathlib import Path

from streamtex.core import validation

PACK_ROOT = Path(__file__).resolve().parent.parent / "streamtex_manuals"


def test_pack_manifest_validates():
    issues = validation.validate_pack(PACK_ROOT)
    errors = [i for i in issues if i.is_error()]
    assert errors == [], f"errors: {errors}"
