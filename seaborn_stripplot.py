# -*- coding: utf-8 -*-
"""seaborn stripplot.py
"""

import seaborn as sns

import matplotlib.pyplot as plt

import pandas as pd

df_ext = pd.read_csv(r'datasets/temp_hum_ext.csv',encoding = "ISO-8859-1",delimiter=',')

df_ext

sns.stripplot(y='Temperatura (ºC)', data=df_ext, jitter=False)

sns.stripplot(x='Provincia', y='Temperatura (ºC)', data=df_ext, jitter=True)
plt.xlabel("Provincia")

#Gráfico para visualizar la distribución de valores de una variable