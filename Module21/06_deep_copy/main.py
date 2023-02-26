site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
     }
}


def my_deep_copy(data, new_data):
    for key, value in data.items():
        if isinstance(value, dict):
            new_data[key] = value.copy()
            my_deep_copy(value, value)


def make_site(site, original, replacement):
    for key, value in site.items():
        if isinstance(value, dict):
            make_site(value, original, replacement)
        else:
            if original in value:
                site[key] = value.replace(original, replacement)


n = int(input('Сколько сайтов: '))
original = 'телефон'

for _ in range(n):
    site_copy = {}
    my_deep_copy(site, site_copy)
    replacement = input('Введите название продукта для нового сайта: ')

    make_site(site_copy, original, replacement)

    print(f'Сайт для {replacement}: \n')
    print(site_copy)










