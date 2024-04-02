# -*- coding: utf-8 -*-
"""Primer Ejercicio Pandas + Matplotlib

# Importación de librería
"""

import pandas as pd

"""# Lectura de datos"""

df = pd.read_csv(r"datasets/info_pais.csv",encoding = "ISO-8859-1",delimiter=';')

df.head()

"""# Manipulación de datos"""

df.sort_values("Esperanza de vida",ascending=True)

df_order = df.sort_values("Esperanza de vida",ascending=True)

df_order.head()

"""# Visualización"""

import matplotlib.pyplot as plt

#grafico1
plt.scatter(df_order["Renta per capita"],df_order["Esperanza de vida"])

#grafico2
plt.scatter(df_order["Renta per capita"],df_order["Esperanza de vida"])
plt.title("Renta per capita vs Esperanza de vida")
plt.xlabel("Renta per capita")
plt.ylabel("Esperanza de vida")

#grafico3
df_order["Pob_norm"]=df_order["Poblacion"]/max((df_order["Poblacion"]/10000))

df_order

plt.scatter(df_order["Renta per capita"],df_order["Esperanza de vida"],
            s=df_order["Pob_norm"],c=df_order["Pob_norm"])

plt.title("Renta per capita vs Esperanza de vida")
plt.xlabel("Renta per capita")
plt.ylabel("Esperanza de vida")

for i in range(1,10):
    plt.annotate(df_order["País"][i],(df_order["Renta per capita"][i],df_order["Esperanza de vida"][i]))
    
fig = plt.gcf()
fig.set_size_inches(14.5, 10)
plt.yticks(ticks=range(1,120,10))
