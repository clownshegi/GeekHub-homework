"""
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій -
необов'язковий параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція вертає False
        якщо silent == False -породжується виключення LoginException (його також треба створити =))

"""


class LoginException(Exception):
    def __init__(self, message="Неправильна пара ім'я/пароль"):
        super().__init__(message)


def check_credentials(username, password, silent=False):
    users = [
        {"username": "user1", "password": "pass1"},
        {"username": "user2", "password": "pass2"},
        {"username": "user3", "password": "pass3"},
        {"username": "user4", "password": "pass4"},
        {"username": "user5", "password": "pass5"}
    ]

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True

    if silent:
        return False
    else:
        raise LoginException()


try:
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")
    result = check_credentials(username, password)
    if result:
        print("Ви увійшли в систему.")
    else:
        print("Неправильна пара ім'я/пароль.")
except LoginException as e:
    print(e)
