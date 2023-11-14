#блоки
def display_file_blocks(file_path, block_size):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            if block_size > len(content):
                raise ValueError("Кількість символів перевищує розмір файлу.")

            start_index = 0
            middle_index = len(content) // 2
            end_index = len(content) - block_size

            print("Start Block:", content[start_index:start_index + block_size])
            print("Middle Block:", content[middle_index:middle_index + block_size])
            print("End Block:", content[end_index:end_index + block_size])

    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except ValueError as ve:
        print(f"Помилка: {ve}")

display_file_blocks("example.txt", 5)
