import requests
from flask import Flask
from flask import request, jsonify
from flask.views import MethodView

from run_perceptron import run_prediction

app = Flask(__name__)

default_dest_airport = "ATL"
default_origin_airport = "BDL"
default_airline = "WN"
default_day_of_week = 3

@app.route('/getprediction')

def get_prediction_delay():

    # get args
    # dest_airport, origin_airport, day_of_week, airline

    dest_airport = request.args.get('dest_airport', type=str, default=default_dest_airport);
    origin_airport = request.args.get('origin_airport', type=str, default=default_origin_airport);
    airline = request.args.get('airline', type=str, default=default_airline);
    day_of_week = request.args.get('day_of_week', type=int, default=default_day_of_week);


    return str(run_prediction(dest_airport, origin_airport, airline, day_of_week))


# for local debugging
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True, debug=True)
