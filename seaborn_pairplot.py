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
