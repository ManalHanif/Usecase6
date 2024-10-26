import streamlit as st
from PIL import Image

# Load the image
image = Image.open('personn.jpg')

# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و الاستثمار </h1>", unsafe_allow_html=True)

# Center the image
st.image(image, width=200)


# Center the image using HTML
st.markdown("<div style='text-align: center;'><img src='data:image/jpeg;base64,{}' width='200'/></div>".format(image_to_base64(image)), unsafe_allow_html=True)

def image_to_base64(image):
    import io
    import base64
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

