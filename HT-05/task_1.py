"""
Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року, якiй цей
мiсяць належить (зима, весна, лiто або осiнь).
У випадку некоректного введеного значення - виводити відповідне повідомлення.

"""


def season(month):
    if 1 <= month <= 12:
        if month in [12, 1, 2]:
            return "зима"
        elif month in [3, 4, 5]:
            return "весна"
        elif month in [6, 7, 8]:
            return "лето"
        else:
            return "осень"
    else:
        return "Некорректное значение. Введите номер месяца от 1 до 12."


month_number = int(input("Введите номер месяца (от 1 до 12): "))
result = season(month_number)
print(f"Месяц номер {month_number} принадлежит к сезону: {result}")
