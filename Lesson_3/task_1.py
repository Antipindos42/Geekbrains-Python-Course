#homework lesson 2: task 1

"""
 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

number = int(input('Что делим: '))
divider = int(input('На что делим: '))


def division(num, div):
    try:
        result = num/div
    except ZeroDivisionError as e:
        print(f'Whoops! division by zero!')
        return
    return result


print(division(number, divider))
