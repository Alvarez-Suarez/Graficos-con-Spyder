# -*- coding: utf-8 -*-
"""Plots línea, scatter, bar.py

"""

import matplotlib.pyplot as plt

import pandas as pd

info_pais = {"pais":["Brasil", "México", "España", "Perú", "Colombia", "Venezuela"],
             "capital":["Brasilia","Ciudad de México","Madrid","Lima","Bogotá","Caracas"],
             "superficie (Mkm2)": [8.5, 1.9, 1.2, 0.5, 1.1,0.9]}

info_pais

df_pais = pd.DataFrame(info_pais)

df_pais

plt.bar(df_pais["pais"],df_pais["superficie (Mkm2)"])

info_poblacion = {"pais":["Perú", "Colombia","Brasil", "México", "España","EEUU","China"],
             "población":[32.6,50.3,211.4,127.8,47,331.8,1393]}

info_poblacion

df_poblacion = pd.DataFrame(info_poblacion)

df_poblacion

df_total_in = df_pais.merge(df_poblacion, on="pais", how="inner")

df_total_in


plt.scatter(df_total_in["superficie (Mkm2)"],
            df_total_in["poblacion"])

"""# Ejercicio"""

df_traf_dis = pd.read_excel(r'datasets/PEATONES_2020_resumen.xlsx',sheet_name="Tráfico medio peatones")


df_traf_dis

#¿Cuál es el barrio con mayor tráfico peatonal?
plt.style.use('classic')

plt.bar(df_traf_dis["DISTRITO"],df_traf_dis["Tráfico medio peatones"])

#Poner etiqueta a los ejes x y 
#Poner título al gráfico
#plt.title("xxx")
#plt.xlabel("xx")
#plt.ylabel("xxx")

"""
Cuál es la tendencia de tráfico en cada barrio? 
¿Está aumentando o disminuyendo el tráfico peatonal? 
(recomendación: usar df_evo.plot() convirtiendo “Fecha” en índice y 
eliminando la columna “Fecha” posteriormente)
"""
df_evo = pd.read_excel(r'datasets/PEATONES_2020_resumen.xlsx',sheet_name="Evolución tráfico por distrito")

df_evo

plt.plot(df_evo["Fecha"],df_evo["Arganzuela"])
plt.plot(df_evo["Fecha"],df_evo["Centro"])
plt.plot(df_evo["Fecha"],df_evo["Chamberí"])
plt.plot(df_evo["Fecha"],df_evo["Latina"])

#Coniverto Fecha en index
df_evo.index=df_evo["Fecha"]

df_evo

#Elimino la columna Fecha
df_evo.drop("Fecha",axis=1,inplace=True)


df_evo

df_evo.plot()





