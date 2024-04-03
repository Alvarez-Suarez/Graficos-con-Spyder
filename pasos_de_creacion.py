# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:14:09 2024

@author: Administrador
"""#primer grafico
#importar
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#poner un archvio al nombre df
df = pd.read_csv("datasets/gapminder.csv")
#llamar df
print(df)
#listado de tabla
df["expVida"].plot()

df["anio"].plot()

df["pobl"].plot()

df["PBI_PC"].plot()








#segundo grafico


import pandas as pd

"""# Lectura de datos"""

df = pd.read_csv(r"datasets/info_pais.csv",encoding = "ISO-8859-1",delimiter=';')

df.head()

"""# Manipulación de datos"""

df.sort_values("Esperanza de vida",ascending=True)

df_order = df.sort_values("Esperanza de vida",ascending=True)

df_order.head()

"""# Visualización"""

import matplotlib.pyplot as plt

#imagen1
plt.scatter(df_order["Renta per capita"],df_order["Esperanza de vida"])

#imagen2
plt.scatter(df_order["Renta per capita"],df_order["Esperanza de vida"])
plt.title("Renta per capita vs Esperanza de vida")
plt.xlabel("Renta per capita")
plt.ylabel("Esperanza de vida")

#imagen3
df_order["Pob_norm"]=df_order["Poblacion"]/max((df_order["Poblacion"]/10000))
#llamo a la lista
df_order

plt.scatter(df_order["Renta per capita"],df_order["Esperanza de vida"],
            s=df_order["Pob_norm"],c=df_order["Pob_norm"])

plt.title("Renta per capita vs Esperanza de vida")
plt.xlabel("Renta per capita")
plt.ylabel("Esperanza de vida")

for i in range(1,10):
    plt.annotate(df_order["País"][i],(df_order["Renta per capita"][i],df_order["Esperanza de vida"][i]))
#posicion
fig = plt.gcf()
fig.set_size_inches(14.5, 10)
plt.yticks(ticks=range(1,120,10))





#tercer grafico




#importo
import pandas as pd

#df = pd.read_csv("datasets/sp500_data.csv")
#nombro a df
df = pd.read_csv(r'datasets/sp500_data.csv',encoding = "ISO-8859-1",delimiter=',')
#llamo a df
print(df)

#veo las columnas
df.columns

print(df)

#cambio el valor del indice por la fecha
df.index = df["Date"]

print(df)

#Visualizar la evolucion de la cotizacion en bolsa

df["Open"].plot()

df["Close"].plot()


#cuarto grafico

#importo
import matplotlib.pyplot as plt
import pandas as pd
#nombro info_pais
info_pais = {"pais":["Brasil", "México", "España", "Perú", "Colombia", "Venezuela"],
             "capital":["Brasilia","Ciudad de México","Madrid","Lima","Bogotá","Caracas"],
             "superficie (Mkm2)": [8.5, 1.9, 1.2, 0.5, 1.1,0.9]}

df_pais = pd.DataFrame(info_pais)
#llamo info_pais
df_pais

#Nuevo: inplace - el cambio se ejecuta en el dataframe
df_pais.sort_values("superficie (Mkm2)",ascending=False,inplace=True)

df_pais

plt.bar(df_pais["pais"],df_pais["superficie (Mkm2)"])


plt.bar(df_pais["pais"],df_pais["superficie (Mkm2)"],
        color=["green","blue","blue","blue","blue","blue"])

plt.title("¿Qué país tiene mayor superficie")
plt.xlabel("País")
plt.ylabel("Superficie (Mkm2)")
plt.legend(["País TOP 1"])

for i in range(0,6):
    plt.annotate(df_pais["superficie (Mkm2)"][i],(df_pais["pais"][i],df_pais["superficie (Mkm2)"][i]))
 
   
fig = plt.gcf()
fig.set_size_inches(10.5, 8)
plt.yticks(ticks=range(1,10,1))

#Como funciona annotate
for i in range(0,6):
    print(df_pais["superficie (Mkm2)"][i],(df_pais["pais"][i],df_pais["superficie (Mkm2)"][i]))

#qué estilos hay
plt.style.available
plt.style.use('seaborn-notebook')

#usando el estilo seleccionado
plt.bar(df_pais["pais"],df_pais["superficie (Mkm2)"],color=["green","blue","blue","blue","blue","blue"])
plt.title("¿Qué país tiene mayor superficie")
plt.xlabel("País")
plt.ylabel("Superficie (Mkm2)")
plt.legend(["País TOP 1"])
for i in range(0,6):
    plt.annotate(df_pais["superficie (Mkm2)"][i],(df_pais["pais"][i],df_pais["superficie (Mkm2)"][i]))
    
#fig = plt.gcf()
fig.set_size_inches(10.5, 8)
plt.yticks(ticks=range(1,10,1))

plt.style.use('tableau-colorblind10')


#quinto grafico




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


#sexto grafico


#importo
import pandas as pd

import matplotlib.pyplot as plt

#nombro a df_temp
df_temp = pd.read_excel(r'datasets\Temperaturas.xlsx',sheet_name="Sheet1")

#llamo a df_temp
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

#septimo grafico

#importo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#nombro df_casas
df_casas = pd.read_excel("datasets/casas.xlsx")

#llamo a df_casas
df_casas

df_casas.dtypes

plt.scatter(df_casas["superficie"],df_casas["valor"])

#declaro la superficie/valor/color
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



#octavo grafico
#importo
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#nombro df_exi
df_ext = pd.read_csv(r'datasets/temp_hum_ext.csv',encoding = "ISO-8859-1",delimiter=',')
#llamo df_ext
df_ext

sns.stripplot(y='Temperatura (ºC)', data=df_ext, jitter=False)

sns.stripplot(x='Provincia', y='Temperatura (ºC)', data=df_ext, jitter=True)
plt.xlabel("Provincia")



#noveno grafico

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


#decimo grafico

# -*- coding: utf-8 -*-
"""Seaborn Pairplot.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_mot = pd.read_csv(r'datasets/datasets_1489_2704_auto-mpg_cont.csv',encoding = "ISO-8859-1",delimiter=',')

df_mot.head()

df_mot.columns

sns.pairplot(df_mot)

sns.pairplot(df_mot,hue="continent")
