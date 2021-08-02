import pandas as pd
import numpy as np
import os

path = "C:\\Users\\Mehdi\\OneDrive\\Documents\\Data Science\\Projects\\Data Cleaning Challenge Handling missing values\\Data"
os.chdir(path)
df1 = pd.read_csv('NFL Play by Play 2009-2017 (v4).csv')

df1.head(3)
missing_values_count = df1.isnull().sum()
missing_values_count_20col = missing_values_count[0:20]

shape_df1= df1.shape
# dropping missing values
df1.dropna()
# add data is removed!
# This is because every row in our dataset had at least one missing value.
# remove all columns with at least one missing value
columns_with_na_dropped = df1.dropna(axis=1)
columns_with_na_dropped.head()