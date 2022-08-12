n = 10 ** 6

arr = [True] * (n + 1)
arr[1] = False

m = int(n ** 0.5)
for i in range(2, m + 1):
    if arr[i] == True:
        for j in range(i + i, n + 1, i):
            arr[j] = False

T = int(input())

for tc in range(1, T + 1):
    d, a, b = map(int, input().split())

    count = 0  # 특별한 소수 개수
    # 범위는 a부터 b까지
    for i in range(a, b + 1):  # 인덱스의 범위를 a ~ b+1까지
        if arr[i] == True:
            if str(d) in str(i):
                count += 1

    print(f"#{tc} {count}")
