"""
Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>)
       та історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних
      (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається.
       Але якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль).
       Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
       (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
"""
import csv
import json
from datetime import datetime


def check_credentials(username, password):
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Username"] == username and row["Password"] == password:
                return True
    return False


def update_balance(username, amount):
    balance_file_path = f"{username}_balance.txt"
    with open(balance_file_path, "r") as file:
        current_balance = int(file.read())
    new_balance = current_balance + amount
    with open(balance_file_path, "w") as file:
        file.write(str(new_balance))

    transaction_file_path = f"{username}_transactions.json"
    transaction = {"amount": amount, "timestamp": str(datetime.now())}
    with open(transaction_file_path, "a") as file:
        file.write(json.dumps(transaction) + "\n")


def check_balance(username):
    balance_file_path = f"{username}_balance.txt"
    with open(balance_file_path, "r") as file:
        current_balance = file.read()
    print(f"Ваш поточний баланс: {current_balance}")


def deposit_money(username):
    amount = int(input("Введіть суму для внесення: "))
    if amount < 0:
        print("Ви не можете внести від'ємну суму.")
        return
    update_balance(username, amount)
    print(f"Успішно внесено {amount} гривень.")


def withdraw_money(username):
    balance_file_path = f"{username}_balance.txt"
    with open(balance_file_path, "r") as file:
        current_balance = int(file.read())
    amount = int(input("Введіть суму для зняття: "))
    if amount < 0:
        print("Ви не можете зняти від'ємну суму.")
    elif amount > current_balance:
        print("Недостатньо коштів.")
    else:
        update_balance(username, -amount)
        print(f"Успішно знято {amount} гривень.")


def start():
    while True:
        username = input("Введіть ваше ім'я користувача: ")
        password = input("Введіть ваш пароль: ")

        if check_credentials(username, password):
            print("Успішний вхід!")
            menu(username)
            break
        else:
            print("Невірні облікові дані. Спробуйте ще раз.")


def menu(username):
    while True:
        print("Виберіть дію:")
        print("1. Перевірити баланс")
        print("2. Поповнити рахунок")
        print("3. Зняти кошти")
        print("4. Вихід")

        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            check_balance(username)
        elif choice == "2":
            deposit_money(username)
        elif choice == "3":
            withdraw_money(username)
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    start()
