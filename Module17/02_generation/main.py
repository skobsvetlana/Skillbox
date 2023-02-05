lenth = int(input('Введите длину списка: '))
my_list = [x % 5 if x % 2 != 0 else 1 for x in range(lenth)]

print(f'Результат: {my_list}')
