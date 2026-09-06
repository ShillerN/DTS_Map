import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Blends Coverage Map", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit's own chrome (header, footer, hamburger menu, page padding)
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        div[data-testid="stToolbar"] {visibility: hidden; height: 0;}
        div[data-testid="stDecoration"] {visibility: hidden;}
        div[data-testid="stStatusWidget"] {visibility: hidden;}
        section.main > div.block-container {padding: 0 !important; max-width: 100% !important;}
        .stApp {margin: 0; padding: 0;}
        iframe {display: block;}
    </style>
""", unsafe_allow_html=True)


@st.cache_data
def load_map():
    with open("Blends map.html", "r", encoding="utf-8") as f:
        return f.read()


components.html(load_map(), height=1080, scrolling=True)
