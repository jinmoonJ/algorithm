# SWEA 5102 노드의 거리
def bfs(g, s, e, v):  # g 그래프, s 시작지점, e 목표지점, v 정점 개수
    visited = [False] * (v + 1)  # 방문 체크 배열
    q = []
    distance = 0  # 정점간의 거리
    q.append(s)
    visited[s] = True

    while q:

        # 몇번 반복을 할지 정해놓고 반복을 하면
        # 해당 단계에서 반복을 제한할 수 있다.
        size = len(q)
        distance += 1
        for _ in range(size):
            t = q.pop(0)
            for i in g[t]:  # 인접리스트를 통해서 t 번 정점과 연결되어있는 정점을 모두 탐색한다.
                if not visited[i]:  # i 번 정점을 방문한 적 없다.
                    # i 번 정점이 내가 목표로 한 정점이다!
                    # 거리를 리턴
                    if i == e:
                        return distance
                    q.append(i)  # i 번 방문 예약
                    visited[i] = True

    # 여기까지 와버렸다 => 함수가 중단된 적이 없다.
    return 0  # 중간에 도착지점을 만나지 못함 ( 길이 없다 ) ===> 0 출력


T = int(input())

for tc in range(1, T + 1):
    v, e = map(int, input().split())  # v는 정점 개수, e는 간선(모서리) 개수

    # 인접 리스트 또는 인접 행렬
    g = [[] for _ in range(v + 1)]  # 인접 리스트 그래프

    # 간선의 정보가 주어진다. 인접 리스트 그리기
    for i in range(e):
        left, right = map(int, input().split())  # 양쪽 노드, 양방향
        g[left].append(right)  # 왼쪽 => 오른쪽
        g[right].append(left)  # 오른쪽 => 왼쪽

    # 시작 지점, 끝 지점 입력
    sv, ev = map(int, input().split())  # sv 시작 지점 ev 목표지점

    # bfs
    print(f"#{tc} {bfs(g,sv,ev,v)}")
