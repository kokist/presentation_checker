import streamlit as st

def setup_sidebar():
    with st.sidebar:
        st.page_link('app.py', label='HOME', icon='🏠')
        st.page_link('pages/ppt2speech.py', label='PPT to Sound', icon='🔊')
