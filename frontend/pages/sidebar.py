import streamlit as st

from pages.repositories import (
    add_repository,
    delete_project,
    load_projects,
)


def render_sidebar():

    with st.sidebar:

        st.title("💬 RepoChat")

        st.divider()

        add_repository()

        st.divider()

        st.subheader("Repositories")

        if not st.session_state.projects:

            st.info("No repositories yet.")

            return

        for project in st.session_state.projects:

            col1, col2 = st.columns([5, 1])

            selected = (
                st.session_state.selected_project
                == project["project_id"]
            )

            button_type = (
                "primary"
                if selected
                else "secondary"
            )

            with col1:

                if st.button(
                    project["repo_name"],
                    key=f"repo_{project['project_id']}",
                    use_container_width=True,
                    type=button_type,
                ):

                    st.session_state.selected_project = project["project_id"]

                    st.session_state.selected_conversation = None

                    st.session_state.messages = []

                    st.rerun()

            with col2:

                if st.button(
                    "🗑",
                    key=f"delete_{project['project_id']}",
                ):

                    delete_project(
                        project["project_id"]
                    )

        st.divider()

        if st.button(
            "🔄 Refresh",
            use_container_width=True,
        ):

            load_projects()

            st.rerun()

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True,
        ):

            st.session_state.token = None
            st.session_state.projects = []
            st.session_state.selected_project = None
            st.session_state.selected_conversation = None
            st.session_state.conversations = []
            st.session_state.messages = []

            st.rerun()