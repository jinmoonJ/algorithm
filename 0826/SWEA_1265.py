# SWEA 1265 달란트2
T = int(input())
for tc in range(1, T + 1):
    n, p = map(int, input().split())

    num = []
    a = n // p
    for i in range(p):
        num.append(a)

    b = n % p
    for i in range(b):
        if b != 0:
            num[i] += 1
    ans = 1
    for i in num:
        ans *= i

    print(f"#{tc} {ans}")
