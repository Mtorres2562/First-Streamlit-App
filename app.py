import streamlit as st

# Title
st.title("My First Streamlit App")

# Write some text
st.write("Welcime to my first Streamlit app!!")

# Add a slider

number = st.slider("Pick a number", 1, 10)

# Display the result
st.write(f"You selected: {number}")