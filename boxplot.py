# -*- coding: utf-8 -*-
"""boxplot.py
"""

import pandas as pd

import matplotlib.pyplot as plt

df_temp = pd.read_excel(r'datasets\Temperaturas.xlsx',sheet_name="Sheet1")

df_temp.head()

#Creo una variable T.Promedio 
df_temp["T.Promedio"]= (df_temp["T. Máxima"]+df_temp["T.Mínima"])/2

df_temp.head()

#Creo un boxplot de la columna T.Promedio
df_temp.boxplot(column="T.Promedio")

#Boxplot creado agrupado ciudad
df_temp.boxplot(column="T.Promedio",by="Ciudad")


"""# Ejercicio
¿Cuáles son los 2 distritos con mayor varianza en su tráfico peatonal?
¿Cuál es el distrito donde es más estable el tráfico de personas?
¿Cuál es el distrito que alcanza mayor valor de tráfico peatonal?
¿Se observan outliers en nuestros datos?

"""


import matplotlib.pyplot as plt

df_peatones = pd.read_csv(r'datasets\PEATONES_2020_mod.csv',encoding = "ISO-8859-1",delimiter=';')

df_peatones.head()

df_peatones.columns

df_peatones.boxplot(column="PEATONES",by="DISTRITO")















