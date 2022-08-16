# SWEA 3143 가장 빠른 문자열 타이핑
T = int(input())

for tc in range(1, T + 1):
    str1, str2 = input().split()

    t = 0
    p = 0
    t_l = len(str1)
    p_l = len(str2)

    count = 0
    while t < t_l and p < p_l:
        if str2[p] != str1[t]:
            t = t - p
            p = -1
        t += 1
        p += 1
        if p == p_l:
            count += 1
            p = 0

    print(f"#{tc}", t_l - p_l * count + count)