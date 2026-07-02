import streamlit as st


def empty_dashboard():

    st.title("💬 RepoChat")

    st.markdown(
        """
## Welcome!

Select a repository from the sidebar.

Or click **➕ Add Repository** to index a new GitHub repository.
"""
    )