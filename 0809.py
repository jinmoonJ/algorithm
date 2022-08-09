T = int(input())

for t in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    high = 0
    low = 1000001
    for i in ai:
        if i > high:
            high = i
        if i < low:
            low = i
    print(f"#{t} {high-low}")

