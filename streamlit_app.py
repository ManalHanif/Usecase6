import streamlit as st
from PIL import Image
image = Image.open('personn.jpg')
st.image(image)
st.write('hello world')


    
