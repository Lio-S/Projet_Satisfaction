import streamlit as st

# switch function for enabling and disabling buttons
def run_disable():
    st.session_state.running = True

def enable():
    st.session_state.running = False
