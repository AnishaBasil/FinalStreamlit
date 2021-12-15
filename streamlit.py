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

#LOADER BAR TO STIMULATE LOADING    
my_bar = st.progress(0)
for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)