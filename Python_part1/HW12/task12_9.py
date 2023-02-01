'''Задача 9. Недоделка
Что нужно сделать

Вы пришли на работу в контору по разработке игр, целевая аудитория — дети и их родители. У прошлого программиста было задание сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них. Однако программист, на место которого вы пришли, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта. Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».

Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит, победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.

Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

def rock_paper_scissors():
    # Здесь будет игра "Камень, ножницы, бумага"


def guess_the_number():
    # Здесь будет игра "Угадай число"


def mainMenu():
    # Здесь главное меню игры


mainMenu():
    pass'''

print('Задача 9. Недоделка \n')

import random


def rock(ans):
    if ans == 1:
        print('\n Ничья')
    elif ans == 2:
        print('Вы победили. Камень бьёт ножницы')
    else:
        print('Вы проиграли. Бумага кроет камень')


def scissors(ans):
    if ans == 1:
        print('Вы проиграли. Камень бьёт ножницы')
    elif ans == 2:
        print('\n Ничья')
    else:
        print('Вы победили. Ножницы режут бумагу')


def paper(ans):
    if ans == 1:
        print('Вы победили. Бумага кроет камень')
    elif ans == 2:
        print('Вы проиграли. Ножницы режут бумагу')
    else:
        print('\n Ничья')


def print_comp_choice(ans):
    if ans == 1:
        print('\nКомпьтер загадал камень')
    elif ans == 2:
        print('\nКомпьтер загадал ножницы')
    else:
        print('\nКомпьтер загадал бумагу')


def rock_paper_scissors():
    ans = random.randint(1, 3)
    choice = int(input('\n Выберите камень, ножницы или бумагу: \n\n камень - 1, \n ножницы - 2, \n бумага - 3 \n\n'))

    if choice == 1:
        print_comp_choice(ans)
        rock(ans)
    elif choice == 2:
        print_comp_choice(ans)
        scissors(ans)
    elif choice == 3:
        print_comp_choice(ans)
        paper(ans)
    else:
        print('\n Неверный ввод')
        rock_paper_scissors()


def guess_the_number():
    number = 78

    while True:
        res = int(input('Введите число: '))

        if res == number:
            print('\n Вы угадали!')
            break
        elif res > number:
            print('\n Число больше, чем нужно. Попробуйте ещё раз!')
        else:
            print('\n Число меньше, чем нужно. Попробуйте ещё раз!')

        print()


def mainMenu():
    choice = int(input('Выберите игру: \n\n Камень, ножницы, бумага - 1 \n Угадай число - 2 \n\n'))
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    else:
        print('\n Неверный ввод')
        mainMenu()


mainMenu()

