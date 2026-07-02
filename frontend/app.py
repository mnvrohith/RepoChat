import streamlit as st

from auth import login_page
from session import initialize_session

from pages.repositories import load_projects
from pages.sidebar import render_sidebar
from pages.conversations import (
    load_conversations,
    render_conversations,
)
from pages.chat import render_chat

st.set_page_config(
    page_title="RepoChat",
    page_icon="💬",
    layout="wide",
)

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