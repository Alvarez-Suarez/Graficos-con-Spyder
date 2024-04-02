# -*- coding: utf-8 -*-
"""Plot objeto groupby.py
"""

import pandas as pd
import matplotlib.pyplot as plt

df_ventas = pd.read_csv(r'datasets/Ventas.csv',encoding = "ISO-8859-1",delimiter=';')
df_ventas

#ver que columnas hay
df_ventas.columns

#vemos los tipos de datos de las columnas
df_ventas.dtypes

#Si trato de convertir una varialble Object(texto) a numérica
df_ventas["Total Venta"]= pd.to_numeric(df_ventas["Total Venta"])
df_ventas["Total Venta"]= pd.to_numeric(df_ventas["Precio Unitario"])


#aplico una función lambda
df_ventas["Total Venta"]=df_ventas["Total Venta"].apply(lambda x:x.replace(",","."))

df_ventas["Total Venta"]

df_ventas["Precio Unitario"]=df_ventas["Precio Unitario"].apply(lambda x:x.replace(",","."))

df_ventas["Precio Unitario"]

#https://recursospython.com/guias-y-manuales/funciones-lambda/

df_ventas

#Convierto variables texto numéricas
df_ventas["Total Venta"]=pd.to_numeric(df_ventas["Total Venta"])
df_ventas["Precio Unitario"]=pd.to_numeric(df_ventas["Precio Unitario"])

df_ventas

df_ventas.dtypes

#quiero el total de la venta por territoria v.1
df_ventas.groupby(["Territorio"]).agg('sum')

#quiero el total de la venta por territoria v.2
df_ventas.groupby(["Territorio"])["Total Venta"].agg('sum')

df_ventas.groupby(["Territorio"])["Unidades"].agg('sum')

#quiero el total de la venta por territoria v.3
df_ventas.groupby(["Territorio"])["Total Venta"].agg('sum').plot(kind="bar")

#quiero el total de la venta por territoria y línea de producto
df_ventas.groupby(["Territorio","Línea de Producto"])["Total Venta"].agg('sum').plot(kind="bar")

df_ventas.groupby(["Territorio","Línea de Producto"])["Total Venta"].agg('sum')

"""# Ejercicio"""

df_peatones = pd.read_csv(r'datasets/PEATONES_2020_mod.csv',encoding = "ISO-8859-1",delimiter=';')

df_peatones.head()

df_peatones.columns

df_peatones.dtypes

#¿cuál es la combinación distrito-nombre_vial que tiene en promedio un tráfico peatonal superior?

#Tomando como referencia el distrito Centro, ¿cuál es la evolución tanto del mínimo como del
#máximo de tráfico de peatones diario?


df_peatones.groupby(["DISTRITO","NOMBRE_VIAL"])["PEATONES"].agg("mean").plot(kind="bar")


#Como filtro los registros de un dataframe
df_peatones[df_peatones["DISTRITO"]=="Centro"]

#filtro -> agrego -> grafico
df_peatones[df_peatones["DISTRITO"]=="Centro"].groupby(["FECHA"])["PEATONES"].agg(["min","max"]).plot()

fig=plt.gcf()
fig.set_size_inches(15,8)
plt.plot(df_peatones[df_peatones["DISTRITO"]=="Centro"].groupby(["FECHA"])["PEATONES"].agg(["min","max"]))
plt.xticks(ticks=["01/01/2020","15/01/2020","31/01/2020"])

#Poner titulos al los ejes y al gráfico