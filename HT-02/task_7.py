## Write a script to concatenate all elements in a list into a string and print it. List must be include both strings and integers and must be hardcoded.

my_list = [5, "яблоко", 17, "лук", "мандарин", 7]

result_string = ''.join(map(str, my_list))

print(result_string)
