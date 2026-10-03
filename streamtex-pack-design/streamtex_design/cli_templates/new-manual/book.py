"""Entry point for a new manual.

Consumes packs declared in stx.toml. The welcome block uses
``level_badge_hero`` from streamtex-pack-manuals as the cover.
"""

from pathlib import Path

import blocks
import streamlit as st
import streamtex as stx
from custom.themes import dark
from streamtex import st_book
from streamtex.styles import StxStyles as sts

PROJECT_DIR = Path(__file__).parent

stx.set_static_sources([str(PROJECT_DIR / "static")])
sts.theme = dark
st.set_page_config(page_title="MANUAL_NAME", layout="wide")

st_book(
    [blocks.bck_welcome],
    paginate=True,
)
