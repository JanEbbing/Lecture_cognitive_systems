""" Models for perceptrons """

import math
import operator

class Perceptron(object):
    """ Models any perceptron, real instances should subclass this.
    Has a list of weights, an activation function that determines
    wether it fires, given some input. """
    def __init__(self, weight_list=None, offset=0, activation_function=None):
        """ Instantiates a perceptron with the given weights (default to [1,1]) and a given activation function (defaults to tanh)
        Args:
            weight_list (list): List of floats determining the weights
            activation_function (function): f: float->float, determinates the response of this perceptron
        Returns:
            New perceptron instance.
        """
        if weight_list == None:
            self.weight_list = [1, 1]
        else:
            self.weight_list = weight_list
        if activation_function == None:
            self.activation_function = math.tanh
        else:
            self.activation_function = activation_function
        self.offset = offset

    def get_output(self, input_list):
        """ Gives this perceptron the inputs from input_list
        (if the number of weights vs inputs dont match a ValueError
        is thrown) and returns the response of this Perceptron.
        Args:
            input_list (list): List of floats, the inputs. Same number as the number of weights.
        Returns:
            float: Output of this perceptron to the new input.
        """
        if len(input_list) != len(self.weight_list):
            raise ValueError("Error! Amount of weights and inputs did not match.\nAmount of weights = %d\nAmount of inputs =%d.\n Complete vectors:\n Weights: %s\nInputs: %s" % (len(self.weight_list), len(input_list), self.weight_list, input_list))
        v = sum([weight*inp for (weight,inp) in zip(self.weight_list,input_list)])
        return self.activation_function(v-self.offset)

#Determines what is recognized as Zero
EPSILON=0.0001
class Classifier_Perceptron(Perceptron):
    """ Models a Perceptron that is used to classify data in two
    classes A and B. """

    def classify(self, vector):
        """ Receives a new data point to classify and
        returns {-1,0,1} depending on the classification result."""
        decision = self.get_output(vector)
        if abs(decision) < EPSILON:
            return 0
        elif decision > 0:
            return 1
        else:
            return -1

    def train_classification(self, input_data):
        """ Trains this perceptron to classify the given data.
        Data must be a list with entries of this format:
        ((a_0, ..., a_n), 1) for elements of class A
        ((b_0, ..., b_n), -1) for elements of class B.
        """
        number_iterations = 0
        number_of_weights = len(input_data[0][0])
        self.__train_initialize(number_of_weights)
        errs = self.__calc_misclassified(input_data)
        while(errs):
            for (wrongly_classified_point, wrong_class) in errs:
                sign = -wrong_class
                self.offset += sign
                self.weight_list = list(map(operator.add, self.weight_list, map(lambda x: operator.mul(x,-1), wrongly_classified_point)))
            errs = self.__calc_misclassified(input_data)
            number_iterations += 1
        print("Finished training after %d iterations" % number_iterations)

    def __train_initialize(self, number_of_weights):
        self.weight_list = [1] * number_of_weights
        self.offset = 0

    def __calc_misclassified(self, input_data):
        result = []
        for (data_point, expected_class) in input_data:
            if expected_class != self.classify(data_point):
                result.append((data_point, expected_class))
        return result
