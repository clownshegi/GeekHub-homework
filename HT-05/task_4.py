"""
 Наприклад маємо рядок -->
 "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345"
 -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)
"""


def process_string(input_string):
    length = len(input_string)
    letters = sum(c.isalpha() for c in input_string)
    digits = sum(c.isdigit() for c in input_string)

    if 30 <= length <= 50:
        print(f"Длина строки: {length}, Количество букв: {letters}, Количество цифр: {digits}")
    elif length < 30:
        digit_sum = sum(int(c) for c in input_string if c.isdigit())
        letters_only = ''.join(c for c in input_string if c.isalpha())
        print(f"Сумма всех чисел: {digit_sum}, Строка без цифр: {letters_only}")
    elif length > 50:
        print("didn't come up with anything interesting(")


input_string = "  65jnpoj35po6j345"
process_string(input_string)
