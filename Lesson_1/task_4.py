# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input('Введите целое положительное число:')
biggest_num = ''
i = 0

while i != len(number):
    if not biggest_num:
        biggest_num = int(number[i])
        i += 1
    elif biggest_num > int(number[i]):
        i += 1
    else:
        biggest_num = int(number[i])
        i += 1

print(f'Самое большое чило: {biggest_num}')

#исправленый вариант:

while number:
    if number % 10 > biggest_num:
        biggest_num = number % 10
    number //= 10

print(f'Самое большое число {biggest_num}')