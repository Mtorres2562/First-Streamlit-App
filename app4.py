import streamlit as st

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page",["Home", "Data Dashboard", "About"])

# Display different pages based on selection 
if page == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home page of your multi-page app.")

elif page == "Data Dashboard":
    st.title("Data Dashboard")
    st.write("Here's where your data visualizations and dashboards will go.")

elif page == "About":
    st.title("About")
    st.write("This is an example of a multi-page streamlit app.")
