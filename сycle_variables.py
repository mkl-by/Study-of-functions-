def fun():
    """
    попытка построить список функций с запоминаемым состоянием i
    Пример 3
    """
    arg = []
    for i in range(5):
        arg.append(lambda x: i+x)  # i запоминает только последнее состояние i=4
    return arg


def fun1():
    """
    попытка построить список функций с запоминаемым состоянием i
    Пример 4
    """
    arg = []
    for i in range(5):
        arg.append(lambda x, i=i: i+x)  # i запоминает все состояния
    return arg

if __name__ == '__main__':
    # для функции пример 3
    print('i запоминает только последнее состояние')
    arg = fun()
    print('i=0', arg[0](1))
    print('i=1', arg[1](2))
    print('i=2', arg[2](3))
    # для функциии пример 4
    print('i запоминает все состояния')
    arg = fun1()
    print('i=0', arg[0](1))
    print('i=1', arg[1](2))
    print('i=2', arg[2](3))
