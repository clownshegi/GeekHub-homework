"""
Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних букв та цифр,
 які зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих і малих).
 Реалізуйте обчислення за допомогою генератора.
"""


def count_repeated_chars(s):
    char_count = {}

    for char in s:
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1

    repeated_chars = (char for char, count in char_count.items() if count > 1)

    return len(list(repeated_chars))


print(count_repeated_chars("abcde"))  # 0
print(count_repeated_chars("aabbcde"))  # 2
print(count_repeated_chars("aabBcde"))  # 2
print(count_repeated_chars("indivisibility"))  # 1
print(count_repeated_chars("Indivisibilities"))  # 2
print(count_repeated_chars("aA11"))  # 2
print(count_repeated_chars("ABBA"))  # 2
