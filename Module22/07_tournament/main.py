import os

def transform_data(data):
    res = [f'{data[1][:1]}. {data[0]}', int(data[2])]

    return res


def add_data(data, file_name):
    path = os.path.abspath(os.path.join(file_name))
    with open(path, 'a', encoding='utf-8') as file:
        if os.stat(path).st_size:
            file.write('\n')
        file.write(data)


file_name = 'first_tour.txt'
file_to_write = 'second_tour.txt'
path = os.path.abspath(os.path.join(file_name))

with open(path, 'r') as file:
    data = [line.split() for line in file.read().split('\n') if line]
    min_scor = int(data[0][0])
    data = data[1:]

data = [transform_data(el) for el in data if int(el[2]) > min_scor]
data = sorted(data, key=lambda x: x[1], reverse=True)
data = [f'{el[0]} {str(el[1])}' for el in data]

add_data(str(len(data)), file_to_write)

for el in data:
    add_data(el, file_to_write)
