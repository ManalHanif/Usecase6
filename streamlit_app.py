import streamlit as st
from PIL import Image
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as pg
import requests
from streamlit_lottie import st_lottie

# load dataframe (villa)
villa = pd.read_csv("Cleaning.csv")
villa.drop(columns='Unnamed: 0', inplace=True)
vill_with_apart = villa[villa['apartments'] <= 5]
vill_with_apart = vill_with_apart[vill_with_apart['price'] <= 6000000]

# load dataframe(real estate)
apdf = pd.read_csv("data/apartments in Riyadh Saudi Arabia/realEstate_cleaned.csv")
apdf.drop(columns="Unnamed: 0",inplace=True)


# Load the image
image = Image.open('avg_lands.png')
# Load the image
image2 = Image.open('with_aparts.png')
# Load the image
image3 = Image.open('imgg.png')
image4 = Image.open('riyadhh.png')


# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و اللإستثمار </h1>", unsafe_allow_html=True)
# Center the image using Streamlit's layout

# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1,4, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image4, width=400)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column


st.markdown("<h5 style='text-align: center;'> أبو خالد رجلاً طموحاً، يعيش حياة مليئة بالتحديات والتطلعات الكبيرة. لديه ثلاثة أطفال ، وكان دائماً يطمح لتوفير أفضل حياة لهم. في أحد الأيام، جاءه قرار مفاجئ؛ الانتقال إلى مدينة الرياض، المدينة الكبيرة التي تحفل بالفرص. لم يكن الانتقال سهلاً، لكنه كان يرى في الرياض بوابة لمستقبل مشرق له ولعائلته .</h5>", unsafe_allow_html=True)


# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1,13, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image, width=650)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column

st.markdown("<h5 style='text-align: center;'>بعد وصوله إلى الرياض، بدأ أبو خالد يفكر في حلمه القديم: بناء فيلته الخاصة. كان يحلم بمساحة خضراء واسعة تحيط بها، وغرف لكل أطفاله الثلاثة، في مكان استراتيجي يسهل عليه الوصول إلى عمله وكل احتياجاته. لكن حين بدأ البحث عن الأراضي في وسط الرياض، صُدم بالأسعار! كانت تكاليف الأراضي مرتفعة جداً، ولم تكن مجرد شراء الأرض هو ما يقلقه؛ بل تكاليف البناء الإضافية التي ستتبعها. هذا الأمر دفعه لإعادة التفكير في خطته.</h5>", unsafe_allow_html=True)
# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1,13, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column
# creat bar chart
top_5_locations = vill_with_apart.groupby('location')['price'].mean().nlargest(5).reset_index()

# Plotting with Plotly
fig1 = px.bar(top_5_locations, 
             x='location', 
             y='price', 
             color='price', 
             color_continuous_scale='Reds',
             title='متوسط سعر الفلل في الرياض(فلل مع شقق)',
             labels={'price': 'Average Price', 'location': 'Location'},
             text='price')

# Show the plot
fig1.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig1.update_layout(xaxis=dict(title='Location'), 
                  yaxis=dict(title='Average Price with apart'),
                  showlegend=False)

with col2:
    st.plotly_chart(fig1)
    #st.image(image2, width=650)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column
    
st.markdown("<h5 style='text-align: center;'> بعد تفكير طويل، قرر أن يستبعد فكرة شراء الأرض والبناء بنفسه. وبدلاً من ذلك، بدأ يفكر في شراء فيلا جاهزة. بحث كثيراً، قرر ان تكون الفلة في شرق الرياض، لقربها من عمله و مناسبه لميزانيته</h5>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,13, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

# create hist chart for Distribution of Property Prices
fig2 = px.histogram(apdf, x='price', nbins=30, title='Distribution of Property Prices',
                   marginal='rug', opacity=0.75)
fig2.update_traces(marker=dict(line=dict(width=1, color='black')))

with col2:
    st.plotly_chart(fig2)
    #st.image(image3, width=650)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column
st.markdown("<h5 style='text-align: center;'>في خضم البحث، لفت انتباهه شيء آخر. وجد أن بعض الفلل المعروضة للبيع تحتوي على شقق للإيجار، وأن أسعار الإيجارات في شرق الرياض كانت مشجعة جداً. فقد بلغ متوسط الإيجار لتلك الشقق حوالي 52,000 ريال سنوياً. هذه الفكرة كانت مغرية لأبو خالد؛ فمن خلال شراء فيلا جاهزة تحتوي على شقة للإيجار، يمكنه أن يؤمن مصدر دخل إضافي يغطي جزءاً من تكاليف الشراء. </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>وبالفعل، بعد دراسة متأنية وتفكير عميق، قرر أبو خالد أن يسكن في إحدى تلك الفلل. ليس فقط لأنه وجد ما يناسب عائلته، بل لأنه أيضاً وجد فرصة استثمارية ممتازة. استقر في الفلة الجديدة، واستأجر الشقة، وبدأ يشعر بأن حلمه يتحقق بطريقة لم يكن يتوقعها. وهكذا، تمكن أبو خالد من تأمين سكن لعائلته والاستثمار في نفس الوقت، مما جعله يشعر بالرضا والطمأنينة تجاه مستقبله ومستقبل أطفاله.بين الحلم والاستثمار </h5>", unsafe_allow_html=True)


