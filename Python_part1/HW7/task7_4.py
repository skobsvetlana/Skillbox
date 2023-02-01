'''Задача 4. Успеваемость в классе
Что нужно сделать
В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. Напишите программу, которая получает список оценок — N чисел — и выводит на экран сообщение о том, кого сегодня больше: отличников, хорошистов или троечников.

Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

Что оценивается
Задание считается успешно выполненным, если:

результат вывода соответствует условию;
input содержит корректное приглашение для ввода;
в выводе присутствует сообщение о том, кого больше;
для решения используется цикл for, а не встроенные функции или рекурсия;
переменные имеют значащие имена, не только a, b, c, d.'''

print()
print('Задача 4. Успеваемость в классе')

students_num = int(input('Введите количество учеников в классе: '))
fours = 0
threes = 0
fives = 0

for i in range(students_num):
    print('Ученик', i + 1)
    score = int(input('Введите оценку: '))
    if score == 3:
        threes += 1
    elif score == 4:
        fours += 1
    else:
        fives += 1

if threes > fours and threes > fives:
    print('сегодня больше троечников')
if fours > threes and fours > fives:
    print('сегодня больше хорошистов')
if fives > threes and fives > fours:
    print('сегодня больше отличников')




