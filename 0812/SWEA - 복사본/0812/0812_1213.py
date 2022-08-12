T = 10
for tc in range(1, T+1):
    A = int(input())
    p = input()
    t = input()
    M = len(p)
    N = len(t)

    i = 0
    j = 0
    count = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i -= j
            j = -1 
        i += 1
        j += 1
        
    if j == M:
        count += 1

