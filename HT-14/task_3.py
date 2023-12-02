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

url = 'http://quotes.toscrape.com/page/{}/'
base_url = 'http://quotes.toscrape.com'

quotes = []

for page in range(1, 11):
    print(f'Парсинг сторінки {page}')
    res = requests.get(url.format(page))
    soup = BeautifulSoup(res.text, 'html.parser')

    for quote in soup.find_all(class_='quote'):
        text = quote.find(class_='text').get_text(strip=True)
        author = quote.find(class_='author').get_text(strip=True)

        bio_link = quote.find('a')['href']
        bio_link = urljoin(base_url, bio_link)

        bio_res = requests.get(bio_link)
        bio_soup = BeautifulSoup(bio_res.text, 'html.parser')

        born_date = bio_soup.find(class_='author-born-date').get_text(strip=True)
        born_location = bio_soup.find(class_='author-born-location').get_text(strip=True)
        bio = bio_soup.find(class_='author-description').get_text(strip=True)

        quotes.append({
            'text': text,
            'author': author,
            'born_date': born_date,
            'born_location': born_location,
            'bio': bio
        })

with open('quotes.csv', 'w', encoding='utf-16') as file:
    writer = csv.writer(file)

    for quote in quotes:
        writer.writerow([])
        writer.writerow([quote['text']])
        writer.writerow([quote['author']])
        writer.writerow([quote['born_date']])
        writer.writerow([quote['born_location']])
        writer.writerow([quote['bio']])

print('parsing finished')

print('Парсинг закінчено, цитати збережено у quotes.csv')
