# SWEA 4875 미로 T
def dfs(i, j, N):
    # visited = [[0] * N for _ in range(N)]
    stack = []

    di = [-1, 1, 0, 0]  # 상하좌우 탐색용 델타 배열
    dj = [0, 0, -1, 1]

    while True:
        # 현재 위치를 방문했다고 체크
        # visited[i][j] = 1
        # 현재 위치가 도착점인지 판단
        if arr[i][j] == 3:
            return 1
        # 방문 배열을 만들지 않고 내가 지났던 곳은 시멘트를 쳐서 벽으로 만들어 버리기

        arr[i][j] = 1

        # 현재 위치 i,j 에서 갈 수 있는 곳 탐색
        # 2차원 배열에서는 상하좌우로 움직일 수 있다.
        for d in range(4):
            ni = di[d] + i
            nj = dj[d] + j
            # 다음 위치정한 다음에 움직일 수 있는지 알아보기
            # 벽이면 못가, 2차원 배열 범위 벗어나도 못가, 방문한적 있는 좌표여도 못가
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                # 갈 수 있는 위치
                # 현재 위치를 스택에 저장
                stack.append((i, j))
                # 현재 위치를 다음위치로 최신화
                i, j = ni, nj
                break  # 현재 갈 수 있는 방향으로 더 가지 않고 다음 방향으로 가게 된다.
        else:
            # 갈수 있는 칸이 없으면?
            # pop() 을 해서 뒤로 다시 돌아간다.
            if stack:
                i, j = stack.pop()
            # 스택이 비어있으면 반복을 종료
            else:
                break
    # 반복문에서 중간에 return 문을 만나서 종료하지 못하고 여기까지  와버린 경우
    # 길이 없다 라는 뜻
    return 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    arr = [list(map(int, input())) for _ in range(n)]  # 미로 입력받기

    si = sj = 0  # 시작행, 시작열 = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si = i
                sj = j  # 시작위치 정해주기
    print(f"#{tc} {dfs(si, sj, n)}")
