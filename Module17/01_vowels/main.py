vowels = 'аеёиоуыэюя'
text = input('Введите текст: ')
vowels_list = [x for x in text if x in vowels]

print(f'Список гласных букв: {vowels_list}')
print(f'Длина списка: {len(vowels_list)}')



