# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:17:40 2023

@author: EZE
"""

import pandas as pd
import re

def get_cal_values (n):
    return int(str(n)[0] + str(n)[-1])

file = "input.csv"

df = pd.read_csv(file, header=None) #there is no header
#print(df)
#print(type(df))
#print(df.columns)

df.columns = ['Strings'] 
df['Numbers'] = df['Strings'].apply(lambda x: re.sub(r'[^0-9]', '', x))  #aplico esa función lambda a todos los registros
df.Numbers = df.Numbers.astype(int)
#print(df)
df['Calibration_Values'] = df['Numbers'].apply(get_cal_values)
#print(df)
print(df['Calibration_Values'].sum())

#56465



