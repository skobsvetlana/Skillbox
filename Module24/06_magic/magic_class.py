class Element:
    def __init__(self, name):
        self.name = name


    def __add__(self, other):
        return self.name + other.name


class Example_2:
    answer = 'сложили два класса и вывели'


a = Element(2)
b = Element(3)
c = a + b
print(c)
