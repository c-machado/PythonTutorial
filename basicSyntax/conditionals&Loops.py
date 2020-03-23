if 100 > 10:
    print('one hundred is greater than 10')

# value = 'green'
# if value == 'green':
#     print('in if')
# elif value == 'blue':
#     print('en elif')
# else:
#     print('in else')

# x = 0
# while x < 10:
#     print('x value' + str(x))
#     x = x + 1
#
# l = []
# num = 0
# while num < 10:
#     l.append(num)
#     num = num + 1
#     if num > 2:
#         break
# print(l)
#
# my_string = 'asdfg'
#
# for c in my_string:
#     if c == 'a':
#         print('A', end=' ')
#     else:
#         print(c, end=' ')
#
# cars = ['jeep', 'mini', 'electric']
# for car in cars:
#     print(car)
#
d = {1: 'one', 2: 'two', 3: 'three'}
# for k in d:
#     print(k + '' + str(d[k]))

for k, v in d.items():
    print(k)
    print(v)

lista1 = [1, 2, 3]
lista2 = [10, 20, 30, 40, 50]

for a, b in zip(lista1, lista2):
    if a > b:
        print(a)
    else:
        print(b)

a = range(0, 10, 2)
print(type(a))
print(list(a))

for num in range(4):
    print(num)
