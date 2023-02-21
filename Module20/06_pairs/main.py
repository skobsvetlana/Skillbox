import random

my_list = [random.randint(0, 100) for _ in range(10)]
lenth = len(my_list)

new_list1 = list(zip(
    [el for i, el in enumerate(my_list) if i % 2 == 0],
    [el for i, el in enumerate(my_list) if i % 2 != 0]
))

new_list2 = [(my_list[i], my_list[i + 1]) for i in range(0, lenth - 1, 2)]

print(f'Оригинальный список: {my_list}')
print(f'Новый список: {new_list1}')
print(f'Новый список: {new_list2}')


#new_list3 = [(my_list.pop(0), my_list.pop(0)) for _ in range(lenth // 2)]
#print(f'Новый список: {new_list3}')

