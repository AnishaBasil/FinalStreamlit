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

def load_hospitals(allow_input_mutation=True):
    df_hospital_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return df_hospital_2
