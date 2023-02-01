'''Задача 9. Уравнение
Что нужно сделать

Даны действительные коэффициенты a, b, c при этом a≠0. Решите квадратное уравнение a∙x2+b∙x+c=0 и выведите все его корни.

Если уравнение имеет два корня, выведите два корня в порядке возрастания, если один корень — выведите одно число, если нет корней — не выводите ничего

'''

print('Задача 9. Уравнение \n')

import math

while True:
    a = float(input('Введите коэффициент a (a≠0): '))
    if a != 0:
        break

b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = round((-b + math.sqrt(discriminant)) / 2 * a, 2)
    x2 = round((-b - math.sqrt(discriminant)) / 2 * a, 2)

    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)

elif discriminant == 0:
    x = round(-b / 2 * a, 2)
    print(x)

else:
    print('Корней не существует.')
