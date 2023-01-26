def display_result(participants_names):
    print(participants_names)


def get_participants_names(names):
    result = []
    lenth = len(names)

    for i in range(lenth):
        if i % 2 == 0:
            result.append(names[i])

    return result

if __name__ == '__main__':
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
