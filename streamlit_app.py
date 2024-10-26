import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
st.write('hello world')

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lot_hello=load_lottieurl('https://lottie.host/5264c145-8e04-4020-a4e2-12b8cfefaf8f/naH2hYZEX1.json')
st_lottie(lot_hello,key='Hello')
    
