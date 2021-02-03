from SaveResults.saveResults import SaveTags
from getPage.PrepareDataBeforeUnpickle import PrepareDataBeforeUnpickle
from getPage.Unpickler import Unpickler


class TagsReader:

    def __init__(self, url):
        self.url = url

    def read_tags(self):
        row = SaveTags.fetch_results(self.url)
        print(row)
        to_unpickle = PrepareDataBeforeUnpickle(row).get_pickled_tags_dict()
        unpickled_dict = Unpickler(to_unpickle).unpickle()
        print(unpickled_dict)
        return unpickled_dict
