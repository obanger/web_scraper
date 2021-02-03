import requests


class PageDownloader:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        page = requests.get(self.url).text
        return page
