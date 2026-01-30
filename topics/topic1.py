import streamlit as st
from utils import log_interaction, add_points

TOPIC_NAME = "Topic 1: Introduction"

def show(user):
    st.title(TOPIC_NAME)
    
    st.write("Welcome to Topic 1! Here is some interactive content.")
    
    if st.button("Mark as Complete"):
        log_interaction(user["id"], TOPIC_NAME, "Completed")
        add_points(user["id"], 10)
        st.success("Topic completed! +10 points")
    
    # Example quiz
    st.subheader("Quick Quiz")
    answer = st.radio("What is 2 + 2?", ["3", "4", "5"])
    if st.button("Submit Answer"):
        if answer == "4":
            log_interaction(user["id"], TOPIC_NAME, "Quiz correct")
            add_points(user["id"], 5)
            st.success("Correct! +5 points")
        else:
            log_interaction(user["id"], TOPIC_NAME, "Quiz incorrect")
            st.error("Wrong answer")
