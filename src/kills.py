import pandas as pd 
import numpy as np

#Lendo o arquivo kills.csv
file_kills_csv = "C:/Users/loran/OneDrive/Documentos/Analise_LoL/data/kills.csv"
df_kills = pd.read_csv(file_kills_csv, sep = ",")

#Analisando o dataframe kills.csv
df_kills.head() #mostra as 10 primeiras linhas do dataframe
df_kills.columns #mostra as colunas existentes no dataframe
df_kills["Team"] #"coleta" as linhas da coluna Team
df_kills.info()
df_kills.shape[0]#número de linhas 
df_kills.isna()#mostra com true/false em que linhas existem missings values


#Retirando missing values
