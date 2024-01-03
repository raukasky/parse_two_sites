# import json
# import os
# import sqlite3
# from datetime import datetime
#
# import requests
#
#
# def open_cache():
#     try:
#         conn = sqlite3.connect('scraper.db')
#         cursor = conn.cursor()
#         cache_contents = cursor.execute('SELECT data from main.scraped_data')  # noqa
#         cache_dict = json.loads(cache_contents)
#         conn.close()
#     except:
#         cache_dict = {}
#     return cache_dict
#
#
# def save_cache(data):
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     db_path = os.path.join(BASE_DIR, "scraper.db")
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO "main.scraped_data" (data, timestamp) VALUES (?, ?)', (data, datetime.now()))  # noqa
#     conn.commit()
#     conn.close()
#
#
# def request_with_cache(url):
#     cache_dict = open_cache()
#     if url in cache_dict.keys():
#         print('Fetching from cache...')
#         return cache_dict[url]
#     else:
#         print('Fetching new data...')
#         r = requests.get(url)
#         html = r.text
#         cache_dict[url] = html
#         save_cache(cache_dict)
#         return html
#
#
# if __name__ == '__main__':
#     result = request_with_cache('https://www.perekrestok.ru')
#     print(result)
