def drive(K, N):    # 버스를 운행하는 함수
    # return == 0 충전소가 제대로 배치 되어있지 않음 완주 불가
    # return > 0 충전소가 제대로 배치
    last = 0    # 마지막으로 충전했던 위치
    next = K    # 버스가 최대로 이동한 위치(초기 값은 한번 이동한 상태로)
    count = 0  # 충전한 횟수

    # 종점에 도착할 때까지 계속 반복
    while next < N:
        # 버스가 이동한 위치에 충전기가 있나 없나 검사
        # 충전기가 없다면 뒤로 한칸씩 돌아가면서 찾을때까지 뒤로 간다.
        while stop[next] == 0:
            next -= 1   # 한칸씩 뒤로 이동
            if next == last:
                return 0    # 운행 불가
        # 만약 뒤로 갔는데 내가 마지막으로 충전한 위치까지 와버렸다면
        # 다시 앞으로 가봤자 다시 돌아올테니까 충전소가 제대로 설치되어있지 않다.

        # 여기까지 왔다면 충전기가 제대로 설치되어 있따.
        # 마지막 충전 위치를 갱신
        last = next
        # 다음 위치로 이동
        next += K
        # 충전 횟수 증가
        count += 1
        # N 보다 next가 크거나 같아졌으니까 완주 했다
    return count


T = int(input())

for tc in range(1, T + 1):

    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    bus = 0
    cha_count = 0
    stop = [0]*N+1    # 정류장 리스트 1 충전소 있음 0 없음
    for x in charge:
        stop[x] = 1
    answer = drive(K, N)
    print(f"#{tc} {answer}")
