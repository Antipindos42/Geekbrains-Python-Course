#homework lesson 3: task 2

"""
 Реализовать функцию, принимающую несколько параметров,
 описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
"""


def person(name, lastname, year_of_birth, city, email, phone):
    return print(f'{name} {lastname}. {year_of_birth}, {city}. {email}, {phone}')


print(person(
    input('Имя: '),
    input('Фамилия: '),
    input('Год Рождения: '),
    input('Город проживания: '),
    input('email: '),
    input('phone: '),
))