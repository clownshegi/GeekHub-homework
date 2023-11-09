"""
Напишіть функцію, яка приймає 2 списки. Результатом має бути новий список, в якому знаходяться елементи першого списку,
 яких немає в другому. Порядок елементів, що залишилися має відповідати порядку в першому (оригінальному) списку.
 Реалізуйте обчислення за допомогою генератора.

"""


def array_diff(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result


result1 = array_diff([1, 2], [1])  # [2]
result2 = array_diff([1, 2, 2, 2, 4, 3, 4], [2])  # [1, 4, 3, 4]

print(result1)
print(result2)