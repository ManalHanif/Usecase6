import streamlit as st
from PIL import Image


# Load the image
image = Image.open('avg_lands.png')
# Load the image
image2 = Image.open('with_aparts.png')

# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و اللإستثمار </h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'> أبو خالد رجلاً طموحاً، يعيش حياة مليئة بالتحديات والتطلعات الكبيرة. لديه ثلاثة أطفال ، وكان دائماً يطمح لتوفير أفضل حياة لهم. في أحد الأيام، جاءه قرار مفاجئ؛ الانتقال إلى مدينة الرياض، المدينة الكبيرة التي تحفل بالفرص. لم يكن الانتقال سهلاً، لكنه كان يرى في الرياض بوابة لمستقبل مشرق له ولعائلته .</h5>", unsafe_allow_html=True)


# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image, width=650)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column

st.markdown("<h5 style='text-align: center;'>بعد وصوله إلى الرياض، بدأ أبو خالد يفكر في حلمه القديم: بناء فيلته الخاصة. كان يحلم بمساحة خضراء واسعة تحيط بها، وغرف لكل أطفاله الثلاثة، في مكان استراتيجي يسهل عليه الوصول إلى عمله وكل احتياجاته. لكن حين بدأ البحث عن الأراضي في وسط الرياض، صُدم بالأسعار! كانت تكاليف الأراضي مرتفعة جداً، ولم تكن مجرد شراء الأرض هو ما يقلقه؛ بل تكاليف البناء الإضافية التي ستتبعها. هذا الأمر دفعه لإعادة التفكير في خطته.</h5>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>بعد تفكير طويل، قرر أن يستبعد فكرة شراء الأرض والبناء بنفسه. وبدلاً من ذلك، بدأ يفكر في شراء فيلا جاهزة. بحث كثيراً، وحدد شروطه: يجب أن تكون الفلة في شرق الرياض، قريبة من عمله، وتحتوي على ثلاث غرف نوم تليق بعائلته. لكن للأسف، وجد أن أسعار الفلل في تلك المنطقة كانت تتجاوز قدراته المالية. </h1>", unsafe_allow_html=True)
# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image, width=650)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column
    
st.markdown("<h1 style='text-align: center;'>بعد تفكير طويل، قرر أن يستبعد فكرة شراء الأرض والبناء بنفسه. وبدلاً من ذلك، بدأ يفكر في شراء فيلا جاهزة. بحث كثيراً، وحدد شروطه: يجب أن تكون الفلة في شرق الرياض، قريبة من عمله، وتحتوي على ثلاث غرف نوم تليق بعائلته. لكن للأسف، وجد أن أسعار الفلل في تلك المنطقة كانت تتجاوز قدراته المالية. </h1>", unsafe_allow_html=True)
