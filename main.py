import streamlit as st
from auth import login
from db import init_db
from topics import topic1, topic2, topic3

init_db()

if "user" not in st.session_state:
    login()

if "user" in st.session_state:
    user = st.session_state["user"]
    st.sidebar.write(f"Hello, {user['username']}! Points: {user['points']}")
    
    topic_choice = st.sidebar.selectbox("Select Topic", ["Topic 1", "Topic 2", "Topic 3"])
    
    if topic_choice == "Topic 1":
        topic1.show(user)
    elif topic_choice == "Topic 2":
        topic2.show(user)
    elif topic_choice == "Topic 3":
        topic3.show(user)
