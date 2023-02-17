import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components

st.header("GDP per capita for all continents")
"""
Gross Domestic Product (GDP) per capita shows a country's GDP divided by its total population.
The plot below shows this parameter for different continents in different years:
"""
GDP = st.session_state.GDP.melt(id_vars='Country Code', value_vars=set(st.session_state.GDP.columns) - set('Country Code'), var_name='Year', value_name='GDP_per_capita').sort_values('Country Code')
GDP['Year'] = pd.to_numeric(GDP['Year'], errors='coerce')
continents_GDP = st.session_state.countries.merge(GDP, how='left', left_on=['Three_Letter_Country_Code', 'Year'], right_on=['Country Code', 'Year'])[['Continent_Name', 'GDP_per_capita', 'Year']]
continents_GDP = continents_GDP[continents_GDP['GDP_per_capita'].notna()]
continents_GDP = continents_GDP.groupby(['Continent_Name', 'Year']).agg({'GDP_per_capita': np.mean})
continents_GDP = continents_GDP.pivot_table('GDP_per_capita', index='Continent_Name', columns='Year')
fig = plt.figure()
for index, row in continents_GDP.iterrows():
    plt.plot(row)
plt.xlabel('Year')
plt.ylabel('GDP per capita')
plt.legend(continents_GDP.index)
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
"""
As we can see, around 1960, GDP was almost the same in different continents. But after that, Europe and North America had a dramatic growth in 
this factor, and now are the leading continents in the world. Asia and Oceania have almost the same GDP, and as expected, Africa has the lowest GDP 
between these continents.
"""