violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

n = int(input('Сколько песен выбрать? '))
total_duration = 0

for i in range(n):
    print('Название {}-ой песни: '.format(i + 1), end='')
    name = input()
    total_duration += violator_songs[name]

print('Общее время звучания песен: {} минуты'.format(round(total_duration, 2)))
