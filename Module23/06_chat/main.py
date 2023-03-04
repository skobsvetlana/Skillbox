import os

FILE_NAME = 'chat.txt'
PATH = os.path.abspath(os.path.join(FILE_NAME))

def chat(name):
    try:
        while True:
            ans = input('Посмотреть текущий текст чата - введите 1:\n'
                        'Отправить сообщение - введите 2:\n')

            if ans == '1':
                if not os.path.exists(PATH):
                    print('Сообщений по нет')
                else:
                    read_from_file(PATH)
            elif ans == '2':
                text = input('Введите сообщение: ')
                add_to_file(PATH, name, text)
            else:
                raise ValueError
    except ValueError:
        print(f'Пользователь вышел {name} из чата.')


def add_to_file(file, name, data):
    with open(file, 'a', encoding='utf-8') as file:
        file.write(''.join([name, ':', '\n']))
        file.write(''.join(['\t', data, '\n']))


def read_from_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        for line in data:
            print(line)


while True:
    name = input('Введите имя: ')
    if name == 'стоп':
        break
    chat(name)




