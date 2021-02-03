from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, page):
        self.page = page

    def get_tags_dict(self):
        tags = (BeautifulSoup(self.page, "html.parser"))
        tags_dict = {}
        for tag in tags.find_all():
            if tag.name not in tags_dict.keys():
                tags_dict.update({tag.name: 1})
            else:
                tags_dict.update({tag.name: tags_dict[tag.name] + 1})
        return tags_dict


