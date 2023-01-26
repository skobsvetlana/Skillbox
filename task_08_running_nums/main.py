def get_input_parameters(shift, original_list):
    return [shift, original_list]


def display_result(shifted_list):
    return shifted_list


def shift_list(shift, original_list):
    lenth = len(original_list)

    if shift == lenth:
        return original_list

    shifted_list = original_list[lenth - shift:] + original_list[:lenth - shift]

    return shifted_list

if __name__ == '__main__':
    input_data = get_input_parameters()  # получаем параметры
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
