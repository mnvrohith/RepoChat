import streamlit as st

from api import RepoChatAPI

api = RepoChatAPI()


# ----------------------------------------
# Load all repositories
# ----------------------------------------

def load_projects():

    try:

        projects = api.get_projects(
            st.session_state.token
        )

        st.session_state.projects = projects

    except Exception as e:

        st.error(e)


# ----------------------------------------
# Add Repository
# ----------------------------------------

def add_repository():

    with st.expander(
        "➕ Add Repository",
        expanded=False,
    ):

        repo_url = st.text_input(
            "GitHub Repository URL",
            placeholder="https://github.com/owner/repository",
        )

        if st.button(
            "Index Repository",
            use_container_width=True,
        ):

            if repo_url.strip() == "":

                st.warning("Please enter a repository URL.")

                return

            with st.spinner("Indexing repository..."):

                try:

                    api.ingest_repository(
                        repo_url=repo_url,
                        token=st.session_state.token,
                    )

                    st.success(
                        "Repository indexed successfully."
                    )

                    load_projects()

                    st.rerun()

                except Exception as e:

                    st.error(e)


# ----------------------------------------
# Delete Repository
# ----------------------------------------

def delete_project(project_id):

    try:

        api.delete_project(
            project_id,
            st.session_state.token,
        )

        if (
            st.session_state.selected_project
            == project_id
        ):

            st.session_state.selected_project = None
            st.session_state.selected_conversation = None
            st.session_state.messages = []

        load_projects()

        st.rerun()

    except Exception as e:

        st.error(e)