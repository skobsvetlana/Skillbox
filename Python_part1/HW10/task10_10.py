'''Задача 10. Яма
Что нужно сделать

Вы пишите компьютерную игру с текстовой графикой, вам поручили написать генератор ландшафта.

Напишите программу, которая получает на вход число N и выводит на экран числа в виде «ямы» вот так:'''

print('Задача 10. Яма \n')

size = int(input('Введите число: '))
print(size)
for row in range(size):
  num1 = size
  num2 = 1 - size
  for col in range(size * 2):
    if col >= 2 * size - row - 1:
      print(num2, end='')
    elif col <= row:
      print(num1, end='')
    else:
      print('.', end='')
    num1 -= 1
    num2 += 1
  print()
