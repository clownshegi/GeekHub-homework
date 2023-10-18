##Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end script must print out result of concatenating all <number> strings.
number_of_strings = int(input("Введите количество строк: "))

result_string = ""

for i in range(number_of_strings):
    user_input = input("Введите строку: ")
    result_string += user_input

print("Результат конкатенации:", result_string)
