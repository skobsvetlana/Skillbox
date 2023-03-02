import os
from zipfile import ZipFile

def analyse_text(text):
    res = {}
    for el in text:
        if el.isalpha():
            if el in res:
                res[el] += 1
            else:
                res[el] = 1

    res = sorted(res.items(), key=lambda x: x[1])
    res = (f'{el[0]} {el[1]}' for el in res)

    return res


def add_data(data, file_name):
    path = os.path.abspath(os.path.join(file_name))
    with open(path, 'a', encoding='utf-8') as file:
        if os.stat(path).st_size:
            file.write('\n')
        file.write(data)


archive = 'voyna-i-mir.zip'
file_name = 'voyna-i-mir.txt'
file_to_write = 'analysis.txt'
archive_path = os.path.abspath(os.path.join(archive))
path = os.path.abspath(os.path.join(file_name))

with ZipFile(archive_path, "r") as myzip:
    myzip.extractall()

with open(path, 'r', encoding='utf-8') as file:
    data = file.read().strip().lower()

data = analyse_text(data)

for el in data:
    add_data(el, file_to_write)


