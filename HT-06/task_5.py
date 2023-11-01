"""
 Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
"""


def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b


max_number = int(input("Введіть максимальне число Фібоначчі: "))
fibonacci(max_number)
