import streamlit as st
from db import get_conn

def login():
    st.sidebar.title("Login / Register")
    choice = st.sidebar.radio("Select Action", ["Login", "Register"])
    
    conn = get_conn()
    c = conn.cursor()
    
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if choice == "Register":
        if st.sidebar.button("Create Account"):
            try:
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                st.success("Account created! Please login.")
            except:
                st.error("Username already exists.")
    
    elif choice == "Login":
        if st.sidebar.button("Login"):
            c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = c.fetchone()
            if user:
                st.session_state["user"] = dict(user)
            else:
                st.error("Invalid credentials.")
    conn.close()
