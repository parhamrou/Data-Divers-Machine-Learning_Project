import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components


word_da = st.session_state.all_data[st.session_state.all_data['Region, subregion, country or area *'] == 'WORLD'].set_index('Year')
columns = ['Life Expectancy at Birth, both sexes (years)']
word_da[columns] = word_da[columns].apply(pd.to_numeric, errors='coerce', axis=1)


st.header('Life expectency at birth for both sexes')
fig = plt.figure()
Life_Expectancy_at_Birth_b = word_da['Life Expectancy at Birth, both sexes (years)']
plt.plot(Life_Expectancy_at_Birth_b)  
plt.xlabel('Year') 
plt.ylabel('Life expectency')
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
st.write('---')


st.header('Life expectency at birth for both sexes change from past year')
fig = plt.figure()
plt.plot(Life_Expectancy_at_Birth_b.diff())  
plt.xlabel('Year') 
plt.ylabel('Change')
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)