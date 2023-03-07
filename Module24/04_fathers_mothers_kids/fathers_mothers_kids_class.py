class Adult():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []


    def info(self):
        print('\nname: {}, age: {}'.format(self.name, self.age))
        if not self.children:
            print('Детей пока нет')
        else:
            print('children: ', end=' ')
            for child in self.children:
                print(child.child_name,  end=', ')


    def to_calm(self, child):
        if child.calm:
            print('Ребенок спокоен.')
        else:
            child.calm = True
            print('Родитетель успокоил ребенка')


    def to_feed(self, child):
        if child.hungry:
            child.hungry = False
            print('Родитетель накормил ребенка.')
        else:
            print('Ребенок уже сыт')


    def add_child(self, child):
        if isinstance(child, Child):
            if self.age - child.child_age > 16:
                self.children.append(child)
            else:
                print('Разница в возрасте родителя и ребенка меньше 16-ти лет')
                try:
                    new_child_age = int(input('Введите корректный возраст ребенка: '))
                    child.child_age = new_child_age
                    self.children.append(child)
                except ValueError:
                    print('Возраст должен быть целым числом.')
        else:
            print('{} не является экземпляром класса Child'.format(child))



class Child():

    def __init__(self, child_name, child_age, calm=True, hungry=False):
        self.child_name = child_name
        self.child_age = child_age
        self.calm = calm
        self.hungry = hungry


    def info(self):
        print('\nname: {}, age: {},\ncalm = {}, hungry = {}'.format(
            self.child_name, self.child_age, self.calm, self.hungry
        ))
