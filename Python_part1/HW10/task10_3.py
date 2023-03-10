'''Задача 3. Рамка
Что нужно сделать

Напишите программу, которая рисует с помощью символьной графики прямоугольную рамку. Для вертикальных линий используйте символ вертикального штриха |, а для горизонтальных — дефис -. Пусть пользователь вводит ширину и высоту рамки.'''

print('Задача 3. Рамка \n')

length = int(input('Введите длину рамки: '))
width = int(input('Введите ширину рамки: '))

for row in range(width):
    for col in range(length):
        if (row == 0 or row == width - 1) and col > 0 and col < length - 1:
            print('-', end='')
        elif col == 0 or col == length - 1:
            print('|', end='')
        else:
            print(' ', end='')

    print()