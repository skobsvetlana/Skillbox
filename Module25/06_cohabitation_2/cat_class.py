from pet_class import Pet
import random

class Cat(Pet):
    def __init__(self, name, home):
        super().__init__(name, home)


    def tear_the_wallpaper(self):
        self.satiety -= 10
        self.home.dirt += 5

    def cat_day(self):
        act = ''
        if self.satiety < 20:
            self.eat()
            act = 'Поела'
        else:
            n = random.randint(1, 2)
            if n == 1:
                self.sleep()
                act = 'Поспала'
            elif n == 2:
                self.tear_the_wallpaper()
                act = 'Поиграла'

        return act