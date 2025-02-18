import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

# Load dataset
df = pd.read_csv('vehicles_us.csv')

# Data cleaning
df[['brand', 'model_name']] = df['model'].str.split(' ', n=1, expand=True)
df.drop(columns=['model'], inplace=True)
df = df.dropna(subset=['model_year', 'odometer'])
median_cylinders = round(df['cylinders'].median())
df['cylinders'] = df['cylinders'].fillna(median_cylinders)
df['paint_color'].fillna('unknown', inplace=True)
df['is_4wd'].fillna(0, inplace=True)
df['model_year'] = df['model_year'].astype('int')
df['odometer'] = df['odometer'].astype('int')
df['cylinders'] = df['cylinders'].astype('int')
df['is_4wd'] = df['is_4wd'].astype('int')
df['date_posted'] = pd.to_datetime(df['date_posted'])
df = df.reset_index(drop=True)
current_year = 2019
df['age'] = current_year - df['model_year']
df['annual_mil'] = (df['odometer'] / df['age']).round()

# Streamlit Headers and Content
st.header('Data viewer')

# Brand filtering
show_brand_1k_ads = st.checkbox('Include brands with less than 1000 ads')
if not show_brand_1k_ads:
    df = df.groupby('brand').filter(lambda x: len(x) > 1000)

st.dataframe(df)

# Vehicle types distribution by brand
st.header('Vehicle types by brand')
st.write(px.histogram(df, x='brand', color='type'))

# Condition vs Model Year Histogram
st.header('Histogram of condition vs model_year')
st.write(px.histogram(df, x='model_year', color='condition'))

# Price distribution comparison between brands
st.header('Compare price distribution between brands')
brand_list = sorted(df['brand'].unique())
brand_1 = st.selectbox('Select brand 1', brand_list, index=brand_list.index('chevrolet'))
brand_2 = st.selectbox('Select brand 2', brand_list, index=brand_list.index('ford'))
mask_filter = (df['brand'] == brand_1) | (df['brand'] == brand_2)
df_filtered = df[mask_filter]
normalize = st.checkbox('Normalize histogram', value=True)
histnorm = 'percent' if normalize else None
st.write(px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='brand',
                      histnorm=histnorm,
                      barmode='overlay'))

# Vehicle Price Distribution by Model Year and Brand
st.header('Vehicle Price Distribution by Model Year and Brand')

# Brand filter (multiselect)
brand_filter = st.multiselect('Select Brands to View', df['brand'].unique(), default=df['brand'].unique(), key="brand_filter_1")

# Year filter (select box for 5-year intervals)
year_min = int(df['model_year'].min())
year_max = int(df['model_year'].max())
year_range = st.selectbox('Select Year Range',
                          [f'{year}-{year+5}' for year in range(year_min, year_max, 5)],
                          index=0)
start_year, end_year = map(int, year_range.split('-'))

# Filter data based on selected brands and year range
df_filtered = df[df['brand'].isin(brand_filter)]
df_filtered = df_filtered[(df_filtered['model_year'] >= start_year) & (df_filtered['model_year'] <= end_year)]

# Histogram showing median price distribution
fig9 = px.histogram(df_filtered, 
                    x='model_year', 
                    y='price', 
                    color='brand', 
                    histfunc='avg', 
                    title=f'Median Price Distribution by Model Year and Brand ({start_year}-{end_year})')

# Display the figure
st.plotly_chart(fig9)

# Vehicle Days Listed by Brand
st.header('Vehicle Days Listed by Brand')

# Brand filter (multiselect)
brand_filter_2 = st.multiselect('Select Brands to View', df['brand'].unique(), default=df['brand'].unique(), key="brand_filter_2")

# Filter data based on selected brands
df_filtered = df[df['brand'].isin(brand_filter_2)]

# Box plot for 'days_listed' vs 'brand'
fig5 = px.box(df_filtered, x='days_listed', color='brand', color_discrete_sequence=px.colors.qualitative.Set1)

# Display the figure
st.plotly_chart(fig5)

# Vehicle Age and Condition by Brand
st.header('Vehicle Age and Condition by Brand')

# Brand filter (multiselect)
brand_filter_3 = st.multiselect('Select Brands to View', df['brand'].unique(), default=df['brand'].unique(), key="brand_filter_3")

# Filter data based on selected brands
df_filtered = df[df['brand'].isin(brand_filter_3)]

# Box plot for 'age' vs 'condition', colored by 'brand'
fig3 = px.box(df_filtered, x='condition', y='age', color='brand', color_discrete_sequence=px.colors.qualitative.Set1)

# Display the figure
st.plotly_chart(fig3)

# Price vs Odometer by Brand
st.title('Price vs Odometer by Brand')

# Checkbox to toggle scatter plot visibility
show_scatter = st.checkbox('Show Scatter Plot: Price vs Odometer')

# Brand filter (multiselect)
brand_filter_4 = st.multiselect(
    'Select Brands to View',
    df['brand'].unique(),
    default=df['brand'].unique(),  # Default selects all brands
    key="brand_filter_4"
)

# Filter the DataFrame based on selected brands
df_filtered = df[df['brand'].isin(brand_filter_4)]

# If checkbox is checked, show the scatter plot
if show_scatter:
    fig = px.scatter(df_filtered, x='odometer', y='price', color='brand', title='Vehicle Price vs Odometer by Brand')
    st.plotly_chart(fig)
    
