'''Задача 4. Среднее на отрезке
Что нужно сделать

Напишите программу, которая считывает с клавиатуры числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.



Что оценивается

Задание считается успешно выполненным, если:

результат вывода соответствует условию;
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);
input содержит корректное приглашение для ввода;
переменные имеют значащие имена, не только a, b, c, d.


Советы и рекомендации

Функция range(start, stop) не включает границу stop, останавливается, не доходя до неё.

'''

print()
print('Задача 4. Среднее на отрезке')

start = int(input('Введите начало отрезка '))
stop = int(input('Введите конец отрезка '))
divider = int(input('Введите делитель '))
total_sum = 0
count = 0

for num in range(start, stop // divider + 1):
  total_sum += num * divider
  count += 1
  #print(num * divider, total_sum, count)
print('среднее арифметическое всех чисел из отрезка [{}; {}], кратных числу {} равно {}.'.format(start, stop, divider, total_sum / count))
