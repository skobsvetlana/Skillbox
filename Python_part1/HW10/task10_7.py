'''Задача 7. Наибольшая сумма цифр
Что нужно сделать

Пользователь вводит N чисел. Среди натуральных чисел, которые были введены, найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.'''

print('Задача 6. Сумма факториалов \n')

n = int(input('Введите число > 0: '))
max_count = 0

for _ in range(n):
    num = int(input('Введите натуральное число: '))
    count = 0
    res_num = num

    while num > 0:
        count += num % 10
        num //= 10

    if count > max_count:
        max_count = count
        max_num = res_num

print(
    f'Среди натуральных чисел, которые были введены, наибольшее по сумме цифр {max_num}, сумма цифр {max_count}'.format())
