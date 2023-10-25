# Create a Python script that takes an age as input. If the age is less than 18 or greater than 120, raise a custom exception called InvalidAgeError. Handle the InvalidAgeError by displaying an appropriate error message.
class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Введите ваш возраст: "))

    if age < 18 or age > 120:
        raise InvalidAgeError("Недопустимый возраст. Возраст должен быть от 18 до 120 лет.")

    print("Ваш возраст:", age)

except InvalidAgeError as e:
    print("Ошибка:", e)
except ValueError:
    print("Ошибка: Пожалуйста, введите корректный возраст в виде числа.")
