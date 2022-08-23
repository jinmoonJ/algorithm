# SWEA 4874 Forth T
T = int(input())
for tc in range(1, T + 1):
    exp = input().split()

    stack = []

    result = 0 # 출력할 결과

    for c in exp:
        if "0" <= c <= "9":
            stack.append(int(c))
        else:
            if c == ".":
                result = stack.pop()
                break

            # 연산자 .. 아직 연산중이다.
            # 연산자가 있는데 피연산자의 개수가 부족하다?
            # 연산자 양쪽에 피연산자가 있어야 하는데 하나밖에 없다거나..
            if len(stack) < 2:
                result = "error"
                break

            # 피연산자의 개수도 충분하다.
            right = stack.pop() # 우항이 먼저
            left = stack.pop()

            if c == "+":
                result = left + right
            elif c == "*":
                result = left * right
            elif c == "/":
                result = left // right
            elif c == "-":
                result = left - right

            # 계산한 결과를 스택에 넣어준다.
            stack.append(result)
    # 다 계산을 했는데 (연산자를 다 썼는데, 피연산자(숫자)가 남았다? => 잘못된식
    if stack:
        result = "error"

    print(f"#{tc} {result}")