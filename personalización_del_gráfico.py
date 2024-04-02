# -*- coding: utf-8 -*-
"""Personalización del gráfico.ipynb

"""

import matplotlib.pyplot as plt
import pandas as pd

info_pais = {"pais":["Brasil", "México", "España", "Perú", "Colombia", "Venezuela"],
             "capital":["Brasilia","Ciudad de México","Madrid","Lima","Bogotá","Caracas"],
             "superficie (Mkm2)": [8.5, 1.9, 1.2, 0.5, 1.1,0.9]}

df_pais = pd.DataFrame(info_pais)

df_pais

#Nuevo: inplace - el cambio se ejecuta en el dataframe
df_pais.sort_values("superficie (Mkm2)",ascending=False,inplace=True)

df_pais

plt.bar(df_pais["pais"],df_pais["superficie (Mkm2)"])


plt.bar(df_pais["pais"],df_pais["superficie (Mkm2)"],
        color=["green","blue","blue","blue","blue","blue"])

plt.title("¿Qué país tiene mayor superficie")
plt.xlabel("País")
plt.ylabel("Superficie (Mkm2)")
plt.legend(["País TOP 1"])

for i in range(0,6):
    plt.annotate(df_pais["superficie (Mkm2)"][i],(df_pais["pais"][i],df_pais["superficie (Mkm2)"][i]))
 
   
fig = plt.gcf()
fig.set_size_inches(10.5, 8)
plt.yticks(ticks=range(1,10,1))

#Como funciona annotate
for i in range(0,6):
    print(df_pais["superficie (Mkm2)"][i],(df_pais["pais"][i],df_pais["superficie (Mkm2)"][i]))

#qué estilos hay
plt.style.available
plt.style.use('seaborn-notebook')

#usando el estilo seleccionado
plt.bar(df_pais["pais"],df_pais["superficie (Mkm2)"],color=["green","blue","blue","blue","blue","blue"])
plt.title("¿Qué país tiene mayor superficie")
plt.xlabel("País")
plt.ylabel("Superficie (Mkm2)")
plt.legend(["País TOP 1"])
for i in range(0,6):
    plt.annotate(df_pais["superficie (Mkm2)"][i],(df_pais["pais"][i],df_pais["superficie (Mkm2)"][i]))
    
#fig = plt.gcf()
fig.set_size_inches(10.5, 8)
plt.yticks(ticks=range(1,10,1))

plt.style.use('tableau-colorblind10')
