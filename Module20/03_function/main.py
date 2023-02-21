def slicer(my_tuple, sym):
    n = my_tuple.count(sym)

    if n == 0:
        return ()

    ind1 = my_tuple.index(sym)

    if n == 1:
        return my_tuple[ind1:]
    else:
        ind2 = my_tuple[ind1 + 1:].index(sym)

        return my_tuple[ind1: ind1 + ind2 + 2]

#print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
