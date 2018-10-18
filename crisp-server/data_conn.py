#!/usr/bin/python
from machine_learning import calculate_prediction 
import sqlite3
from sqlite3 import Error
import datetime
import holidays
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

def process_data(date_str):
    day_of_week = get_day(date_str)
    data = []
    if day_of_week == "Sunday":
        for i in range(12):
            data.append({'time': "Closed On Sundays", 'number': 0})
        return data
    if day_of_week == "Saturday":
        for i in range(12):
            data.append({'time': "%i:00 %s" %( i if (i + 7) > 12 else (i + 7), ("PM" if (i + 7) >= 12 else "AM")), 'number': 0})
        return data
    if is_holiday(date_str):
        pred = calculate_prediction(True, True, 70)
        print(pred)
        for i in range(12):
            data.append({'time': "%i:00 %s" %( i if (i + 7) > 12 else (i + 7), ("PM" if (i + 7) >= 12 else "AM")), 'number': 0})
        return data
    else:
        for i in range(12):
            data.append({'time': "%i:00 %s" %( i if (i + 7) > 12 else (i + 7), ("PM" if (i + 7) >= 12 else "AM")), 'number': 0})
        return data


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row) 
 
def get_result(date_str):
    
    data = process_data(date_str)

    
    # create a database connection
    #database = "/home/bitnami/crisp-server/historic_data.db"
    #conn = create_connection(database)
    #with conn:
        #select_task_by_priority(conn,1)
    return data	
 
if __name__ == '__main__':
    get_result()
