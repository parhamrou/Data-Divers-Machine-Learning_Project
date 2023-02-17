import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components

word_da = st.session_state.all_data[st.session_state.all_data['Region, subregion, country or area *'] == 'WORLD'].set_index('Year')
columns = ['Crude Birth Rate (births per 1,000 population)', 'Total Deaths (thousands)']
word_da[columns] = word_da[columns].apply(pd.to_numeric, errors='coerce', axis=1)

st.header('Crude birth rate')
fig = plt.figure()
Crude_Birth = word_da['Crude Birth Rate (births per 1,000 population)']
plt.plot(Crude_Birth)  
plt.xlabel('Year') 
plt.ylabel('Births')
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
st.write('---')

st.header('Total deaths')
fig = plt.figure()
Total_Deaths = word_da['Total Deaths (thousands)']
plt.plot(Total_Deaths)  
plt.xlabel('Year') 
plt.ylabel('Total deaths')
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)