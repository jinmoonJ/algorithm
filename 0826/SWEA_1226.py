# SWEA 1226 미로1 과제
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = 10
for tc in range(1, T + 1):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    answer = 0
    x, y = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:  # 출발점 찾아서 넣어주기
                x, y = i, j

    # dfs
    stack = [(x, y)]
    while stack:
        r, c = stack.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] != 1:
                # 길을 만날 경우
                if maze[nr][nc] == 0:
                    stack.append((nr, nc))
                    maze[nr][nc] = -1  # 다시 탐색 못하게 숫자 바꿔버리기
                # 끝점을 만날 경우
                elif maze[nr][nc] == 3:  # 탐색 가능하면 answer에 1
                    answer = 1
                    break

    print(f"#{tc} {answer}")
