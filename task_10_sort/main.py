def get_input_parameters(original_list):
    return original_list


def display_result(sorted_list):
    print(sorted_list)


def sort_list(original_list):
    for i in range(1, len(original_list)):
        for j in range(i, 0, -1):
            if original_list[j] < original_list[j - 1]:
                original_list[j], original_list[j - 1] = original_list[j - 1], original_list[j]
            else:
                break

    return original_list


if __name__ == '__main__':
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
