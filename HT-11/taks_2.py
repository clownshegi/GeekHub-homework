"""
Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи,
 які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print(f"{self.name} {self.age} років.")

    def print_name(self):
        print(f"Ім'я: {self.name}")

    def show_all_information(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")


person1 = Person("Аліса", 30)
person2 = Person("Ваня", 25)

person1.profession = "Інженер"
person2.profession = "Вчитель"

person1.show_age()
person1.print_name()
person1.show_all_information()
print(f"Професія: {person1.profession}\n")

person2.show_age()
person2.print_name()
person2.show_all_information()
print(f"Професія: {person2.profession}")
