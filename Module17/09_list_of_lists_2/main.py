nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

flat_list =[el for sub_list2 in nice_list for sub_list1 in sub_list2 for el in sub_list1]

print(f'Ответ: {flat_list}')
