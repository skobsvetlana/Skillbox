import os

file_name = 'people.txt'
path = os.path.abspath(os.path.join(file_name))

with open(path, 'r', encoding='utf-8') as file:
    try:
        names = file.read().strip().split()
        res = len(''.join(names))
        for i, line in enumerate(names):
            if len(line) < 3:
                raise ValueError
    except ValueError:
        print('Ошибка: менее трёх символов в строке {}.'.format(i + 1))
    finally:
        print('Общее количество символов: {}.'.format(res))

