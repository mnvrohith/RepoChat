import streamlit as st

from api import RepoChatAPI
from styles import load_css
from components import render_chat, repo_card


# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="RepoChat",
    page_icon="💬",
    layout="wide",
)

st.markdown(load_css(), unsafe_allow_html=True)

api = RepoChatAPI()


# ----------------------------------
# Session State
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "repo_url" not in st.session_state:
    st.session_state.repo_url = ""

if "repo_name" not in st.session_state:
    st.session_state.repo_name = ""

if "files_processed" not in st.session_state:
    st.session_state.files_processed = 0

if "chunks_created" not in st.session_state:
    st.session_state.chunks_created = 0

if "repo_loaded" not in st.session_state:
    st.session_state.repo_loaded = False


# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.title("📂 Repository")

    if st.session_state.repo_loaded:

        repo_card(
            st.session_state.repo_name,
            st.session_state.files_processed,
            st.session_state.chunks_created,
        )

        st.success("✅ Repository Indexed")

        if st.button("🗑 Clear Chat"):

            st.session_state.messages = []
            st.rerun()

    else:

        st.info("No repository loaded.")


# ----------------------------------
# Header
# ----------------------------------

st.title("💬 RepoChat")

st.caption("Chat with any GitHub Repository using RAG")


# ----------------------------------
# Repository Input
# ----------------------------------

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/owner/repository",
)

if st.button("🚀 Ingest Repository"):

    if repo_url.strip() == "":

        st.warning("Please enter a repository URL.")

    else:

        with st.spinner("📥 Indexing repository..."):

            try:

                result = api.ingest_repository(repo_url)

                st.session_state.repo_url = repo_url
                st.session_state.repo_name = repo_url.rstrip("/").split("/")[-1]

                st.session_state.files_processed = result["files_processed"]
                st.session_state.chunks_created = result["chunks_created"]

                st.session_state.repo_loaded = True

                st.success("Repository indexed successfully!")

                st.rerun()

            except Exception as e:

                st.error(f"Error: {e}")


st.divider()


# ----------------------------------
# Chat Section
# ----------------------------------

if st.session_state.repo_loaded:

    # Display previous chat history
    render_chat(st.session_state.messages)

    question = st.chat_input(
        "Ask anything about the repository..."
    )

    if question:

        # Store user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.status("Generating Answer...", expanded=True) as status:

            status.write("🔍 Searching repository...")
            status.write("🧠 Retrieving relevant chunks...")
            status.write("🤖 Asking Gemini...")

            try:

                response = api.ask_question(question)

                answer = response["answer"]
                sources = response.get("sources", [])

                status.update(
                    label="✅ Answer Ready",
                    state="complete",
                )

            except Exception as e:

                answer = str(e)

                status.update(
                    label="❌ Error",
                    state="error",
                )

        # Store assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": sources
            }
        )

        st.rerun()

else:

    st.markdown(
        """
# 👋 Welcome to RepoChat

Chat with any GitHub repository using Retrieval-Augmented Generation (RAG).

### You can ask questions like:

- How authentication works?
- Explain the project architecture.
- Which database is used?
- Describe the folder structure.
- How are APIs implemented?
- Explain a specific class or function.
- Where is JWT implemented?

⬆️ Enter a GitHub repository URL above and click **Ingest Repository** to begin.
"""
    )