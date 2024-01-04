import os
import sys
import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from scraper.models import Product, ScrapingTask
from scraper.sears_scraper import SearsProductScraper


def extract_product_ids_from_string(string_object):
    if string_object:
        return [id_obj.strip() for id_obj in string_object.replace(';', ' ').replace(',', ' ').split() if id_obj]
    return []


def update_product_in_database(product_id, sears_parser):
    try:
        product_data = sears_parser.parse_product_data(item_id=product_id)
    except Exception as e:
        logging.error(f"Failed. ID {product_id}: {e}")
        return

    if product_data:
        Product.objects.update_or_create(
            product_id=product_id,
            defaults={
                'product_id': product_data['product_id'],
                'brand_name': product_data['brand_name'],
                'product_name': product_data['product_name'],
                'category': product_data['category'],
                'discounted_price': product_data['discounted_price'],
                'product_link': product_data['product_link']
            }
        )


def main():
    logging.basicConfig(level=logging.INFO)

    string_object = ScrapingTask.objects.values_list('input_string', flat=True).last()
    sears_product_parser = SearsProductScraper()

    for product_id in extract_product_ids_from_string(string_object):
        update_product_in_database(product_id, sears_product_parser)


if __name__ == '__main__':
    main()
