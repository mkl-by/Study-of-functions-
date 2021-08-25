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

if __name__ == '__main__':
    L = [1, 2, 3]
    L1 = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(mysum(L))
    print(ssum(L))

    print(list_sum(L1))
    print(list_sum ([1, [2, [3, [4, [5]]]]]))
    print(list_sum([[[[ [1], 2], 3], 4], 5]))
# Выводит 15 (перегруженное справа)
# Выводит 15 (п
