#!/usr/bin/python:q
from machine_learning import calculate_prediction 
import datetime
import holidays
import requests
"""
We make the assumption that an employee can deal with up to 4 orders and hour
"""
months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June" : 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December":
12}
def get_day(date_str):
    date_str = date_str.replace(",", "")
    date_params = date_str.split(" ")
    month = months[date_params[0]]
    x = datetime.datetime(int(date_params[2]), int(month), int(date_params[1]))
    return x.strftime("%A")

def is_holiday(date_str):
    date_str = date_str.replace(",", "")
    date_params = date_str.split(" ")
    month = months[date_params[0]]
    us_holidays = holidays.UnitedStates()     
    return datetime.date(int(date_params[2]), int(month), int(date_params[1])) in us_holidays

def date_to_epoch(date_str):
    date_str = date_str.replace(",", "")
    date_params = date_str.split(" ")
    month = months[date_params[0]]
    return (datetime.datetime(int(date_params[2]), int(month), int(date_params[1])) - datetime.datetime(1970,1,1)).total_seconds()

def get_weather(date_str):
    epoch = date_to_epoch(date_str)
    r = requests.get(url="https://api.darksky.net/forecast/5ce89eb439990b9931bb745f9935ac27/40.274617,-111.68853,%i" % epoch)
    data = r.json() 
    return data["currently"]["temperature"]


def process_data(date_str):
    day_of_week = get_day(date_str)
    weather = get_weather(date_str)
    pred = calculate_prediction(date_str, weather, is_holiday, day_of_week)
    return pred

def get_result(date_str):
    data = process_data(date_str)
    return data	
