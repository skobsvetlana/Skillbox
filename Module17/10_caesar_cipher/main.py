
def new_el(el, shift):
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    if el in alphabet:
        new_ind = alphabet.index(el) + shift
        if new_ind > 32:
            new_ind -= 33
        el = alphabet[new_ind]

    return el


# text = input('Введите сообщение: ')
# shift = int(input('Введите сдвиг: '))




text = list('это питон.')
shift = 3
text = [new_el(el, shift) for el in text]

print(f'Зашифрованное сообщение: {"".join(text)}')



