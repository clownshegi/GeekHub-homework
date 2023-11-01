"""
 Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True,
  якщо це число просте і False - якщо ні.
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


number_to_check = 9
if is_prime(number_to_check):
    print(f"{number_to_check} є простим числом.")
else:
    print(f"{number_to_check} не є простим числом.")
