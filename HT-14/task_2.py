"""
Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова
і кінцева дати, продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
"""
import datetime
import requests

CURRENCY_CODES = ['USD', 'EUR']


def get_dates():
    print("Виберіть варіант:")
    print("1 - конкретна дата")
    print("2 - інтервал дат\n")

    choice = input("Ваш вибір (1/2)? ")

    if choice == "1":
        date_text = input("Введіть дату (РРРР-ММ-ДД): ")
        try:
            date = datetime.datetime.strptime(date_text, "%Y-%m-%d")
            if is_future_date(date):
                print("Введена дата з майбутнього\n")
                return get_dates()
            return [date]
        except ValueError:
            print("Невірний формат дати!\n")
            return get_dates()
    elif choice == "2":
        try:
            start_text = input("Початкова дата (РРРР-ММ-ДД): ")
            start_date = datetime.datetime.strptime(start_text, "%Y-%m-%d")

            end_text = input("Кінцева дата (РРРР-ММ-ДД): ")
            end_date = datetime.datetime.strptime(end_text, "%Y-%m-%d")

            if start_date > end_date:
                print("Початкова дата повинна бути меншою за кінцеву!")
                return get_dates()

            dates_range = []
            current_date = start_date
            while current_date <= end_date:
                dates_range.append(current_date)
                current_date += datetime.timedelta(days=1)

            return dates_range
        except ValueError:
            print("Невірний формат дати!\n")
            return get_dates()
    else:
        print("\nНевірний вибір! Виберіть 1 або 2.")
        return get_dates()


def is_future_date(date):
    today = datetime.datetime.now().date()
    return date.date() > today



def get_currency():
    currency = input("Введіть код валюти(USD \ EUR): ").upper()
    if currency not in CURRENCY_CODES:
        print("Невірний код валюти!")
        return get_currency()
    else:
        return currency


def get_rates(date, currency):
    url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date.strftime("%Y%m%d")}&json'
    resp = requests.get(url)
    resp.raise_for_status()

    rates = resp.json()
    for rate in rates:
        if rate['cc'] == currency:
            return rate['rate']


dates = get_dates()
currency = get_currency()

for date in dates:
    rate = get_rates(date, currency)
    print(f'{currency} до гривні на {date:%d.%m.%Y}: {rate}')
