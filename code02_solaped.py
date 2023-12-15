# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:31:46 2023

@author: EZE
"""

import pandas as pd
import re

def str_to_numbers(s):
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,n in enumerate(numbers):
        while n in s:
            s = s[:s.find(n)+1] + str(i) + n[-1:] + s[s.find(n)+len(n):]
    return s
            
    
def get_cal_values (n):
    return int(str(n)[0] + str(n)[-1])

file = "input.csv"

df = pd.read_csv(file, header=None) #there is no header
#print(df)
#print(type(df))
#print(df.columns)

#data = {'columna1': ['pcg91vqrfpxxzzzoneightzt']}
#df = pd.DataFrame(data)

df.columns = ['Strings']
df['String_converted'] = df['Strings'].apply(str_to_numbers)
#print(df)
df['Numbers'] = df['String_converted'].apply(lambda x: re.sub(r'[^0-9]', '', x))  #aplico esa función lambda a todos los registros
df.Numbers = df.Numbers.astype(int)
#print(df)
df['Calibration_Values'] = df['Numbers'].apply(get_cal_values)
#print(df)
print(df['Calibration_Values'].sum())