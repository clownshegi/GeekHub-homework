"""
Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію).
 Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.
"""

import sqlite3

class Library:
    def __init__(self, db_name='library.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                taken INTEGER DEFAULT 0,
                                borrower TEXT DEFAULT NULL
                            )''')
        self.conn.commit()

    def add_book(self, title, author):
        self.cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
        self.conn.commit()
        print(f'Книгу "{title}" автора {author} додано до бібліотеки.')

    def take_book(self, book_id, borrower_name):
        self.cursor.execute('SELECT * FROM books WHERE id=?', (book_id,))
        book = self.cursor.fetchone()
        if book:
            if book[3] == 0:
                self.cursor.execute('UPDATE books SET taken=1, borrower=? WHERE id=?', (borrower_name, book_id))
                self.conn.commit()
                print(f'{borrower_name}, ви взяли книгу "{book[1]}" автора {book[2]}.')
            else:
                print('Ця книга вже взята.')
        else:
            print('Книга з таким ID не знайдена.')

    def return_book(self, book_id, borrower_name):
        self.cursor.execute('SELECT * FROM books WHERE id=?', (book_id,))
        book = self.cursor.fetchone()
        if book:
            if book[3] == 1 and book[4] == borrower_name:
                self.cursor.execute('UPDATE books SET taken=0, borrower=NULL WHERE id=?', (book_id,))
                self.conn.commit()
                print(f'{borrower_name}, ви повернули книгу "{book[1]}" автора {book[2]}. Дякую!')
            elif book[3] == 0:
                print('Ця книга вже є у бібліотеці.')
            else:
                print('Цю книгу взяв інший користувач.')
        else:
            print('Книга з таким ID не знайдена або не була взята.')

    def display_books(self):
        self.cursor.execute('SELECT * FROM books')
        books = self.cursor.fetchall()
        if books:
            print("Список книг у бібліотеці:")
            for book in books:
                status = "Взята" if book[3] == 1 else "У бібліотеці"
                borrower = book[4] if book[4] else "Ніхто"
                print(f"ID: {book[0]}, Назва: {book[1]}, Автор: {book[2]}, Статус: {status}, Взяв: {borrower}")
        else:
            print('Бібліотека порожня.')

    def display_menu(self):
        print("\nМеню:")
        print("1. Додати книгу")
        print("2. Взяти книгу")
        print("3. Повернути книгу")
        print("4. Показати список книг")
        print("5. Вийти з програми")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Виберіть опцію (1-5): ")

            if choice == '1':
                title = input("Введіть назву книги: ")
                author = input("Введіть ім'я автора: ")
                self.add_book(title, author)
            elif choice == '2':
                book_id = int(input("Введіть ID книги, яку бажаєте взяти: "))
                borrower_name = input("Введіть ваше ім'я: ")
                self.take_book(book_id, borrower_name)
            elif choice == '3':
                book_id = int(input("Введіть ID книги, яку бажаєте повернути: "))
                borrower_name = input("Введіть ваше ім'я: ")
                self.return_book(book_id, borrower_name)
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                print("Дякую за користування! Вихід з програми.")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    library = Library()
    library.run()
