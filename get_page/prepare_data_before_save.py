from datetime import date

from tld import get_tld


class PrepareDataBeforeSave:
    def __init__(self, url, pickled_data):
        self.url = url
        self.pickled_data = pickled_data

    def get_row(self):
        web_site_url = self.url
        web_site_name = get_tld(self.url, as_object=True).domain
        check_date = str(date.today())
        pickled_data = self.pickled_data
        row = (web_site_name, web_site_url, check_date, pickled_data)
        return row
