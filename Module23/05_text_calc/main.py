import os

def do_math(data):
    x, math_operation, y = tuple(data.split())
    x = int(x)
    y = int(y)
    res = 0

    if math_operation == '+':
        res += x + y
    elif math_operation == '-':
        res += x - y
    elif math_operation == '/':
        res += x / y
    elif math_operation == '//':
        res += x // y
    elif math_operation == '*':
        res += x * y
    elif math_operation == '%':
        res += x % y
    else:
        return None

    return res

file_name = 'calc.txt'
path = os.path.abspath(os.path.join(file_name))
res = 0
try:
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.read().split('\n'):
            try:
                spam = do_math(line)
                if spam:
                    res += spam
                else:
                    ans = input(f'Обнаружена ошибка в строке: {line}   Хотите исправить?').lower()
                    if ans == 'да':
                        new_line = input('Введите исправленную строку: ')
                        res += do_math(new_line)
                    else:
                        raise NameError
            except ZeroDivisionError:
                print('Ошибка: деление на ноль')
            except NameError:
                print(f'Ошибка: неверная математическая операция {line}')
except FileNotFoundError:
    print(f'Ошибка: файл {path} не существует')
finally:
    print(res)


