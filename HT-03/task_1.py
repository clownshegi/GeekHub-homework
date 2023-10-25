#1. Write a script that will run through a list of tuples and replace the last value for each tuple. The list of tuples can be hardcoded. The "replacement" value is entered by user. The number of elements in the tuples must be different.

list_of_tuples = [(11, 23, 64), ('dsa', 'badsad', 'cdsa', 'd'), (True, False, 28, 'Geek')]

replacement = input("Введите значение для замены: ")

for i in range(len(list_of_tuples)):
    current_tuple = list(list_of_tuples[i])
    current_tuple[-1] = replacement
    list_of_tuples[i] = tuple(current_tuple)

print("Обновленный список кортежей:")
for tuples in list_of_tuples:
    print(tuples)
