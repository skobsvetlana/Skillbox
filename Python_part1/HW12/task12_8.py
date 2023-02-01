'''Задача 8. НОД
Что нужно сделать

Напишите функцию, вычисляющую наибольший общий делитель двух чисел.'''

print('Задача 8. НОД \n')


def greatest_common_divisor(a, b):
    min_num = min(a, b)
    for res in range(min_num, 0, -1):
        if a % res == 0 and b % res == 0:
            print(f'\n Наибольший общий делитель двух чисел {a} и {b} равен {res}'.format())
            break


a = int(input('Введите первое число: '))
b = int(input('\n Введите втрое число: '))
greatest_common_divisor(a, b)

