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
bar1 = hospitals_info['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)

st.caption('Most of the hospitals in the New York area are acute care, followed by psychiatric')
































