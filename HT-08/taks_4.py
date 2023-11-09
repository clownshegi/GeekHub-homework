"""
Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж)
і повертає генератор, який буде вертати значення з цієї послідовності, при цьому,
 якщо було повернено останній елемент із послідовності - ітерація починається знову.
"""
from itertools import cycle


def generator(iterable):
    cyclic_iterator = cycle(iterable)
    for item in cyclic_iterator:
        yield item


sequence = [1, 2, 3]

for elem in generator(sequence):
    print(elem)
