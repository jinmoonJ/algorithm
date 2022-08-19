# SWEA 5789 현주의 상자 바꾸기

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())  # 상자 개수 N 숫자바꾸는 횟수 Q
    lst = [0] * (N + 1)   # 상자 개수+1만큼 0인 리스트를 만든다

    for i in range(1, Q + 1):  # Q횟수 반복
        Li, Ri = map(int, input().split())  # 숫자넣을 상자 받고
        for j in range(Li, Ri + 1):  # 반복
            lst[j] = i  # lst[j]에  i값을 넣어준다

    print(f"#{tc}", end=" ")
    for answer in lst[1:]:
        print(answer, end=" ")
    print()