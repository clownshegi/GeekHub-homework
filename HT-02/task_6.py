##Write a script to check whether a value from user input is contained in a group of values.
group_of_values = [1, 2, 'u', 'a', 4, True]

user_input = input("Введите значение: ")

if user_input.isdigit():
    user_input = int(user_input)
elif user_input == 'True':
    user_input = True
elif user_input == 'False':
    user_input = False
else:
    user_input = str(user_input)

is_contained = user_input in group_of_values

print(is_contained)
