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
    except Exception as e:
        return f"Ошибка: {e}"


operator = input("Введите оператор (+, -, *, /, %, //, **): ")
operand_1 = float(input("Введите первый операнд: "))
operand_2 = float(input("Введите второй операнд: "))

result = calculator(operator, operand_1, operand_2)
print(result)
