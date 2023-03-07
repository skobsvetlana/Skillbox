import math

class Circle:
    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius


    def get_square(self):
        return math.pi * self.radius ** 2


    def get_perimeter(self):
        return 2 * math.pi * self.radius


    def increase_circle(self, n):
        self.radius *= n


    def get_is_intersect(self, circle2):
        distance = math.sqrt((self.x - circle2.x) ** 2 + (self.y - circle2.y) ** 2)
        return distance < self.radius + circle2.radius


    def print_info(self):
        print('x = {}, y = {}, радиус = {}, площадь круга = {}, периметр круга = {}'.format(
            self.x, self.y, self.radius, self.get_square(), self.get_perimeter()))


    def is_intersect(self, circle2):
        try:
            res = self.get_is_intersect(circle2)
            if res:
                print('Круги пересекаются.')
            else:
                print('Круги не пересекаются.')
        except AttributeError:
            print('{} не является экземпляром класса Circle. Невозможно получить корректный ответ'.format(circle2))
