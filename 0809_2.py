T = int(input())

for t in range(1, T + 1):

    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    bus = 0
    cha_count = 0
    cha_list = [0]*(N+1)

    for i in charge:
        cha_list[i] = 1

    while True:
        bus_start = bus
        bus += K
        if bus >= N:
            break
        while cha_list[bus] == 0:
            if bus == bus_start:
                print(f"{t} 0")
                break
            else:
                bus -= 1
        cha_count += 1
    print(f"#{t} {cha_count}")




