"""
Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж)
і повертає генератор, який буде вертати значення з цієї послідовності, при цьому,
 якщо було повернено останній елемент із послідовності - ітерація починається знову.
"""
def my_cycle(iterable):
    while True:
        for item in iterable:
            yield item

sequence = [1, 2, 3]

cyclic_generator = my_cycle(sequence)

for elem in range(10):
    print(next(cyclic_generator))

