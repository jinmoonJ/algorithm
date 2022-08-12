T = int(input())
D, A, B = map(int, (input().split()))


def get_prime(n):
    arr = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if arr[i] == True:
            for j in range(i + i, n, i):
                arr[j] = False
    return [i for i in range(2, n) if arr[i] == True]


for tc in range(1, T + 1):
    if arr in D:
        count += 1
