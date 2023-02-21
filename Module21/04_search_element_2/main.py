def find_value_by_key(data, my_key, deep=0):
    if my_key in data:
        return data[my_key]

    res = None

    for value in data.values():
        if deep == 1:
            break

        if isinstance(value, dict):
            res = find_value_by_key(value, my_key, deep - 1)
            if res:
                break

    return res


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key_to_find = input('Введите искомый ключ: ')
deep = input('Хотите ввести максимальную глубину? Y/N: ').lower()

if deep == 'y':
    deep = int(input('Введите максимальную глубину: '))
else:
    deep = 0


my_value = find_value_by_key(site, key_to_find, deep)

print('Значение ключа: {}'.format(my_value))

