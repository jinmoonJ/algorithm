# SWEA 5188 2일차 최소합

T = int(input())
for tc in range(1, T + 1):
    # 배열의 크기
    N = int(input())

    # 각 칸에 값을 저장
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 중간까지의 합을 다시 계산하지 않도록
    # 기억해 놓는 방법을 사용한다.
    dp = [[0] * N for _ in range(N)]

    # 이동 방향이 왼쪽 -> 오른쪽, 위 -> 아래
    for i in range(N):
        for j in range(N):
            # 현재 i,j 위치에서 위에서도 올 수 있고, 왼쪽에서도 올 수 있다.
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = min((dp[i - 1][j], dp[i][j - 1]) + arr[i][j])
            # 위에서만 올 수 있고, 왼쪽에서는 올 수 없다.
            elif i - 1 >= 0 and j - 1 < 0:
                dp[i][j] = dp[i - 1][j] + arr[i][j]
            # 왼쪽에서만 올 수 있고, 위에서는 올 수 없다.
            elif i - 1 < 0 and j - 1 >= 0:
                dp[i][j] = dp[i][j - 1] + arr[i][j]
            # 왼쪽도 없고, 위쪽도 없다.(시작지점)
            elif i - 1 < 0 and j - 1 < 0:
                dp[i][j] = arr[i][j]

    # 반복이 다 끝나면 맨 오른쪽 아래 칸에 최소값이 들어있을 것
    print(f"#{tc} {dp[N - 1][N - 1]}")
