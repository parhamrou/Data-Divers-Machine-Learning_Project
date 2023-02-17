import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def import_and_clean():
    all_data = pd.read_excel('data/WPP2022.xlsx', skiprows=16, index_col=0)
    all_data['Life Expectancy at Birth, both sexes (years)'] = pd.to_numeric(all_data['Life Expectancy at Birth, both sexes (years)'], errors='coerce')
    countries = all_data[all_data['Type'] == 'Country/Area']
    country_continent = pd.read_csv('data/country_continent.csv')
    countries = countries.merge(country_continent[['Country_Number', 'Continent_Name', 'Three_Letter_Country_Code']], how='left', left_on='Location code', right_on='Country_Number')
    st.session_state.all_data = all_data
    st.session_state.countries = countries
    GDP = pd.read_csv('data/GDP.csv', skiprows=4)
    GDP = GDP.drop(['Country Name', 'Indicator Name', 'Indicator Code'], axis=1)
    st.session_state.GDP = GDP




import_and_clean()
st.title('Life expectancy analysis')
st.write("""#### Creator: Data Divers Group""")
image = plt.imread('data/elderly-couple.jpg')
st.image(image)
"""
The term “life expectancy” refers to the number of years a person can expect to live. 
By definition, life expectancy is based on an estimate of the average age that members of a particular population group will be when they die.
Significant factors in life expectancy include gender, genetics, access to health care, hygiene, diet and nutrition, exercise, lifestyle, and crime rates. 
Evidence-based studies indicate that longevity is based on two major factors, genetics, and lifestyle choices.
In this project, we want to do analysis on life expectancy and its factors from different aspects, and get some different facts from them.   
"""
st.write('----')
st.header('Our used data')
"""
We've used a excel file that is published from United Nations, and merged that data with other different sources to have a good analysis. You can 
see our main raw data source here. Feel free to explore them: 
"""
all_data = st.session_state.all_data
st.dataframe(all_data)