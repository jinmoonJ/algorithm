# SWEA 1226 미로1 T
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(si, sj):
    # bfs 탐색을 위한 큐
    q = [(si, sj)]
    maze[si][sj] = 1

    # 반복문을 통해 bfs탐색
    while q:
        i, j = q.pop(0)  # 탐색 위치 꺼내기

        # 다음 갈 곳 정하기 (4방)
        for d in range(4):
            ni = i + di[d]
            nj = i + dj[d]
            # 다음 갈 곳이 갈수 있는 위치인지 검사
            # 인덱스 범위, 방문 여부, 벽인지
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1:
                # 다음 위치에 왔는데 도착점이면
                # return
                if maze[ni][nj] == 3:
                    return 1
                maze[ni][nj] = 1
                q.append((ni, nj))

        return 0


for T in range(10):
    tc = int(input())

    n = 16

    maze = [list(map(int, input())) for _ in range(n)]

    si = sj = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 3:
                i, j = si, sj
