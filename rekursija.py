# косвенная рекурсия

def mysum(L):
    if not L: return 0
    return nonempty(L)

def nonempty(L):
    return L[0]+mysum(L[1:])

# прямая рекурсия

def ssum(L):
    return 0 if not L else L[0]+ssum(L[1:])

if __name__ == '__main__':
    L = [1, 2, 3]
    print(mysum(L))
    print(ssum(L))
