def fill_the_list(my_list, n):
    for i in range(n):
        print(f'Введите {i + 1}-е число для первого списка: ')
        number = int(input())
        my_list.append(number)


def delete_el(my_list, el):
    my_list.remove(el)

list1 = []
list2 = []

fill_the_list(list1, 3)
fill_the_list(list2, 7)

list1.extend(list2)

for el in list1:
    n = list1.count(el)
    for _ in range(1, n):
        delete_el(list1, el)

print(list1)



