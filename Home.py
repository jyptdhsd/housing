import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("Housing Dashboard")
st.write("Welcome to the Housing app. Choose an option below to continue.")
st.write("This is the main entry page for the project.")

if st.button("Go to App"):
    st.switch_page("pages/app.py")
