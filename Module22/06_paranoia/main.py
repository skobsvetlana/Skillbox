import os
def caesar_cipher(text, shift):
    alphabet = list('abcdefghijklmnopqrstuvwx')
    res = []

    for el in text:
        if el.isupper():
            flag = 1
        else:
            flag = 0

        if el.lower() in alphabet:
            new_ind = (alphabet.index(el.lower()) + shift) % 24
            if flag:
                res.append(alphabet[new_ind].upper())
            else:
                res.append(alphabet[new_ind])
        else:
            res.append(el)

    return ''.join(res)


def add_data(data, file_name):
    path = os.path.abspath(os.path.join(file_name))
    with open(path, 'a', encoding='utf-8') as file:
        if os.stat(path).st_size:
            file.write('\n')
        file.write(data)


file_name = 'text.txt'
file_to_write = 'cipher_text.txt'
path = os.path.abspath(os.path.join(file_name))
shift = 1

with open(path, 'r') as file:
    while True:
        line = file.readline().strip()

        if not line:
            break

        encrypted_line = caesar_cipher(line, shift)
        add_data(encrypted_line, 'cipher_text.txt')
        shift += 1

print(f'зашифрованные данные заптсаны в файл {file_to_write}')









