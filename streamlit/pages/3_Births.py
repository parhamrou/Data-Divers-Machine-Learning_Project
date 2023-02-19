import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


st.header('Births by women between 15 and 19 years old based on income level and year')
"""
Here, we want to have a look to the impact of income level on births by women between 15 and 19 years old:
"""
births = st.session_state.all_data.iloc[1155:1587][['Births by women aged 15 to 19 (thousands)','Year','Region, subregion, country or area *']].set_index('Region, subregion, country or area *')
births = births.pivot_table('Births by women aged 15 to 19 (thousands)', index='Region, subregion, country or area *', columns='Year')
fig = go.Figure()
for index, row in births.iterrows():
    fig.add_traces(go.Scatter(x=row.index, y=row.values, mode='lines', name=row.name))
fig.update_layout(xaxis_title="Year", yaxis_title="Births (thousands)")
st.plotly_chart(fig)
"""
There is substantial agreement in the literature that women who become pregnant and give birth very early in their reproductive lives are subject to higher risks of complications or even death during pregnancy and birth and their children are also more vulnerable.
Therefore, preventing births very early in a woman's life is an important measure to improve maternal health and reduce infant mortality.
Furthermore, women having children at an early age experience a curtailment of their opportunities for socio-economic improvement, particularly because young mothers are unlikely to keep on studying and, if they need to work, may find it especially difficult to combine family and work responsibilities. 
If we look at the graph, countires which have high income, have less births by women in this age range, and as the income gets lower, this factor gets high. Also, we can see that this factor is getting 
reduce with passing time.
"""

st.header('Ten countries with highest birth rate between 15 and 19 years old women')

"""
We can see which counties has the highest birth rates in women between 15 and 19 years old with this bar chart below:
"""
highest_countries = st.session_state.countries[['Region, subregion, country or area *', 'Year', 'Births by women aged 15 to 19 (thousands)']].set_index('Region, subregion, country or area *')
highest_countries = highest_countries[highest_countries['Year'].isin(list(range(2000, 2022)))]
highest_countries['Births by women aged 15 to 19 (thousands)'] = pd.to_numeric(highest_countries['Births by women aged 15 to 19 (thousands)'], errors='coerce')
highest_countries = highest_countries.groupby('Region, subregion, country or area *').agg({'Births by women aged 15 to 19 (thousands)': np.sum}).sort_values('Births by women aged 15 to 19 (thousands)', ascending=False).iloc[:10]
fig = go.Figure()
fig.add_bar(x=highest_countries.index, y=highest_countries['Births by women aged 15 to 19 (thousands)'])
fig.update_layout(yaxis_title="Births (thousands)")
st.plotly_chart(fig)
"""
As we can see, India and China as the countries with most poplulation number are in the top four countries, and that is not strange, considering that usually 
metrics get higher with poplulation growing. But with ignoring these two, most of the countries between other eight countries are not in a good situation.
They haven't good incomes, and we can expect that they have high numbers in this factor.
"""