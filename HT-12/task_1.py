"""
Банкомат 3.0
- реалізуйте видачу купюр за логікою видавання найменшої кількості купюр. Наприклад: 2560 --> 2х1000, 1х500, 3х20.
Будьте обережні з "жадібним алгоритмом"!
"""
import sqlite3
import random


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.db = sqlite3.connect("atm.db")
        self.sql = self.db.cursor()

    def check_user_balance(self, login):
        sql.execute("SELECT money FROM users WHERE login=?", (login,))
        user_money = sql.fetchone()
        if user_money:
            print(f"Ваш баланс: {user_money[0]} грн\n")

    def deposit_money(self, login):
        amount = int(input("Введіть суму, яку хочете додати: "))
        if amount <= 0:
            print("Сума має бути додатньою.\n")
            return
        if amount % 10 != 0:
            change = amount % 10
            amount -= change
            print(f"Сума {amount} грн буде додана на рахунок.")
            sql.execute(
                "UPDATE users SET money = money + ? WHERE login=?", (amount, self.login)
            )
            db.commit()
            print(f"Ваша сдача: {change} грн")

        else:
            sql.execute(
                "UPDATE users SET money = money + ? WHERE login=?", (amount, self.login)
            )
            db.commit()
            print("Гроші успішно додані на рахунок.\n")

    def withdraw_money(self, login):
        amount = int(input("Введіть суму, яку хочете зняти: "))
        if amount <= 0:
            print("Сума має бути додатньою.\n")
            return

        sql.execute("SELECT money FROM users WHERE login=?", (login,))
        user_money = sql.fetchone()[0]

        if amount > user_money:
            print("У вас недостатньо коштів на рахунку.\n")
            return

        if amount % 10 != 0:
            print(f"Неможливо зняти суму.\n")
            return

        sql.execute("SELECT * FROM atm")

        i = 7

        available_denominations_copy = [10, 20, 50, 100, 200, 500, 1000]

        remaining_amount = amount

        to_withdraw = {}

        atm_money = sql.fetchone()

        while i > 0 and remaining_amount > 0:

            remaining_amount = amount

            to_withdraw = {}

            atm_money = list(atm_money)

            atm_money_10 = int(atm_money[0])
            atm_money_20 = int(atm_money[1])

            if amount % 50 != 0 or atm_money_10 == 0 or atm_money_20 > 2 or amount > 40:
                atm_money[1] = atm_money[1] - 3
                atm_money.insert(3, 1)
                available_denominations_copy.insert(4, 60)

            for denom in sorted(available_denominations_copy, reverse=True):
                count = min(
                    remaining_amount // denom,
                    atm_money[available_denominations_copy.index(denom)],
                )
                if count > 0:
                    to_withdraw[denom] = count
                    remaining_amount -= count * denom

            try:
                available_denominations_copy.pop(i)
            except IndexError:
                pass

            i -= 1

        if remaining_amount == 0:
            sql.execute(
                "UPDATE users SET money = money - ? WHERE login=?", (amount, login)
            )
            db.commit()
            print(f"Успішно знято {amount} грн\n")

            print("Купюри для видачі:")
            for denom, count in to_withdraw.items():
                equiv_denom = denom
                equiv_count = count
                if equiv_denom == 60:
                    equiv_count = 3
                    equiv_denom = 20

                print(f"{equiv_denom} грн: {equiv_count} купюрами")

            for denom, count in to_withdraw.items():
                if denom == 60:
                    sql.execute(
                        f"UPDATE atm SET banknote20 = banknote20 - {3} WHERE banknote20 >= {3}"
                    )
                else:
                    sql.execute(
                        f"UPDATE atm SET banknote{denom} = banknote{denom} - {count} WHERE banknote{denom} >= {count}"
                    )

                db.commit()

        else:
            print(
                f"Неможливо зняти суму {amount} грн через обмеження в наявності купюр у банкоматі.\n"
            )


