def get_input_parameters(сells):
    return сells


def display_result(cells):
    print(cells)


def select_cells(cells):
    result = []
    lenth = len(cells)

    for i in range(lenth):
        if cells[i] < i:
            result.append(cells[i])

    return result


if __name__ == '__main__':
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
