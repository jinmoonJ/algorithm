# SWEA 4843 특별한 정렬
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    index = 0  # 바꿀 원소의 인덱스 (최대값 or 최소값)
    i = 0  # 탐색을 시작할 위치

    for ni in range(10):
        # 정렬시작
        for j in range(i, n):  # 최대값 또는 최소값을 찾기 시작
            if ni % 2 == 0 and numbers[j] > numbers[index]:
                # 최대값의 인덱스
                index = j
            if ni % 2 == 1 and numbers[j] < numbers[index]:
                # 최소값의 인덱스
                index = j

        i += 1  # 다음에 와야할 원소의 위치를 증가
        # 현재 위치와 최대값 최소값의 위치에 있는 원소를 자리 바꿔주기
        numbers[ni], numbers[index] = numbers[index], numbers[ni]

    print(f"#{tc}", end=" ")
    for i in range(10):
        print(f"{numbers[i]}", end=" ")
    print()
