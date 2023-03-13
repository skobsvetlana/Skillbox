class MyDict(dict):
    def get(self, key, default=None):
        return super().get(key, 0)



my_dict = MyDict()

my_dict[1] = 'A'
my_dict[2] = 'B'
my_dict[3] = 'C'
my_dict[4] = 'D'
my_dict[5] = 'E'

print(my_dict.get(1))
print(my_dict.get(7))