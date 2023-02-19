import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


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
fig = go.Figure()
for index, row in continents_GDP.iterrows():
    fig.add_traces(go.Scatter(x=row.index, y=row.values, mode='lines', name=row.name))    
fig.update_layout(xaxis_title="Year", yaxis_title="GDP per capita")
st.plotly_chart(fig)

"""
As we can see, around 1960, GDP was almost the same in different continents. But after that, Europe and North America had a dramatic growth in 
this factor, and now are the leading continents in the world. Asia and Oceania have almost the same GDP, and as expected, Africa has the lowest GDP 
between these continents. Another interesting fact is that all continents have growed in this factor, maybe because of improving in many important world metrics.
"""