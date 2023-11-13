"""
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
"""


def my_range(start, stop, step=1):
    if step == 0:
        raise ValueError("Step cannot be zero")

    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        return

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

for i in my_range(1, 1000, 21):
    print(i)

