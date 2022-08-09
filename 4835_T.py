T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 구간합의 최소, 최대값
    max_sum = 0
    min_sum = 10000 * M

    for i in range(0, N-M+1):
        sub_sum = 0     # 구간합
        # M 만큼 가면서 구간합을 구해준다.
        # i = 현재위치
        # j = 0, 1, 2, 3 ....
        # i + j = 구간합에 더할 원소 위치
        for j in range(0, M):
            sub_sum += numbers[i+j]
        max_sum = sub_sum if sub_sum > max_sum else max_sum
        min_sum = sub_sum if sub_sum < min_sum else min_sum

    print(f"#{tc} {max_sum - min_sum}")
