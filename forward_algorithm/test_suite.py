import unittest
from markov_model import construct_model_from_file

class TestBasicFunctions(unittest.TestCase):
    MODEL_FILE = "/home/jan/Lecture_cognitive_systems/forward_algorithm/example_model.txt"
    def test_reading_file(self):
        test_model = construct_model_from_file(self.MODEL_FILE)
        self.assertEqual(test_model.number_of_states, 3, "wrong number of states")
        self.assertEqual(test_model.number_of_symbols, 3, "wrong number of symbols")
        self.assertEqual(test_model.get_transfer_probability(0,0), 0.8, "wrong probability in transfer matrix")
        self.assertEqual(test_model.get_transfer_probability(1,0), 0.0, "wrong probability in transfer matrix")
        self.assertEqual(test_model.get_transfer_probability(1,1), 0.5, "wrong probability in transfer matrix")
        self.assertEqual(test_model.get_emission_probability(0,0), 0.7, "wrong probability in emission matrix")
        self.assertEqual(test_model.get_emission_probability(1,0), 0.2, "wrong probability in emission matrix")
        self.assertEqual(test_model.get_emission_probability(2,1), 0.1, "wrong probability in emission matrix")
        self.assertEqual(test_model.get_emission_probability(2,2), 0.8, "wrong probability in emission matrix")
        self.assertEqual(test_model.get_initial_probability(2), 0.5, "wrong probability for initial states")
