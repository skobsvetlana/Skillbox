def get_input_parameters(word):
    return word


def display_result(number_unique_letters):
    print(number_unique_letters)


def count_number_unique_letters(word):
    unique_letters = []
    counter = 0

    for letter in word:
        if letter in unique_letters:
            counter += 1
        else:
            unique_letters.append(letter)

    result = len(unique_letters) - counter

    return result


if __name__ == '__main__':
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
