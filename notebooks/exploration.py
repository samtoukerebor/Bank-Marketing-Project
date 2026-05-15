import pandas as pd

df = pd.read_csv("Data/Raw/bank_data.csv")

print("===== APERÇU =====")
print(df.head())

print("\n===== INFOS =====")
print(df.info())

print("\n===== VALEURS MANQUANTES =====")
print(df.isna().sum().sort_values(ascending=False))

print("\n===== NOMBRE DE VALEURS UNIQUES =====")
print(df.nunique())

print("\n===== STATISTIQUES DESCRIPTIVES =====")
print(df.describe())

print("\n===== DISTRIBUTION DE LA CIBLE =====")
print(df["deposit"].value_counts())
print("\n===== POURCENTAGE =====")
print(df["deposit"].value_counts(normalize=True))
