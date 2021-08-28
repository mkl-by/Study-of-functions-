# косвенная рекурсия

def mysum(L):
    if not L: return 0
    return nonempty(L)

def nonempty(L):
    return L[0]+mysum(L[1:])

# прямая рекурсия


def ssum(L: list) ->int:
    return 0 if not L else L[0]+ssum(L[1:])


def list_sum(L: list) -> int:
        tot = 0
        for i in L:
            if not isinstance(i, list):
                tot += i
            else:
                tot += list_sum(i)
        return tot


''' факториал
    5!=1*2*3*4*5
    4!=1*2*3*4
    3!=1*2*3
    2!=1*2
    1!=1
    0!=1
    '''
def factorial(N: int) -> int:
    """
    factorial(5) -> 120
    factorial(4) -> 24
    factorial(3) -> 6
    factorial(2) -> 2
    factorial(1) -> 1
    factorial(0) -> 1
    """
    return N*factorial(N-1) if N else 1

"""
    hello
    hell
    hel
    he
    h
"""
def pars_str(stroka: str) -> None:
    print(stroka)
    return pars_str(stroka[:-1]) if stroka else 0


if __name__ == '__main__':
    L = [1, 2, 3]
    L1 = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(mysum(L))
    print(ssum(L))

    print(list_sum(L1))
    print(list_sum([1, [2, [3, [4, [5]]]]]))
    print(list_sum([[[[[1], 2], 3], 4], 5]))
    # Выводит 15 (перегруженное справа)
    # Выводит 15 (перегруженное слева)
    print('*****Факториал******')
    print(f'факториал 5={factorial(5)}')

    print('*****Cтрока******')
    pars_str('hello')

