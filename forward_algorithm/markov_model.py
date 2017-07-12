class MarkovModel(object):
    def __init__(self, nr_states, nr_symbols, matrix_A, matrix_B, initial_states_probabilities):
        self.number_of_states = nr_states
        self.number_of_symbols = nr_symbols
        self.transfer_probabilities = matrix_A
        self.emission_probabilities = matrix_B
        self.initial_states_probabilities = initial_states_probabilities

    def get_transfer_probability(self, state1, state2):
        """ From state1 to state2, as int """
        return self.transfer_probabilities[state1][state2]

    def get_emission_probability(self, state, symbol):
        """ Probability to emit symbol while in state. Both ints """
        return self.emission_probabilities[state][symbol]

    def get_initial_probability(self, state):
        """ Probability to start the model in state, as int """
        return self.initial_states_probabilities[state]

def construct_model_from_file(filepath):
    with open(filepath) as f:
        nr_states = int(f.readline())
        nr_symbols = int(f.readline())
        matrix_A_line = f.readline()
        matrix_B_line = f.readline()
        initial_states_line = f.readline()
    matrix_A = create_matrix_from_line(matrix_A_line, nr_states)
    matrix_B = create_matrix_from_line(matrix_B_line, nr_symbols)
    initial_states = create_intlist_from_line(initial_states_line)
    return MarkovModel(nr_states, nr_symbols, matrix_A,
                        matrix_B, initial_states)

def create_matrix_from_line(string_of_matrix, size_of_row):
    list_of_ints = create_intlist_from_line(string_of_matrix)
    result = []
    for pos in range(0, len(list_of_ints), size_of_row):
        result.append(list_of_ints[pos:pos + size_of_row])
    return result

def create_intlist_from_line(line):
    list_of_strings = line.split()
    list_of_ints = list(map(float, list_of_strings))
    return list_of_ints
