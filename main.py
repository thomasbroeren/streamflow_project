# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:51:19 2026

@author: thoma
"""

basin_info = {
    'Upper_Colorado_Basin':{'name': 'Colorado river', 'units': 'MAF/yr'},
    "Gunnison_Basin": {"name": "Gunnison River", 'units': 'MAF/yr'},
    'Yampa_Basin': {"name": "Yampa River", 'units': 'MAF/yr'},
    'White_Basin':{'name': 'White river', 'units': 'MAF/yr'},
    'South_West_Basin':{'name': 'South west river', 'units': 'MAF/yr'}}

for i in basin_info:
    print(basin_info[i])

df = load_streamflow('C:/Users/thoma/OneDrive/Documenten/Studie/Earthmod/streamflow_project/data/AnnualStreamflow.csv')

for i in basin_info:
    data = basin_stats(df, i)
    basin_info[i]['mean'] = data['mean']
    basin_info[i]['std'] = data['std']
    basin_info[i]['min'] = data['min']
    basin_info[i]['max'] = data['max']
    
col = "Gunnison_Basin" 
mean = basin_info[col]["mean"] 
std = basin_info[col]["std"]
years = df["Year"].values
flows = df[col].values
labels = [classify_year(f, mean, std) for f in flows] 
for yr, lab in zip(years, labels): 
    print(f"{yr}: {lab}")
    
anomaly = anomaly_timeseries(df, 'Yampa_Basin')
flow = df['Yampa_Basin'].values

plot_all_basins(df, basin_info)

storage, n_deficit_years, reliability = reservoir_simulation(df, inflows = df['Gunnison_Basin'].values, capacity = 5, initial_storage = 2.5, demand = 3)

print('The number of deficit years is',n_deficit_years, 'and the reliability is', reliability)

plot_reservoir(0, years, storage, 5)