# SWEA 4866 괄호검사
T = int(input())
for tc in range(1, T + 1):
    N = input()

    stack = []
    stack2 = []
    answer = 1
    for c in N:
        if c == "(":
            stack.append(c)
        if c == "{":
            stack2.append(c)
        elif c == ")":
            if len(stack) == 0:
                answer = 0
                break
            stack.pop(-1)
        elif c == "}":
            if len(stack2) == 0:
                answer = 0
                break
            stack2.pop(-1)

    if len(stack) > 0 or len(stack2) > 0:
        answer = 0

    print(f"#{tc} {answer}")
