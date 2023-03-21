import os
from collections.abc import Iterable

def read_file(path: str) -> str:
    count = 0
    if path.endswith('.py'):
        with open(path, 'r', encoding='utf-8') as file:
            for el in file.readlines():
                if el != '\n' and not el.startswith('#'):
                    count += 1

    return 'В файле {file_name} - {num} строк'.format(file_name=path,
                                                    num=count)


def get_files(path: str) -> Iterable:
    for root, dirs, files in os.walk(path):
        for name in files:
            path = os.path.join(root, name)
            yield read_file(path)


path = '/Users/svetlanaskobeltcyna/PycharmProjects/Python_Basic/Module26'
res = get_files(path=path)

for el in res:
    print(el)