# -*- coding: utf-8 -*-
"""Seaborn Regresión lineal.py


# **Precio de las casa**
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_casas = pd.read_excel("datasets/casas.xlsx")

df_casas

df_casas.dtypes

plt.scatter(df_casas["superficie"],df_casas["valor"])

sns.regplot(data=df_casas, x="superficie", y="valor",scatter=True, color='blue', order=1, label="Orden 1")

from scipy import stats

pendiente, intercepto, r_value, p_value, std_err = stats.linregress(df_casas["superficie"],df_casas["valor"])

sns.regplot(data=df_casas, x="superficie", y="valor", scatter=True, order=1,
            color='blue',line_kws={'label':"y={0:.1f}x+{1:.1f}".format(pendiente,intercepto)})
plt.legend()

#Cuanto valdría una casa de x m2

x = 200
y = 1159.6*x + 76657.7
y


""" **Más información**
https://seaborn.pydata.org/tutorial/regression.html 

https://seaborn.pydata.org/generated/seaborn.regplot.html

"""

"""# Ejercicio"""

df_act = pd.read_excel(r'datasets/Datos población activa.xlsx',sheet_name="Total Histórico")

df_act.head()

#Crear una regresión lineal de orden 1 con eje x “Periodo num_int” / eje y “Total Activos.

sns.regplot(data=df_act, x="Periodo num_int", y="Total Activos",scatter=True, color='blue', label='order 1')

#Añadir la fórmula de la ecuación de esta regresión.

pendiente, intercepto, r_value, p_value, std_err = stats.linregress(df_act["Periodo num_int"],df_act["Total Activos"])

sns.regplot(data=df_act, x="Periodo num_int", y="Total Activos", scatter=True, order=1, color='blue', label='order 1',line_kws={'label':"y={0:.1f}x+{1:.1f}".format(pendiente,intercepto)})
plt.legend()

#¿cuál sería el número de personas activas estimadas en 202201 (1er trimestre de 2022)

y_202201 = 1.8*202201-340650.1

y_202201

