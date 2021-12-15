#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:18:42 2021

@author: anishabasil
"""

import pandas as pd
import plotly.express as px
import pandas as pd
import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly


hospitaldf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')

outpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')

inpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

print ('hospital_info:' , len(hospitaldf))


print ('outpatient_info:' , len(outpatientdf))


print ('inpatient_info:' , len(inpatientdf))

st.title('STREAMLIT APP DEPLOYMENT')
st.write('Welcome, *Everyone!* :sunglasses:')

def load_hospitals(allow_input_mutation=True):
    df_hospital_1 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return df_hospital_1


def load_inatpatient(allow_input_mutation=True):
    df_inpatient_1 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return df_inpatient_1


def load_outpatient(allow_input_mutation=True):
    df_outpatient_1= pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return df_outpatient_1


    
# FAKE LOADER BAR TO STIMULATE LOADING    
# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)



# Load the data:     
df_hospital_1 = load_hospitals()
df_inpatient_1 = load_inatpatient()
df_outpatient_1 = load_outpatient()

# Preview the dataframes 
st.header('Hospital Data Preview')
st.dataframe(df_hospital_1)

st.header('Outpatient Data Preview')
st.dataframe(df_outpatient_1)

st.header('Inpatient Data Preview')
st.dataframe(df_inpatient_1)


#Bar Chart
st.subheader('Hospital Type in New York')
bar1 = df_hospital_1['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)
st.caption('Acute care hospitals is the most common hospital type in New York ')

st.subheader('Visual Representation of hospital types:')
fig = px.pie(bar1, values='hospital_type', names='index')
st.plotly_chart(fig)
st.caption('Different hospital types in the New York Area above, with acute care hospitals taking a huge chunk')

#Timeliness of Care
ny_hospitals = df_hospital_1[df_hospital_1['state'] == 'NY']

nc_hospitals = df_hospital_1[df_hospital_1['state'] == 'NC']


st.subheader('NY Hospitals - Timeliness of Care')
bar2 = ny_hospitals['timeliness_of_care_national_comparison'].value_counts().reset_index()
fig2 = px.bar(bar2, x='index', y='timeliness_of_care_national_comparison')
st.plotly_chart(fig2)
st.caption('Majority of hospitals in the NY area fall below the national\
        average as it relates to timeliness of care')

st.subheader('NC Hospitals - Timeliness of Care')
bar4 = nc_hospitals['timeliness_of_care_national_comparison'].value_counts().reset_index()
fig5 = px.bar(bar4, x='index', y='timeliness_of_care_national_comparison')
st.plotly_chart(fig5)
st.caption('Based on the bar chart above, we can see the the timeliness\
           of care data for the majority of hospitals in the North Carolina area \
               is the same as the national average and a little bit below the national average')



st.markdown('1. What are the most common hospital types and where does New York rank in regards to timeliness of care?')
st.markdown('- As shown by the analysis above, the most common hospital type in NY is acute care (144 acute care hospitals).\
            In terms of ranking, most of the New York Hospitals are below national average in regards to timeliness of care')  

##INPATIENT and OUTPATIENT 
st.title('Inpatient and outpatient dataframes')
st.markdown('The dataframe displayed below is for the Inpatient facility')

st.subheader('Inpatient Facility')
bar7 = df_inpatient_1['provider_state'].value_counts().reset_index()
st.dataframe(bar7)

st.subheader('Bar Chart of Inpatient Facilities by state')
fig7 = px.bar(bar7, x='index', y='provider_state')
st.plotly_chart(fig7)


st.markdown('The dataframe displayed below is for the outpatient facility')

st.subheader('Outpatient Facility')
bar7 = df_outpatient_1['provider_state'].value_counts().reset_index()
st.dataframe(bar7)

st.subheader('Bar Chart of outpatient Facilities by state')
fig7 = px.bar(bar7, x='index', y='provider_state')
st.plotly_chart(fig7)

st.markdown('2.  Which states have the greatest number of inpatient and outpatient facilities?')
st.markdown('- As shown by the analysis above, Florida has the most inpatient facilities and Texas has the most outpatient facilities') 


##Common D/C 
st.markdown('3. What is Stony Brooks top three and bottom three inpatient DRG service?')
st.markdown('- As shown by the analysis above, the top 3 are heart transplant, ecmo, and t rach\
            while the bottom 3 are trauma related, hiv related conditions') 


common_discharges = df_inpatient_1.groupby('drg_definition')['total_discharges'].sum().reset_index()


top10 = common_discharges.head(10)
bottom10 = common_discharges.tail(10)



st.subheader('DRGs')
st.dataframe(common_discharges)


col1, col2 = st.columns(2)

col1.subheader('Top 10 DRGs')
col1.dataframe(top10)

col2.subheader('Bottom 10 DRGs')
col2.dataframe(bottom10)

    

           



















