import pickle


class Unpickler:

    def __init__(self, data):
        self.data = data

    def unpickle(self):
        unpickled_data = pickle.loads(self.data)
        return unpickled_data

