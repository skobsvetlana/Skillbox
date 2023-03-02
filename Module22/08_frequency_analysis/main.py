import os

def analyse_text(text):
    res = {}
    count = 0
    for el in text:
        if el.isalpha():
            count += 1
            res[el] = text.count(el)

    for key, value in res.items():
        res[key] = round(value / count, 3)

    res = sorted(res.items(), key=lambda x: (-x[1], x[0]))

    return res


def add_data(data, file_name):
    path = os.path.abspath(os.path.join(file_name))
    with open(path, 'a', encoding='utf-8') as file:
        if os.stat(path).st_size:
            file.write('\n')
        file.write(data)


file_name = 'text.txt'
file_to_write = 'analysis.txt'
path = os.path.abspath(os.path.join(file_name))

with open(path, 'r') as file:
    data = file.read().strip().lower()

data = analyse_text(data)

for el in data:
    add_data(f'{el[0]} {el[1]}', file_to_write)

