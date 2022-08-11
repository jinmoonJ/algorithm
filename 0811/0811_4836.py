# SWEA 4836 색칠하기
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    box = [[0] * 10 for _ in range(10)]
    count = 0
    for _ in range(N):
        row1, col1, row2, col2, colo = map(int, (input().split()))
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                if colo == 1:
                    if box[i][j] == 0:
                        box[i][j] = 1
                    else:
                        box[i][j] == 3
                        count += 1
                if colo == 2:
                    if box[i][j] == 0:
                        box[i][j] = 2
                    else:
                        box[i][j] == 3
                        count += 1

    print(f"#{tc} {count}")
