import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components

"""
In this page, we have a quick review on other facts that can be interesting from our data.
"""

word_da = st.session_state.all_data[st.session_state.all_data['Region, subregion, country or area *'] == 'WORLD'].set_index('Year')
columns = ['Total Population, as of 1 July (thousands)', 'Female Population, as of 1 July (thousands)', 'Male Population, as of 1 July (thousands)']
word_da[columns] = word_da[columns].apply(pd.to_numeric, errors='coerce', axis=1)

st.header('World population')
population = word_da['Total Population, as of 1 July (thousands)']
fig = plt.figure()
plt.plot(population) 
plt.xlabel('Year') 
plt.ylabel('Population') 
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
st.write('---')


st.header('Men and women population')
fig = plt.figure()
Female_Population = word_da['Female Population, as of 1 July (thousands)']
Male_Population = word_da['Male Population, as of 1 July (thousands)']
plt.plot(Female_Population, label="female") 
plt.plot(Male_Population, label="male") 
plt.xlabel('Year') 
plt.ylabel('Population')
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
"""
As we can see, always poplulation in both sexes has been growing. It's because of improvement in health, income of countries, and other factors that 
we studied until now.
"""
