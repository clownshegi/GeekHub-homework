#банкомат
import csv
import json
from datetime import datetime
import os

def check_credentials(username, password):
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[1] == password:
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
    print(f"Your current balance: {current_balance}")

def deposit_money(username):
    amount = int(input("Enter the amount to deposit: "))
    update_balance(username, amount)
    print(f"Successfully deposited {amount} dollars.")

def withdraw_money(username):
    balance_file_path = f"{username}_balance.txt"
    with open(balance_file_path, "r") as file:
        current_balance = int(file.read())
    amount = int(input("Enter the amount to withdraw: "))
    if amount > current_balance:
        print("Insufficient funds.")
    else:
        update_balance(username, -amount)
        print(f"Successfully withdrew {amount} dollars.")

def start():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if check_credentials(username, password):
            print("Login successful!")
            menu(username)
            break
        else:
            print("Invalid credentials. Try again.")

def menu(username):
    while True:
        print("Choose an action:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(username)
        elif choice == "2":
            deposit_money(username)
        elif choice == "3":
            withdraw_money(username)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    start()
