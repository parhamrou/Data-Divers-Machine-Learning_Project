import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components


st.title("Life expectancy in countries and continents")
"""
Here, we want to compare life expectancy in different continents and countries, and have a simple analysis on them.
Below, You can see life expectancy for different continents from 1950 until 2021:
"""
countries = st.session_state.countries
grouped_countries = countries.groupby(['Continent_Name', 'Year']).agg({'Life Expectancy at Birth, both sexes (years)': 'mean'})
grouped_countries = grouped_countries.pivot_table('Life Expectancy at Birth, both sexes (years)', index='Continent_Name', columns='Year')
colors = ['orange', 'yellow', 'blue', 'green', 'red', 'purple']
fig = plt.figure()
for idx, row in grouped_countries.iterrows():
    plt.plot(row)
plt.legend(grouped_countries.index)
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
"""
As we can see, all the continents had growth over time. Betwee the six continents, Europe has the highest life expectency, but 
other countries except Africa are also close to that. It is interesting that if we notice, we can see a decrease for all continents in the last 
2-3 years. Maybe we can consider that because of Corona virus. 
"""
st.write('----')
# Here, we have to have a plot for countries in different continents.
pivot_countries = countries[['Region, subregion, country or area *' , 'Year', 'Life Expectancy at Birth, both sexes (years)', 'Continent_Name']]
pivot_countries = pivot_countries.pivot_table('Life Expectancy at Birth, both sexes (years)', index=['Region, subregion, country or area *', 'Continent_Name'], columns='Year').reset_index(level=[1])
st.session_state.pivot_countries = pivot_countries
fig = plt.figure()
choice1 = st.selectbox('Graph on:', ['Countries', 'Continents'])
if choice1 == 'Continents':
    selected = st.selectbox('Select continent:', pivot_countries['Continent_Name'].unique())
    continent = pivot_countries[pivot_countries['Continent_Name'] == selected].drop('Continent_Name', axis=1)
    for index, row in continent.iterrows():
        plt.plot(row)
    plt.legend(continent.index)
else:
    selected = st.multiselect('Select Countries:', pivot_countries.index)
    COUNTRIES = pivot_countries.loc[selected].drop('Continent_Name', axis=1)
    for index, row in COUNTRIES.iterrows():
        plt.plot(row)
    plt.legend(selected)
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)