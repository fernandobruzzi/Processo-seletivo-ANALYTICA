import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica_2022.1.csv")

filtro_1991 = df["ano"] == 1991
df_filtrado_1991 = df[filtro_1991]
arr_exp_vida_1991 = np.array(df_filtrado_1991.loc[:, "expectativa_vida"])

filtro_2010 = df["ano"] == 2010
df_filtrado_2010 = df[filtro_2010]
arr_exp_vida_2010 = np.array(df_filtrado_2010.loc[:, "expectativa_vida"])


# print(arr_exp_vida_1991,len(arr_exp_vida_1991))
diferenca_exp_vida = np.zeros(shape = (arr_exp_vida_1991.size))
for i in range(len(arr_exp_vida_1991)):
    val = arr_exp_vida_2010[i] - arr_exp_vida_1991[i]
    diferenca_exp_vida[i] = val
    
sigla_uf = np.array(df_filtrado_1991.loc[:, "sigla_uf"])
plt.bar(sigla_uf, diferenca_exp_vida, width = 0.4)
plt.show()

for i in range(len(diferenca_exp_vida)):
    if diferenca_exp_vida[i] >= 10:
        print(sigla_uf[i])
        