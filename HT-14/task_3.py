"""
3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
 цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

base_url = 'http://quotes.toscrape.com'
url = base_url

quotes = []

while url:
    print(f'Parsing {url}...')
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    for quote in soup.select('.quote'):
        text = quote.find(class_='text').get_text(strip=True)
        author = quote.find(class_='author').get_text(strip=True)

        bio_url = quote.find('a')['href']
        bio_res = requests.get(urljoin(base_url, bio_url))
        bio_soup = BeautifulSoup(bio_res.text, 'html.parser')

        born_date = bio_soup.find(class_='author-born-date').get_text(strip=True)
        born_loc = bio_soup.find(class_='author-born-location').get_text(strip=True)
        bio = bio_soup.find(class_='author-description').get_text(strip=True)

        quotes.append({
            'text': text,
            'author': author,
            'born_date': born_date,
            'born_loc': born_loc,
            'bio': bio
        })

    next_btn = soup.find('li', class_='next')
    url = urljoin(base_url, next_btn.find('a')['href']) if next_btn else None


with open('quotes.csv', 'w', encoding='utf16') as f:
    writer = csv.DictWriter(f, fieldnames=quotes[0].keys())
    writer.writeheader()
    writer.writerows(quotes)

print('Parsing finished!')