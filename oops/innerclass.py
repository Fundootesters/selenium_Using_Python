

class car:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


    def show(self):
        print(self.brand, self.name)

    class facilities:

        def __init__(self):
            self.window = 'automatic'
            self.fuel = 'petrol'


c = car('BMW', 'Series 5')
c.show()