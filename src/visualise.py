# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:50:52 2026

@author: thoma
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

def plot_timeseries(ax, years, flow, anomaly, basin_name):
    fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(10, 13))
    ax1 = axes[ax]
    
    bar_colors = []
    for i in anomaly:
        if i > 0:
            bar_colors.append('blue')
        else:
            bar_colors.append('red')
    ax1.plot(years,flow)
    ax1.bar(years,anomaly, color = bar_colors)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Streamflow (MAF/yr)')
    ax1.set_title(basin_name)


def plot_all_basins(df, basin_info):
    for count, i in enumerate(basin_info):
        col = i 
        mean = basin_info[col]["mean"] 
        std = basin_info[col]["std"]
        years = df["Year"].values
        flow = df[col].values
        anomaly = anomaly_timeseries(df, i)
        plot_timeseries(count, years, flow, anomaly, i)
    plt.show()
    