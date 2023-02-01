'''Задача 6. Метеостанция
Что нужно сделать

Сотрудники международной метеостанции должны каждый день передавать показания градусов по шкалам и Цельсия, и Фаренгейта. Напишите программу, которая принимает на вход три целых числа в градусах Цельсия: нижняя граница температуры, верхняя граница температуры и шаг. Программа выводит на экран таблицу соответствия градусов Цельсия градусам Фаренгейта от нижней до верхней границы с указанным шагом. Обеспечьте контроль ввода. Верхняя граница должна печататься, даже если последний шаг “перепрыгнул “ ее. Известно, что 0С соответствует 32F, а каждый градус Цельсия эквивалентен 1.8 градусам Фаренгейта.



Пример:

Ввод:

Нижняя граница: 0

Верхняя граница: 50

Шаг: 20

Вывод:

C   F

0   32

20  68

40  104

50  122'''

print('Задача 6. Метеостанция \n')

bottom = int(input('Нижняя граница: '))
top = int(input('Верхняя граница: : '))
step = int(input('Шаг: '))
zero = 32
curr = bottom

print('C \t F \n')

while curr <= top:
    print(curr, '\t', int(zero + (curr * 1.8)), '\n')
    curr += step

if (top - bottom) % step != 0:
    print(top, "\t", int(zero + (top * 1.8)), '\n')





