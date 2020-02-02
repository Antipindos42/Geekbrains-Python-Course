# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

ratings = [22, 10, 4]
#Исправленный вариант:
while True:
    rating = input('Введите новое значение рейтинга: ')

    try:
        rating = abs(int(rating))
    except ValueError as e:
        print('Ошибка ввода')
        continue

    #rating еще не встречался в списке
    if not ratings.count(rating):
        #вставляем впереди или вконце списка
        if rating > ratings[0]:
            ratings.insert(0, rating)
        elif rating < ratings[-1]:
            ratings.append(rating)
        # ищем куда можем вставить внутри списка
        else:
            for k, v in enumerate(ratings):
                if rating > v:
                    ratings.insert(k, rating)
                    break
    #уже есть такое значение
    else:
        new_index = ratings.index(rating) + ratings.count(rating)
        ratings.insert(new_index, rating)

    print(ratings)

# Спорный вариант через sorted, было первоначально
# my_list = [7, 5, 3, 3, 2]
# print(f'есть список {my_list}')
# my_list.append(int(input('Добавьте значение рейтига: ')))
# print(f'теперь список такой:{sorted(my_list, reverse=True)}')












