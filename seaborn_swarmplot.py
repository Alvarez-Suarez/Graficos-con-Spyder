# -*- coding: utf-8 -*-
"""Seaborn swarmplot.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_ext = pd.read_csv(r'datasets/temp_hum_ext.csv',encoding = "ISO-8859-1",delimiter=',')

df_ext


#Gráfico para visualizar la concentración de valores de una variable.

sns.swarmplot(x='Provincia', y='Velocidad del viento (km/h)', data=df_ext)
plt.xlabel("Provincia")

sns.swarmplot(x='Provincia', y='Velocidad del viento (km/h)', data=df_ext, hue="Dirección del viento")
plt.xlabel("Provincia")
plt.legend(loc="upper right")
fig = plt.gcf()
fig.set_size_inches(10.5, 7)

