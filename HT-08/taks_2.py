"""
Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100),
сума цифр кожного елемент якого буде дорівнювати 10.
"""
result = [x for x in range(101) if sum(int(digit) for digit in str(x)) == 10]
print(result)