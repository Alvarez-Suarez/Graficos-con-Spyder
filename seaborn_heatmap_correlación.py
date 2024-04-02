# -*- coding: utf-8 -*-
"""Seaborn heatmap correlación.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_mot = pd.read_csv(r'datasets/datasets_1489_2704_auto-mpg_cont.csv',encoding = "ISO-8859-1",delimiter=',')

df_mot.columns

corr = df_mot.corr()

corr

sns.heatmap(corr, xticklabels=corr.columns.values,yticklabels=corr.columns.values, cmap='RdYlGn')

"""# Ejercicio"""

df_mot.head()

corr80 = df_mot[df_mot["model year"]==80].corr()

corr80

sns.heatmap(corr80,xticklabels=corr80.columns.values,yticklabels=corr80.columns.values, cmap='RdYlGn')















