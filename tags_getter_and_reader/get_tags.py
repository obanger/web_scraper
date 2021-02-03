from save_results.save_results import SaveTags
from get_page.page_downloader import PageDownloader
from get_page.pickler import Pickler
from get_page.prepare_data_before_save import PrepareDataBeforeSave
from get_page.prepare_data_before_unpickle import PrepareDataBeforeUnpickle
from get_page.scraper import Scraper
from get_page.unpickler import Unpickler


class TagsGetter:
    def __init__(self, url):
        self.url = url

    def get_tags(self):
        new_page = PageDownloader(self.url).get_html()
        scrap = Scraper(new_page).get_tags_dict()
        pickled_dict = Pickler(scrap).pickle()
        prepared_data = PrepareDataBeforeSave(self.url, pickled_dict).get_row()
        print(prepared_data)
        SaveTags.create_table()
        SaveTags.save_results(prepared_data)
        row = SaveTags.fetch_results(self.url)
        print(row)
        to_unpickle = PrepareDataBeforeUnpickle(row).get_pickled_tags_dict()
        unpickled_dict = Unpickler(to_unpickle).unpickle()
        print(unpickled_dict)
        if unpickled_dict is None:
            print("Seems like ")
        return unpickled_dict



