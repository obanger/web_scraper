import pickle


class Pickler:

    def __init__(self, data):
        self.data = data

    def pickle(self):
        pickled_data = pickle.dumps(self.data, pickle.HIGHEST_PROTOCOL)
        return pickled_data

