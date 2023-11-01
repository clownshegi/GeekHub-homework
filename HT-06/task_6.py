"""
Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто функція приймає два аргументи:
 список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки -
 пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""


def cyclic_shift(arr, shift):
    if shift > 0:
        shift = shift % len(arr)
        return arr[-shift:] + arr[:-shift]
    elif shift < 0:
        shift = abs(shift) % len(arr)
        return arr[shift:] + arr[:shift]
    else:
        return arr


list1 = [1, 2, 3, 4, 5]
shifted_list1 = cyclic_shift(list1, 1)
print(shifted_list1)

list2 = [1, 2, 3, 4, 5]
shifted_list2 = cyclic_shift(list2, -2)
print(shifted_list2)
