# Second Way to create method

class car:

    wheel = 4

    def __init__(self, make, model = '550i'):
        self.make = make
        self.model = model

    def info(self):
        print('Make of the car is ' + self.make)
        print('Model of the car is ' + self.model)


c = car('Honda')
c.wheel = 5
c.info()

print(c.wheel)

c1 = car('BMW')
c1.info()
print(c1.wheel)

print(car.wheel)