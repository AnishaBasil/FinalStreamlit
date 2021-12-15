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

@st.cache
def load_hospitals():
    hospital_info = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return hospital_info

@st.cache
def load_outpatient():
    outpatient2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return outpatient2015

@st.cache
def load_inpatient():
    inpatient2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return inpatient2015


    
# FAKE LOADER BAR TO STIMULATE LOADING    
# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)



# Load the data:     
hospital_info = load_hospitals()
outpatient2015 = load_outpatient()
inpatient2015 = load_inpatient()


# Preview the dataframes 
st.header('Hospital Data Preview')
st.dataframe(hospital_info)

st.header('Outpatient Data Preview')
st.dataframe(outpatient2015)

st.header('Inpatient Data Preview')
st.dataframe(inpatient2015)

# Merging Datasets 
st.header('Hospital/Outpatient Merged Data')
df_merge_outpt = df_outpatient.merge(df_hospital, how = 'left', left_on = 'provider_id', right_on = 'provider_id')
st.dataframe(df_merge_outpt)

st.header('Hospital/Inpatient Merged Data')
df_merge_inpt = df_inpatient.merge(df_hospital, how = 'left', left_on = 'provider_id', right_on = 'provider_id')
st.dataframe(df_merge_outpt)

st.header('DRGs')
st.dataframe(common_discharges)

col1, col2 = st.beta_columns(2)

col1.header('Top 10 DRGs')
col1.dataframe(top10)

col2.header('Bottom 10 DRGs')
col2.dataframe(bottom10)

#Bar Charts of the costs 

costs = inpatient_ny.groupby('provider_name')['avsterage_total_payments'].sum().reset_index()
costs['average_total_payments'] = costs['average_total_payments'].astype('int64')


costs_medicare = inpatient_ny.groupby('provider_name')['average_medicare_payments'].sum().reset_index()
costs_medicare['average_medicare_payments'] = costs_medicare['average_medicare_payments'].astype('int64')


costs_sum = costs.merge(costs_medicare, how='left', left_on='provider_name', right_on='provider_name')
costs_sum['delta'] = costs_sum['average_total_payments'] - costs_sum['average_medicare_payments']


st.title('COSTS')

bar3 = px.bar(costs_sum, x='provider_name', y='average_total_payments')
st.plotly_chart(bar3)
st.header("Hospital - ")
st.dataframe(costs_sum)


#Costs by Condition and Hospital / Average Total Payments
costs_condition_hospital = inpatient_ny.groupby(['provider_name', 'drg_definition'])['average_total_payments'].sum().reset_index()
st.header("Costs by Condition and Hospital - Average Total Payments")
st.dataframe(costs_condition_hospital)



































