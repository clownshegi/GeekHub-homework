##Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end script must print out result of concatenating all <number> strings.
number_of_strings = int(input("Введите количество строк: "))

user_inputs = []

for i in range(number_of_strings):
    user_input = input("Введите строку: ")
    user_inputs.append(user_input)

result_string = ''.join(user_inputs)

print("Результат конкатенации:", result_string)
