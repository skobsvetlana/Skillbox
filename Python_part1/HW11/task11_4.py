'''Задача 4. Первая цифра
Что нужно сделать

Дано положительное действительное число X. Выведите его первую цифру после десятичной точки. При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками.

'''

print('Задача 4. Первая цифра \n')

x = float(input('Введите положительное действительное число: '))
res = int(x * 10 % 10)
print(f'Первая цифру после десятичной точки {res}'.format())