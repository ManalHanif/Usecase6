import streamlit as st



# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و الاستثمار </h1>", unsafe_allow_html=True)

df=pandas.DataFrame({'col1':[1,2,3,4],'col2':[1,2,3,4]})

st.dataframe(df)