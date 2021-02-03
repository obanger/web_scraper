class PrepareDataBeforeUnpickle:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def get_pickled_tags_dict(self):
        row_tuple = self.raw_data[0]
        pickled_tags_dict = row_tuple[3]
        return pickled_tags_dict
