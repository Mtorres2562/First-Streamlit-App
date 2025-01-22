import streamlit as st
import pandas as pd
import plotly.express as px

# title
st.title("Simple Data Dashboard")

# Add sliders for each category with default values
value_a = st.slider("Value for Category A", 0, 100, 47)
value_b = st.slider("Value for Category B", 0, 100, 41)
value_c = st.slider("Value for Category C", 0, 100, 64)
value_d = st.slider("Value for Category D", 0, 100, 50)

# Update the DataFrame based on user input
updated_data = pd.DataFrame({
    'Category':['A','B','C','D'],
    'Values':[value_a, value_b, value_c, value_d]
})

# Update the plot based on user iput using plotly
fig = px.bar(updated_data, x = 'Category', y = 'Values', title = 'Updated Category Values',
             labels = {'Category':'Category', 'Values':'Values'})

# Display the Plotly chart in streamlit
st.plotly_chart(fig)