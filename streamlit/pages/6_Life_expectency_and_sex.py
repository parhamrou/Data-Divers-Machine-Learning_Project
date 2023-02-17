import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components

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
fig = plt.figure()
plt.bar(ages ,men, label='Men')
plt.bar(ages, women, label='Women', bottom=men)
plt.legend()
st.pyplot(fig)