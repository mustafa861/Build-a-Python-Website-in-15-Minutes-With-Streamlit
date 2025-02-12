import streamlit as st

# Title and Description
st.title("Welcome to My Streamlit Website")
st.subheader("A simple web app built with Streamlit")

# Text Section
st.write("This is a demonstration of building a website with Python in 15 minutes.")

# Image Section
st.image(
    "https://placekitten.com/800/400", 
    caption="An adorable placeholder cat image."
)

# Interactive Section
st.write("### Enter Your Name Below:")
name = st.text_input("Your Name", placeholder="Type here...")

if name:
    st.success(f"Hello, {name}! Welcome to the site.")

# Interactive Slider
st.write("### Adjust the Slider to Select a Value")
value = st.slider("Choose a number", 0, 100, 50)
st.write(f"You selected: {value}")

# Footer
st.write("---")
st.write("Built with using Streamlit")
