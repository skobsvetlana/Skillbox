guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
guests_count = len(guests)
max_guests_count = 6

while True:
    print(f'Сейчас на вечеринке {guests_count} человек: {guests}')
    guest_status = input('Гость пришёл или ушёл? ')
    guest_name = input('Имя гостя: ')

    if guest_status == 'пришел'  or guest_status == 'Пришел':
        if guests_count < max_guests_count:
            guests.append(guest_name)
            guests_count += 1
            print(f'Привет, {guest_name}!')
        else:
            print(f'Прости, {guest_name}, но мест нет.')
    elif guest_status == 'ушел'  or guest_status == 'Ушел':
        guests.remove(guest_name)
        guests_count -= 1
        print(f'Пока, {guest_name}!')
    elif guest_status == 'пора спать'  or guest_status == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
    else:
        print('Неверный ввод')
        print("Введите: 'пришел', 'ушел' или 'пора спать'")





