# SWEA 4615 재미있는 오셀로 게임

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    duk = [[0] * (n + 1) for _ in range(n + 1)]
    # 초기 설정
    duk[n // 2][n // 2] = 2
    duk[n // 2 - 1][n // 2 - 1] = 2
    duk[n // 2][n // 2 - 1] = 1
    duk[n // 2 - 1][n // 2] = 1
    # 델타 설정 상 우 하 좌 대각선
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

    for _ in range(m):
        x, y, c = map(int, input().split())
        x = x - 1
        y = y - 1

        if not duk[x][y]:
            duk[x][y] = c
            for i in range(8):
                dx, dy = delta[i]
                nx = x + dx
                ny = y + dy
                game = []
                while True:
                    if nx < 0 or n - 1 < nx or ny < 0 or n - 1 < ny:
                        game = []
                        break
                    # 공백이 아닌지 확인
                    if duk[nx][ny] == 0:
                        game = []
                        break
                    # 같은 색 만나면 멈춤
                    if duk[nx][ny] == c:
                        break
                    # 다른 색이면 좌표를 저장한다.
                    else:
                        game.append((nx, ny))
                    nx += dx
                    ny += dy
                # 색 뒤집기
                for rx, ry in game:
                    duk[rx][ry] = c
    white, black = 0, 0
    for i in range(n):
        for j in range(n):
            if duk[i][j] == 1:
                white += 1
            elif duk[i][j] == 2:
                black += 1

    print(f"#{tc} {white} {black}")
