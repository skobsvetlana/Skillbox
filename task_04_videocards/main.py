def get_input_parameters(video_cards):
    return video_cards


def display_result(old_video_cards, new_video_cards):
    print(old_video_cards)
    print(new_video_cards)


def select_video_cards(video_cards):
    new_video_cards = []
    new_video_card_id = max(video_cards)

    for el in video_cards:
        if el != new_video_card_id:
            new_video_cards.append(el)

    return new_video_cards


if __name__ == '__main__':
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
