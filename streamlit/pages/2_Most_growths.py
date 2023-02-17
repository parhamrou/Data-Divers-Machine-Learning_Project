import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components

st.header('Countries with most growth in life expectency')
"""
Here, we want to find countries with the highest amount of growth in life expectency factor between 2000 to 2021. Here is the plot:
"""
top_countries = st.session_state.pivot_countries.loc[:, [2021.0, 2000.0]]
top_countries['Most increased'] = top_countries[2021.0] - top_countries[2000.0]
top_countries = top_countries[['Most increased']].sort_values('Most increased', ascending=False).iloc[:10]
fig = plt.figure()
plt.bar(top_countries.index, top_countries['Most increased'])
plt.xlabel('Country')
plt.ylabel('Growth(Years)')
plt.xticks(range(len(top_countries.index)), top_countries.index, rotation='vertical')
st.pyplot(fig)
"""
As we can see, all of the top ten countires in this factor are from Africa. It makes sense after considering the aims from countries to afircan countries to improve 
them in health, studying, etc.
"""
st.write('---')
st.header('Relation between Life expectency and income amount')
"""
It is not that hard to guess that there is a relation between the income amount of countries and the life expectency. We can see this relationship below:
"""
incomes = st.session_state.all_data.iloc[1155: 1515,][['Year', 'Region, subregion, country or area *', 'Life Expectancy at Birth, both sexes (years)']].set_index('Region, subregion, country or area *')
incomes = incomes.pivot_table('Life Expectancy at Birth, both sexes (years)', index='Region, subregion, country or area *', columns='Year').sort_values(1950.0, ascending=False)
fig = plt.figure()
for index, row in incomes.iterrows():
    plt.plot(row)
plt.legend(incomes.index)
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
"""
As we can see, there is a direct relationship between the income amount and life expectency in the world, and it's not hard to explain why. With more income, people have more money to spend 
on their health, food, exercise, etc, and it causes them to have a longer lifetime.
"""