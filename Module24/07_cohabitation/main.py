from cohabitation_class import Human
from random import randint

def roll_the_dice():
    res = randint(1, 6)

    return res


def is_dead(human):
    if human.satiety <= 0:
        print('{} умер'.format(human.name))
        return True
    else:
        return False


def act():
    dice = roll_the_dice()

    if human.satiety < 20:
        human.eat()
        print('{} поел'.format(human.name))
    elif human.home.fridge == 0:
        human.do_shoping()
        print('{} сходил в магазин'.format(human.name))
    elif human.home.drawer < 50:
        human.work()
        print('{} поработал'.format(human.name))
    elif dice == 1:
        human.work()
        print('{} поработал'.format(human.name))
    elif dice == 2:
        human.eat()
        print('{} поел'.format(human.name))
    else:
        human.play()
        print('{} поиграл'.format(human.name))

    human.print_info()


human1 = Human('Артем')
human2 = Human('Света')
humans = (human1, human2)

for i in range(1, 365):
    if is_dead(human1) or is_dead(human2):
        break

    print('День {}'.format(i))
    for human in humans:
        act()





