# 11671. 기지국

T = int(input())
for tc in range(1, T + 1):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    N = int(input())
    MAP = [list(input()) for _ in range(N)]

    len_dict = {'A': 1, 'B': 2, 'C': 3}

    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 'X' or MAP[r][c] == 'H':
                continue
            K = len_dict[MAP[r][c]]

            for i in range(4):
                for j in range(1, K + 1):
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        break
                    if MAP[nr][nc] == 'H':
                        MAP[nr][nc] = 'X'

    ans = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 'H':
                ans += 1

    print(f"#{tc} {ans}")

