import streamlit as st
from streamlit_option_menu import option_menu
from pages import login

st.set_page_config(page_title="Expense Tracker", layout="wide")

if "token" not in st.session_state:
    st.session_state["token"] = None
if "username" not in st.session_state:
    st.session_state["username"] = None
    
    
st.title("💸 Expense Tracker")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Login", "Add Expense", "View Expenses", "Dashboard"],
        icons=["box-arrow-in-right", "plus-circle", "table", "bar-chart"],
        menu_icon="cast",
        default_index=0
    )
    
if selected == "Login":
    login.render()
elif selected == "Add Expense":
    pass
elif selected == "View Expenses":
    pass
elif selected == "Dashboard":
    pass
