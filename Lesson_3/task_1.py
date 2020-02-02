#homework lesson 3: task 1

"""
 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(num, div):
    try:
        return num/div
    except ZeroDivisionError as e:
        print(f'Whoops! division by zero!')




print(division(int(input('Что делим: ')), int(input('На что делим: '))))
