# 7. Write a script which accepts a <number> from user and generates dictionary in range <number> where key is <number> and value is <number>*<number>
#   e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}
user_number = int(input("Введите число: "))

result_dict = {}
for i in range(user_number + 1):
    result_dict[i] = i * i

print(result_dict)
