import time

import requests
from django.utils import timezone
from requests import JSONDecodeError


def get_response_json(product_id):
    while True:
        try:
            cookies = {
                '__cf_bm': '.T691RBgMr.IgCal3iOoKRDF1PSQLYlNadS_vI0I3RY-1704141121-1-AUbnSPcfJkJe'
                           '/8jiXxvzWO8RkyuoaxrrHEHoanfzH9CPy7uiux2YOKsSQ2oHo2ZDqReM1ouHhbMagHgDBfs6gj'
                           '/Px0kjEW3FXEHWJm3Z7aN7',
                '_gid': 'GA1.2.2020879329.1704141123',
                'cf_clearance': 'zkIYq_rfrnvfGf9u0Mt05VApGid_iSDdSSag9ckL8tY-1704141123-0-2-df116c6a.b6b65621'
                                '.2411c6a2-0.2.1704141123',
                'ftr_blst_1h': '1704141123141',
                'zipCode': '10101',
                'city': 'New York',
                'state': 'NY',
                'irp': '1680a67a-1a6c-4065-ae97-f647ee5c5c67|%2BARMWZ9w7HwJfLRv93Fg5zqg9J3nKNMe3i2S7GnqRqs%3D|G'
                       '|aa36184c-1042-40f7-bd87-0b90e215e194|0|NO_SESSION_TOKEN_COOKIE',
                'initialTrafficSource': 'utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)',
                '__utmzzses': '1',
                '_gcl_au': '1.1.2004487084.1704141125',
                'ltkSubscriber-Footer': 'eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9',
                '_clck': 'bq0b5w%7C2%7Cfi1%7C0%7C1461',
                '_fbp': 'fb.1.1704141125651.1844351240',
                '__gsas': 'ID=a68ed45cfe4984d6:T=1704141125:RT=1704141125:S=ALNI_MZeebA5rPwP_C4mWBdmz8L_GOX70A',
                'GSIDNqXoacKY53MN': '58e4e68a-868d-40a0-912c-aba8232eb796',
                'STSID974004': '17c886c0-a2c6-47fa-b677-7ea28ce28e8c',
                '_li_dcdm_c': '.sears.com',
                '_lc2_fpi': 'ec742730c587--01hk3bkyvpxnpqzdey3zvtdra9',
                '_lc2_fpi_meta': '{%22w%22:1704141126518}',
                '__qca': 'P0-1812215260-1704141126502',
                '_li_ss': 'ChMKCQj_____BxDwFgoGCN0BEO8W',
                '_uetsid': 'd3c97ca0a8e411ee8fd03b007cc09e08',
                '_uetvid': 'd3ca0b00a8e411eebbd4d94c7bb674ca',
                '__pr.3q8y1p': 'ETErJ89BF1',
                'ltkpopup-session-depth': '1-1',
                '_clsk': '1hkln09%7C1704141343051%7C3%7C1%7Cy.clarity.ms%2Fcollect',
                'cookie': 'e70643ac-3c13-4223-9a04-998b5e1bb334',
                'cookie_cst': 'zix7LPQsHA%3D%3D',
                'cto_bundle': 'cCnTDF82VzRHalZJVXppNGxvTEczanBMTW5PdG9iMSUyQk1DTHluaU9hdiUyQkdleVZrZ1YzaVRZaGdVZ2NHQ'
                              '282a2pVaWdDJTJGWldIJTJGc25mWk5yJTJCb2Q5UTMlMkZ3Nk5VRDBxdk5DNE9jdUVjUGZKelc2QlN6RnclMk'
                              'ZXeWxTdlhnNEg0aVBFWGslMkJlRllCOTFqV2JmV01JYlJMelJ0a2xqUk9RJTNEJTNE',
                'cto_bidid': 'wdrt719XUmR5ZFo4MTh0WWRMcGo4VW9mRjclMkZIazN2VzMxWUwlMkIxbmFLMnRyRlkzWWJwbEM5Z3UxQ2Nx'
                             'JTJCMXB3UXN4dUd0dm00YyUyQlM0TzVwVUk1MWh1RXhHazJQak5tODhodWpoMHppQUp6MXg3R0VZJTNE',
                '_li_ss_meta': '{%22w%22:1704141345449%2C%22e%22:1706733345449}',
                '__gads': 'ID=90d0f9d8bf986840:T=1704141127:RT=1704141508:S=ALNI_MbGrU9yh94ZjSCRorTY_p5XlnQ-Rw',
                '__gpi': 'UID=00000d32b0aa3805:T=1704141127:RT=1704141508:S=ALNI_MbqLOlx4GcTnzrkFMFaIwz54i83kA',
                'OptanonConsent': 'isIABGlobal=false&datestamp=Mon+Jan+01+2024+22%3A38%3A50+GMT%2B0200+'
                                  '(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+'
                                  '%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+'
                                  '%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+'
                                  '%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&hosts=&'
                                  'landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSPD_'
                                  'BG%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=UA%3B30',
                'OptanonAlertBoxClosed': '2024-01-01T20:38:50.718Z',
                '_gat_UA-224801747-1': '1',
                'forterToken': '8c326367bd9244a6af9cd897ab9d3055_1704141529958__UDF43_13ck',
                '_ga_L7QE48HF7H': 'GS1.1.1704141123.1.1.1704141531.58.0.0',
                '_ga': 'GA1.1.1114810739.1704141123',
            }

            headers = {
                'authority': 'www.sears.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'SEARS',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'pragma': 'no-cache',
                # 'referer': 'https://www.sears.com/craftsman-3-drawer-portable-tool-chest/p-00935112000P',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/120.0.0.0 Safari/537.36',
            }

            params = {
                'storeName': 'Sears',
                'memberStatus': 'G',
                'zipCode': '10101',
            }

            response = requests.get(
                f'https://www.sears.com/api/sal/v3/products/details/{product_id}',
                params=params,
                cookies=cookies,
                headers=headers,
            )

            return response.json()
        except JSONDecodeError:
            print(f"Too many requests! Additional 10 seconds wait before retrying")
            time.sleep(10)


def get_parsed_data(product_id):
    response_json = get_response_json(product_id)
    try:
        product_raw_data = response_json['productDetail']['softhardProductdetails'][0]
        product = {'product_id': product_id,
                   'name': product_raw_data['descriptionName'],
                   'price': product_raw_data['price']['finalPrice'],
                   'short_description': product_raw_data['shortDescription'],
                   'brand': product_raw_data['brandName'],
                   'category': product_raw_data['hierarchies']['specificHierarchy'][-1]['name'],
                   'link_to_product': 'https://www.sears.com' + product_raw_data['seoUrl'],
                   'update_date': timezone.now()}
    except KeyError:
        product = None
        print(f"No product found with {product_id=}")
    return product