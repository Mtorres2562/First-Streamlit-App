import streamlit as st
import pandas as pd
import plotly.express as px

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page",["Home", "Data Dashboard", "About"])

# Display different pages based on selection 
if page == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home page of your multi-page app.")

elif page == "Data Dashboard":
    st.title("Data Dashboard")

# Example of displaying a DataFrame and chart on the dashboard page

# Create sample page
    data = pd.DataFrame({
        'Category':['A','B','C','D'],
        'Values':[10,23,45,15]
    })

    st.write("Here's the sample data")
    st.dataframe(data)

# Creat and display a bar chart using plotly
    fig = px.bar(data, x = 'Category', y = 'Values', title ='Category Values',
                labels = {'Category':'Category', 'Values':'Values'})

# Display the plotly chart in streamlit
    st.plotly_chart(fig)

elif page == "About":
    st.title("About")
    st.write("This is an example of a multi-page streamlit app.")