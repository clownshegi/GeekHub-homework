"""
Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі <a> одиниць строком
на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються
до суми вкладу і в наступному році на них також нараховуються відсотки).
Параметр <percents> є необов'язковим і має значення по замовчуванню <10> (10%). Функція повинна принтануть суму,
 яка буде на рахунку, а також її повернути (але округлену до копійок).
"""


def bank(amount, years, percents=0):
    for year in range(years):
        inter = amount * (percents / 100)
        amount += inter

    amount = round(amount, 2)
    return amount


initial_deposit = 1000
deposit_years = 5
river_price = 10

final_amount = bank(initial_deposit, deposit_years, river_price)
print(f"Кінцева сума вкладу після {deposit_years} років: {final_amount:.2f}")
