"""
Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями. Створiть просту умовну конструкцiю
(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних
"x" та "y" та у випадку нервіності - виводити ще і різницю.
    Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      вiдповiдь - "х дорiвнює z"
"""


def compare_numbers(x, y):
    if x > y:
        result = f"x більше ніж у на {x - y}"
    elif x < y:
        result = f"у більше ніж х на {y - x}"
    else:
        result = "x дорівнює y"

    return result


x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))

result_message = compare_numbers(x, y)
print(result_message)
