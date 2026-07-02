import streamlit as st

from api import RepoChatAPI

api = RepoChatAPI()


def login_page():

    st.title("💬 RepoChat")

    st.caption("Chat with GitHub repositories using AI")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # --------------------------------------------------
    # Login
    # --------------------------------------------------

    with tab1:

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login",
            use_container_width=True,
        ):

            try:

                response = api.login(
                    email=email,
                    password=password,
                )

                st.session_state.token = response["access_token"]

                st.success("Login Successful!")

                st.rerun()

            except Exception as e:

                st.error(str(e))

    # --------------------------------------------------
    # Register
    # --------------------------------------------------

    with tab2:

        name = st.text_input(
            "Name",
            key="register_name"
        )

        email = st.text_input(
            "Email",
            key="register_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="register_password"
        )

        if st.button(
            "Register",
            use_container_width=True,
        ):

            try:

                api.register(
                    name=name,
                    email=email,
                    password=password,
                )

                st.success(
                    "Registration successful. Please login."
                )

            except Exception as e:

                st.error(str(e))