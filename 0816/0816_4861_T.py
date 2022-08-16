# SWEA 4861 회문 T

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 글자판 , M = 회문
    arr = [list(input()) for _ in range(N)]  # N N 판 생성

    answer = ""
    for i in range(N):
        for j in range(N - M + 1):  # 인덱스 범위 조심
            # (i, j)에 있는 글자부터 단어 만들기 시작
            # 원하는 단어의 길이 => M
            word_row = ""
            for k in range(M):
                word_row += arr[i][j + k]
                # 만든 단어, 거꾸로 뒤집은 단어 비교
                # 일치하는 답을 찾았으면 answer 바꾸기
                if arr[i][j + k] != arr[i][j + M - k - 1]:
                    break
                    # 일치하는 답을 찾았다. k 가  M -1이 되었을때
                    if k == M - 1:
                        answer = word_row

            # 세로 검사
            word_col = ""
            for k in range(m):
                word_col += arr[j + k][i]
                if arr[j + k][i] != arr[j + M - k - 1][i]:
                    break
            if k == M - 1:
                answer = word_col

    print(f"{tc} {answer}")
