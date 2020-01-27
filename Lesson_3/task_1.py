#homework lesson 2: task 1

"""
 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def division(number, divider):
    try:
        result = number/divider
    except ValueError as e:
        print(f'Divided by zero')
        print(e)
    return print(result)


number = int(input('Что делим: '))
divider = int(('На что делим: '))

print(division(number, divider))