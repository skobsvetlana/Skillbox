
def new_el(el, shift):
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    if el in alphabet:
        new_ind = (alphabet.index(el) + shift) % 33
        print(alphabet.index(el), new_ind)
        el = alphabet[new_ind]

    return el


text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
text = [new_el(el, shift) for el in text]

print(f'Зашифрованное сообщение: {"".join(text)}')



