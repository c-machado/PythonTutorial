#object inherit the things within the object python class

class Car(object):

    wheels = 4

    #use to initialize all the objects within the class, it's like the constructor methos in java
    #_self param use to refer the object that gets created
    def __init__(self, make):
        #assigning make value received to the make attribute in the current class
        self.make = make

    def info(self):
        print('make of the car: ' + self.make)

    def drive(self):
        print('in drive')

    def stop(self):
        print('in stop')
        

print(Car.wheels)

c1 = Car('bmw')
c1.info()
c1.wheels = 3
print(c1.wheels)

#changing global values doesn't change the original value
print(Car.wheels)