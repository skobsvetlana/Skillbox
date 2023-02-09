def sort_list(my_list):
    i = 0
    j = len(my_list)

    while i <= j:
        min_ind = i
        max_ind = i

        for k in range(i, j):
            if my_list[k] < my_list[min_ind]:
                min_ind = k

            if my_list[k] > my_list[max_ind]:
                max_ind = k

        my_list[i], my_list[min_ind] = my_list[min_ind], my_list[i]
        my_list[j - 1], my_list[max_ind] = my_list[max_ind], my_list[j - 1]
        i += 1
        j -= 1

height1 = [x for x in range(160, 177, 2)]
height2 = [x for x in range(162, 181, 3)]

height1.extend(height2)
sort_list(height1)

print(height1)
