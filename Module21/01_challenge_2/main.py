def print_num(num):
    if num >= 1:
        print_num(num - 1)
        print(num)


num = int(input('Введите num: '))
print_num(num)
