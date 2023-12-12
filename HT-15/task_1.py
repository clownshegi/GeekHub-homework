"""
1. Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту https://www.sears.com
і буде збирати всі товари із цієї категорії, збирати по ним всі можливі дані
(бренд, категорія, модель, ціна, рейтинг тощо) і зберігати їх у CSV файл
(наприклад, якщо категорія має ID 12345 то файл буде називатись 12345_products.csv)
Наприклад, категорія https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184
"""

import csv
import time
import requests
from fake_useragent import UserAgent


def make_request(url, headers, params):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get("items", [])
    except requests.RequestException as e:
        print(f"Произошла ошибка: {e}")
        return []


def fetch_products(category_id, start_index, end_index):
    user_agent = UserAgent()
    headers = {
        "Authorization": "SEARS",
        "User-Agent": user_agent.random
    }
    url = "https://www.sears.com/api/sal/v3/products/search"
    all_product_items = []

    while True:
        params = {
            "startIndex": start_index,
            "endIndex": end_index,
            "searchType": "category",
            "store": "Sears",
            "storeId": 10153,
            "catGroupId": category_id,
        }
        print(f"Обработка товаров с {start_index} по {end_index}")
        product_data = make_request(url, headers, params)

        if not product_data:
            break
        all_product_items.extend(product_data)

        start_index += 300
        end_index += 300
        time.sleep(5)

    return all_product_items


def save_to_csv(category_id, all_product_items):
    headers = ["Brand Name", "Name", "Category", "Final Price"]
    file_name = f"{category_id}_products.csv"

    with open(file_name, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(headers)

        for item in all_product_items:
            product_data = [
                item.get("brandName", ""),
                item.get("name", ""),
                item.get("category", ""),
                item.get("price", {}).get("messageTags", {}).get("finalPrice", ""),
            ]
            writer.writerow(product_data)

    print("Процесс завершен!")


def get_data():
    category_id = input("Введите идентификатор категории: ")
    start_index = 1
    end_index = 300
    products = fetch_products(category_id, start_index, end_index)
    save_to_csv(category_id, products)


get_data()
