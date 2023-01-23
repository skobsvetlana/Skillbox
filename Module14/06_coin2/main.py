#Задача 6. Монетка 2

import math

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

lenth = math.sqrt(x ** 2 + y ** 2)

if lenth <= r:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')