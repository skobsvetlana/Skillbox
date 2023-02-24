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

def make_site(site, original, replacement):
    for key, value in site.items():
        if isinstance(value, dict):
            make_site(value, original, replacement)
        else:
            if original in value:
                site[key] = value.replace(original, replacement)


import copy

n = int(input('Сколько сайтов: '))
original = 'телефон'

for _ in range(n):
    site_copy= copy.deepcopy(site)
    replacement = input('Введите название продукта для нового сайта: ')

    make_site(site_copy, original, replacement)

    print(f'Сайт для {replacement}: \n')
    print(site_copy)









