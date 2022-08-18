# SWEA 4873 반복문자 지우기

T = int(input())

for tc in range(1, T + 1):
    words = input()

    stack = []

    for word in words:
        if stack and word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)

    print(f"#{tc} {len(stack)}")
