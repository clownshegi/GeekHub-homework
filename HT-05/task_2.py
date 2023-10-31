"""
Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат (напр. інпут від юзера,
результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині викликає 3 попереднi,обробляє
їх результат та також повертає результат своєї роботи.
Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3."""


def get_user_integer():
    while True:
        try:
            user_input = int(input("Введите целое число: "))
            return user_input
        except ValueError:
            print("Ошибка. Введите целое число.")


def square_number(number):
    return number ** 2


def double_number(number):
    return number * 2


def process_data():
    user_integer = get_user_integer()
    squared = square_number(user_integer)
    doubled = double_number(user_integer)

    return f"Введено число: {user_integer}, его квадрат: {squared}, удвоенное значение: {doubled}"


result = process_data()
print(result)
