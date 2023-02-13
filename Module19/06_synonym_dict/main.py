n = int(input('Введите количество пар слов: '))
synonyms = {}

for i in range(n):
    print(f'Введите {i + 1}-ую пару через пробел: ', end='')
    pair = input().lower().split()
    synonyms[pair[0]] = pair[1]

word = input('Введите слово: ').lower()

for key, value in synonyms.items():
    if key == word:
        print('Синоним: {}'.format(value))
        break
    elif value == word:
        print('Синоним: {}'.format(key))
        break
else:
    print('Такого слова в словаре нет.')



#text = [Привет Здравствуйте, Печально Грустно, Весело Радостно]

