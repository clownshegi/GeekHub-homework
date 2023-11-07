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


def check_credentials(credentials):
    try:
        username = credentials["username"]
        password = credentials["password"]
        validate_username_password(username, password)
        status = "OK"
    except ValidationException as e:
        status = str(e)

    return f"Name: {username}\nPassword: {password}\nStatus: {status}\n{'-' * 5}"


user_data = [
    {"username": "vasya", "password": "wasd"},
    {"username": "vasya", "password": "vasyapupkin2000"},
    {"username": "user123", "password": "password123"},
    {"username": "alice", "password": "Pa$$w0rd"},
    {"username": "john_doe", "password": "JohnDoe123"},
    {"username": "username_with_long_name", "password": "1234"}
]

for credentials in user_data:
    print(check_credentials(credentials))
