# -*- coding: utf-8 -*-
"""Seaborn Violinplot.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_temp = pd.read_excel(r'datasets/Temperaturas.xlsx',sheet_name="Sheet1")

df_temp.head()

df_temp["T.Promedio"]=(df_temp["T. Máxima"]+df_temp["T.Mínima"])/2

df_temp.head()

sns.boxplot(x='Ciudad', y='T.Promedio', data=df_temp)

sns.violinplot(x='Ciudad', y='T.Promedio', data=df_temp)

"""# Ejercicio"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Gráfico para visualizar la función de densidad de probabilidad de una variable y percentiles a la par

df_peatones = pd.read_csv(r'datasets/PEATONES_2020_mod.csv',encoding = "ISO-8859-1",delimiter=';')

df_peatones.head()

df_peatones.columns

sns.violinplot(data=df_peatones,y="PEATONES",x="DISTRITO")
fig = plt.gcf()
fig.set_size_inches(14, 7)

sns.boxplot(x="DISTRITO",y="PEATONES",data=df_peatones)

df_peatones[df_peatones["DISTRITO"]=="Chamberí"].groupby("HORA")["PEATONES"].agg("mean").plot()
