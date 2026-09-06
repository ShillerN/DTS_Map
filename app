import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")  # щоб карта займала всю ширину сторінки

@st.cache_data
def load_map():
    with open("Blends map.html", "r", encoding="utf-8") as f:
        return f.read()

components.html(load_map(), height=1000, scrolling=True)
