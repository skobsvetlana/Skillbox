import os

file_name = 'people.txt'
path = os.path.abspath(os.path.join(file_name))
count = 0

with open(path, 'r', encoding='utf-8') as file:
        names = file.read().strip().split()
        for i, line in enumerate(names):
            lenth = len(line)

            try:
                if lenth < 3:
                    count += lenth
                    raise ValueError
                else:
                    count += lenth
            except ValueError:
                print('Ошибка: менее трёх символов в строке {}.'.format(i + 1))

print('Общее количество символов: {}.'.format(count))
