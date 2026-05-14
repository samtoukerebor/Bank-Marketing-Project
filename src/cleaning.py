
import pandas as pd
import numpy as np 
import seaborn as sns

df = pd.read_csv('data/raw/bank_data.csv')

def prinnt(df):
    print(df.head())
    print(df.info())
    print(df.isnull().sum())
    print(df.nunique())
    print(df.columns)
    print(df.dtypes)
    print(df.shape)
    print(df.describe())
    return

prinnt(df)  
    