import streamlit as st

from styles import load_css

from auth import login_page
from session import initialize_session

from component.repositories import load_projects
from component.sidebar import render_sidebar
from component.conversations import (
    load_conversations,
    render_conversations,
)
from component.chat import render_chat

st.set_page_config(
    page_title="RepoChat",
    page_icon="💬",
    layout="wide",
)


st.markdown(load_css(), unsafe_allow_html=True)

initialize_session()

# -----------------------------
# Login
# -----------------------------

if st.session_state.token is None:

    login_page()

    st.stop()

# -----------------------------
# Load repositories
# -----------------------------

if not st.session_state.projects:

    load_projects()

# -----------------------------
# Sidebar
# -----------------------------

render_sidebar()

# -----------------------------
# Main Layout
# -----------------------------

left, right = st.columns([1, 3])

with left:

    if st.session_state.selected_project:

        load_conversations()

    render_conversations()

with right:

    render_chat()