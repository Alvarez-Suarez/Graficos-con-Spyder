# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:36:41 2024

@author: Administrador
"""

import pandas as pd

df = pd.read_csv("datasets/gapminder.csv")

print(df)

df["expVida"].plot()

df["anio"].plot()

df["pobl"].plot()

df["PBI_PC"].plot()
