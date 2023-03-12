from taxes_classes import Person, Apartment, Car, CountryHouse

person1 = Person(name='Artem', money=100000)

apt29 = Apartment(worth=20000000)
skoda1 = Car(worth=3600000)

person1.add_property(apt29)
person1.add_property(skoda1)
print(person1)
person1.print_taxes()


person2 = Person(name='Sveta', money=10000)
apt14 = Apartment(worth=3500000)
skoda2 = Car(worth=1600000)
chouse = CountryHouse(worth=2000000)

person2.add_property(apt14)
person2.add_property(skoda2)
person2.add_property(chouse)
person2.add_property('apt74')
print(person2)
person2.print_taxes()


