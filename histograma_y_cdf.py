# -*- coding: utf-8 -*-
"""
Histograma y CDF.py

"""

import pandas as pd

import matplotlib.pyplot as plt

df_temp = pd.read_excel(r'datasets\Temperaturas.xlsx',sheet_name="Sheet1")

df_temp

#calculo el promedio de temperatura por registro
df_temp["T.Promedio"]= (df_temp["T. Máxima"]+df_temp["T.Mínima"])/2

df_temp

#Histograma
plt.hist(df_temp["T.Promedio"],bins=50)
plt.title("¿Cuál es la distribución de temperatura?")

#Cambio el número de bins
plt.hist(df_temp["T.Promedio"],bins=10)
plt.title("¿Cuál es la distribución de temperatura?")

#Frecuencia acumulada
plt.hist(df_temp["T.Promedio"],bins=50,cumulative=True,density=True)
plt.title("¿Cuál es la CDF de la temperatura?")