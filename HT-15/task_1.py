"""
1. Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту https://www.sears.com
і буде збирати всі товари із цієї категорії, збирати по ним всі можливі дані
(бренд, категорія, модель, ціна, рейтинг тощо) і зберігати їх у CSV файл
(наприклад, якщо категорія має ID 12345, то файл буде називатись 12345_products.csv)
Наприклад, категорія https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184
"""
import csv
import requests
from fake_useragent import UserAgent


def get_data(category_id):
    user_agent = UserAgent()
    params = {
        "searchType": "category",
        "store": "Sears",
        "storeId": 10153,
        "catGroupId": category_id,
    }
    headers = {
        "Authorization": "SEARS",
        "User-Agent": user_agent.random
    }
    url = "https://www.sears.com/api/sal/v3/products/search"

    response = requests.get(url, headers=headers, params=params)
    product_items = response.json()["items"]

    headers = ["Brand Name", "Name", "Category", "Final Price"]
    file_name = f"{category_id}_products.csv"

    with open(file_name, "a+", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=",")

        if file.tell() == 0:
            writer.writerow(headers)

        for item in product_items:
            product_data = [
                item["brandName"],
                item["name"],
                item["category"],
                item["price"]["messageTags"]["finalPrice"],
            ]
            writer.writerow(product_data)

    print("Завершено!")


def find_product_info():
    category_id = input("Введіть ідентифікатор категорії: ")
    get_data(category_id)


find_product_info()
