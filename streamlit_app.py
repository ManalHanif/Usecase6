import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و الاستثمار </h1>", unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_family = load_lottieurl("https://lottie.host/c0cbe4ae-6193-4417-b105-5c6519235745/hW7UA2JbjT.json")


st_lottie(
lottie_family,
)
