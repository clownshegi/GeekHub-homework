##Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
input_numbers = input("Введите последовательность чисел, разделенных запятыми: ")

numbers_list = input_numbers.split(',')

numbers_list = [int(num) for num in numbers_list]

numbers_tuple = tuple(numbers_list)

print("Созданный список:", numbers_list)
print("Созданный кортеж:", numbers_tuple)