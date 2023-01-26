def get_input_parameters(list_container_weights, new_container_weight):
    return [list_container_weights, new_container_weight]


def display_result(serial_number_new_container):
    print(serial_number_new_container)


def search_serial_number_new_container(list_container_weights, new_container_weight):
    serial_number_new_container = 0
    lenth = len(list_container_weights)
    for i in  range(lenth):
        if new_container_weight > list_container_weights[i]:
            serial_number_new_container = i + 1
            break

    return serial_number_new_container


def input_conrol(input_data):
    for el in input_data:
        if el >= 200:
            return False

    return True


if __name__ == '__main__':
    input_data = get_input_parameters()  # получаем параметры

    while True:
        if input_conrol(input_data):
            break
        else:
            print('Вес одного из контейнеров превышает 200 кг')

    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
