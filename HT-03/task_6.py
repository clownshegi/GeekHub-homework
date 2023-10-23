#6. Write a script to get the maximum and minimum value in a dictionary.
my_dict = {
    'a': 10,
    'b': 5,
    'c': 20,
    'd': 30,
    'e': 5,
    'f': 15,
    'g': 25,
    'h': 35,
    'i': 40,
    'j': 45,
    'k': 50,
    'l': 55
}

max_value = max(my_dict.values())
min_value = min(my_dict.values())

print("Макс. значение:", max_value)
print("Мини. значение:", min_value)
