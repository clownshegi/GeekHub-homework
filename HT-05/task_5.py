"""
Ну і традиційно - калькулятор  Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2).
Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями
на предмет помилок!
"""


def calculator(operator, operand_1, operand_2):
    try:
        if operator == '+':
            result = operand_1 + operand_2
        elif operator == '-':
            result = operand_1 - operand_2
        elif operator == '*':
            result = operand_1 * operand_2
        elif operator == '/':
            result = operand_1 / operand_2
        elif operator == '%':
            result = operand_1 % operand_2
        elif operator == '//':
            result = operand_1 // operand_2
        elif operator == '**':
            result = operand_1 ** operand_2
        else:
            return "Неизвестный оператор"
        return f"Результат: {result}"
    except ZeroDivisionError:
        return "Деление на ноль невозможно"


operator = input("Введите оператор (+, -, *, /, %, //, **): ")
operand_1 = float(input("Введите первый операнд: "))
operand_2 = float(input("Введите второй операнд: "))

result = calculator(operator, operand_1, operand_2)
print(result)
