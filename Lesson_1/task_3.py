# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('введите однозначное число. Например 3:')
double_n = n * 2
triple_n = n * 3
sum_of_numbers = int(n) + int(double_n) + int(triple_n)

print(f'{n}+{double_n}+{triple_n}={sum_of_numbers}')
