"""
Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел
 всередині цього діапазона. Не забудьте про перевірку на валідність введених даних та у випадку невідповідності
 - виведіть повідомлення.
"""


def is_prime(number):
    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False

        i += 6

    return True


def prime_list(start, end):
    if not (isinstance(start, int) and isinstance(end, int) and start >= 0 and end <= 1000):
        print("Початок і кінець діапазону повинні бути цілими числами від 0 до 1000.")
        return []

    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


start_range = 0
end_range = 1000

result = prime_list(start_range, end_range)
print(f"Прості числа в діапазоні від {start_range} до {end_range}: {result}")
