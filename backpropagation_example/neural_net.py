""" Provides utility functions to compute a MLP. """

import math
from perceptron import Perceptron

class Connectionist_Perceptron( Perceptron ):
    def __init__(self, weight_list, offset):
        super(Perceptron, self).__init__(weight_list,offset,lambda x:1/(1+math.exp(-x)))

class Neural_Net( object ):
    def __init__(self, number_inputs, number_outputs, number_hidden_neurons):
        """ Creates a new neural net with the given parameters.
        Args:
            number_inputs (int): Size of the input vectors
            number_outputs (int): Size of the output vectors
            number_hidden_neurons (int): Number of neurons in the hidden layer.
        """
        self.input_layer = []
        self.hidden_layer = []
        self.output_layer = []
        for i in xrange(0, number_inputs):
            self.input_layer.append(Connectionist_Perceptron([1.0],0))
        for i in xrange(0, number_hidden_neurons):
            self.hidden_layer.append(Connectionist_Perceptron([1.0]*number_inputs, 0))
        for i in xrange(0, number_outputs):
            self.output_layer.append(Connectionist_Perceptron([1.0]*number_hidden_neurons),0)

    def calculate_output(self, given_input):
        pass
