"""Kopitiam ordering app, served inside Streamlit.

The ordering UI itself is the original single-file HTML/JS app
(kopitiam.html). Streamlit only wraps it, so the app keeps its
splash screen, Coffee / Tea / Drinks tabs, customisation
(cup size, Hot / Bua Siow / Peng, Siu Dai / Gah Dai / Kosong),
quantity, order view and confirmation exactly as built.
Orders are not sent to a server - they live in the browser,
just like the original app.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="23T Kopitiam",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the app fills the page like a mobile app.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "kopitiam.html"
html = html_path.read_text(encoding="utf-8")

# The app is designed for a phone-width column; centre it and
# give it plenty of height. Scrolling is handled inside the app.
components.html(html, height=900, scrolling=True)
