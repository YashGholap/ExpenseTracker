import streamlit as st
from utils.auth import login_user, register_user

def render():
    st.subheader("🔐 Login or Register")
    
    tabs = st.tabs(['Login', 'Register'])
    
    with tabs[0]:
        st.write("Log in to your account")
        email= st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            if login_user(email,password):
                st.success(f"Logged in as {email}")
                st.rerun()
                
    with tabs[1]:
        st.write("Create a new account")
        new_username = st.text_input("Username", key="register_username")
        new_email = st.text_input("Email", key="register_email")
        new_password = st.text_input("Password", type="password", key="register_password")
        
        if st.button("Register"):
            if register_user(new_username, new_email, new_password):
                st.success("Account Created. you can now login in.")
            else:
                st.error("Registration failed.")