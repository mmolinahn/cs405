from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
import datetime
app = Flask(__name__)
CORS(app)
from data_conn import get_result


def get_day(date_str):
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June" : 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    date_str = date_str.replace(",", "")
    date_params = date_str.split(" ")
    month = months[date_params[0]]
    x = datetime.datetime(int(date_params[2]), int(month), int(date_params[1]))
    return x.strftime("%A")



@app.route('/')
def get_data():
    date_str =  request.args.get("date")
    day_of_week = get_day(date_str)
    data = []
    return jsonify(get_result(date_str))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
