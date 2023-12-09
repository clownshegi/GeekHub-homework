import scrapy
from bs4 import BeautifulSoup


class MyGoogleSpider(scrapy.Spider):
    name = 'my_google_spider'
    start_urls = ['https://chrome.google.com/webstore/sitemap']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        for sitemap_loc in soup.select('sitemap > loc'):
            yield scrapy.Request(url=sitemap_loc.text, callback=self.parse_urls)

    def parse_urls(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        for url_loc in soup.select('url > loc'):
            if "/detail" not in url_loc.text:
                continue
            yield scrapy.Request(url=url_loc.text, callback=self.parse_extensions)

    def parse_extensions(self, response):
        extension_id = response.css('[property="og:url"]::attr(content)').get().split('/').pop()
        yield {
            'extension_id': f'{extension_id}',
            'extension_name': response.css('[property="og:title"]::attr(content)').get(),
            'extension_description': response.css('[property="og:description"]::attr(content)').get()
        }
