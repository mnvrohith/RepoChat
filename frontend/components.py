import streamlit as st
import streamlit.components.v1 as components



def render_chat(messages):
    """
    Render complete chat history.
    """

    for message in messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])
           

            # Show sources only for assistant messages
            if (
                message["role"] == "assistant"
                and "sources" in message
                and len(message["sources"]) > 0
            ):

                with st.expander("📄 Sources", expanded=False):

                    for source in message["sources"]:

                        st.markdown(
                            f"""
**📁 {source['file_path']}**

**Function/Class:** `{source['name']}`

**Similarity:** `{source['score']}`
"""
                        )

                        st.divider()


def repo_card(name, files=None, chunks=None):

    st.markdown(
        f"""
### 📦 Repository

**{name}**

📄 **Files Indexed:** {files}

🧩 **Chunks Created:** {chunks}
"""
    )