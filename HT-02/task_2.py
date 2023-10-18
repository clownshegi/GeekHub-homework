##Write a script which accepts two sequences of comma-separated colors from user. Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = input("Введите цвета для первого списка (через запятую): ")
color_list_2 = input("Введите цвета для второго списка (через запятую): ")

colors_1 = [color.strip() for color in color_list_1.split(',')]
colors_2 = [color.strip() for color in color_list_2.split(',')]

set_1 = set(colors_1)
set_2 = set(colors_2)

unique_colors = set_1 - set_2

print("Уникальные цвета:", unique_colors)
