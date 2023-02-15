def main_menu():
    print(
        'Введите номер действия:'
        '\n\t1. Добавить контакт'
        '\n\t2. Найти человека'
    )
    return int(input())


def add_cont(data):
    name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())

    if data.get(name, 0):
        print('Такой человек уже есть в контактах.')
    else:
        phone = input('Введите номер телефона: ')
        data[name] = phone

    print('\nТекущий словарь контактов: {}'.format(data))


def find_cont(data):
    surname = input('Введите фамилию для поиска: ').lower()
    count = 0

    for key, value in data.items():
        data_name, data_surname = key

        if data_surname.lower().startswith(surname) or surname.startswith(data_surname.lower()):
            print(data_surname, data_name, value)
            count += 1
    if count == 0:
        print('Контакта {} нет в телефонной книге.'.format(surname))


phone_book = dict()

while True:
    action = main_menu()

    if action == 1:
        add_cont(phone_book)
    elif action == 2:
        find_cont(phone_book)
    else:
        break
