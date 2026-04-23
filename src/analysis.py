# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:50:24 2026

@author: thoma
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

def load_streamflow(filepath):
    '''This function takes a filepath and loads the file. it returns the dataframe'''
    df = pd.read_csv(filepath)
    print(df.describe())
    return df


def basin_stats(df, column):
    x = df[column].values
    mean = np.mean(x)
    Max = np.max(x)
    Min = np.min(x)
    std = np.std(x)
    data = {'mean':mean,'std':std,'max':Max,'min':Min}
    return data

def classify_year(flow, mean, std):
    if flow < (mean-std):
        year = 'dry'
    elif flow > (mean+std):
        year = 'wet'
    else:
        year = 'normal'
    return year

def anomaly_timeseries(df, column):
    strmflw = df[column].values
    anomaly = strmflw - np.mean(strmflw)
    return anomaly
    