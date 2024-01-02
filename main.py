import re

import requests
from bs4 import BeautifulSoup


def foo():
    """

    :return:
    """
def parse_item(sub_category_url):
    url = 'https://www.perekrestok.ru' + sub_category_url
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.select('.product-card-wrapper')
    # items_url = [(a.string, a.get('')) for a in items]
    for item in items:
        print(item)
    return items


def run_code(url):
    response = requests.get(url=url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = soup.select('.catalog-aside a[href^="/cat/c/"]')
        category_name_url = [(a.string, a.get('href')) for a in categories]
        for sub in category_name_url:
            MAIN_URL = 'https://www.perekrestok.ru'
            # url = "".join([MAIN_URL, sub[1]])
            url = MAIN_URL + 'cat/c/1067/dla-olive'
            print(url)


if __name__ == '__main__':
    # url = 'https://www.perekrestok.ru/cat'
    # result = run_code(url)
    url = '/cat/c/1067/dlya-olive'
    res = parse_item(url)
    # print(res)

