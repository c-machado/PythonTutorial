class Fruit(object):

    def __init__(self):
        print('constructor in Fruit class')

    def nutrition(self, fruit):
        fruit_nutrition = {'banana': 4, 'orange': 5, 'exotic': 6}
        if fruit in fruit_nutrition:
            print('nutrition: ' + str(fruit_nutrition[fruit]))

    def shape(self, shape):
        flag = 0
        fruitShapes = ['round', 'oval', 'other']
        for fruitShape in fruitShapes:
            if fruitShape == shape:
                flag = flag + 1
        if flag == 0:
            fruitShapes.append(shape)
            return True
        else:
            return False

a = Fruit()
print(a.nutrition('banana'))
if a.shape('one'):
    print('new shape was added')
if a.shape('round'):
    print('new shape was added')
else:
    print('shape has already existed')
