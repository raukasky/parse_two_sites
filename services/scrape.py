import os
import sqlite3

from errors.errors import error
import requests
from bs4 import BeautifulSoup


# TODO: need to first init app for collect data from websites
def init():
    """
    This is first init part to create table in db
    :return: Nothing, only run first step
    """
    conn = sqlite3.connect('scraper.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS scraped_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                timestamp DATETIME NOT NULL
            );
        ''')
    conn.commit()
    conn.close()


def main(url):
    try:
        response = requests.get(url=url, timeout=30)
        print(response.headers)
        # soup = BeautifulSoup(response.content, 'html.parser')
        # return soup
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main(url='https://www.perekrestok.ru')