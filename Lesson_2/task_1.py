# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


float_var = 12.443
int_var = 12
complex_var = complex(1, 2)
string_var = 'this is a string'
list_var = [1, 2, 3]
tuple_var = tuple('tuple')
set_var = set('this is a set var')
bool_var = True
list_of_types = [float_var, int_var, complex_var, string_var, list_var, tuple_var, set_var, bool_var]

for variable in list_of_types:
    print(type(variable))


