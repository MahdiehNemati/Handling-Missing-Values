import pandas as pd
import numpy as np
import os

path = "C:\\Users\\Mehdi\\OneDrive\\Documents\\Data Science\\Projects\\Data Cleaning Challenge Handling missing values\\Data"
os.chdir(path)

df = pd.read_csv('Building_Permits.csv')

df.head(3)
shape = df.shape
info = df.info()
describe = df.describe()

# handling error: "DtypeWarning: Columns (22,32) have mixed types.Specify dtype option on import or set low_memory=False."
columns = df.columns

df["Voluntary Soft-Story Retrofit"].value_counts()
df["TIDF Compliance"].value_counts()
df["Voluntary Soft-Story Retrofit"].isnull().sum()
df["TIDF Compliance"].isnull().sum()

# because the none values are many in two coloumns of Voluntary Soft-Story Retrofit and TIDF Compliance, it is better to be deleted!
df1=df.drop(["Voluntary Soft-Story Retrofit", "TIDF Compliance"], axis=1)

# lets explore column 'Filed Date' with 0 missing values
Filled_Date = df1['Filed Date']
pd.to_datetime(df1['Filed Date'])




