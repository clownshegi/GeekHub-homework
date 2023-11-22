"""
Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції
 з 2-ма числами, а саме додавання, віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повенен повернути результат виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
"""
class Calc:
    """
    Клас Calc призначений для виконання математичних операцій та збереження результатів.

    """

    def __init__(self):
        """
        Ініціалізує клас Calc з початковим значенням last_result, який дорівнює None.
        """
        self.last_result = None

    def add(self, a, b):
        """
        Додає два числа.

        Args:
            a (int, float): Перше число.
            b (int, float): Друге число.

        Returns:
            int, float: Результат додавання a та b.
        """
        self.last_result = a + b
        return self.last_result

    def subtract(self, a, b):
        """
        Віднімає одне число від іншого.

        Args:
            a (int, float): Перше число.
            b (int, float): Число, яке потрібно відняти від першого числа.

        Returns:
            int, float: Результат віднімання b від a.
        """
        self.last_result = a - b
        return self.last_result

    def multiply(self, a, b):
        """
        Перемножує два числа.

        Args:
            a (int, float): Перше число.
            b (int, float): Друге число.

        Returns:
            int, float: Результат множення a на b.
        """
        self.last_result = a * b
        return self.last_result

    def divide(self, a, b):
        """
        Ділить одне число на інше.

        Args:
            a (int, float): Число, яке потрібно поділити.
            b (int, float): Число, на яке потрібно поділити.
.
        """
        if b == 0:
            return "Error: Не можна ділити на нуль"
        self.last_result = a / b
        return self.last_result


calculator = Calc()

print(calculator.last_result)  # Виведе None
print(calculator.add(1, 1))  # Додає 1 та 1, результат 2
print(calculator.last_result)  # Виведе 2
print(calculator.multiply(2, 3))  # Множить 2 на попередній результат 2, результат 6
print(calculator.last_result)  # Виведе 6
print(calculator.multiply(3, 4))  # Множить 3 на попередній результат 6, результат 18
print(calculator.last_result)  # Виведе 18
