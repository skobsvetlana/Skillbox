def get_country(city):
    for key, value in countries.items():
        if city in value:
            return key


n = int(input('Количество стран: '))
countries = dict()

for i in range(n):
    print('{}-ая страна: '.format(i + 1), end='')
    country = input().split()
    countries[country[0]] = country[1:]

for i in range(3):
    print('{}-ый город: '.format(i + 1), end='')
    city = input()
    res = get_country(city)
    if res:
        print('\nГород {} расположен в стране {}.'.format(city, res))
    else:
        print('\nПо городу {} данных нет.'.format(city))
