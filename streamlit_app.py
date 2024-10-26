import streamlit as st
import pandas as pd
import plotly.express as px


df_land = pd.read_csv('Aqqar_lands.csv')

neighborhood_counts = df_land['الحي'].value_counts()

neighborhoods_over_5 = neighborhood_counts[neighborhood_counts > 5].index
filtered_df = df_land[df_land['الحي'].isin(neighborhoods_over_5)]

avg_price_per_neighborhood = filtered_df.groupby('الحي')['السعر الإجمالي'].mean().reset_index()
sorted_avg_prices = avg_price_per_neighborhood.sort_values(by='السعر الإجمالي', ascending=False)
# Select the top 5 and bottom 5 neighborhoods by average price
top_5 = sorted_avg_prices.head(5)
bottom_5 = sorted_avg_prices.tail(5)
# Combine top 5 and bottom 5 into a single DataFrame for plotting
top_bottom_5 = pd.concat([top_5, bottom_5])

# Create a bar chart
fig = px.bar(
    top_bottom_5,
    x='الحي',
    y='السعر الإجمالي',
    title="أقل وأعلى 5 أحياء بناء على متوسط أسعار الأراضي",
    labels={'الحي': 'الحي', 'السعر الإجمالي': 'متوسط السعر'},
)

# Show the chart
fig.show()