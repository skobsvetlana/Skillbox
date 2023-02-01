'''Задача 9. Выражение
Что нужно сделать

Дано число x. Напишите программу для вычисления следующего выражения:
'''

print()
print('Задача 9. Выражение')

x = int(input('Введите число x: '))
# n = int(input('Введите число n: '))
n = 6
prev = 0
dividable = 1
divider = 1
for i in range(n):
    curr = prev + 2 ** i
    dividable *= x - curr
    prev = curr

    divider *= x - 2 ** (i + 1)

    # print(curr,  2**(i + 1))
if divider == 0:
    print('Ошибка. Делитель равен 0 при х = ', x)
else:
    res = dividable / divider
    print('res = ', res)



