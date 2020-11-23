# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:34:06 2020

@author: Nelson J Hwu
"""

import pandas as pd
import numpy as np
import datetime as dt
import re

og_data = pd.read_csv('StockX-Data-Contest-2019-3.csv')
df = og_data.copy()

df.columns
df.shape
df.dtypes
df.describe()

# Checking for null values
nulls = pd.concat([df.isnull().sum()], axis=1)
nulls[nulls.sum(axis=1) > 0]

#Change 'order date' dtype
df['Order Date'] = pd.to_datetime(df['Order Date'], format = '%m/%d/%Y').dt.date
df.head()

# Change 'release date' dtype
df['Release Date'] = pd.to_datetime(df['Release Date'], format = '%m/%d/%Y').dt.date
df.head()

df['Days After Release'] = df['Order Date'] - df['Release Date']
df['Days After Release'] = df['Days After Release'] / np.timedelta64(1, 'D')

# Remove $ and comma from sale price
df['Sale Price'] = df['Sale Price'].apply(lambda x: x.replace('$', '').replace(',', ''))

# Remove $ and comma from retail price
df['Retail Price'] = df['Retail Price'].apply(lambda x: x.replace('$', '').replace(',', ''))

# Convert price object columns into numerical columns
obj_cols = ['Sale Price', 'Retail Price']
for col in obj_cols:
    df[str(col)] = pd.to_numeric(df[str(col)])

# Remove '-' from sneaker name
df['Sneaker Name'] = df['Sneaker Name'].apply(lambda x: x.replace('-', ' '))

# Attempt to run through for loop to isolate colors
# # Isolate Colors
# shoe_name = df['Sneaker Name']
# shoe_obj = enumerate(shoe_name)

# for index,shoe in shoe_obj:
#     colors = []
#     colors = re.findall( r'Black|White|Red|Orange|Yellow|Green|Blue|Purple', shoe)
#     for i in range(len(colors)):
#         df.at[index,"color"+str(i)] = colors[i]
        
df.to_csv('sneaker_data_cleaned.csv', index = False)
