from SaveResults.saveResults import SaveTags
from getPage.PageDownloader import PageDownloader
from getPage.Pickler import Pickler
from getPage.PrepareDataBeforeSave import PrepareDataBeforeSave
from getPage.PrepareDataBeforeUnpickle import PrepareDataBeforeUnpickle
from getPage.Scraper import Scraper
from getPage.Unpickler import Unpickler


class TagsGetter:
    def __init__(self, url):
        self.url = url

    def get_tags(self):
        new_page = PageDownloader(self.url).get_html()
        scrap = Scraper(new_page).get_tags_dict()
        pickled_dict = Pickler(scrap).pickle()
        prepared_data = PrepareDataBeforeSave(self.url, pickled_dict).get_row()
        print(prepared_data)
        # test = DBConnection()
        SaveTags.create_table()
        SaveTags.save_results(prepared_data)
        row = SaveTags.fetch_results(self.url)
        print(row)
        to_unpickle = PrepareDataBeforeUnpickle(row).get_pickled_tags_dict()
        unpickled_dict = Unpickler(to_unpickle).unpickle()
        print(unpickled_dict)
        return unpickled_dict



