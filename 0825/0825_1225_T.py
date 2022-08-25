# SWEA 1225 암호 생성기 T
for _ in range(10):
    tc = int(input())

    q = list(map(int, input().split()))  # 들어온 리스트를 그대로 받아서 큐에 사용한다

    number = 1  # 큐에서 나온 수를 number 만큼 뺄것이고, 이 숫자는 1씩 증가하다가
    # 5가 되는 순간 다시 1로 돌아간다. => 한 사이클

    # 반복시작
    while True:
        item = q.pop(0)  # 큐의 맨 앞의 숫자 꺼내기
        item -= number  # 숫자에서 뺴주기
        # 뺸 수가 0 이하기 되버리면 큐의 맨 끝에 0을 붙이고 반복 종료
        if item <= 0:
            item = 0
            q.append(item)
            break

        # 0 이하가 아니면 계속 진행
        q.append(item)
        number += 1
        if number > 5:  # 한 사이클 처리
            number = 1

    print(f"#{tc}", end=" ")
    while q:
        print(q.pop(0), end=" ")
    print()
