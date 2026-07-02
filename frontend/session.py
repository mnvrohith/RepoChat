import streamlit as st


def initialize_session():

    defaults = {

        # -------------------------
        # Authentication
        # -------------------------

        "token": None,

        # -------------------------
        # Projects
        # -------------------------

        "projects": [],
        "selected_project": None,

        # -------------------------
        # Conversations
        # -------------------------

        "conversations": [],
        "selected_conversation": None,

        # -------------------------
        # Messages
        # -------------------------

        "messages": [],

        # -------------------------
        # UI
        # -------------------------

        "show_add_repo": False,

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value