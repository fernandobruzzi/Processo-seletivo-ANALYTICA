import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica_2022.1.csv")

#1

filtro_1991 = df["ano"] == 1991
df_filtrado_1991 = df[filtro_1991]

arr_estados = np.array(df_filtrado_1991.loc[:, "sigla_uf"])
arr_pop_urb_1991 = np.array(df_filtrado_1991.loc[:, "populacao_urbana"])

plt.bar(arr_estados, arr_pop_urb_1991, width = 0.4)
plt.show()

#2

arr_idhm_1991 = np.array(df_filtrado_1991.loc[:, "idhm"])
plt.hist(arr_idhm_1991)
plt.show()

filtro_2000 = df["ano"] == 2000
df_filtrado_2000 = df[filtro_2000]
arr_idhm_2000 = np.array(df_filtrado_2000.loc[:, "idhm"])
plt.hist(arr_idhm_2000)
plt.show()

filtro_2010 = df["ano"] == 2010
df_filtrado_2010 = df[filtro_2010]
arr_idhm_2010 = np.array(df_filtrado_2010.loc[:, "idhm"])
plt.hist(arr_idhm_2010)
plt.show()

#3

arr_idhm_todos = np.array(df.loc[:, "idhm"])
arr_expc_vida_todos = np.array(df.loc[:, "expectativa_vida"])
plt.scatter(arr_idhm_todos, arr_expc_vida_todos, color = "green")
plt.show()
