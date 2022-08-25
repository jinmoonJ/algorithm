# SWEA 5099 피자 굽기
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    pizza_list = list(map(int, input().split()))

    oven = [[] for _ in range(n)]
    next_i = 0  # 다음에 넣을 피자 번호

    for i in range(n):  # 오븐에 피자 넣기
        oven[i] = [i, pizza_list.pop(0)]  # 피자 번호랑 같이 넣어보기
        next_i += 1

    remain = n  # 오븐에 남아있는 피자 갯수
    last_index = -1  # 마지막에 꺼낸 피자의 번호

    # 치즈 다 녹을때까지 반복
    while True:
        # 피자 번호, 피자 꺼내기 (맨앞에서)
        # pizza = oven.pop(0) # pizza[0] pizza[1]
        i, pizza = oven.pop(0)  # i는 피자번호, pizza는 치즈

        # 치즈 녹이기
        pizza //= 2

        # 치즈가 0이 되면 피자가 다 구워졌다.

        # 피자 치즈가 다 녹지 않았으면? 다시 넣기
        if pizza != 0:
            oven.append([i, pizza])
        # 피자 치즈가 다 구워졌으면 현재 피자를 꺼낸다.
        else:
            # 1. 아직 넣을 피자가 남았다. = > 다음 피자 넣기(번호도 같이)
            if pizza_list:
                oven.append(next_i, pizza_list.pop(0))
                next_i += 1  # 다음에 꺼내올 피자 번호 증가

            # 2. 넣을 피자도 없다. => 오븐에 남아있는 피자 갯수 감소시킨다.
            else:
                remain -= 1
                # 그런ㄷ 오븐에 남은 피자도 없으면 인덱스 저장하고 반복 중단
                if remain == 0:
                    # 현재 피자의 번호 i 가 마지막에 나온 피자의 번호가 된다.
                    last_index = i
                    break
    print(f"#{tc} {last_index + 1}")
