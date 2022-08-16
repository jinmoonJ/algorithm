# SWEA 4864 문자열 비교

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    p = 0
    t = 0
    p_l = len(str1)
    t_l = len(str2)

    while t < t_l and p < p_l:
        if str2[t] != str1[p]:
            t = t - p
            p = -1
        t += 1
        p += 1
    if p == p_l:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")

