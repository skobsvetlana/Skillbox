'''Задача 5. Отрезок
Что нужно сделать
Напишите программу, которая считывает с клавиатуры два числа: a и b, — считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.

Что оценивается
Задание считается успешно выполненным, если:

результат вывода соответствует условию;
input содержит корректное приглашение для ввода;
в выводе присутствует описание результата;
для решения используется конструкция for.'''

print()
print('Задача 5. Отрезок')

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
count = 0
total_sum = 0

for num in range(num_1, num_2 + 1):
  if num % 3 == 0:
    total_sum += num
    count += 1

print(f'среднее арифметическое всех чисел из отрезка [{num_1}; {num_2}], кратных числу 3 - {total_sum / count}')
