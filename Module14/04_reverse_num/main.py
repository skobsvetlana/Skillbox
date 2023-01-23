#Задача 4. Число наоборот 3
def split_number(number):
    int_part = ''
    float_part = ''
    flag = 0
    for symbol in str(number):
        if symbol == '.':
            flag = 1
            continue

        if flag:
            float_part += symbol
        else:
            int_part += symbol

    return int_part, float_part

def reverse_number(number):
    result = ''
    for symbol in number:
        result = symbol + result

    return result

#reverse number, int part and float part separatly
def modify_number(number):
    int_part, float_part = split_number(number)
    result = reverse_number(int_part) + '.' + reverse_number(float_part)

    return float(result)

number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))

reversed_number1 = modify_number(number1)
reversed_number2 = modify_number(number2)

print(f'Первое число наоборот: {reversed_number1}')
print(f'Второе число наоборот: {reversed_number2}')
print(f'Сумма: {reversed_number1 + reversed_number2}')




