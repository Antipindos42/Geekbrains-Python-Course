#Lesson 5 task 1

"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file = open('./files/task1.txt', 'w',  encoding='utf-8')
while True:
    string = input('Введите что-либо: ')
    if not string:
        file.close()
        print('Выход')
        break

    file.write(f'{string}\n')
