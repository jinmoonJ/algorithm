# SWEA 1265 달란트2 - 2
T = int(input())
for tc in range(1, T + 1):
    n, p = map(int, input().split())

    num = 1

    cnt = n-n // p*p

    for i in range(p-cnt):
        num *= (n//p)

    for i in range(cnt):
        num *= (n//p+1)

    print(f"#{tc} {num}")