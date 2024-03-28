# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import stats

#read 
lockdown_data = pd.read_excel("C:/Users/rrath/Desktop/college/spring 2023/OxCGRT_US_latest_full.xlsx")

AQ_poop_data = pd.read_csv("C:/Users/rrath/Desktop/college/spring 2023/NewJeresyAirQualityIndex.csv")

lockdown_data = lockdown_data.drop(columns=["RegionCode", "Jurisdiction", "ConfirmedCases",
                                  "ConfirmedDeaths", "StringencyLegacyIndex", "GovernmentResponseIndex",
                                  "ContainmentHealthIndex", "EconomicSupportIndex"])

AQ_data = AQ_poop_data.drop(columns=["Unnamed: 0", "CBSA", "CBSA Code",
                                  "Category", "Defining Parameter", "Defining Site",
                                  "Number of Sites Reporting"])

NJ_data = lockdown_data[(lockdown_data['RegionName'] == 'New Jersey')]
NJ_data = NJ_data.reset_index()
for ind in NJ_data.index:
    
    NJ_data["Date"][ind] = datetime.fromisoformat(str(NJ_data["Date"][ind]))



NJ_AQ_lockdown_Spearman_data = pd.DataFrame(columns = ["Stringency Index", "AQI"])
NJ_stripped_data = []
for ind in AQ_data.index:
    NJ_stripped_data.append(NJ_data["StringencyIndex"][ind])
    
plt.scatter(AQ_data["Date"], NJ_stripped_data, s = 1)
plt.scatter(AQ_data["Date"], AQ_data["AQI"], s = 1)
plt.show()

res = stats.spearmanr(NJ_stripped_data, AQ_data["AQI"], axis = 0, nan_policy = "omit", 
                      alternative = "two-sided")
res.statistic
