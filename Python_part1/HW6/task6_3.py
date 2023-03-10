'''Задача 3. Слишком большие числа
Что нужно сделать
У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета, что числа не помещаются на бумаге.

Напишите программу, которая считала бы для него, сколько цифр во вводимом числе. Обратите внимание, что число 0 имеет одну цифру.

Что оценивается
Input содержит корректное приглашение для ввода.
Результат вывода корректен, правильно подсчитано количество цифр в числе.
Переменные имеют значащие имена, не только a, b, c, d (видео 2.3).
Правильное употребление пробелов после запятых и при бинарных операциях.
Используется цикл while.
Решение не использует работу со строками и операции над ними.'''

print('Задача 3. Слишком большие числа')

number = int(input('Введите число: '))
count = 0

if number == 0:
    count = 1

while number > 0:
    number //= 10
    count += 1

print('Во вводимом числе', count, 'цифр')

print()


