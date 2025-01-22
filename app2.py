import streamlit as st
import pandas as pd
import plotly.express as px

# Creat a sample DataFrame
data = pd.DataFrame({
    'Category':['A','B','C','D'],
    'Values':[10,23,45,15]
})

# Title
st.title("Simple Data Dashboard")

# Write test and display DataFrame
st.write("Here's the sample data.")
st.dataframe(data)


# Creat a bar plot using plotly
fig = px.bar(data, x = 'Category', y = 'Values', title = 'Category Values', labels= {'Category':'Category', 'Values':'Values'})

# Display the plot in streamlit
st.plotly_chart(fig)