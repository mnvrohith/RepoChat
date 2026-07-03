import streamlit as st

from api import RepoChatAPI

api = RepoChatAPI()


def render_chat():

    # ----------------------------------
    # No repository selected
    # ----------------------------------

    if st.session_state.selected_project is None:

        st.title("💬 RepoChat")

        st.info("Select a repository from the sidebar.")

        return

    # ----------------------------------
    # No conversation selected
    # ----------------------------------

    if st.session_state.selected_conversation is None:

        st.title("💬 RepoChat")

        st.info("Create or select a conversation.")

        return

    st.title("💬 RepoChat")

    # ----------------------------------
    # Existing Messages
    # ----------------------------------

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # ----------------------------------
    # Chat Input
    # ----------------------------------

    question = st.chat_input(
        "Ask anything about the repository..."
    )

    if not question:

        return

    # -----------------------------
    # User Message
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # -----------------------------
    # Assistant
    # -----------------------------

    with st.chat_message("assistant"):

        placeholder = st.empty()

        placeholder.markdown("Thinking...")

        try:

            response = api.ask_question(
                question=question,
                project_id=st.session_state.selected_project,
                conversation_id=st.session_state.selected_conversation,
                token=st.session_state.token,
            )

            answer = response["answer"]

            placeholder.markdown(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                }
            )

        except Exception as e:

            placeholder.error(e)