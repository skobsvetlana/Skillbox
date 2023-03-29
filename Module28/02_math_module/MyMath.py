from math import pi

class MyMath:
    '''Класс для вычисления пазличных характеристик геометрических фигур,
    в том числе площадей, периметров, объемов '''

    '''вычисление длины окружности'''
    @classmethod
    def circle_len(cls, radius: float) -> float:

        return 2 * pi * radius


    '''вычисление площади круга'''
    @classmethod
    def circle_sq(cls, radius: float) -> float:
        return pi * radius ** 2


    '''вычисление объёма куба'''
    @classmethod
    def cube_vol(cls, lenght: float) -> float:
        return lenght ** 3


    '''вычисление площади поверхности сферы'''
    @classmethod
    def sphere_sq(cls, radius: float) -> float:
        return 4 * pi * radius ** 2
