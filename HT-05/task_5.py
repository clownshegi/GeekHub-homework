# Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку зробити! Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2). Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями на предмет помилок!

def calculator(operator, operand1, operand2):
    try:
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                return "Деление на ноль невозможно"
            result = operand1 / operand2
        elif operator == '%':
            result = operand1 % operand2
        elif operator == '//':
            if operand2 == 0:
                return "Деление на ноль невозможно"
            result = operand1 // operand2
        elif operator == '**':
            result = operand1 ** operand2
        else:
            return "Неизвестный оператор"
        return f"Результат: {result}"
    except ZeroDivisionError:
        return "Деление на ноль невозможно"
    except Exception as e:
        return f"Ошибка: {e}"

operator = input("Введите оператор (+, -, *, /, %, //, **): ")
operand1 = float(input("Введите первый операнд: "))
operand2 = float(input("Введите второй операнд: "))

result = calculator(operator, operand1, operand2)
print(result)
