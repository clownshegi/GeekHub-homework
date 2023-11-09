"""
Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину найкоротшого слова.
 Реалізуйте обчислення за допомогою генератора
"""


def shortest_word_length(sentence):
    words = sentence.split()

    shortest_length = min(len(word) for word in words)

    return shortest_length


sentence = "Саша ходила по шоссе і сосала сушку"
result = shortest_word_length(sentence)
print("Довжина найкоротшого слова:", result)
