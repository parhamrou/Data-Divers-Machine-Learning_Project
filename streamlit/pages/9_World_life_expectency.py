import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


word_da = st.session_state.all_data[st.session_state.all_data['Region, subregion, country or area *'] == 'WORLD'].set_index('Year')
columns = ['Life Expectancy at Birth, both sexes (years)']
word_da[columns] = word_da[columns].apply(pd.to_numeric, errors='coerce', axis=1)


st.header('Life expectency at birth for both sexes')
fig = go.Figure()
Life_Expectancy_at_Birth_b = word_da['Life Expectancy at Birth, both sexes (years)']
fig.add_traces(go.Scatter(x=Life_Expectancy_at_Birth_b.index, y=Life_Expectancy_at_Birth_b.values, mode='lines', name=Life_Expectancy_at_Birth_b.name))
fig.update_layout(xaxis_title="Year", yaxis_title="Life expectency")
st.plotly_chart(fig)
st.write('---')


st.header('Life expectency at birth for both sexes change from past year')
fig = go.Figure()  
fig.add_traces(go.Scatter(x=Life_Expectancy_at_Birth_b.index, y=Life_Expectancy_at_Birth_b.diff(), mode='lines', name=Life_Expectancy_at_Birth_b.name))
fig.update_layout(xaxis_title="Year", yaxis_title="Life expectency diff")
st.plotly_chart(fig)
"""
We can see that life expectency has been growing in the world, and the diff graph says that in another way; It's always been positive values.
"""