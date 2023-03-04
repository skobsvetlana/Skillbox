import random

def add_to_file(number):
    with open('result.txt', 'a') as file:
        file.write(str(number)+ '\n')


numbes_sum = 0
errors = ['NameError', 'TypeError', 'ValueError', 'IndexError']


while numbes_sum < 777:
    number = int(input('Введите число: '))
    rand_num = random.randint(1, 13)
    if rand_num == 13:
        print('Вас постигла неудача!')
        raise Exception(random.choice(errors))
    else:
        add_to_file(number)

    numbes_sum += number

print('Вы успешно выполнили условие для выхода из порочного цикла!')








