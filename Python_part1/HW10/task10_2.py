'''Задача 2. Лестница
Что нужно сделать

Пользователь вводит число N. Напишите программу, которая выводит такую «лесенку» из чисел:'''

print('Задача 2. Лестница \n')

size = int(input('Введите число:'))
for row in range(1, size + 1):
  for col in range(size):
    if row > col:
      print(row, end=' ')
  print()