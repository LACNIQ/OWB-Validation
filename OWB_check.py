# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:48:31 2022

@author: uth2001
"""


import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

st.title('OWB Validation')
rr01 = st.file_uploader("Upload recent RR01 report")
alloc = st.file_uploader("Upload allocation file")
if rr01 and alloc is not None:

    df = pd.read_csv(rr01)
    df1 = pd.read_csv(alloc, encoding='unicode_escape')

    df['Seq'] = df['Seq'].astype(int)
    df['LACORGSEQ'] = df['External Code'].astype(
        str)+df['Processing Group Code'].astype(str)+df['Seq'].astype(str)
    df['LACORGSEQ'] = df['LACORGSEQ'].str.replace("'", "")

    pend = df1[df1['LACORGSEQ'].isin(df['LACORGSEQ'].tolist())]

    z = pend['User Action'].value_counts()
    test = z.astype(str)
    st.dataframe(test)

    def convert_dff(dff):
        return dff.to_csv().encode('utf-8')

    df_01 = convert_dff(pend)
    st.download_button(
        label="Download Non Committed items",
        data=df_01,
        file_name='Non Committed items.csv',
        mime='text/csv')
