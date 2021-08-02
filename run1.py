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
# lost quit large number of data! at the begining 102 columns and now 41 columns
# filling in missing values
# it is good idea to see data types
df1.info()
# replace all None's with 0
df1.fillna(0)
# to test the code
missing_values_count = df1.isnull().sum()
missing_values_count_20col0 = missing_values_count[0:20]
# replace missing values with whatever value comes directly after it in the same column.
# replace all None's the value that comes directly after it in the same column
# then replace all the reamining None's with 0
df1.fillna(method='bfill', axis=0).fillna(0)
