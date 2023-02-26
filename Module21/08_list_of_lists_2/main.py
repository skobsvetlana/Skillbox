def flat(my_list):
    if not my_list:
        return []

    if isinstance(my_list[0], list):
        return flat(my_list[0]) + flat(my_list[1:])
    else:
        return my_list[:1] + flat(my_list[1:])


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(flat(nice_list))
