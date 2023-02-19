import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


st.header("Life expectency based on sex")
"""
Here, we want to compare life expectency for women and men, and see are they different or not. Life expectency is measured in three ages: birth, 15, 65 and 80.
We want to compare men and women life expectency in each one. Here is our graph:
"""

df = st.session_state.all_data[st.session_state.all_data['Region, subregion, country or area *'] == 'WORLD']
columns = ['Year' ,'Male Life Expectancy at Age 15 (years)', 'Female Life Expectancy at Age 15 (years)', 'Male Life Expectancy at Age 65 (years)', 'Female Life Expectancy at Age 65 (years)', 'Male Life Expectancy at Age 80 (years)', 'Female Life Expectancy at Age 80 (years)']
df = df[columns]
df[columns] = df[columns].apply(pd.to_numeric, errors='coerce', axis=1)
ages=['At 15', 'At 65', 'At 80']
men = df[['Male Life Expectancy at Age 15 (years)', 'Male Life Expectancy at Age 65 (years)', 'Male Life Expectancy at Age 80 (years)']].mean()
women = df[['Female Life Expectancy at Age 15 (years)', 'Female Life Expectancy at Age 65 (years)', 'Female Life Expectancy at Age 80 (years)']].mean()
fig = go.Figure()
fig.add_bar(name='Men' ,x=ages ,y=men)
fig.add_bar(x=ages, y=women, name='Women', base='Men')
fig.update_layout(yaxis_title="Life expectency (years)")
st.plotly_chart(fig)

"""
We usually hear that women live longer than men, and this graph shows that it is not a wrong claim. 
Biological differences help to explain women's higher longevity. Scientists believe that estrogen in women combats conditions such as heart disease by helping reduce circulatory levels of harmful cholesterol. 
Women are also thought to have stronger immune systems than men, and all of these factors cause women to have longer lives than men.
"""