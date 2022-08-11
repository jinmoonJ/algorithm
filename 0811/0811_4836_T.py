# SWEA 4836 색칠하기
T = int(input())

for tc in range(1, T + 1):
    n = int(input())  # 색칠 횟수

    paper = [[0] * 10 for _ in range(10)]  # 종이

    purple_count = 0  # 겹친 칸 개수(빨+파)

    for i in range(n):
        command = list(map(int, input().split()))
        from_i, from_j = command[0], command[1]  # 색칠 시작 위치
        to_i, to_j = command[2], command[3]  # 색칠 끝 위치
        color = command[4]  # 색

        for r in range(from_i, to_i + 1):  # 색칠 시작 행 ~ 색칠 끝날 행
            for c in range(from_j, to_j + 1):  # 색칠 시작 열 ~ 색칠 끝날 열
                # 만약 내가 칠하려는 칸에 색이 없으면 색칠
                if paper[r][c] == 0:
                    paper[r][c] == color
                # 칸에 색이 있으면 색이 겹친다. ==> 보라색
                else:
                    purple_count += 1
    print(f"#{tc} {purple_count}")
