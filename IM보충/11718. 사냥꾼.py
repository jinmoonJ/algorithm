# 11718. 사냥꾼

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    MAP = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 1:


                for a in range(4):
                    for b in range(n):
