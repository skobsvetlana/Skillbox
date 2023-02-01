'''Задача 9. Пирамидка 2
Что нужно сделать

Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами вот так:'''

print('Задача 9. Пирамидка 2 \n')

size = int(input('Введите высоту пирамиды: '))
base = 2 * size - 1
num = 1

for row in range(size):
    for col in range(size):
        if col >= base - size - row and col <= base - size + row:
            print(num, end='  ')
            num += 2
        else:
            print('  ', end='')

    print()