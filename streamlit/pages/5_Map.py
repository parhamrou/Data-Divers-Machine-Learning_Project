import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

countries = st.session_state.countries
map_df = countries[['Region, subregion, country or area *', 'Year', 'Life Expectancy at Birth, both sexes (years)', 'ISO3 Alpha-code']][countries['Year'].isin(list(range(2000, 2022)))]
map_df = map_df.groupby(['Region, subregion, country or area *', 'ISO3 Alpha-code']).agg({'Life Expectancy at Birth, both sexes (years)': np.mean})
map_df = map_df.reset_index(level=[0])
map_df = map_df[map_df['Life Expectancy at Birth, both sexes (years)'].notna()]

fig = px.scatter_geo(
    data_frame=map_df,
    text=map_df.index,
    locations=map_df.index, 
    locationmode='ISO-3',
    height=800,
    color_continuous_scale=px.colors.sequential.Oranges,
    color="Life Expectancy at Birth, both sexes (years)",
    fitbounds='locations',
)
st.plotly_chart(fig, use_container_width=True)