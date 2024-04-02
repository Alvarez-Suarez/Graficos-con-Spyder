# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:19:03 2024

@author: Administrador
"""

import pandas as pd










df = pd.read_csv("datasets/gapminder.csv")

print(df)

print(df["continente"])

print(df["pais"])

print(df["anio"])

print(df["expVida"])

print(df["pobl"])
df["PBI_PC"]