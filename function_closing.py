def fun1(x):
    """
    Пример 1
    замыкание функции, функция хранит fun хранит x из fun1
    """
    def fun(y):
        return x*y
    return fun


def funlamda(x):
    """
    Пример 2
    замыкание функции, только с лямбда
    х в области видимости ламбда
    """
    return lambda y: x*y


def f1(x):
    f2(x)  # ссылка на f2, опережающая допустима


def f2(x):
    print('запоминание', x)


if __name__ == '__main__':
    f = fun1(10)
    print('замыкание функции без лямбда')
    print(f(10))
    print(f(30))

    print('замыкание функции с лямбда')
    flambda = funlamda(10)
    print(flambda(10))
    print(flambda(30))

    print('Эквивалент примера 1, без вложения def')
    f1(10)