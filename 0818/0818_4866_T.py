# SWEA 4866 괄호검사 T

T = int(input())

for tc in range(1, T + 1):
    row = input()

    stack = []

    answer = 1  # 1이면 괄호가 제대로, 0 이면 괄호 제대로 x

    for c in row:
        # 열린괄호가 나오면 무지성으로 스택에 push
        if c == "(" or c == "{":
            stack.append(c)
        if c == ")" or c == "}":
            # 닫힌 괄호가 나오면 해야할 일
            # 먼저 스택의 크기를 검사해서 안에 열린 괄호가 남아있는지 확인
            if len(stack) == 0:
                answer = 0
                break

            # 열린괄호가 있다면
            # 열린괄호 모양이 지금 나온 닫힌 괄호의 모양과 일치하는지 검사
            bracket = stack.pop()
            if not ((bracket == "(" and c == ")") or (bracket == "{" and c == "}")):
                answer = 0
                break

        # 반복이 다 끝나고 나서 남은 열린 괄호가 있는지 검사
        if len(stack) > 0:
            answer = 0

        print(f"#{tc} {answer}")
