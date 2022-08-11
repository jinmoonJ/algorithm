# SWEA 4839 이진탐색
T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    cntA = 0
    cntB = 0
    left = 1
    right = P
    while left <= right:
        center = int((left + right) / 2)
        cntA += 1
        if center == Pa:
            break
        elif center > Pa:
            right = center
        else:
            left = center

    left = 1
    right = P
    while left <= right:
        center = int((left + right) / 2)
        cntB += 1
        if center == Pb:
            break
        elif center > Pb:
            right = center
        else:
            left = center

    if cntA == cntB:
        print(f"#{tc} 0")
    elif cntA > cntB:
        print(f"#{tc} B")
    else:
        print(f"#{tc} A")
print()
