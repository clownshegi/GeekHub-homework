"""
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
"""


class ValidationException(Exception):
    pass


def validate_username_password(username, password):
    if not (3 <= len(username) <= 50):
        raise ValidationException("Ім'я повинно бути від 3 до 50 символів.")

    if not (8 <= len(password) and any(c.isdigit() for c in password)):
        raise ValidationException("Пароль повинен бути не менше 8 символів і містити хоча б одну цифру.")

    if username in password:
        raise ValidationException("Пароль не повинен містити ім'я користувача.")


try:
    username = "user123"
    password = "user5121"
    validate_username_password(username, password)
    print("Пара ім'я/пароль пройшла валідацію.")
except ValidationException as e:
    print(f"Помилка валідації: {e}")
