import sqlite3


class SaveTags:

    @staticmethod
    def create_table():
        conn = sqlite3.connect("web_scraper_db.sqlite")
        sql = '''SELECT name FROM sqlite_master WHERE type='table' AND name='web_scraper_data';'''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        row = cur.fetchall()
        print(row)
        if not row:

            conn = sqlite3.connect("web_scraper_db.sqlite")
            cur = conn.cursor()
            cur.execute('''
                        CREATE TABLE web_scraper_data (
                        website_name TEXT NOT NULL UNIQUE PRIMARY KEY,
                        website_url TEXT NOT NULL,
                        check_date TEXT NOT NULL ,
                        tags_data BLOB NOT NULL
                        ) WITHOUT ROWID;
                        ''')
            conn.commit()
            conn.close()
            print("Table has been created")
        else:
            print("Table already exists")

    @staticmethod
    def save_results(row):
        conn = sqlite3.connect("web_scraper_db.sqlite")
        sql = '''INSERT INTO web_scraper_data (website_name, website_url, check_date, tags_data) VALUES(?, ?, ?, ?);'''
        cur = conn.cursor()
        cur.execute(sql, row)
        conn.commit()
        print("Saved successful")

    @staticmethod
    def fetch_results(url):
        conn = sqlite3.connect("web_scraper_db.sqlite")
        sql = '''SELECT website_name, website_url, check_date, tags_data FROM web_scraper_data WHERE website_url = ?'''
        cur = conn.cursor()
        cur.execute(sql, (url,))
        conn.commit()
        row = cur.fetchall()
        return row


