import random

lenth = int(input('Количество чисел в списке: '))
my_list = [random.randint(0, 2) for _ in range(lenth)]
zeros = [x for x in my_list if x == 0]
res = [x for x in my_list if x != 0] + zeros

print(f'Список до сжатия: {my_list}')
print(f'Список после сжатия: {res[:lenth - len(zeros)]}')