##Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.
user_input = input("Введите положительное целое число: ")

if user_input.isdigit():
    user_number = int(user_input)

    if user_number > 0:
        total_sum = sum(range(1, user_number + 1))
        print("Сумма первых {} положительных целых чисел: {}".format(user_number, total_sum))
    else:
        print("Пожалуйста, введите положительное целое число.")
else:
    print("Неверный ввод. Пожалуйста, введите допустимое целое число.")
