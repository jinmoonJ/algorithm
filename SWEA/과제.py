# SWEA 과제 1231 9일차 중위순회

def inorder(V):
    if V <= n:
        inorder(V * 2)  # 왼쪽 자식
        print(data[V], end='')  # 루트
        inorder(V * 2 + 1)  # 오른쪽 자식


T = 10
for tc in range(1, T + 1):
    n = int(input())
    data = [0] * (n + 1)
    for i in range(n):
        temp = list(input().split())
        data[i + 1] = temp[1]  # 각 정점의 문자열 입력받아 data에 할당

    print(f"#{tc}", end=' ')
    inorder(1)
    print()
