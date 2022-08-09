T = int(input())

for t in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input()))

    card = [0] * 10

    for i in ai:
        card[i] += 1

    max_idx = N-1
    for j in range(len(card)-1, -1, -1):
        if card[j] > card[max_idx]:
            max_idx = j

    print(f"#{t} {max_idx} {card[max_idx]}")