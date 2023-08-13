import pandas as pd
import numpy as np

#1

df = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica_2022.1.csv")

#2

# print(df)

#3

filtro = df["ano"] == 1991
df_filtrado = df[filtro]

# print(df_filtrado.loc[:, "idhm"])
arr = np.array(df_filtrado.loc[:, "idhm"])
# print(arr)
media = arr.mean()
print(media)

#4

filtro_media_maior = df["idhm"] > media
df_filtrado_maioridhm = df[filtro_media_maior]
# print(df_filtrado_maioridhm)
arr_maior_idh = np.array(df_filtrado_maioridhm.loc[:, "sigla_uf"])
print(arr_maior_idh)

#5

df_organizado_por_idh = df.sort_values( by = ["idhm"],
               axis = 0,
               ascending = True)

# print(df_organizado_por_idh)
print(df_organizado_por_idh.head(5))

#6

maximo = df_organizado_por_idh.loc[:, "idhm"].max()
print(maximo)
minimo = df_organizado_por_idh.loc[:, "idhm"].min()
print(minimo)
indice_maximo = df["idhm"].idxmin()
print(indice_maximo)
indice_minimo = df["idhm"].idxmax()
print(indice_minimo)