# SWEA 4837 부분집합의 합
T = int(input())

arr = [i for i in range(1, 13)]  # 0~12
N = 12

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    # n = 부분집합의 원소의 개수
    # k = 부분집합의 합

    answer = 0  # 위의 두 조건을 만족하는 부분집합의 개수
    # 운소의 개수가 n이고 합이 k인 부분집합의 개수

    for i in range(1 << N):
        subset_sum = 0  # 현재 부분집합의 합
        subset_count = 0  # 현재 부분집합의 원소 개수
        for j in range(N):
            if i & (i << j):  # j번째 인덱스의 원소를 부분집합에 포함하고 있다.
                subset_sum += arr[j]
                subset_count += 1
        if subset_count == n and subset_sum == k:
            answer += 1
    print(f"#{tc} {answer}")