class ATM:
    def __init__(self):
        self.db = sqlite3.connect("atm.db")
        self.sql = self.db.cursor()

    def update_atm(self, banknotes):
        sql.execute("SELECT * FROM atm")
        row = sql.fetchone()

        if row:
            current_banknotes_dict = {
                "banknote10": row[0],
                "banknote20": row[1],
                "banknote50": row[2],
                "banknote100": row[3],
                "banknote200": row[4],
                "banknote500": row[5],
                "banknote1000": row[6],
            }

            can_update = True

            for key in banknotes:
                if banknotes[key] < 0:
                    print("Некоректні дані. Кількість купюр не може бути від'ємною.\n")
                    can_update = False
                    break
                current_amount = current_banknotes_dict.get(f"banknote{key}", 0)
                if current_amount + banknotes[key] < 0:
                    print(
                        f"Недостатньо купюр для зняття. Доступна кількість купюр номіналом {key} грн: {current_amount}\n"
                    )
                    can_update = False
                    break

            if can_update:
                for key in banknotes:
                    sql.execute(
                        f"UPDATE atm SET banknote{key} = banknote{key} + ? WHERE banknote{key} >= ?",
                        (banknotes[key], -banknotes[key]),
                    )
                db.commit()
                print("Операція виконана. Купюри успішно додано до банкомату.\n")
            else:
                print("Операція не виконана. Помилка під час додавання купюр.\n")
        else:
            print("Помилка: Банкомат порожній або немає даних.\n")

    def entrance_collector(self, login, password):
        sql.execute(
            "SELECT status FROM users WHERE login=? AND password=?", (login, password)
        )
        user_status = sql.fetchone()
        if user_status is not None and user_status[0] == 1:
            print("Ви ввійшли як інкасатор\n")
            return True
        else:
            return False

    def withdraw_from_atm(self, banknotes):
        sql.execute("SELECT * FROM atm")
        current_banknotes = sql.fetchone()

        if current_banknotes:
            current_banknotes_dict = {
                "banknote10": current_banknotes[0],
                "banknote20": current_banknotes[1],
                "banknote50": current_banknotes[2],
                "banknote100": current_banknotes[3],
                "banknote200": current_banknotes[4],
                "banknote500": current_banknotes[5],
                "banknote1000": current_banknotes[6],
            }

            can_withdraw = True

            for key in banknotes:
                if banknotes[key] > current_banknotes_dict[f"banknote{key}"]:
                    can_withdraw = False
                    break
                if current_banknotes_dict[f"banknote{key}"] - banknotes[key] < 0:
                    can_withdraw = False
                    break

            if can_withdraw:
                for key in banknotes:
                    sql.execute(
                        f"UPDATE atm SET banknote{key} = banknote{key} - ? WHERE banknote{key} >= ?",
                        (banknotes[key], banknotes[key]),
                    )
                db.commit()
                print("Операція виконана.\n")
            else:
                print("Недостатньо купюр для зняття або некоректні дані.\n")
        else:
            print("Помилка: Банкомат порожній або немає даних.\n")

    def check_balance(self):
        sql.execute("SELECT * FROM atm")
        row = sql.fetchone()
        if row:
            print(f"Сумма купюр {sum(row)}\n")
            print(f"Сумма грошей {self.calculate_total_money(row)}\n")
            print(
                f"10 грн: {row[0]}, 20 грн: {row[1]}, 50 грн: {row[2]}, 100 грн: {row[3]}, 200 грн: {row[4]}, 500 грн: {row[5]}, 1000 грн: {row[6]}\n"
            )

    def calculate_total_money(self, dig):
        denominations = [10, 20, 50, 100, 200, 500, 1000]
        total_money = sum(qty * denom for qty, denom in zip(dig, denominations))
        return total_money

    def menu_collector(self):
        while True:
            print("Виберіть дію:")
            print("1. Перевірити баланс банкомату та кількість купюр")
            print("2. Додати купюри до банкомату")
            print("3. Зняти купюри з банкомату")
            print("4. Вихід\n")

            choice = input("Введіть ваш вибір: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                banknotes_to_add = {
                    10: int(input("Кількість купюр номіналом 10 грн: ")),
                    20: int(input("Кількість купюр номіналом 20 грн: ")),
                    50: int(input("Кількість купюр номіналом 50 грн: ")),
                    100: int(input("Кількість купюр номіналом 100 грн: ")),
                    200: int(input("Кількість купюр номіналом 200 грн: ")),
                    500: int(input("Кількість купюр номіналом 500 грн: ")),
                    1000: int(input("Кількість купюр номіналом 1000 грн: ")),
                }
                self.update_atm(banknotes_to_add)

            elif choice == "3":
                banknotes_to_withdraw = {
                    10: int(input("Кількість купюр номіналом 10 грн: ")),
                    20: int(input("Кількість купюр номіналом 20 грн: ")),
                    50: int(input("Кількість купюр номіналом 50 грн: ")),
                    100: int(input("Кількість купюр номіналом 100 грн: ")),
                    200: int(input("Кількість купюр номіналом 200 грн: ")),
                    500: int(input("Кількість купюр номіналом 500 грн: ")),
                    1000: int(input("Кількість купюр номіналом 1000 грн: ")),
                }
                self.withdraw_from_atm(banknotes_to_withdraw)

            elif choice == "4":
                print("До побачення!\n")
                break

            else:
                print("Невірний вибір. Спробуйте ще раз.\n")

    def user_menu(self, login):
        while True:
            print("Виберіть дію:")
            print("1. Перевірити баланс")
            print("2. Поповнити рахунок")
            print("3. Зняти гроші")
            print("4. Вихід\n")

            choice = input("Введіть ваш вибір: ")

            if choice == "1":
                user.check_user_balance(login)
            elif choice == "2":
                user.deposit_money(login)
            elif choice == "3":
                user.withdraw_money(login)
            elif choice == "4":
                print("До побачення!\n")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.\n")

    def validate_password(self, password):
        min_length = 5

        if len(password) < min_length:
            return print(
                "Пароль занадто короткий. Мінімальна довжина: {} символів.\n".format(
                    min_length
                )
            )

        else:
            if not any(char.isdigit() for char in password):
                return print("Пароль повинен містити хоча б одну цифру.\n")
            else:
                return True


