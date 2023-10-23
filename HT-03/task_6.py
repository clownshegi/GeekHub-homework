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

max_value = 0
min_value = 0

for value in my_dict.values():
    if isinstance(value, int):
        if  value > max_value:
            max_value = value
        if  value < min_value:
            min_value = value

if max_value is not None:
    print("Максимальное значение:", max_value)
else:
    print("Нету чисел для максимума")

if min_value is not None:
    print("Минимальное значение:", min_value)
else:
    print("Нет целых чисел для минимума")

