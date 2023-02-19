import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


word_da = st.session_state.all_data[st.session_state.all_data['Region, subregion, country or area *'] == 'WORLD'].set_index('Year')
columns = ['Crude Birth Rate (births per 1,000 population)', 'Total Deaths (thousands)']
word_da[columns] = word_da[columns].apply(pd.to_numeric, errors='coerce', axis=1)

st.header('Crude birth rate')
fig = go.Figure()
Crude_Birth = word_da['Crude Birth Rate (births per 1,000 population)']
fig.add_traces(go.Scatter(x=Crude_Birth.index, y=Crude_Birth.values, mode='lines', name=Crude_Birth.name))
fig.update_layout(xaxis_title="Year", yaxis_title="Crude birth rate (per 1,000)")
st.plotly_chart(fig)
"""
As we can see, crude birth rate is falling with passing time in the workd. 
For the last 70 years, fertility rates have decreased worldwide, with a total 50% decline. 
Reasons include women's empowerment in education and the workforce, lower child mortality and the increased cost of raising children.
"""
st.write('---')

st.header('Total deaths')
fig = go.Figure()
Total_Deaths = word_da['Total Deaths (thousands)']
fig.add_traces(go.Scatter(x=Total_Deaths.index, y=Total_Deaths.values, mode='lines', name=Total_Deaths.name))
fig.update_layout(xaxis_title="Year", yaxis_title="Totla deaths (thousands)")
st.plotly_chart(fig)
"""
As wen can see, total deaths in world is growing, and it had a really fast pace after 2018. It's not hard to guess that is because of Corona vairus, which led
millions of people to die.
"""