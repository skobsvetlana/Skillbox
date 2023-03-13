import math

class Auto:
    def __init__(self, coordinates=(0, 0), angle=45):
        self.set_coordinates(coordinates)
        self.set_angle(angle)


    def __str__(self):
        return 'Автомобиль сейчас находится в точке с координатами {}, направление движения - {} градусов'.format(
            self.__coordinates,
            self.__angle
        )


    def drive(self, distance):
        x, y = self.__coordinates
        x += round(distance * math.cos(math.radians(self.__angle)), 0)
        y += round(distance * math.sin(math.radians(self.__angle)), 0)
        self.__coordinates = (x, y)


    # def change_direction(self, new_angle):
    #     self.__angle = new_angle


    def turn_right(self, angle):
        self.__angle -= angle


    def turn_left(self, angle):
        self.__angle += angle

    def set_coordinates(self, coordinates):
        if isinstance(coordinates, tuple):
            if len(coordinates) == 2:
                self.__coordinates = coordinates
            else:
                print("Необходимоввести две координаты через запятую (x, y): ")
        else:
            print('Координаты необходимо ввести в круглых скобках через запятую (x, y')


    def set_angle(self, angle):
        if 0 < angle < 360:
            self.__angle = angle
        else:
            print('Угол должен быть числом от 0 до 360')


    def get_coordinates(self):
        return self.__coordinates

class Bus(Auto):
    def __init__(self):
        super().__init__()


