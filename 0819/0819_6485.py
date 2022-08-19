# SWEA 6485 삼성시의 버스 노선
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus = [0] * 5001

    for i in range(N):
        ai, bi = map(int, input().split())
        for j in range(ai, bi + 1):
            bus[j] += 1

    P = int(input())
    lst = []
    for i in range(P):
        stop = int(input())
        lst.append(bus[stop])

    print(f"#{tc}", end=" ")
    for b in lst:
        print(b, end=" ")
    print()
