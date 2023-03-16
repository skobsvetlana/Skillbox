from home_class import Home
from husband_class import Husband
from wife_class import Wife
from cat_class import Cat

def write_the_logs(data):
    with open('life_logs.txt', 'a', encoding='utf-8') as file:
        file.write(data)

our_home = Home()
husband = Husband('Artem', our_home)
wife = Wife('Sveta', our_home)
cat1 = Cat('Gerda', our_home)
cat2 = Cat('Daisy', our_home)
familly = (husband, wife, cat1, cat2)

flag = 1

for day in range(1, 366):
    write_the_logs((f'День {day}-ый\n'))
    write_the_logs(f'Чистота в доме: {our_home.dirt}, '
                   f'количество еды: {our_home.food}, '
                   f'количество денег: {our_home.money} '
                   f'количество корма: {our_home.cat_food}\n'
                   )

    if flag == 0:
        break

    if our_home.dirt > 90:
        wife.happiness -= 10
        husband.happiness -= 10

    our_home.dirt += 5

    act = ''
    info = ''

    for obj in familly:
        if isinstance(obj, Wife):
            act = obj.wife_day()
            info = f'сытость: {obj.satiety}, счастье: {obj.happiness}'
            if not obj.is_ok():
                flag = 0
                break
        elif isinstance(obj, Husband):
            act = obj.husband_day()
            info = f'сытость: {obj.satiety}, счастье: {obj.happiness}'
            if not obj.is_ok():
                flag = 0
                break
        elif isinstance(obj, Cat):
            act = obj.cat_day()
            info = f'сытость: {obj.satiety}'

        data = '\t{} {}, {}\n'.format(obj.name, act, info)
        write_the_logs(data)

earned_money = husband.earned_money
eaten_food = husband.eaten_food + wife.eaten_food
fur_coats = wife.bought_fur_coats

print('Заработано денег: {}, съедено еды: {}, куплено шуб: {}'.format(earned_money,
                                                                      eaten_food,
                                                                      fur_coats
                                                                      ))








