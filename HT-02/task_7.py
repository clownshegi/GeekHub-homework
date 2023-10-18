## Write a script to concatenate all elements in a list into a string and print it. List must be include both strings and integers and must be hardcoded.

my_list = [5, "яблоко", 17, "лук", "мандарин", 7]

result_string = ""

for item in my_list:
    result_string += str(item)

print(result_string)
