# SWEA 4865 글자수 T
T = int(input())

for tc in range(1, T + 1):
    s1 = input()
    s2 = input()
    
    s1_cnt = [0] * 26
    
    # s1 알파벳이 몇개 들었는지 배열에 저장
    for c in s1:
        s1_cnt[ord(c) - 65] = 1 # s1 안에 있는 알파벳은 1로 표시

    s2_cnt = [0] * 26

    for c in s2:
        if s1_cnt[ord(c) - 65] == 1:
            s2_cnt[ord(c) - 65] += 1
    # s1 에 있는 알파벳이 s2에 몇개 포함되어 있는지,
    # 그 중에 최대값을 구하는 문제

    max_cnt = 0
    for i in range(26):
        if s2_cnt[i] > max_cnt:
            max_cnt = s2_cnt[i]

    print(f"#{tc} {max_cnt}")
