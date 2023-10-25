# Create a custom exception class called NegativeValueError. Write a Python program that takes an integer as input and raises the NegativeValueError if the input is negative. Handle this custom exception with a try/except block and display an error message.
class NegativeValueError(Exception):
    pass


def check_positive_input(value):
    if value < 0:
        raise NegativeValueError("Отрицательные значения не допускаются")


try:
    num = int(input("Введите целое число: "))

    check_positive_input(num)

    print("Вы ввели:", num)

except NegativeValueError as e:
    print("Ошибка:", e)
except ValueError:
    print("Ошибка: Пожалуйста, введите корректное целое число")
