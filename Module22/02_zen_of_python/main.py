with open("zen.txt") as my_file:
    data = my_file.read().split('\n')

for el in reversed(data):
    print(el)
