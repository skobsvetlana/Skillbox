def get_songs_duration(song):
    duration = 0
    for el in violator_songs:
        if el[0] == song:
            duration = el[1]

    return duration


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count = int(input('Сколько песен выбрать?'))
total_duration = 0

for i in range(count):
    print(f'Название {i + 1}-й песни: ')
    song = input()
    duration = get_songs_duration(song)
    if duration == 0:
        print(f'{song} не в альбоме')
    total_duration += duration
    total_duration = round(total_duration, 2)

print(f'Общее время звучания песен: {total_duration} минуты')

