# -*- coding: utf-8 -*-
"""Subplots.py
"""

import pandas as pd
import matplotlib.pyplot as plt

df_temp = pd.read_excel(r'datasets/Temperaturas.xlsx',sheet_name="Sheet1")

df_temp 

df_temp["T.Promedio"]= (df_temp["T. Máxima"]+df_temp["T.Mínima"])/2

df_temp


#Filtrar los registros por la ciudad Madrid
df_temp=df_temp[df_temp["Ciudad"]=="Madrid"]

df_temp

df_temp["Ciudad"]=="Barcelona"
#Crear un dataframe df_temp_barcelona
df_temp_barcelona=df_temp[df_temp["Ciudad"]=="Barcelona"]

df_temp_barcelona


df_temp.head()

plt.plot(df_temp["FECHA"],df_temp["T. Máxima"],color="red")
plt.plot(df_temp["FECHA"],df_temp["T.Mínima"],color="blue")
plt.plot(df_temp["FECHA"],df_temp["T.Promedio"],color="orange")

fig, (ax1,ax2,ax3) = plt.subplots(3, 1,constrained_layout=True)

#fig, (ax1,ax2,ax3) = plt.subplots(3, 1)

ax1.plot(df_temp["FECHA"],df_temp["T. Máxima"],color="yellow")
ax2.plot(df_temp["FECHA"],df_temp["T.Promedio"],color="green")
ax3.plot(df_temp["FECHA"],df_temp["T.Mínima"],color="brown")

fig.suptitle('Temperatura Máxima, Promedio y Mínima de Madrid')
ax1.set_title('Temperatura Máxima')
ax2.set_title('Temperatura Promedio')
ax3.set_title('Temperatura Mínima')

fig.tight_layout()
#https://www.delftstack.com/howto/matplotlib/how-to-improve-subplot-size-or-spacing-with-many-subplots-in-matplotlib/