a = float(input('введите радиус круга в см'))

def circle(a):
    b = (2*3.14*a)
    print('длинна окружности равна', b)
    c = (3.14*a**2)
    print('площадь окружности равна', c)
    return(b,c)

print(circle(a))