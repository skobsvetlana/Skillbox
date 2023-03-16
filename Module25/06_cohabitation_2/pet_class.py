class Pet:
    satiety = 30

    def __init__(self, name, home):
        self.name = name
        self.home = home


    def eat(self):
        if self.home.cat_food > 10:
            self.home.cat_food -= 10
            self.satiety += 20
        else:
            self.satiety += 2 * self.home.cat_food
            self.cat_food = 0


    def sleep(self):
        self.satiety -= 10

    def is_ok(self):
        if self.satiety <= 0:
            return False
        return True

