'''Задача 6. Проверяем бухгалтера
Что нужно сделать

Невнимательный бухгалтер Антон складывает числа быстро, но иногда забывает о двух последних разрядах. Чтобы помочь Антону, напишите программу, которая бы складывала только два последних разряда.

Реализуйте программу, которая запрашивает два числа у пользователя. После этого у каждого числа возьмите две последние цифры. Получившиеся два числа сложите и выведите на экран.

Пример:




Что оценивается

Результат вычислений корректен.
В input содержится корректное приглашение для ввода.
Переменные имеют значащие названия.
Есть пробелы после запятых и при бинарных операциях.'''

print('Задача 6. Проверяем бухгалтера')

number_1 = int(input('Введите первое число '))
number_2 = int(input('Введите второе число '))

res = number_1 % 100 + number_2 % 100

print(f'Сумма двух последних разрядов чисел равна {res}')
