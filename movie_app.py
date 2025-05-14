import streamlit as st
import pandas as pd
from home import home_page
from dashboard import dashboard_page
from release_forecast import release_forecast_page
from recommended import recommended_page
from popularity_predictor import popularity_predictor_page
from revenue_predictor import revenue_predictor_page  # Import the new page
from auth_pages import login_page, signup_page, logout
from auth import init_db

st.set_page_config(page_title="Movie Analytics & Recommendation App", layout="wide")

# Initialize the database
init_db()

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "page" not in st.session_state:
    st.session_state.page = "login"  # Default page is login

# Main App
def main_app():
    st.sidebar.title("📊 Movie App")
    st.sidebar.write(f"Welcome, {st.session_state.username}!")
    if st.sidebar.button("Logout"):
        logout()

    page = st.sidebar.radio("Navigate to", ["Home", "Dashboard", "Release Pattern Forecast", "Recommended", "Popularity Predictor", "Revenue Predictor"])

    if page == "Home":
        home_page()
    elif page == "Dashboard":
        dashboard_page(df)
    elif page == "Release Pattern Forecast":
        release_forecast_page(df)
    elif page == "Recommended":
        recommended_page(df)
    elif page == "Popularity Predictor":
        popularity_predictor_page(df)
    elif page == "Revenue Predictor":
        revenue_predictor_page(df)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("D:/RVU/Sem_4/Agile/movie2_final-main/movie2_final-main/data/movie_.csv")
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    return df.dropna(subset=['release_date'])

df = load_data()

# App Logic
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "signup":
    signup_page()
else:
    main_app()