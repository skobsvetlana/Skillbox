def get_input_parameters(films):
    return films


def display_result(favorite_films, errors):
   print(favorite_films)
   print(errors)


def add_favorite_film(new_favorite_films, available_films):
    favorite_films = []
    errors = []

    for film in new_favorite_films:
        if film in available_films:
            favorite_films.append(film)
        else:
            errors.append(film)

    return (favorite_films, errors)


if __name__ == '__main__':
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист",
        "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(
        new_favorite_films,
        available_films
    )  # добавлем фильмы в список "любимых".
    display_result(favorite_films, errors)  # выводим результат
