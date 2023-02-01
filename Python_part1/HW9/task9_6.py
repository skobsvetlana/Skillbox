'''Задача 6. Спецшифр
Что нужно сделать

Два сотрудника спецслужб переписываются необычным шифром. Каждую букву они шифруют в виде строки, внутри которой есть длинная последовательность букв “s”, а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.

Напишите программу, которая получает на вход строку, подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.

'''

print('Задача 6. Спецшифр \n')

sequence = input('Введите строку: ')
max_sequence = 0
curr_sequence = 0

for letter in sequence:
    if letter == 's':
        curr_sequence += 1
    else:
        if curr_sequence >= max_sequence:
            max_sequence = curr_sequence
            curr_sequence = 0
    print(curr_sequence, max_sequence)
if curr_sequence > max_sequence:
    max_sequence = curr_sequence
print(f'Самая длинная последовательность: {max_sequence}')



