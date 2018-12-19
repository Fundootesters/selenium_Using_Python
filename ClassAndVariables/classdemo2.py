"""
Object Oriented Programming
"""

class Car(object):

    wheels = 4

    def __init__(self, make, model="550i"):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the card is " + self.make)
        print("Model of car is " + self.model)


c1 = Car('bmw')
c1.info()

c2 = Car('benz')
c2.info()

print(Car.wheels)
