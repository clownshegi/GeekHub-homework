"""
 Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. Файл також додайте в репозиторій.
  На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
  Кількість символів в блоках - та, яка введена в другому параметрі. Придумайте самі, як обробляти помилку, наприклад,
   коли кількість символів більша, ніж є в файлі або, наприклад, файл із двох символів і треба вивести по одному
   символу, то що виводити на місці середнього блоку символів?). Не забудьте додати перевірку чи файл існує.
"""


def divide_into_blocks(file_content: str, symbol_count: int, is_even: bool) -> list:
    text_block_list = []
    first_block_start = symbol_count
    last_block_start = symbol_count * -1

    if is_even:
        middle_block_start = len(file_content) // 2 - (symbol_count // 2)
        middle_block_end = len(file_content) // 2 + (symbol_count // 2)
    else:
        middle_block_start = (len(file_content) - symbol_count) // 2
        middle_block_end = (len(file_content) + symbol_count) // 2

    text_block_list.append(file_content[:first_block_start])
    text_block_list.append(file_content[middle_block_start:middle_block_end])
    text_block_list.append(file_content[last_block_start:])

    return text_block_list


def verify_content_length(content: str, symbol_count: int) -> bool:
    if len(content) < symbol_count * 3:
        try:
            raise ValueError("Помилка: Недостатня кількість символів у файлі для трьох блоків.")
        except ValueError as text_error:
            print(text_error)
            return False
    else:
        return True


def retrieve_file_data(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().replace('\n', '')


def custom_file_existence_check(file_path: str) -> bool:
    try:
        with open(file_path, 'r'):
            return True
    except FileNotFoundError:
        print(f'Помилка: Файл "{file_path}" не знайдено!')
        return False


def create_blocks_from_file(file_path: str, symbol_count: int):
    file_content = retrieve_file_data(file_path)

    if custom_file_existence_check(file_path) is False:
        return "Зупинка роботи."

    if len(file_content) < symbol_count * 3:
        print("Помилка: Недостатня кількість символів у файлі для трьох блоків.")
        return "Зупинка роботи."

    middle = len(file_content) // 2
    half_symbol_count = symbol_count // 2

    first_block_start = 0
    middle_block_start = middle - half_symbol_count
    last_block_start = len(file_content) - symbol_count

    text_block_list = [
        file_content[first_block_start: first_block_start + symbol_count],
        file_content[middle_block_start: middle_block_start + symbol_count],
        file_content[last_block_start:],
    ]

    return text_block_list


result = create_blocks_from_file(file_path="example.txt", symbol_count=2)
print(result)
