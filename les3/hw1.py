"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_func(number1, number2):
    return number1 / number2 if number2 != 0 else print("Вы делите на ноль!")


number1 = input("Введите первое число: \n")
number2 = input("Введите второе число: \n")

if number1.isdigit() and number2.isdigit() and number2 != 0:
    number1, number2 = int(number1), int(number2)
    print(my_func(number1,number2))
elif number2 == 0:
    print("/0")
else:
    print("Вы ввели не число, введите число!")