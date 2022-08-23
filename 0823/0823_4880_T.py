# SWEA 4880 토너먼트 카드 게임
# 카드 게임 분할정복 함수
# i, j : i 번쨰 학생부터 j 번쨰 학생까지
def tournament(i, j):
    if i == j:
        # i 랑 j가 같으면 둘로 쪼개는게 불가능하다.
        return i
    else:
        # 왼쪽과 오른쪽을 나누는 일을 계속 반복적으로 하니까
        # 재귀함수로 만든다.
        left = tournament(i, (i + j) // 2)  # 왼쪽 쪼개기
        right = tournament((i + j) // 2 + 1, j)  # 오른쪽
        return winner(left, right)  # left와 right 중 승자를 구해서 리턴


# 왼쪽과 오른쪽 중에 승자를 정한다
# 승자의 인덱스를 리턴하도록
def winner(left, right):
    if arr[left] == arr[right]:
        return left
    elif arr[left] == 1:
        if arr[right] == 2:
            return right
        else:
            return left
    elif arr[left] == 2:
        if arr[right] == 1:
            return left
        else:
            return right
    elif arr[left] == 3:
        if arr[right] == 2:
            return left
        else:
            return right


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f"#{tc} {tournament(0, n-1)+1}")
