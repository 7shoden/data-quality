"""Exploration simple. On conserve toutes les chaînes originales."""
from pathlib import Path
import pandas as pd

path = Path(__file__).resolve().parents[1] / "data/demo/toy10.csv"
df = pd.read_csv(path, dtype=str, keep_default_na=False)
print(df.head())
print("Dimensions :", df.shape)
age_num = pd.to_numeric(df["age"], errors="coerce")
print("À vérifier :")
print(df.loc[age_num.isna() | ~age_num.between(0, 120)])
print("Le premier code postal reste :", df.loc[0, "code_postal"])
