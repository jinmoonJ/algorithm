# SWEA 6485 삼성시의 버스 노선
T = int(input())
for tc in range(1, T + 1):
    n = int(input())  # 버스 수

    bus_list = [list(map(int, input().split())) for _ in range(n)]  # 노선 정보
    # bus_list [0] = [1,5]

    p = int(input())  # 정류장 수
    stop = [int(input()) for _ in range(p)]  # 정류장 번호 정보
    cnt_stop = [0] * p  # 정류장 수만큼 크기를 가진 카운트 배열 생성

    for i in range(n):
        bus = bus_list[i]  # i 번째 버스의 노선 정보
        # bus[0] : 출발 지점 / bus[1] : 종점
        for j in range(p):
            if bus[0] <= stop[j] <= bus[1]:  # 해당 정류장 번호가 버스가 다니는 정류장 안에 포함
                cnt_stop[j] += 1  # 범위에 포함되어 있다면 개수 증가

    print(f"#{tc}", end=" ")
    for i in range(p):
        print(f"{cnt_stop[i]}", end=" ")
    print()
