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


def pars_str(stroka: str) -> None:
    """
     hello
     hell
     hel
     he
     h
 """
    print(stroka)
    return pars_str(stroka[:-1]) if stroka else 0


def pars_str1(stroka: str) -> str:
    """
     hello
     hell
     hel
     he
     h
    ниже вызовы стека для закоментированной строки иначе елка перевернется
     pars_str1(hello) - '\nh\nhe\nhel\nhell\nhello'
     pars_str1(hell)  - '\nh\nhe\nhel\nhell'
     pars_str1(hel)   - '\nh\nhe\nhel'
     pars_str1(he)    - '\nh\nhe'
     pars_str1(h)     - '\nh'
     pars_str1()      - ''
    для незакоментированной строки елка развернулась
     pars_str1(hello) - 'hello\nhell\nhel\nhe\nh\n'
     pars_str1(hell)  - 'hell\nhel\nhe\nh\n'
     pars_str1(hel)   - 'hel\nhe\nh\n'
     pars_str1(he)    - 'he\nh\n'
     pars_str1(h)     - 'h\n'
     pars_str1()      - ''

 """
    if stroka:
        return f'{stroka}\n{pars_str1(stroka[:-1])}'
        # return f'{pars_str1(stroka[:-1])}\n{stroka}''
    return ''


def print_star(N: int) -> None:
    print("*"*N)
    if N:
        print_star(N-1)
    print("*"*N)
    return 0


def print_stars(N: int) -> str:
    """
    print_stars(5) - *\n*\n*\n*\n*\n
    print_stars(4) - *\n*\n*\n*\n
    print_stars(3) - *\n*\n*\n
    print_stars(2) - *\n*\n
    print_stars(1) - *\n
    print_stars(0) - ''
    """
    # if N:
    #     return f'*\n{print_stars(N-1)}'
    # return ''
    return '' if not N else f'*\n{print_stars(N-1)}'


def func(L: list, res=[]) -> list:
    """ No additional checks """
    if len(L) == 1: return res
    if L:
        x = min(L)
        res.append(L.pop(L.index(x)))
        func(L, res)
    return res




def febonachi(N: int) -> int:
    """
        0,1,1,2,3,5,8,13,21,...., где N количество чисел Фeбоначи которых нужно найти
        febonachi(5) - [0,1,1,2,3,5]
        febonachi(4) - [0,1,1,2,3]
        febonachi(3) - [0,1,1,2]
        febonachi(2) - [0,1,1]
        febonachi(1) - [0, 1]
    """
    if N == 0:
        return [0]
    if N == 1:
        return [0, 1]
    res = febonachi(N-1)  # при N=2 -> [0,1]
    res.append(res[-1]+res[-2])
    return res

def permutel(seq):
    # Тасование любой последовательности
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permutel(rest):
                res.append(seq[i:i+1] + x)
    return res


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
    print('***** Факториал ******')
    print(f'факториал 5={factorial(5)}')

    print('***** Cтрока ******')
    # кто последний попал в рекурсию, тот первый из нее выйдет
    pars_str('hello')

    print('***** Cтрока1 ******')
    print(pars_str1('hello'))

    print('***** Звезда *****')
    print_star(5)

    print('***** Звезды *****')
    print(print_stars(5))

    print('***** Фeбоначи *****')
    print(febonachi(25))

    print('***** fun sort by choice *****')
    print('sorted:', func([43, 6, 2, 5, 8, 32, 9]))

    print('***** Перемешивание последовательностей *****')
    print(permutel('ab'))