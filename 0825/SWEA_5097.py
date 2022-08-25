# SWEA 5097 회전
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    for i in range(M):
        last_n = q.popleft(0)
