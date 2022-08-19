# SWEA 4408 자기 방으로 돌아가기 T

T = int(input())


def get_way_idx(v):
    # if v % 2 == 0
    return (v + 1) // 2


for tc in range(1, T + 1):
    n = int(input())
    students = [0] * n

    for i in range(n):
        v1, v2 = list(map, input().split())  # v1 : 시작지점 v2 : 도착지점
        # 시작은 무조건 도착 위치보다 작게해서 혼돈 피하자
        if v1 > v2:
            v1, v2 = v2, v1
        students[i] = [v1, v2]
        # students[i][0] : 학생이 지금 있는 방의 번호
        # students[i][1] : 학생이 가야 하는 방의 번호

        remain = n  # 자기 방으로 되돌려 보내야 하는 남은 학생 수
        time = 0  # 다 보내는데 걸린 시간

        while remain > 0:  # 학생을 다 보낼때 까지 반복
            way = []  # 복도를 사용중인지 체크
            for i in range(n):
                if students[i] != -1:  # 이미 보낸 학생은 검사하지 않도록 한다.
                    v1 = get_way_idx(students[i][0])  # 시작위치
                    v2 = get_way_idx(students[i][1])  # 도착위치

                    move = True  # 이동하는데 복도를 사용할 수 있으면 True, 이미 누가 사용중이면 False
                    for u in way:  # way 안에는 사용중인 복도의 정보가 들어있다.
                        if u[0] <= v1 <= u[1] or u[0] <= v2 <= u[1]:
                            move = False  # 학생이 움직여야하는 복도의 범위를 다른 누군가가 쓰고 있다면
                            # 움직이지 못하게 한다.

                    if move:
                        way.append([v1, v2])  # 복도에 움직인 학생이 사용한 위치 저장
                        students[i] = -1  # 이동한 학생은 다음에 안보게 체크
                        remain -= 1
            time += 1

        print(f"#{tc} {time}")
