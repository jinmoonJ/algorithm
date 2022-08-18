# SWEA 4869 종이 붙이기 T
T = int(input())


# n
# f(n) = f(n-1) + f(n-2) * 2
def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3

    return paper(n - 1) + paper(n - 2) * 2


for tc in range(1, T + 1):
    n = int(input()) // 10  # n = 1, 2, 3...

    print(f"#{tc} {paper}")
