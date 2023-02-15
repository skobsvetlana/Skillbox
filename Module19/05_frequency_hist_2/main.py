def symbol_count(text):
    res = dict()
    for sym in text:
        if sym in res:
            res[sym] += 1
        else:
            res[sym] = 1

    return res


text = input('Введите текст: ')
frequency_dict = symbol_count(text)

res = dict()

for key, value in frequency_dict.items():
    if value in res:
        res[value].append(key)
    else:
        res[value] = [key]

print('\nИнвертированный словарь частот:')

for key, value in res.items():
    print('{} : {}'.format(key, value))
