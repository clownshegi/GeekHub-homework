"""
Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньомy
і виводить результат. Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
"""


def count_elements(input_list):
    element_count = {}
    for item in input_list:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1

    result = ', '.join(f"{key} -> {value}" for key, value in element_count.items())
    return result


input_list = [1, 1, 'foo', (1, 2), True, 'foo', 1, (1, 2)]
result = count_elements(input_list)
print(result)
