"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

my_f = open("text3.txt", "r", encoding="utf-8")

x = 1
y = 1
b = int()
z = 0
for line in my_f:
    if x == 1:
        print(line.split()[0])
        x = 0
    x += 1
    if y == 1:
        a = int(line.split()[1])
        b += a
        y = 0
    y += 1
    z += 1
print(f'Средняя величина дохода сотрудников - {b / z}')
my_f.close()