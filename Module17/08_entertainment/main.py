import random

stick_num = int(input('Количество палок: '))
rock_num = int(input('Количество бросков: '))

res = ['|' for _ in range(stick_num)]

for i in range(rock_num):
    left = random.randint(1, stick_num)
    right = random.randint(left, stick_num)
    res[left - 1: right] = ['.' for _ in range(right - left + 1)]
    print(f'\nБросок {i + 1}. Сбиты палки с номера {left} по номер {right}.')

print(f'\nРезультат: {"".join(res)}')
