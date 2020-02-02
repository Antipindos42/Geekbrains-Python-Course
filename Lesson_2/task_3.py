# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number_of_month = int(input('Введите номер месяца(числа от 1 до 12), чтобы получить сезон: '))

list_of_seasons = [
    'Зима',
    'Весна',
    'Лето',
    'Осень'
]

dict_of_seasons = {
    'зима': (12, 1, 2),
    'весна': (3, 4, 5),
    'лето': (6, 7, 8),
    'осень': (9, 10, 11)
}

while True:
    if (number_of_month <= 0 or number_of_month > 12):
        print('Месяцев 12, введите число от 1 до 12')
        continue

    print(f'Список: Введенный номер месяца {number_of_month} и это {list_of_seasons[number_of_month // 3 % 4]}')

    for k, v in dict_of_seasons.items():
        if number_of_month in v:
            print(f'Словарь: Введенный номер месяца {number_of_month} и это {k}')
        break

    break
