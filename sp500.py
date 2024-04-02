# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:56:38 2024

@author: Administrador
"""

import pandas as pd

#df = pd.read_csv("datasets/sp500_data.csv")

df = pd.read_csv(r'datasets/sp500_data.csv',encoding = "ISO-8859-1",delimiter=',')

print(df)

#veo las columnas
df.columns

df["Close"].plot()

print(df)

#cambio el valor del indice por la fecha
df.index = df["Date"]

print(df)

#Visualizar la evolucion de la cotizacion en bolsa

df["Close"].plot()

df["Open"].plot()

