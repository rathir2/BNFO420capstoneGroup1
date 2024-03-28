# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:44:56 2024

@author: rrath
"""

import pandas as pd
from pathlib import Path

AQI2019 = pd.read_csv("C:/Users/rrath/Desktop/college/spring 2024/daily_aqi_by_cbsa_2019.csv")
AQI2020 = pd.read_csv("C:/Users/rrath/Desktop/college/spring 2024/daily_aqi_by_cbsa_2020.csv")
AQI2021 = pd.read_csv("C:/Users/rrath/Desktop/college/spring 2024/daily_aqi_by_cbsa_2021.csv")
AQI2022 = pd.read_csv("C:/Users/rrath/Desktop/college/spring 2024/daily_aqi_by_cbsa_2022.csv")

stateAQIs = pd.read_excel("C:/Users/rrath/Desktop/college/spring 2024/Largest CBSAs per state.xlsx")

AQI2019 = AQI2019.drop(columns=["CBSA Code", "Category", "Defining Parameter",
                                  "Defining Site", "Number of Sites Reporting"])
AQI2020 = AQI2020.drop(columns=["CBSA Code", "Category", "Defining Parameter",
                                  "Defining Site", "Number of Sites Reporting"])
AQI2021 = AQI2021.drop(columns=["CBSA Code", "Category", "Defining Parameter",
                                  "Defining Site", "Number of Sites Reporting"])
AQI2022 = AQI2022.drop(columns=["CBSA Code", "Category", "Defining Parameter",
                                  "Defining Site", "Number of Sites Reporting"])
AQIall = pd.concat([AQI2019,AQI2020,AQI2021,AQI2022])
AQIall = AQIall.sort_values("Date")
AQIall = AQIall.sort_values("CBSA")
AQIall = AQIall.reset_index()
AQIall = AQIall.drop(columns = ["index"])

AQIfinal = pd.DataFrame()
for CBSA in stateAQIs.CBSA:
    AQItemp = AQIall[(AQIall["CBSA"] == CBSA)]
    stateindex = stateAQIs.index[(stateAQIs["CBSA"] == CBSA)].tolist()
    statetemp = []
    statetemp = [stateAQIs.State[stateAQIs['CBSA'] == CBSA].loc[stateindex[0]]] * AQItemp.shape[0]
    AQItemp.insert(1,"State", statetemp, True)
    AQItemp = AQItemp.sort_values("Date")
    AQIfinal = pd.concat([AQIfinal, AQItemp])


filepath = Path('C:/Users/rrath/Desktop/college/spring 2024/AQIfinal.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
AQIfinal.to_csv(filepath, index = False) 

