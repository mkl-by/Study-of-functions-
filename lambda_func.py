def func(x: int, y: int, z: int) -> int:
    return x+y+z


def func1():
    ss = 'as'
    act = lambda x: ss+x
    return act

L = [
    lambda x: x*2,
    lambda x: x*4,
    lambda x: x*6,
] # or [f1, f2, f3...], where def f1(x): return x*2, def f2(x)...

if __name__ == '__main__':

    print(func(1, 2, 3))

    f = lambda x, y, z: x+y+z   # то же что и func
    print(f(1, 2, 3))

    x = lambda a='fee', b='fie', c='foe': a + b + c
    print(x('www'))

    f = func1()
    print(f('qqq'))

    print('list in cycle')
    for i in L:
        print(i(2))

    print('dict and key')
    key = 'got'
    # можно делать и в обычных функциях
    print(
        {'already': (lambda: 2 + 2), 'got': (lambda: 2*4), 'one': (lambda: 2 ** 6)}[key]()
    )

    print('Operator branching ')
    lower = (lambda х, у: х if х < у else у)
    print(lower('xx', 'yy'))
    # or
    # showall = lambda x: list (map (sys . stdout, write, x))
    # t= showall(['spam\n’, ’toast\n’, ’eggs\n’])
    # showall = lambda x: [sys. stdout .write (line) for line in x]
    # showall = lambda x: [print(line, end=' ’) for line in x]
    # showall = lambda x: print ( *x, sep='', end='')
    print('вложенные функции и область видимости ламбда, лучше избегать')
    action = (lambda х: (lambda у: х + у))
    act = action(99)
    print(act(1))