import streamlit as st

from add_to_qase import add_bulk_to_qase
from export_to_excel import export_to_excel
from main import stream_graph_updates
from tester_agent import generate_test_cases

st.title("AI Powered QASE")

# Input field for user story
user_story = st.text_area("Enter the user story or functionality description:")

if st.button("Generate Test Cases"):
    if user_story.strip():
        test_cases = generate_test_cases(user_story)
        # export_to_excel(test_cases)
        add_bulk_to_qase(test_cases)
        st.success("🎉 Your test cases have been generated and exported successfully! Check your downloaded file.")
    else:
        st.warning("Please enter a user story to generate test cases.")
