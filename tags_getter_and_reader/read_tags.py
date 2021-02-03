from save_results.save_results import SaveTags
from get_page.prepare_data_before_unpickle import PrepareDataBeforeUnpickle
from get_page.unpickler import Unpickler


class TagsReader:

    def __init__(self, url):
        self.url = url

    def read_tags(self):
        row = SaveTags.fetch_results(self.url)
        print(row)
        to_unpickle = PrepareDataBeforeUnpickle(row).get_pickled_tags_dict()
        unpickled_dict = Unpickler(to_unpickle).unpickle()
        print(unpickled_dict)
        if unpickled_dict is None:
            print("Got an error during execution, seems like this web site not scraped yet")
        else:
            return unpickled_dict
