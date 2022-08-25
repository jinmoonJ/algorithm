# SWEA 5099 피자 굽기
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    q = []

    for i in range(N):  # 화덕의 크기만큼 반복
        q.append([lst[i], i])  # 화덕에 들어간 치즈양, 피자 번호

    print(q)
    i = 0
    while len(q) != 1:
        q[0][0] //= 2

        if q[0][0] == 0:
            if N + i < M:
                q.pop(0)
                q.append([lst[N + i], N + i])
                i += 1
            if N + i >= M:
                q.pop(0)
        else:
            q.append(q.pop(0))

    print(q[0][1]+1)
