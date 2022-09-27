# SWEA 5178 노드의 합
def postorder(v):
    global tree
    if tree[v] == 0:
        if n >= v * 2 + 1:
            tree[v] = postorder(v * 2) + postorder(v * 2 + 1)
        else:
            tree[v] = postorder(v * 2)
    return tree[v]


T = int(input())

for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)

    for i in range(m):
        a, b = map(int, input().split())
        tree[a] = b

    postorder(1)
    print(f"#{tc} {tree[l]}")
