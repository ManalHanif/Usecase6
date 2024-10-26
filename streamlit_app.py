import streamlit as st
from PIL import Image


# Load the image
image = Image.open('avg_lands.png')



# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بيت المتقبل</h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'> أبو خالد رجلاً طموحاً، يعيش حياة مليئة بالتحديات والتطلعات الكبيرة. لديه ثلاثة أطفال ، وكان دائماً يطمح لتوفير أفضل حياة لهم. في أحد الأيام، جاءه قرار مفاجئ؛ الانتقال إلى مدينة الرياض، المدينة الكبيرة التي تحفل بالفرص. لم يكن الانتقال سهلاً، لكنه كان يرى في الرياض بوابة لمستقبل مشرق له ولعائلته .</h5>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>بعد وصوله إلى الرياض، بدأ أبو خالد يفكر في حلمه القديم: بناء فيلته الخاصة. كان يحلم بمساحة خضراء واسعة تحيط بها، وغرف لكل أطفاله الثلاثة، في مكان استراتيجي يسهل عليه الوصول إلى عمله وكل احتياجاته. لكن حين بدأ البحث عن الأراضي في وسط الرياض، صُدم بالأسعار! كانت تكاليف الأراضي مرتفعة جداً، ولم تكن مجرد شراء الأرض هو ما يقلقه؛ بل تكاليف البناء الإضافية التي ستتبعها. هذا الأمر دفعه لإعادة التفكير في خطته.</h5>", unsafe_allow_html=True)


# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([0, 3, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image, width=600)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column

