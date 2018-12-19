
class Car(object):

    def __init__(self):
        print("Created instance for car....")

    def drive(self):
        print("Car Started.........")

    def stop(self):
        print("Car stopped....")


class Bmw(Car):

    def __init__(self):
        Car.__init__(self)
        print("created instance for BMW")

    def drive(self):
        super(Bmw, self).drive()
        print("You are driving BMW, Enjoy..")


c = Car()
c.drive()
c.stop()

b = Bmw()
b.stop()
b.drive()
