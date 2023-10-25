# Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
# Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в float, а якщо і там ловить помилку - пропонує ввести значення ще раз (зручніше на даному етапі навчання для цього використати цикл while)
# Виводить результат ділення першого на друге. Якщо при цьому виникає помилка - оброблює її і виводить відповідне повідомлення
while True:
    try:
        input_1 = input("Введите первое число (int или float): ")
        number1 = int(input_1)
        break
    except ValueError:
        try:
            number1 = float(input_1)
            break
        except ValueError:
            print("Неверный формат числа. Попробуйте еще раз.")

while True:
    try:

        input_2 = input("Введите второе число (int или float): ")
        number2 = int(input_2)
        break
    except ValueError:
        try:
            number2 = float(input_2)
            break
        except ValueError:
            print("Неверный формат числа. Попробуйте еще раз.")

try:
    result = number1 / number2
    print(f"Результат деления: {result}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль.")
except Exception as e:
    print(f"Ошибка: {e}")
