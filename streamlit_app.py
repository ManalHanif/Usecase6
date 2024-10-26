import streamlit as st
from PIL import Image
image = Image.open('personn.jpg')
st.title('بيت المتقبل')
st.image(image,width=300)
st.write('hello world')


    
