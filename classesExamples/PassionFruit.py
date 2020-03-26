from classesExamples.Fruit import Fruit


class PassionFruit(Fruit):

    def nutrition(self):
        print('this is the more delicious, but not the most nutritive one')

    def color(self):
        print('It is usually yellow')

b = Fruit()
b.nutrition('passion fruit')
b.shape('round')

a = PassionFruit()
a.nutrition()
a.color()


