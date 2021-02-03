import os
import sqlite3


class DBConnection:

    def __init__(self):
        if os.path.isfile("web_scraper_db.sqlite"):
            print("DB already exists")
        else:
            self.conn = sqlite3.connect("web_scraper_db.sqlite")
            print("DB has been created")
