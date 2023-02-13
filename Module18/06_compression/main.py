text = input('Введите строку: ')
res = []
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        res.append(text[i - 1])
        res.append(str(count))
        count = 1

res.append(text[-1])
res.append(str(count))

res = ''.join(res)

print(f'Закодированная строка: {res}')
