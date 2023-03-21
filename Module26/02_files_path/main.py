import os

def gen_files_path(required_dir, path=os.path.abspath(os.path.join(os.path.sep))):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield os.path.join(root, name)

        for name in dirs:
            if name == required_dir:
                break


path = os.path.abspath('../../')
#required_dir = '02_files_path'
required_dir = 'Module26'



for file in gen_files_path(required_dir=required_dir, path=path):
    print(file)




