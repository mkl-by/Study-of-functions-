#  генераторные функции, пройти по ней можно только 1 раз, затем создаем новую

def fun(data):
    for i in range(data+1)[1:]:
        yield i*2  # позже возобновляем работу с этого места


def gen():
    for i in range(10):
        x = yield i
        print(x)


# расширенный синтаксис yield: делегирование работы подгенератору с помощью конструкции from <генератор>.
def func1(data: int) -> int:
    for i in range(data): yield i
    for i in (x ** 2 for x in range(data)): yield i


# то же что и func1 только с from
def func2(data: int) -> int:
    yield from range(data)
    yield from (x ** 2 for x in range(data))


if __name__ == '__main__':

    a = fun(10)  # a генераторная функция, поддерживает метод __next__
    print(a.__next__())
    print(a.__next__())

    for i in a:
        print(i, ':')

    # send metod
    a = gen()
    print(a.__next__())
    print(a.send(12))
    print(a.send(10))

    # генераторное выражение
    print('Генераторное выражение')
    print('списковое включение', [x*2 for x in range(5)])
    a = (x*2 for x in range(5))  # генераторное выражение
    print(a.__next__())
    print(a.__next__())
    for i in a:
        print(i, ':')

    # расширение yield c помощью from
    print('расширение yield c помощью from')
    print('func1:', list(func1(5)), 'без from')
    print('func2:', list(func2(5)), 'c from')
