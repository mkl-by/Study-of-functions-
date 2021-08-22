def fun1(x):
    """замыкание функции, функция хранит fun хранит x из fun1"""
    def fun(y):
        return x*y
    return fun


def funlamda(x):
    """замыкание функции, только с лямбда"""
    return lambda y: x*y

if __name__ == '__main__':
    f = fun1(10)
    print('замыкание функции без лямбда')
    print(f(10))
    print(f(30))

    print('замыкание функции с лямбда')
    flambda = funlamda(10)
    print(flambda(10))
    print(flambda(30))