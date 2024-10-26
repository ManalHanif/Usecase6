import streamlit as st
import pandas as pd


# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و الاستثمار </h1>", unsafe_allow_html=True)

df=pd.read_csv('https://github.com/ManalHanif/Usecase6/data/Riyadh_Aqqar/Aqqar_lands.csv')

df