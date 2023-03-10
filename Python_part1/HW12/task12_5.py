'''Задача 5. Текстовый редактор
Что нужно сделать

Мы продолжаем разрабатывать новый текстовый редактор, и в этот раз нам поручили написать для него код, который считает количество любой буквы и любой цифры в тексте (а не только буквы Ы, как раньше).

Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое в нём количество цифр K и букв N. Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.



Пример:

Введите текст: 100 лет в обед

Какую цифру ищем? 0

Какую букву ищем? л

Количество цифр 0: 2

Количество букв л: 1'''

print('Задача 5. Текстовый редактор \n')


def count_letters(text, digit, letter):
    digit_count = 0
    letter_count = 0

    for symbol in text:
        if symbol == digit:
            digit_count += 1

        if symbol == letter:
            letter_count += 1

    print(f'\n Количество цифр {digit}: {digit_count}'.format())
    print(f'\n Количество цифр {letter}: {letter_count}'.format())


text = input('Введите текст: ')
digit = input('\n Какую цифру ищем? ')
letter = input('\n Какую букву ищем? ')
count_letters(text, digit, letter)