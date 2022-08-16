# SWEA 1859 백만장자 프로젝트

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    count = 0
    money = 0
    for i in range(N - 2, 1, -1):
