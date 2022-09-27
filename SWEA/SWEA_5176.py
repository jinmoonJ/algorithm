# SWEA 5176 이진탐색
def inorder(v):
    global number
    if v <= n:
        inorder(v * 2)
        tree[v] = number
        number += 1
        inorder(v * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    tree = [0] * (n + 1)
    number = 1

    inorder(1)
    print(f"#{tc} {tree[1]} {tree[n // 2]}")
