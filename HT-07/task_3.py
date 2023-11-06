"""
На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції)
    - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує
   для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
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


user_data = [
    ("vasya", "wasd"),
    ("vasya", "vasyapupkin2000"),
    ("user123", "password123"),
    ("alice", "Pa$$w0rd"),
    ("john_doe", "JohnDoe123"),
    ("username_with_long_name", "1234")
]

for username, password in user_data:
    try:
        validate_username_password(username, password)
        status = "OK"
    except ValidationException as e:
        status = str(e)

    print("Name:", username)
    print("Password:", password)
    print("Status:", status)
    print("-----")
