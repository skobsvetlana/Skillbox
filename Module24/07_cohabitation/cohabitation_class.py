class Home:
    def __init__(self):
        self.drawer = 0
        self.fridge = 50



class Human:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.home = Home()


    def eat(self):
        if self.home.fridge > 20:
            self.satiety += 20
            self.home.fridge -= 20
        else:
            self.satiety += self.home.fridge
            self.home.fridge = 0


    def work(self):
        self.satiety -=20
        self.home.drawer += 20


    def play(self):
        self.satiety -= 10


    def do_shoping(self):
        self.home.drawer -= 30
        self.home.fridge += 30


    def print_info(self):
        print('У {} - сытость = {}, количество денег = {}, количество еды = {}'.format(self.name,
                                                                                       self.satiety,
                                                                                       self.home.drawer,
                                                                                       self.home.fridge))












