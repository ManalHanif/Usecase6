import streamlit as st
import pandas as pd


# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و الاستثمار </h1>", unsafe_allow_html=True)

df=pd.read_csv('Aqqar_lands.csv')

df