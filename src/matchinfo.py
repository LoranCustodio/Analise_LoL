import pandas as pd 
import numpy as np

#Lendo o arquivo kills.csv
file_matchinfo_csv = "D:\Analise_LoL\data\matchinfo.csv"
df_matchinfo = pd.read_csv(file_matchinfo_csv, sep = ",")
df_matchinfo.head()
df_matchinfo.isnull().sum()
match_info = df_matchinfo.drop(columns=["Address"])