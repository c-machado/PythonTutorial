from classesExamples.CarExample import CarExample


class Bmw(CarExample):

    def __init__(self):
        CarExample.__init__(self)
        print('in init Bmw')

    def drive(self):
        print('in drive bmw')

    def display(self):
        print('in display')


car = CarExample()
car.drive()
car.stop()

b = Bmw()
b.drive()
b.display()



