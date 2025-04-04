import streamlit as st
import validators
import time

from rag import generate_answer
from rag_main import create_db_and_retriever

st.title("AbsoluteMind")

# Initialize session state
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False
if "result" not in st.session_state:
    st.session_state.result = ""
if "question" not in st.session_state:
    st.session_state.question = ""
if "answer" not in st.session_state:
    st.session_state.answer = ""

# URL input field
url = st.text_input("Enter a valid document URL:")

# Button to trigger function
if st.button("Submit"):
    if validators.url(url):
        with st.spinner("Analyzing document..."):
            st.session_state.result = create_db_and_retriever([url])
        st.session_state.analysis_done = True
        st.session_state.answer = ""  # Reset answer when a new URL is submitted
    else:
        st.error("Invalid URL. Please enter a valid web address.")

# Show result and question input field if analysis is done
if st.session_state.analysis_done:
    st.session_state.question = st.text_input("Ask a question:")

    # Button to submit question
    if st.button("Submit Question"):
        if st.session_state.question:
            with st.spinner("Generating answer..."):
                st.session_state.answer = generate_answer(st.session_state.question,st.session_state.result)
            st.success(st.session_state.answer)
        else:
            st.error("Please enter a question.")
