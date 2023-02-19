import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


"""
In this page, we have a quick review on other facts that can be interesting from our data.
"""

word_da = st.session_state.all_data[st.session_state.all_data['Region, subregion, country or area *'] == 'WORLD'].set_index('Year')
columns = ['Total Population, as of 1 July (thousands)', 'Female Population, as of 1 July (thousands)', 'Male Population, as of 1 July (thousands)']
word_da[columns] = word_da[columns].apply(pd.to_numeric, errors='coerce', axis=1)

st.header('World population')
population = word_da['Total Population, as of 1 July (thousands)']
fig = go.Figure()
fig.add_traces(go.Scatter(x=population.index, y=population.values * 1000, mode='lines', name=population.name))
fig.update_layout(xaxis_title="Year", yaxis_title="Population")
st.plotly_chart(fig)
st.write('---')


st.header('Men and women population')
fig = go.Figure()
Female_Population = word_da['Female Population, as of 1 July (thousands)']
Male_Population = word_da['Male Population, as of 1 July (thousands)']
fig.add_traces(go.Scatter(x=Female_Population.index, y=Female_Population.values * 1000, mode='lines', name='Female Population, as of 1 July'))
fig.add_traces(go.Scatter(x=Male_Population.index, y=Male_Population.values * 1000, mode='lines', name='Male Population, as of 1 July'))
fig.update_layout(xaxis_title="Year", yaxis_title="Population")
st.plotly_chart(fig)

"""
As we can see, always poplulation in both sexes has been growing. It's because of improvement in health, income of countries, and other factors that 
we studied until now. Also, we can say that poplulation of women and men have been equal in most years, and also growed with a same pace.
"""
