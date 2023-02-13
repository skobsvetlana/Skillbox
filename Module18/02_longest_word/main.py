text = input('Введите строку: ').split()
res = ''

for word in text:
    if len(word) > len(res):
        res = word

print(f'\nСамое длинное слово: {res}')
print(f'Длина этого слова: {len(res)}')
