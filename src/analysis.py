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

def reservoir_simulation(df, inflows, capacity, initial_storage, demand):
    storage = []
    n_deficit_years = 0
    inflows_s = inflows * 10**-6
    for count, inflow in enumerate(inflows_s):
        if count == 0:
            st = initial_storage + inflow  - demand
        else:
            st = storage[count-1] + inflow - demand
        if st > capacity:
            st = capacity
        if st < 0:
            n_deficit_years += 1
            st = 0
        storage.append(st)
    reliability = n_deficit_years/len(df['Year'].values)
    return storage, n_deficit_years, reliability
    