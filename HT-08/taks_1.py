"""
Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), кожен елемент якого буде ділитись без остачі
 на 5 але не буде ділитись на 3.
"""
result = [x for x in range(101) if x % 5 == 0 and x % 3 != 0]
print(result)
