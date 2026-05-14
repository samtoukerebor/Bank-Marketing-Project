
import pandas as pd
import numpy as np 
import seaborn as sns

df = pd.read_csv('data/raw/bank_data.csv')
print(df.head())
print(df.info())

df["default"] = df["default"].astype('bool')
df["housing"] = df["housing"].astype('bool')
df["loan"] = df["loan"].astype('bool')
df["deposit"] = df["deposit"].astype('bool')
df["marital"] = df["marital"].astype('category')
df["education"] = df["education"].astype('category')
df["job"] = df["job"].astype('category')
df["contact"] = df["contact"].astype('category')
df["month"] = pd.Categorical(df["month"], categories=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',   'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],ordered=True)
df["day"] = pd.Categorical(df["day"], categories=list(range(1, 32)),ordered=True)
df["poutcome"] = df["poutcome"].astype('category')

print(df.isnull().sum())
df = df.drop_duplicates()

df.to_csv('data/processed/bank_data_cleaned.csv', index=False)

