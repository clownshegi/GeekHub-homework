"""
2. Викорисовуючи requests, заходите на ось цей сайт
"https://www.expireddomains.net/deleted-domains/" (з ним будьте обережні),
 вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів -
 їх там буде десятки тисяч (звичайно ураховуючи пагінацію) Всі отримані значення зберігти в CSV файл.
"""

import csv
import os
import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

DOMAINS_FILE = "domains.csv"
BASE_URL = "https://www.expireddomains.net/expired-domains/"
WAIT_TIME = 15


def get_data(url, params=None, headers=None):
    if headers is None:
        headers = {"User-Agent": UserAgent().random}

    response = requests.get(url, params=params, headers=headers)
    return response.content


def write_to_csv(data):
    headers = ["Domain"]
    file_exists = os.path.exists(DOMAINS_FILE)

    with open(DOMAINS_FILE, "a+", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or file.tell() == 0:
            writer.writerow(headers)

        for row in data:
            writer.writerow([row])


def find_info():
    while True:
        page_content = get_data(BASE_URL)
        print("Код працює, все іде по плану")
        soup = BeautifulSoup(page_content, features="html.parser")
        rows = soup.find_all("td", class_="field_domain")
        domain_text_list = [row.text for row in rows]

        write_to_csv(domain_text_list)

        next_page = soup.find("a", class_="next")
        if not next_page:
            print("Збір даних завершено!")
            break

        time.sleep(WAIT_TIME)


find_info()
