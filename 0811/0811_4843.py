T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    lst = []

    for i in range(N - 1, 0, -1):
        for j in range(i):
            if ai[j] > ai[j + 1]:
                ai[j], ai[j + 1] = ai[j + 1], ai[j]

    for i in range(len(ai), 0, -2):
        lst.append(i)
    
