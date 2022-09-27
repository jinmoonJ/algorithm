# SWEA 5203 베이비 진 게임 과제

T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, (input().split())))
    one = [0] * 10
    two = [0] * 10
    ans = 0
    for i in range(len(lst)):
        if i % 2 == 0:      # 짝수
            one[lst[i]] += 1
            if 3 in one:
                ans = 1
                break
            for j in range(8):
                if one[j] != 0 and one[j + 1] != 0 and one[j + 2] != 0:
                    ans = 1
                    break
            if ans == 1:
                break

        else:       # 홀수
            two[lst[i]] += 1
            if 3 in two:
                ans = 2
                break
            for j in range(8):
                if two[j] != 0 and two[j + 1] != 0 and two[j + 2] != 0:
                    ans = 2
                    break
            if ans == 2:
                break

    print(f"#{tc} {ans}")