global sql
db = sqlite3.connect("atm.db")
sql = db.cursor()

sql.execute(
    "CREATE TABLE IF NOT EXISTS users (\n"
    "login TEXT, \n"
    "password TEXT, \n"
    "money BIGINT, \n"
    "status BIGINT \n"
    ")"
)

sql.execute(
    "CREATE TABLE IF NOT EXISTS atm (\n"
    "banknote10 BIGINT, \n"
    "banknote20 BIGINT, \n"
    "banknote50 BIGINT,\n"
    "banknote100 BIGINT,\n"
    "banknote200 BIGINT,\n"
    "banknote500 BIGINT,\n"
    "banknote1000 BIGINT\n"
    ")"
)
db.commit()
atm = ATM()

print(
    "Вас вітає банкомат, введіть свій логін та пароль якщо ви зареєстровані, або хочете зареєструватись\n"
)
while True:
    user_login = input("Логін:")
    user_password = input("Пароль:")
    if atm.entrance_collector(user_login, user_password):
        atm.menu_collector()

    elif atm.validate_password(user_password):
        sql.execute("SELECT login FROM users WHERE login=?", (user_login,))
        existing_user = sql.fetchone()
        if existing_user is None:
            sql.execute(
                "INSERT INTO users VALUES (?,?,?,?)", (user_login, user_password, 0, 0)
            )
            db.commit()
            print("Ви успішно зареєструвалися\n")
            random_number = random.randint(1, 100)
            if random_number <= 10:
                self.sql.execute(
                    "UPDATE users SET account_balance = account_balance + ? WHERE login = ?",
                    (100,  login),
                )
                db.commit()
                print("Вам начислено 100 гривен на счет\n")
            user = User(user_login, user_password)
            atm.user_menu(user_login)
        else:
            print("Ви успішно ввішли в систему\n")
            user = User(user_login, user_password)
            atm.user_menu(user_login)
