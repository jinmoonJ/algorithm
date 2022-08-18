# SWEA 4873 반복문자 지우기 T 메소드 사용 x

T = int(input())

for tc in range(1, T + 1):
    row = input()

    size = 1000  # 스택의 사이즈
    top = -1
    stack = [0] * size

    top += 1
    stack[top] = row[0]  # 제일 처음 글자는 앞글자가 없으니까 그냥 넣기

    for i in range(1, len(row)):  # 비교는 2번째 글자부터
        if top != -1 and stack[top] == row[i]:  # 같은 글자니까 stack pop
            top -= 1
        else:
            # 다른 글자면 push
            top += 1
            stack[top] = row[i]

    print(f"#{tc} {top + 1}")
