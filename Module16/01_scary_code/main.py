list1 = [1, 5, 3]
list2 = [1, 5, 1, 5]
list3 = [1, 3, 1, 5, 3, 3]

list1.extend(list2)

print(f'Кол-во цифр 5 при первом объединении: {list1.count(5)}')

while 5 in list1:
    list1.remove(5)

list1.extend(list3)
print(f'Кол-во цифр 3 при втором объединении: {list1.count(3)}')

print(f'Итоговый список: {list1}')





