"""Entry point for a new training session.

Uses pack-manuals training components (trainer_profile, training_header /
footer) and pack-design content components.
"""

from pathlib import Path

import streamlit as st
import streamtex as stx
from streamtex import st_book
from streamtex.styles import StxStyles as sts

from custom.themes import dark
import blocks

PROJECT_DIR = Path(__file__).parent

stx.set_static_sources([str(PROJECT_DIR / "static")])
sts.theme = dark
st.set_page_config(page_title="TRAINING_NAME", layout="wide")

st_book(
    [blocks.bck_welcome],
    paginate=True,
)
