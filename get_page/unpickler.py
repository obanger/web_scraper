import pickle


class Unpickler:

    def __init__(self, data):
        self.data = data

    def unpickle(self):
        try:
            unpickled_data = pickle.loads(self.data)
            return unpickled_data
        except TypeError:
            print("Type Error Raised")

