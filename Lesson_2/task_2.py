# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_from_input = [int(i) for i in input('Введите значения списка через пробел: ').split()]
print(f'Ваш список {list_from_input}')

i = 0

while True:
    if i >= len(list_from_input) - 1:
        break

    list_from_input[i], list_from_input[i+1] = list_from_input[i+1], list_from_input[i]
    i += 2

print(f'теперь массив выглядит вот так: {list_from_input}')
