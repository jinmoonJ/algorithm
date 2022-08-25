# SWEA 5105 미로의 거리
from collections import deque


def bfs(x, y):
    q = deque([(x, y)])
    arr[x][y] = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == -1:
                if maze[nr][nc] == 0:
                    arr[nr][nc] = arr[r][c] + 1
                    q.append((nr, nc))
                elif maze[nr][nc] == 3:
                    arr[nr][nc] = arr[r][c]
                    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]

    arr = [[-1 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                bfs(i, j)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                if arr[i][j] == -1:
                    print(f"#{tc} 0")
                else:
                    print(f"#{tc} {arr[i][j]}")
