import streamlit as st


def footer_home():

    st.markdown(
        f"""

            <div style="margin-top: 2rem; display: flex; gap: 6px; justify-content: center; items-align: center;">

            <p style="font-weight: bold; color: white;"> © 2026 SnapRoll AI • Built for Educators </p>

            </div>
                
                """,
        unsafe_allow_html=True,
    )


def footer_dashboard():

    st.markdown(
        f"""

            <div style="margin-top: 2rem; display: flex; gap: 6px; justify-content: center; items-align: center;">

            <p style="font-weight: bold; color: black;"> © 2026 SnapRoll AI • Built for Educators </p>

            </div>
                
                """,
        unsafe_allow_html=True,
    )
