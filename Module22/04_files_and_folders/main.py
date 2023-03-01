import os

def get_dir_info(path, dir_num=0, file_num=0, dir_size=0):
    for el in os.listdir(path):
        new_path = os.path.join(path, el)

        if os.path.isfile(new_path):
            file_num += 1
            dir_size += os.path.getsize(new_path)
        elif os.path.isdir(new_path):
            dir_num += 1
            dir_num, file_num, dir_size = get_dir_info(new_path, dir_num, file_num, dir_size)

    return dir_num, file_num, dir_size


path = input('Введите путь до каталога: ')
#path = '/Users/svetlanaskobeltcyna/PycharmProjects/Python_Basic/Module22'
dir_num, file_num, dir_size = get_dir_info(path)

print('Размер каталога (в Кб): {size}\n'
      'Количество подкаталогов: {dirs}\n'
      'Количество файлов: {files}'.format(size=dir_size,
                                          dirs=dir_num,
                                          files=file_num,))

