T = int(input())

for t in range(1, T + 1):
    N = int(input())    # 숫자 카드의 개수
    numbers = input()

    counts = [0] * 10

    for number in numbers:
        counts[int(number)] += 1    # 숫자 카드 갯수 세기

    max_count = 0   # 최대 개수
    number_max = 0  # 가장 큰수

    for i in range(10):
        if counts[i] > max_count:
            # i 카드가 등장한 횟수가 지금 내가 알고있는 최대 횟수보다 많으면 바꾸자
            max_count = counts[i]
            number_max = i

    print(f"#{t} {number_max} {max_count}")
