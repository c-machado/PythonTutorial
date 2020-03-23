a = 10

def sum_numbers(n1, n2):
    global a
    print('global '+ str(a))
    a=2
    print('local a ' + str(a))
    return n1 + n2

sum = sum_numbers(3, 4)
print(sum)
sum2 = sum_numbers(n1=3, n2=8)
print(sum2)

def isMetro(city):
    l = ['sfo', 'nyc']
    if city in l:
        return True
    else:
        return False

x = isMetro('nyc')
print(x)


def largest_num(*args):
    return max(args)

def min_num(*args):
    return min(args)

max = largest_num(0, -4, 60, 80, 8)
min = min(0, 9, -50, 9)

print(abs(-40))
print(abs(40))

print(type(5))





