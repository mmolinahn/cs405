#!/usr/bin/python
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
#dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y')
#data = pd.read_csv('sales_2.csv', parse_dates=['date'], index_col='date',date_parser=dateparse)
def calculate_prediction(holiday=False, sunday=False, temp=60):
    df = pd.read_csv('sales_2.csv')
    if holiday:
        df = df.loc[df['holiday'].isin([True])]
    return df
