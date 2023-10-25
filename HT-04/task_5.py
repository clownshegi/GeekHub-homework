#Create a Python program that repeatedly prompts the user for a number until a valid integer is provided. Use a try/except block to handle any ValueError exceptions, and keep asking for input until a valid integer is entered. Display the final valid integer.

while True:
    user_input = input("Введите целое число: ")

    try:
        user_number = int(user_input)
        print("Введено корректное целое число:", user_number)
        break  

    except ValueError:
        print("Ошибка: Неверный формат числа. Пожалуйста, введите целое число.")

    except TypeError:
        print("Ошибка: Неправильный тип данных. Пожалуйста, введите целое число.")

    except OverflowError:
        print("Ошибка: Превышено допустимое значение. Пожалуйста, введите целое число, не превышающее максимальное значение.")

