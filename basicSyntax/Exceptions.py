def exceptionHandling():
    try:
        car = {'make': 'bmw', 'model': 'jeep', 'year': '2020'}
        carColor = car['color']
        print(carColor)
    except:
        print('exception')
    else:
        print('not exception')
    finally:
        print('finally')


exceptionHandling()


