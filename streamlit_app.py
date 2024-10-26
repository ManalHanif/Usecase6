import streamlit as st
from PIL import Image

# Load the image
image = Image.open('personn.jpg')

# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و الاستثمار </h1>", unsafe_allow_html=True)

# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([3, 4, 3])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image, width=200)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column



