from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
app = Flask(__name__)
CORS(app)





@app.route('/')
def get_result():
    date_str =  request.args.get("date")
    data = [] 
    test = {'time': "8:00 AM", "number": 3}
    #test['data'] = "Hello, THERE"
    for i in range(10):
        data.append(test)
    return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
