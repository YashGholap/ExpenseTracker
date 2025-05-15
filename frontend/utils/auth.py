import requests
import streamlit as st


API_BASE_URL = "http://localhost:8000"

def login_user(email, password):
    
    print(type(email), type(password))
    
    data={"email": email, "password": password}
    try: 
        res = requests.post(f"{API_BASE_URL}/auth/login", json=data)
        if res.status_code == 200:
            token = res.json()["access_token"]
            st.session_state["token"] = token
            # st.session_state["username"] = ["username"]
            return True
        else:
            st.error("Login failed.")
            return False
    except Exception as e:
        st.error(f"Error: {str(e)}")
    return False
    
    
def register_user(email,username, password):
    try:
        res = requests.post(f"{API_BASE_URL}/auth/register", json={
            "username": username,
            "email": email,
            "password": password,
        })
        return res.status_code == 200
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return False