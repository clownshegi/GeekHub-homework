# 5. Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.
input_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2,
    'f': 4,
    'g': 5,
    'h': 5,
    'i': 6,
    'j': 7,
    'k': 7,
    'l': 8
}

unique_dict = {}
for key, value in input_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value

print("Словарь с удаленными дубликатами:", unique_dict)
