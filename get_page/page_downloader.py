import requests


class PageDownloader:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        try:
            page = requests.get(self.url).text
            return page
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


