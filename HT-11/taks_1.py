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
    Клас Calc для виконання математичних операцій та збереження результату попередньої операції.

    Атрибути:
        last_result  Зберігає результат останньої проведеної операції. Початкове значення - None.
    """

    def __init__(self):
        """Ініціалізує клас Calc, встановлюючи початкове значення last_result на None."""
        self.last_result = None

    def add(self, a, b):
        """
        Виконує операцію додавання двох чисел та зберігає результат як попередній результат.

        Приклад:
            calculator.add(2, 3)
            2 + 3
            last_result --> None
        """
        result = a + b
        prev_result = self.last_result
        self.last_result = result
        if prev_result is None:
            print(f"{a} + {b}\nlast_result --> None")
        else:
            print(f"{a} + {b}\nlast_result --> {prev_result}")
        return self

    def subtract(self, a, b):
        """Віднімає число b від числа a."""
        result = a - b
        prev_result = self.last_result
        self.last_result = result
        if prev_result is None:
            print(f"{a} - {b}\nlast_result --> None")
        else:
            print(f"{a} - {b}\nlast_result --> {prev_result}")
        return self

    def multiply(self, a, b):
        """Множить число a на число b."""
        result = a * b
        prev_result = self.last_result
        self.last_result = result
        if prev_result is None:
            print(f"{a} * {b}\nlast_result --> None")
        else:
            print(f"{a} * {b}\nlast_result --> {prev_result}")
        return self

    def divide(self, a, b):
        """Ділить число a на число b."""
        if b == 0:
            print("Cannot divide by zero")
            return self
        result = a / b
        prev_result = self.last_result
        self.last_result = result
        if prev_result is None:
            print(f"{a} / {b}\nlast_result --> None")
        else:
            print(f"{a} / {b}\nlast_result --> {prev_result}")
        return self


calculator = Calc()

calculator.add(1, 1).multiply(2, 3).multiply(3, 4)
