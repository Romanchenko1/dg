# 1. Напишите программу, которая сообщает размер штрафа в зависимости от превышения скорости.
# Сейчас действуют такие правила:
# - за превышение скорости от 20 до 40 км/ч предусмотрен штраф 500 рублей,
# - от 40 до 60 км/ч — 1000–1500 рублей,
# - от 60 до 80 км/ч — штраф 2000–2500 рублей,
# - от 80 км/ч — 5000 рублей или лишение прав на полгода.
# Лишение прав рассматривать не будем.
# Пусть ваша программа принимает на ввод разрешённую скорость и скорость, с которой ехал автомобиль,
# высчитывает разницу и сообщает размер штрафа в зависимости от превышения скорости.

speed_limit = float(input('Введите разрешённую скорость '))
fact_speed = float(input('Введите скорость, с которой ехал автомобиль '))
if fact_speed - speed_limit > 80:
    print('Штраф — 5000 рублей')
elif fact_speed - speed_limit > 60:
    print('Штраф — 2000–2500 рублей')
elif fact_speed - speed_limit > 40:
    print('Штраф — 1000–1500 рублей')
elif fact_speed - speed_limit > 20:
    print('Штраф — 500 рублей')
else:
    print('Штрафа нет')

# 2. Напишите программу, которая запрашивает на ввод число. После этого она проверяет,
# является ли число чётным или нечётным. Если число чётное, программа проверяет,
# делится ли оно на 5 без остатка. Если да, программа сообщает, что вы ввели круглое число.
# Если нет, сообщает, что число некруглое. Используйте вложенные условия. Для нечётных чисел
# программа сообщает, что получила нечётное число.

num = int(input('Введите число '))
if num % 2 == 0:
    if num % 5 == 0:
        print('Число круглое')
    else:
        print('Число некруглое')
else:
    print('Число нечётное')


# 3. Напишите программу "Времена года".
# Программа должна запрашивать, какой сейчас месяц,
# а в ответ выводить, какое сейчас время года: зима, весна, лето или осень.

month = input('Какой сейчас месяц? ')
if month == 'декабрь' or month == 'январь' or month == 'февраль':
    print('Сейчас зима')
elif month == 'март' or month == 'апрель' or month == 'май':
    print('Сейчас весна')
elif month == 'июнь' or month == 'июль' or month == 'август':
    print('Сейчас лето')
else:
    print('Сейчас осень')


