"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

var_str = input('Введите строку из нескольких слов через пробел: ')
var_str = var_str.split()
for number, step in enumerate(var_str, 1):
    if len(step) > 10:
        print(number, step[:10])
    else:
        print(number, step)