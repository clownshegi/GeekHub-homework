"""
Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів. Якщо в попередньому завданні
    ви добре продумали структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити новго користувача (при створенні новго користувача,
    перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор, який матиме розширені
    можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному номіналу що підтримує банкомат.
    В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на
    баланс/кількість купюр банкомату, лише збільшуєтсья баланс користувача (моделюємо наявність двох незалежних касе
    т в банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (не вірний логін/пароль,
    недостатньо коштів на раунку, неможливо видати суму наявними купюрами тощо.)
"""
import sqlite3

def entrance_collector(login, password):
    sql.execute("SELECT status FROM users WHERE login=? AND password=?", (login, password))
    user_status = sql.fetchone()
    if user_status is not None and user_status[0] == 1:  # Assuming status = 1 for collector
        print("Ви ввійшли як інкасатор")
        return True
    else:
        return False


def validate_password(password):
    min_length = 5

    if len(password) < min_length:
        return print("Пароль занадто короткий. Мінімальна довжина: {} символів.".format(min_length))

    else:
        if not any(char.isdigit() for char in password):
            return print("Пароль повинен містити хоча б одну цифру.")
        else:
            return True


def log_reg(admin_logged, user_password, user_login):
    if entrance_collector(user_login, user_password) == True:
        admin_logged = 1
        menu_collector()

    if admin_logged == 0 and validate_password(user_password) == True:
        sql.execute("SELECT login FROM users WHERE login=?", (user_login,))
        existing_user = sql.fetchone()
        if existing_user is None:
            sql.execute("INSERT INTO users VALUES (?,?,?,?)", (user_login, user_password, 0, 0))
            db.commit()
            print("Ви успішно зареєструвалися")
            user_menu(user_login)
        else:
            print('Ви успішно ввішли в систему')
            user_menu(user_login)


def calculate_total_money(row):
    denominations = [10, 20, 50, 100, 200, 500, 1000]
    total_money = sum(qty * denom for qty, denom in zip(row, denominations))
    return total_money


def check_balance():
    sql = db.cursor()
    sql.execute('SELECT * FROM atm')
    row = sql.fetchone()
    if row:
        print(f"Сумма купюр {sum(row)}")
        print(f"Сумма грошей {calculate_total_money(row)}")
        print(
            f"10 грн: {row[0]}, 20 грн: {row[1]}, 50 грн: {row[2]}, 100 грн: {row[3]}, 200 грн: {row[4]}, 500 грн: {row[5]}, 1000 грн: {row[6]}")


def update_atm(banknotes):
    sql.execute('SELECT * FROM atm')
    row = sql.fetchone()

    if row:
        current_banknotes_dict = {
            'banknote10': row[0],
            'banknote20': row[1],
            'banknote50': row[2],
            'banknote100': row[3],
            'banknote200': row[4],
            'banknote500': row[5],
            'banknote1000': row[6]
        }

        can_update = True

        for key in banknotes:
            if banknotes[key] < 0:
                print("Некоректні дані. Кількість купюр не може бути від'ємною.")
                can_update = False
                break
            current_amount = current_banknotes_dict.get(f'banknote{key}', 0)
            if current_amount + banknotes[key] < 0:
                print(f"Недостатньо купюр для зняття. Доступна кількість купюр номіналом {key} грн: {current_amount}")
                can_update = False
                break

        if can_update:
            for key in banknotes:
                sql.execute(f'UPDATE atm SET banknote{key} = banknote{key} + ? WHERE banknote{key} >= ?',
                            (banknotes[key], -banknotes[key]))
            db.commit()
            print("Операція виконана. Купюри успішно додано до банкомату.")
        else:
            print("Операція не виконана. Помилка під час додавання купюр.")
    else:
        print("Помилка: Банкомат порожній або немає даних.")


def withdraw_from_atm(banknotes):
    sql = db.cursor()
    sql.execute('SELECT * FROM atm')
    current_banknotes = sql.fetchone()

    if current_banknotes:
        current_banknotes_dict = {
            'banknote10': current_banknotes[0],
            'banknote20': current_banknotes[1],
            'banknote50': current_banknotes[2],
            'banknote100': current_banknotes[3],
            'banknote200': current_banknotes[4],
            'banknote500': current_banknotes[5],
            'banknote1000': current_banknotes[6]
        }

        can_withdraw = True

        for key in banknotes:
            if banknotes[key] > current_banknotes_dict[f'banknote{key}']:
                can_withdraw = False
                break
            if current_banknotes_dict[f'banknote{key}'] - banknotes[key] < 0:
                can_withdraw = False
                break

        if can_withdraw:
            for key in banknotes:
                sql.execute(f'UPDATE atm SET banknote{key} = banknote{key} - ? WHERE banknote{key} >= ?', (banknotes[key], banknotes[key]))
            db.commit()
            print("Операція виконана.")
        else:
            print("Недостатньо купюр для зняття або некоректні дані.")
    else:
        print("Помилка: Банкомат порожній або немає даних.")



