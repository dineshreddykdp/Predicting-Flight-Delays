#!/usr/bin/env python3
"""
This module trains a neural network to determine whether a flight will reach
on time or not to a specific airport entered by the user. For this purpose,
in the folder of this module must be the files provided by Kaggle in the
directorate https://www.kaggle.com/usdot/flight-delays/data
These files are: flights.csv, airlines.csv y airports.csv
"""
import csv

from perceptron import Perceptron


ORIGIN_AIRPORT = dict()
AIRLINE        = dict()

print("\n* Loading data from the airlines...")
with open("data/airlines.csv") as fairlines:
    airlines = csv.reader(fairlines)
    i = 0
    next(airlines)
    for airline in airlines:
        i += 1
        AIRLINE[airline[0]] = i
        
        #enumerated types

print(airline)
print(AIRLINE)

print("* Loading data from airports...")
with open("data/airports.csv") as fairports:
    airports = csv.reader(fairports)
    i = 0
    next(airports)
    for airport in airports:
        i += 1
        ORIGIN_AIRPORT[airport[0]] = i

print(airport)
print(ORIGIN_AIRPORT)

def run_prediction(dest_airport, origin_airport, airline, day_of_week):
    """
    Main neural network training menu.
    """

    destination_airport = dest_airport
    training_size = 10000

    training_inputs, training_outputs = training_perceptron(destination_airport, training_size)

    print (training_inputs)
    return predicting_perceptron(training_inputs,
                                 training_outputs,
                                 day_of_week,
                                 airline,
                                 origin_airport )




def training_perceptron(destination_airport, training_size):
    """
    Loading of airlines, airports and flights from the given data.
    """
    print("\n* Loading flight data...")
    with open('data/flights.csv') as fflights:
        print("inside while loop")
        flights          = csv.reader(fflights)
        training_inputs  = list()
        training_outputs = list()
        i                = 0
        next(flights)
        for flight in flights:
           # print (flight[7], destination_airport)
            if flight[9] == destination_airport:

                i += 1
                day_of_week    = int(flight[4])
                origin_airport = ORIGIN_AIRPORT[flight[8]]
                airline        = AIRLINE[flight[5]]
                item           = day_of_week, origin_airport, airline
                training_inputs.append(item)
                print(item, flight[23])

                # if ARRIVAL_DELAY <= 0: ON TIME: 1
                # index ARRIVAL_DELAY = 23
                training_outputs.append(1 if (flight[23] == "" or float(flight[23])) <= 0 else 0)
                if i == training_size:
                    break
    print(training_inputs)
    print(training_outputs) 
    return training_inputs, training_outputs
  

def predicting_perceptron(training_inputs,
                          training_outputs,
                          day_of_week,
                          airline,
                          origin_airport):
    """
    This function trains the neural network.
    """
    neuron = Perceptron(training_inputs, training_outputs)
    print("* Training the neural network...")
    neuron.train()

    print("\n# Neural network PREDICTION mode:")
    day_of_week    = day_of_week
    origin_airport = origin_airport
    airline        = airline

    origin_airport = ORIGIN_AIRPORT[origin_airport]
    airline        = AIRLINE[airline]

    prediction = day_of_week, origin_airport, airline
    

    return round(neuron.think(prediction));


if __name__ == '__main__':
    main_menu()