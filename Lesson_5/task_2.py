#Lesson 5 task 2

"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

import os

DIR = 'files'
file_path = os.path.join(DIR, 'task2.txt')
file = open(file_path, 'r', encoding='utf-8')
lines = file.readlines()

print(f'В файле {len(lines)} строк(и)')

i = 1
for string in lines:
    print(f'В строке {i} {len(string.split())} слов')
    i+=1