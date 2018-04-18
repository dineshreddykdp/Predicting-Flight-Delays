#!/usr/bin/env python3
"""
This module implements a perceptron-type neural network.
"""
from random import random, seed
from math import exp

class Perceptron:

    def __init__(self, training_inputs, training_outputs):
        """
        training_inputs  = ((0, 0, 1), (1, 1, 1), (1, 0, 1), (0, 1, 1))
        training_outputs = (0, 1, 1, 0)

        neuron = Perceptron(training_inputs, training_outputs)
        neuron.train()

        prediction = (1, 0, 0)

        print(neuron.think(prediction))
        """
        seed(1)
        input_vars            = len(training_inputs[0])
        self.training_inputs  = training_inputs
        self.training_outputs = training_outputs
        self.weights          = [2 * random() - 1 for x in range(input_vars)]

    def __sigmoid(self, x):
        return 1/(1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self):
        """
        It trains the perceptron: inputs to the neuron.
        """
        for i, item in enumerate(self.training_inputs):
            output     = self.think(item)
            error      = self.training_outputs[i] - output
            adjustment = (x * error * self.__sigmoid_derivative(output) for x in item)
            self.weights = [w + a for w, a in zip(self.weights, adjustment)]

    def think(self, item):
        """
        Output of the neuron.
        """
        return self.__sigmoid(sum(x*w for x, w in zip(item, self.weights)))


if __name__ == '__main__':
    # Testing...
    training_inputs  = ((0, 0, 1), (1, 1, 1), (1, 0, 1), (0, 1, 1))
    training_outputs = (0, 1, 1, 0)

    neuron = Perceptron(training_inputs, training_outputs)

    predecir = (1, 0, 0)

    for _ in range(10000):
        neuron.train()

    print(neuron.think(predecir))