'''Задача 3. Апгрейд калькулятора
Что нужно сделать

Степан, как и большая часть населения планеты, для расчёта суммы и разности чисел использует калькулятор. Однако в работе ему нужно делать не только обычные действия вроде сложения и вычитания, а делать что-то вручную он уже устал. Поэтому Степан решил немного расширить функционал своего калькулятора.

Напишите программу, запрашивающую у пользователя число и действие, которое нужно с ним сделать: вывести сумму его цифр, максимальную или минимальную цифру. Каждое действие оформите в виде отдельной функции, а основную программу зациклите.'''

print('Задача 3. Апгрейд калькулятора \n')


def sum_of_digits(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    print(f'Сумма цифр равна {res}'.format())
    main_func()


def min_digit(num):
    res = 9
    if num < 0:
        num = -num

    while num > 0:
        curr_digit = num % 10
        if res > curr_digit:
            res = num % 10
        num //= 10

    print(f'Минимальная цифра числа равна {res}'.format())
    main_func()


def max_digit(num):
    res = 0
    if num < 0:
        num = -num
    while num > 0:
        curr_digit = num % 10
        if res < curr_digit:
            res = num % 10
        num //= 10
    print(f'Максимальная цифра числа равна {res}'.format())
    main_func()


def main_func():
    num = int(input('\n Введите число: '))
    print(
        'Что вы хотите сделать? \n 1 - вывести сумму цифр \n 2 - вывести максимальную цифру числа\n 3 - вывести минимальную цифру числа \n 0 - stop')
    choice = int(input('Введите число: '))
    if choice == 1:
        sum_of_digits(num)
    elif choice == 2:
        max_digit(num)
    elif choice == 3:
        min_digit(num)
    elif choice == 0:
        print('Программа завершена')
    else:
        print('Неверный ввод.')


main_func()



