'''Задача 1. Сумма чисел
Что нужно сделать

Напишите функцию summa_n, которая принимает одно целое положительное число N и выводит сумму всех чисел от 1 до N включительно.

Пример работы программы:

Введите число: 5

Я знаю, что сумма чисел от 1 до 5 равна 15'''

print('Задача 1. Сумма чисел \n')

def summa_n(num):
  res = 0
  for i in range(1, num + 1):
    res += i
  print(f'Я знаю, что сумма чисел от 1 до {num} равна {res}'.format())

num = int(input('Введите число: \n'))
summa_n(num)


