from fathers_mothers_kids_class import Adult, Child

mama = Adult('Luda', 20)
mama.info()
child1 = Child('SS', 2)
mama.add_child(child1)
mama.info()

child1.info()
mama.to_calm(child1)
child1.calm = False
child1.info()
mama.to_calm(child1)
child1.info()

child1.hungry = True
child1.info()
mama.to_feed(child1)
child1.info()

child2 = Child('AV', 10)
mama.add_child(child2)
mama.info()
