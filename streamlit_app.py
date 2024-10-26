import streamlit as st
import pandas as pd


df = pd.read_csv('Aqqar_lands.csv')
st.dataframe(df, height=300)

