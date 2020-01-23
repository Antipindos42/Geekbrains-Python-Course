# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# для проверки использовался https://www.convert-me.com/ru/convert/time/dhms.html?u=dhms&v=1
posix_time_stamp = int(input('Введите время в секундах:\n'))

print('Введенное время в формате чч:мм:сс составляет: {hours}:{minutes}:{seconds}'.format(
    hours=posix_time_stamp // 3600,
    minutes=posix_time_stamp % 3600 // 60,
    seconds=posix_time_stamp % 3600 % 60
))

