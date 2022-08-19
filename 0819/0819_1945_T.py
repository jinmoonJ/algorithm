# SWEA 1945 간단한 소인수분해
T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    numbers = [2, 3, 5, 7, 11]
    cnt = [0] * 5  # 2 3 5 7 11 으로 나눈 횟수

    for i in range(5):
        temp_n = n  # n 을 계속 나누면서 진행
        while temp_n % numbers[i] == 0:  # 나눴을떄 나머지가 0이면
            temp_n //= numbers[i]  # 나누고
            cnt[i] += 1  # 개수 증가

    print(f"#{tc}", end=" ")
    for i in range(5):
        print(f"{cnt[i]}", end=" ")
    print()
