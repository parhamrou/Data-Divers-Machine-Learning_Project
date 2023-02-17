import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components

st.header('Births by women between 15 and 19 years old based on income level and year')
"""
Here, we want to have a look to the impact of income level on births by women between 15 and 19 years old:
"""
births = st.session_state.all_data.iloc[1155:1587][['Births by women aged 15 to 19 (thousands)','Year','Region, subregion, country or area *']].set_index('Region, subregion, country or area *')
births = births.pivot_table('Births by women aged 15 to 19 (thousands)', index='Region, subregion, country or area *', columns='Year')
fig = plt.figure()
for index, row in births.iterrows():
    plt.plot(row)
plt.xlabel('Year')
plt.ylabel('Births')
plt.legend(births.index, loc='upper left')
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
st.header('Ten countries with highest birth rate between 15 and 19 years old women')
"""
We can see which counties has the highest birth rates in women between 15 and 19 years old with this bar chart below:
"""
highest_countries = st.session_state.countries[['Region, subregion, country or area *', 'Year', 'Births by women aged 15 to 19 (thousands)']].set_index('Region, subregion, country or area *')
highest_countries = highest_countries[highest_countries['Year'].isin(list(range(2000, 2022)))]
highest_countries['Births by women aged 15 to 19 (thousands)'] = pd.to_numeric(highest_countries['Births by women aged 15 to 19 (thousands)'], errors='coerce')
highest_countries = highest_countries.groupby('Region, subregion, country or area *').agg({'Births by women aged 15 to 19 (thousands)': np.sum}).sort_values('Births by women aged 15 to 19 (thousands)', ascending=False).iloc[:10]
fig = plt.figure()
plt.bar(highest_countries.index, highest_countries['Births by women aged 15 to 19 (thousands)'])
plt.xlabel('Country')
plt.ylabel('Births')
plt.xticks(range(len(highest_countries.index)), highest_countries.index, rotation='vertical')
st.pyplot(fig)