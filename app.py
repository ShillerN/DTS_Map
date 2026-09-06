import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Blends Coverage Map", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit's own chrome (header, footer, hamburger menu, page padding).
# display:none (not visibility:hidden) so the reserved space collapses too.
st.markdown("""
    <style>
        #MainMenu, footer, header,
        div[data-testid="stToolbar"],
        div[data-testid="stDecoration"],
        div[data-testid="stStatusWidget"],
        div[data-testid="stHeader"] { display: none !important; height: 0 !important; }

        div[data-testid="stAppViewContainer"],
        div[data-testid="stAppViewBlockContainer"],
        div[data-testid="stMainBlockContainer"],
        section[data-testid="stMain"],
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            top: 0 !important;
        }
        div[data-testid="stVerticalBlock"] { gap: 0 !important; }

        html, body, .stApp { margin: 0 !important; padding: 0 !important; overflow: hidden !important; }
        iframe { display: block !important; }
    </style>
""", unsafe_allow_html=True)


@st.cache_data
def load_map():
    with open("Blends map.html", "r", encoding="utf-8") as f:
        return f.read()


components.html(load_map(), height=1080, scrolling=True)
