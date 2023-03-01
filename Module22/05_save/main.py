import os

def save_text(path, text):
    with open(path, 'w') as my_file:
        my_file.write(text)


text = input('Введите строку: ')
folders_list = input('Куда хотите сохранить документ? '
                     'Введите последовательность папок (через пробел): ').split()
file_name = input('Введите имя файла: ')
path = os.path.join(os.path.sep, '/'.join(folders_list), file_name)

if os.path.exists(path):
    ans = input('Вы действительно хотите перезаписать файл? ')
    if ans.lower() == 'да':
        save_text(path, text)
        print('Файл успешно перезаписан!')
    else:
        print('Текст не сохранен')
else:
    save_text(path, text)
    print('Файл успешно сохранён!')





#   Users svetlanaskobeltcyna PycharmProjects Python_Basic Module22 05_save