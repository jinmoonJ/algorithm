# SWEA 1945 간단한 소인수분해
T = int(input())
lst = [2, 3, 5, 7, 11]
for tc in range(1, T + 1):
    N = int(input())

    lst = [0] * 5
    while True:
        if N % 2 == 0:
            N = N // 2
            lst[0] += 1

        elif N % 3 == 0:
            N = N // 3
            lst[1] += 1

        elif N % 5 == 0:
            N = N // 5
            lst[2] += 1

        elif N % 7 == 0:
            N = N // 7
            lst[3] += 1

        elif N % 11 == 0:
            N = N // 11
            lst[4] += 1

        if N == 1:
            break

    print(f"#{tc}", end=" ")
    for i in lst:
        print(i, end=" ")
    print()