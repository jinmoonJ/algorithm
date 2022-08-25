# SWEA 5105 미로의 거리 T
T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    maze = [list(map(int, input())) for _ in range(n)]

    si = sj = 0  # 시작위치

    # 시작 위치 (값이 2인위치) 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                si = i
                sj = i

    q = []
    # 큐 초기화
    # 시작위치 큐에 넣고 방문체크
    q.append((si, sj))
    maze[si][sj] = 1  # 내가 갔던 위치는 벽으로 만들어서 다음에 방문 못하게 한다.
    distanse = -1

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    find = False  # 중간에 도착지점을 찾았다면 True로 바꿔줄 것
    while q and not find:
        size = len(q)  # 큐의 길이를 통해서 해당 단계에서의 반복을 제한
        distanse += 1
        for _ in range(size):
            i, j = q.pop(0)
            # 4방향 탐색
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                # 다음 위치가 유효한 위치인지 검사 (방문해도 되는 위치인지 확인)
                if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1:
                    # 다음위치가 방문가능한데, 도착지점일 경우
                    if maze[ni][nj] == 3:
                        q = []
                        find = True  # 찾았다.
                        break
                    maze[ni][nj] = 1
                    q.append((ni, nj))
            if find:
                break

    # 도착지점을 만나지 못한 경우
    if not find:
        distanse = 0

    print(f"#{tc} {distance}")
