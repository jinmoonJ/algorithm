# SWEA 4861 회문

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 글자판 , M = 회문
    arr = [input() for _ in range(N)]  # N N 판 생성

    for i in range(N):
        for j in range(N - M + 1):
            if arr[i][j:j + M] == arr[i][j:j + M][::-1]:
                print(f"#{tc} {arr[i][j:j + M]}")

            for k in range()