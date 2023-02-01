'''Задача 4. Крест
Что нужно сделать

Напишите программу, которая выводит на экран крест из символов ^

(символы выводятся по диагоналям воображаемого квадрата).'''

print('Задача 4. Крест \n')

size = int(input('Введите число:'))
for row in range(size):
  for col in range(size):
    if row == col or col == size - row - 1:
      print('^', end='')
    else:
      print(' ', end='')
  print()