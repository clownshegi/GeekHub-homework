from random import choice
from time import sleep
from typing import Any
from urllib.parse import urljoin

import requests


class SearsProductScraper:

    BASE_URL = 'https://www.sears.com'
    HEADERS = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'uk,ru;q=0.9',
        'authorization': 'SEARS',
        'content-type': 'application/json',
        'user-agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        ),
    }

    def parse_product_data(self, item_id: Any):
        sleep(choice(range(4, 7)))
        request_url = (
            f'https://www.sears.com/api/sal/v3/products/search?q={item_id}&'
            f'startIndex=1&endIndex=48&searchType=keyword&catalogId=12605&store='
            f'Sears&storeId=10153&zipCode=10101&bratRedirectInd=true&'
            f'catPredictionInd=true&disableBundleInd=true&filterValueLimit=500&'
            f'includeFiltersInd=true&shipOrDelivery=true&solrxcatRedirection=true&'
            f'sortBy=ORIGINAL_SORT_ORDER&whiteListCacheLoad=false&'
            f'eagerCacheLoad=true&slimResponseInd=true&catRecommendationInd=true'
        )

        response = requests.get(request_url, headers=self.HEADERS).json()['items'][0]

        product_data = {
            'product_id': response['partNum'],
            'brand_name': response['brandName'],
            'product_name': response['name'],
            'category': response['category'],
            'discounted_price': response['price']['finalPriceDisplay'],
            'price_before_discount': response['price']['regularPriceDisplay'],
            'savings_percent': response['price'].get('savingsDisplay', 'No savings'),
            'product_link': urljoin(self.BASE_URL, response['additionalAttributes']['seoUrl'])
        }

        return product_data
