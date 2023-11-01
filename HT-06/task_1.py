"""
Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення у вигляді кортежа:
периметр квадрата, площа квадрата та його діагональ.
"""


def square(side_length):
    perimeter = 4 * side_length

    area = side_length ** 2

    diagonal = (2 ** 0.5) * side_length

    return (perimeter, area, diagonal)


side = 5
result = square(side)
print(f"Периметр: {result[0]}, Площа: {result[1]}, Діагональ: {result[2]}")