def check_user_balance(user_login):
    sql.execute("SELECT money FROM users WHERE login=?", (user_login,))
    user_money = sql.fetchone()
    if user_money:
        print(f"Ваш баланс: {user_money[0]} грн")
    else:
        print("Ви не зареєстровані в системі.")


def deposit_money(user_login):
    amount = int(input("Введіть суму, яку хочете додати: "))
    if amount % 10 != 0:
        change = amount % 10
        amount -= change
        print(f"Сума {amount} грн буде додана на рахунок.")
        sql.execute("UPDATE users SET money = money + ? WHERE login=?", (amount, user_login))
        db.commit()
        print(f"Ваша сдача: {change} грн")
    else:
        sql.execute("UPDATE users SET money = money + ? WHERE login=?", (amount, user_login))
        db.commit()
        print("Гроші успішно додані на рахунок.")



def withdraw_money(user_login):
    amount = int(input("Введіть суму, яку хочете зняти: "))
    sql.execute("SELECT money FROM users WHERE login=?", (user_login,))
    user_money = sql.fetchone()[0]

    if amount > user_money:
        print("У вас недостатньо коштів на рахунку.")
        return

    sql.execute("SELECT * FROM atm")
    atm_money = sql.fetchone()
    available_denominations = [1000, 500, 200, 100, 50, 20, 10]

    remaining_amount = amount
    to_withdraw = {}

    for denom in sorted(available_denominations, reverse=True):
        count = remaining_amount // denom
        if count > 0 and atm_money[available_denominations.index(denom)] >= count:
            to_withdraw[denom] = count
            remaining_amount -= count * denom

    if remaining_amount == 0:
        sql.execute("UPDATE users SET money = money - ? WHERE login=?", (amount, user_login))
        db.commit()
        print(f"Успішно знято {amount} грн")
    else:
        print(f"Неможливо зняти суму {amount} грн через обмеження в наявності купюр у банкоматі.")




def menu_collector():
    while True:
        print("Виберіть дію:")
        print("1. Перевірити баланс банкомату та кількість купюр")
        print("2. Додати купюри до банкомату")
        print("3. Зняти купюри з банкомату")
        print("4. Вихід")

        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            banknotes_to_add = {
                10: int(input("Кількість купюр номіналом 10 грн: ")),
                20: int(input("Кількість купюр номіналом 20 грн: ")),
                50: int(input("Кількість купюр номіналом 50 грн: ")),
                100: int(input("Кількість купюр номіналом 100 грн: ")),
                200: int(input("Кількість купюр номіналом 200 грн: ")),
                500: int(input("Кількість купюр номіналом 500 грн: ")),
                1000: int(input("Кількість купюр номіналом 1000 грн: "))
            }
            update_atm(banknotes_to_add)

        elif choice == "3":
            banknotes_to_withdraw = {
                10: int(input("Кількість купюр номіналом 10 грн: ")),
                20: int(input("Кількість купюр номіналом 20 грн: ")),
                50: int(input("Кількість купюр номіналом 50 грн: ")),
                100: int(input("Кількість купюр номіналом 100 грн: ")),
                200: int(input("Кількість купюр номіналом 200 грн: ")),
                500: int(input("Кількість купюр номіналом 500 грн: ")),
                1000: int(input("Кількість купюр номіналом 1000 грн: "))
            }
            withdraw_from_atm(banknotes_to_withdraw)

        elif choice == "4":
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

def user_menu(user_login):
    while True:
        print("Виберіть дію:")
        print("1. Перевірити баланс")
        print("2. Поповнити рахунок")
        print("3. Зняти гроші")
        print("4. Вихід")

        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            check_user_balance(user_login)
        elif choice == "2":
            deposit_money(user_login)
        elif choice == "3":
            withdraw_money(user_login)
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


admin_logged = 0
db = sqlite3.connect('atm.db')
sql = db.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS users (\n"
            "login TEXT, \n"
            "password TEXT, \n"
            "money BIGINT, \n"
            "status BIGINT \n"
            ")")

sql.execute("CREATE TABLE IF NOT EXISTS atm (\n"
            "banknote10 BIGINT, \n"
            "banknote20 BIGINT, \n"
            "banknote50 BIGINT,\n"
            "banknote100 BIGINT,\n"
            "banknote200 BIGINT,\n"
            "banknote500 BIGINT,\n"
            "banknote1000 BIGINT\n"
            ")")
db.commit()
print("Вас вітає банкомат, введіть свій логін та пароль якщо ви зареєстровані, або хочете зареєструватись")
user_login = input('Логін:')
user_password = input('Пароль:')

log_reg(admin_logged, user_password, user_login)
