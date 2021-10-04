def insert_sort(A: list) -> None:
    """сортировка списка А вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def choise_sort(A: list) -> None:
    """сортировка списка А выбором"""
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A: list) -> None:
    """сортировка списка А пузырька"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k + 1] = A[k+1], A[k]


def count_sort(A: list) -> None:
    """сортировка подсчетом, только для определенного небольшого диапазона
        чисел (1,2,3,4,5,6,7,8,9,0), но очень большого колличества
        [1,2,0,0,3,4,5,6,7,4,3,4,1,6,7,8,5,6,3,2,4,5,7,6,8,9,0,2,8,6,4]
        0 - колличество повторений допустим 3
        1 - колличество повторений допустим 2
        2 - колличество повторений допустим 3
        и т.д.
        """
    A_sorted = []
    print(A)
    rang = [0]*10  # допустим, что диапазон чисел от 0 до 9
    for i in A:
        rang[i] += 1  # каждой цифре из последовательности (месту в списке) присваиваем колличество повторений в массиве
    for i in range(len(rang)):
        A_sorted += [i]*rang[i]
    print(A_sorted)

def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 5, 1, 3, 4]
    A_sorted = [1, 2, 3, 4, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
    count_sort([1, 2, 0, 0, 3, 4, 5, 6, 7, 4, 3, 4, 1, 6, 7, 8, 5, 6, 3, 2, 4, 5, 7, 6, 8, 9, 0, 2, 8, 6, 4])