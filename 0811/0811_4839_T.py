# SWEA 4839
T = int(input())

for tc in range(1, T + 1):
    p, a, b = map(int, input().split())
    # p : 페이지 수
    # a : a 가 찾아야 할 페이지
    # b : b 가 찾아야 할 페이지

    winner = ""  # 승리자
    a_start, a_end = 1, p  # a의 이진탐색 범위
    b_start, b_end = 1, p  # b의 이진탐색 범위

    while True:
        a_find = False  # a 가 페이지를 찾았는지
        b_find = False  # b 가 페이지를 찾았는지

        # a 부터 페이지를 찾기 시작
        mid = (a_start + a_end) // 2

        if mid == a:
            a_find = True
        elif mid > a:
            a_end = mid
        else:
            a_start = mid

        # b의 페이지를 찾기 시작
        mid = (b_start + b_end) // 2

        if mid == b:
            b_find = True
        elif mid > b:
            b_end = mid
        else:
            b_start = mid

        if a_find and b_find:
            answer = 0
            break
        if a_find:
            answer = "A"
            break
        if b_find:
            answer = "B"
            break

    print(f"#{tc} {winner}")
