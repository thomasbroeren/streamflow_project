# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:50:52 2026

@author: thoma
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


def plot_timeseries(ax_obj, years, flow, anomaly, basin_name):
    # Verwijder fig, axes = plt.subplots hier
    bar_colors = []
    for i in anomaly:
        if i > 0:
            bar_colors.append('blue')
        else:
            bar_colors.append('red')
    
    ax_obj.plot(years, flow)
    ax_obj.bar(years, anomaly, color=bar_colors)
    ax_obj.set_xlabel('Year')
    ax_obj.set_ylabel('Streamflow (MAF/yr)')
    ax_obj.set_title(basin_name)

def plot_all_basins(df, basin_info):
    # Maak de subplots hier éénmalig aan
    fig, axes = plt.subplots(nrows=len(basin_info), ncols=1, figsize=(10, 13))
    
    for count, i in enumerate(basin_info):
        col = i 
        years = df["Year"].values
        flow = df[col].values
        anomaly = anomaly_timeseries(df, i)
        plot_timeseries(axes[count], years, flow, anomaly, i)
    
    plt.tight_layout()
    plt.show()
    plt.savefig('streamflow_timeseries.png')


def plot_reservoir(ax, years, storage, capacity):
    plt.fill_between(years,storage)
    z_years = []
    z_storage = []
    for i,j in zip(years,storage):
        if j == 0:
            z_years.append(i)
            z_storage.append(j)
    arr = np.full(len(years),capacity)
    plt.fill_between(years, 0, capacity, where=(np.array(storage) <= 0), color='red', alpha=0.3)
    arr = np.full(len(years),capacity)
    plt.plot(years,arr,linestyle='dashed')
    plt.xlabel('year')
    plt.ylabel('Storage (MAF/yr)')
    plt.title('Water storage in the basin')
    plt.savefig('reservoir_simulation.png')

