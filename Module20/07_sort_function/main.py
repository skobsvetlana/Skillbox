def tpl_sort(tpl):
    sorted_tpl = list(tpl)
    i, j = 0, len(sorted_tpl) - 1

    while i < j:
        max_el, max_ind  = sorted_tpl[i], i
        min_el, min_ind = sorted_tpl[i], i

        for k in range(i + 1, j + 1):
            if sorted_tpl[k] > max_el:
                max_el, max_ind  = sorted_tpl[k], k

            if sorted_tpl[k] < min_el:
                min_el, min_ind = sorted_tpl[k], k

        sorted_tpl[i], sorted_tpl[min_ind] = sorted_tpl[min_ind], sorted_tpl[i]
        sorted_tpl[j], sorted_tpl[max_ind] = sorted_tpl[max_ind], sorted_tpl[j]
        i += 1
        j -= 1

    return tuple(sorted_tpl)


#print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
