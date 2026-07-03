import streamlit as st

from api import RepoChatAPI

api = RepoChatAPI()


# ----------------------------------------
# Load Conversations
# ----------------------------------------

def load_conversations():

    if st.session_state.selected_project is None:

        st.session_state.conversations = []

        return

    try:

        conversations = api.get_conversations(
            project_id=st.session_state.selected_project,
            token=st.session_state.token,
        )

        st.session_state.conversations = conversations

    except Exception as e:

        st.error(e)


# ----------------------------------------
# Load Messages
# ----------------------------------------

def load_messages(conversation_id):

    try:

        messages = api.get_messages(
            conversation_id=conversation_id,
            token=st.session_state.token,
        )

        st.session_state.messages = messages

    except Exception as e:

        st.error(e)


# ----------------------------------------
# Create Conversation
# ----------------------------------------

def new_chat():

    if st.session_state.selected_project is None:

        st.warning("Select a repository first.")

        return

    try:

        conversation = api.create_conversation(
            project_id=st.session_state.selected_project,
            token=st.session_state.token,
        )

        st.session_state.selected_conversation = conversation["conversation_id"]

        st.session_state.messages = []

        load_conversations()

        st.rerun()

    except Exception as e:

        st.error(e)


# ----------------------------------------
# Delete Conversation
# ----------------------------------------

def delete_conversation(conversation_id):

    try:

        api.delete_conversation(
            conversation_id=conversation_id,
            token=st.session_state.token,
        )

        if (
            st.session_state.selected_conversation
            == conversation_id
        ):

            st.session_state.selected_conversation = None
            st.session_state.messages = []

        load_conversations()

        st.rerun()

    except Exception as e:

        st.error(e)


# ----------------------------------------
# Render Conversation List
# ----------------------------------------

def render_conversations():

    if st.session_state.selected_project is None:

        st.info("Select a repository.")

        return

    st.subheader("💬 Conversations")

    if st.button(
        "➕ New Chat",
        use_container_width=True,
    ):

        new_chat()

    st.divider()

    if not st.session_state.conversations:

        st.info("No conversations yet.")

        return

    for conversation in st.session_state.conversations:

        col1, col2 = st.columns([5, 1])

        selected = (
            st.session_state.selected_conversation
            == conversation["conversation_id"]
        )

        button_type = (
            "primary"
            if selected
            else "secondary"
        )

        with col1:

            if st.button(
                conversation["title"],
                key=f"conv_{conversation['conversation_id']}",
                use_container_width=True,
                type=button_type,
            ):

                st.session_state.selected_conversation = (
                    conversation["conversation_id"]
                )

                load_messages(
                    conversation["conversation_id"]
                )

                st.rerun()

        with col2:

            if st.button(
                "🗑",
                key=f"delete_conv_{conversation['conversation_id']}",
            ):

                delete_conversation(
                    conversation["conversation_id"]
                )