'''Задача 3. Поступление
Что нужно сделать
В университете на факультет кибернетики очень серьёзный конкурс — поступают только сильнейшие, первые десять человек из списка. Потом среди поступивших определяется, кто будет получать стипендию. Для стипендии общий балл при поступлении должен быть не менее 290.

Напишите программу, которая получает на вход место студента в списке и его балл, а затем выводит соответствующие сообщения о поступлении и получении стипендии.

Пример 1:

Введите место в списке поступающих: 3

Введите количество баллов за экзамены: 295

Поздравляем, вы поступили!

Бонусом вам будет начисляться стипендия.

Пример 2:

Введите место в списке поступающих: 3

Введите количество баллов за экзамены: 270

Поздравляем, вы поступили!

Но вам не хватило баллов для стипендии.

Пример 3:

Введите место в списке поступающих: 11

К сожалению, вы не поступили.

Что оценивается
результат вывода корректен и соответствует примеру;
input содержит корректное приглашение для ввода;
переменные имеют значащие имена, а не только a, b, c, d (видео 2.3);
правильное употребление пробелов после запятых при бинарных и логических операциях;
правильно оформлены блоки if-elif-else, отступы одинаковы во всех блоках одного уровня.
'''
print('Задача 3. Поступление')

place = int(input('Введите место в списке поступающих: '))

if place > 10:
    print('К сожалению, вы не поступили.')
else:
    print('Поздравляем, вы поступили!')
    score = int(input('ведите количество баллов за экзамены: '))
    if score >= 290:
        print('Бонусом вам будет начисляться стипендия.')
    else:
        print('Но вам не хватило баллов для стипендии.')

print()


