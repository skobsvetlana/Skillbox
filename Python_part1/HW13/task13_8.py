'''Задача 8. Сумма ряда
Что нужно сделать

Пользователь вводит действительное число х и точность precision. Напишите программу, которая по числу х вычисляет сумму ряда в точности до precision.

Операцией возведения в степень и функцией factorial пользоваться нельзя.

Пример:

Введите точность: 0.0001

Введите x: 5

Сумма ряда =  0.2836250150891709'''

print('Задача 8. Сумма ряда \n')


def exp_(x, n):
    if n == 0:
        return 1
    res = x
    for i in range(1, n):
        res *= x

    return res


def factorial_(n):
    if n == 0:
        return 1

    res = 1
    for i in range(2, n + 1):
        res *= i

    return res


def series_sum(x, precision):
    res = 0
    i = 0
    addmember = exp_(-1, i) * exp_(x, 2 * i) / factorial_(2 * i)
    while abs(addmember) > precision:
        res += addmember
        i += 1
        addmember = (-1) ** i * exp_(x, 2 * i) / factorial_(2 * i)

    return res


precision = float(input('Введите точность: '))
x = int(input('Введите x: '))

res = series_sum(x, precision)

print(f'Сумма ряда =  {res}')




