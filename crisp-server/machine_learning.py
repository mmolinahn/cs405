#!/usr/bin/python/
from statsmodels.tsa.arima_model import ARIMA
import pandas as pd
import numpy as np
import math
def get_holiday_bias(holiday, dow, temp, forecast):
    df = pd.read_csv('sales_2.csv')
    if holiday:
        df = df.loc[df['holiday'].isin([True])]
    sales = list(df['sales']) 
    pred_sales = []
    if abs(list(df['weather'])[0] - temp) > 15:
        for sale in sales:
            if list(df['weather'])[0] > temp:
                pred_sales.append(sale/2)
            else:
                sale = sale + sale/2
                pred_sales.append(sale)
    else:
        pred_sales = sales
    hours = list(df['hour'])
    dictionary = dict(zip(hours, sales))
    data = []
    for i in range(12):
            data.append({'time': "%i:00 %s" %( (i + 7 -12) if (i + 7) > 12 else (i + 7), ("PM"
    if (i + 7) >= 12 else "AM")), 'number': math.ceil((pred_sales[i] / 6)/8)})

    return data

def get_normal_days(dow, temp, pred):
    df = pd.read_csv('sales_2.csv')
    df = df.loc[df['dow'].isin([dow])]
    relevant_data = []
    for index, row in df.iterrows():
        if abs(row['weather'] -  temp) < 15:
            relevant_data.append({'hour':row['hour'], 'sales':row['sales']})
    if len(relevant_data) < 12:
        data = []
        cur = pred[0]
        for i in range(12):
            if i <= 6:
                cur += 15
            if i > 6 and i < 10:
                cur -= 5
            else:
                cur -= 15
            data.append({'time': "%i:00 %s" %( ((i + 7 - 12) if (i + 7) > 12 else (i
 + 7)), ("PM" if (i + 7) >= 12 else "AM")), 'number': math.ceil((cur/6)/8)})
        return data
    data = []
    for i in range(12):
            data.append({'time': "%i:00 %s" %( ((i + 7 - 12) if (i + 7) > 12 else (i + 7)), ("PM"
    if (i + 7) >= 12 else "AM")), 'number': math.ceil((relevant_data[i]['sales']/6)/8)})
    return data

def difference(dataset, interval=1):
	diff = []
	for i in range(interval, len(dataset)):
		if i - interval != 0:
			value = float(dataset[i][3]) - float(dataset[i - interval][3])
			diff.append(value)
	return np.array(diff)

def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval][3]


def calculate_prediction(date_str, weather, is_holiday, day_of_week):
    # load dataset
    series = pd.read_csv('dataset.csv')
    # seasonal difference
    X = series.values
    days_in_year = 365
    differenced = difference(X, days_in_year)
    # fit model
    model = ARIMA(differenced, order=(7,0,1))
    model_fit = model.fit(disp=0)
    forecast = model_fit.predict(start=999,end=1500) 
    forecast = inverse_difference(X, forecast, days_in_year)
    
    data = []
    if day_of_week == "Sunday":
        for i in range(12):
            data.append({'time': "Closed On Sundays", 'number': 0})
        return data
    if is_holiday(date_str):
        df = get_holiday_bias(True, day_of_week, weather, forecast)
        return df
    else:
        df = get_normal_days(day_of_week, weather, forecast)
        return df
    return forecast
