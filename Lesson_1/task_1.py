# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные,
# выведите на экран.

var_a = 1
var_b = 2.23
var_string = 'string'
var_string_1 = 'one more string'

print('Есть переменные со следующими значениями:\nВы можете изменить их значения')

print(f'''
    var_a={var_a}
    var_b={var_b}
    var_string={var_string}
    var_string_1={var_string_1}
    ''')

print('Введите новые значения переменных')

var_a = input('var_a=')
print(f'var_a={var_a}')

var_b = input('var_b=')
print(f'var_b={var_b}')

var_string = input('var_string=')
print(f'var_string={var_string}')

var_string_1 = input('var_string_1=')
print(f'var_string_1={var_string_1}')

print('Теперь значения переменных выглядят следующим образом:')

print(f'''
    var_a={var_a}
    var_b={var_b}
    var_string={var_string}
    var_string_1={var_string_1}
    ''')