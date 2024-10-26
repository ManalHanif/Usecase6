import streamlit as st
from PIL import Image

# Load the image
image = Image.open('personn.jpg')

# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و الاستثمار </h1>", unsafe_allow_html=True)

# Center the image
st.image(image, width=200)

# Display a message centered
st.markdown("<h2 style='text-align: center;'>hello world</h2>", unsafe_allow_html=True)




    
