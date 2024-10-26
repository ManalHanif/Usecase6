import streamlit as st
from PIL import Image
image = Image.open('personn.jpg')
st.title('بيت المتقبل')
st.image(image,width=80,height=80)
st.write('hello world')


    
