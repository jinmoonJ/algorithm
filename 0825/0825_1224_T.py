# SWEA 1224 계산기3 T
# 함수 두개로 분리
# 중위 표기식 => 후위 표기식
# 후위표기식을 계산해서 결과를 주는 함수

# 연산자의 우선순위
icp = {"+": 1, "*": 2, "(": 3, "-": 1, "/": 2}
isp = {"+": 1, "*": 2, "(": 0, "-": 1, "/": 2}


def get_postfix(infix, n):
    postfix = ""  # 결과로 나올 후위 표기식
    stack = []  # 스택
    for i in range(n):  # 중위 표기식 하나씩 떼서 확인
        # 하나 떼서 왔는데 숫자일때(피연산자)
        if "0" <= infix[i] <= "9":
            postfix += infix[i]  # 이어 붙인다.
        else:
            # 연산자일 때
            # 그 연산자가 닫는 괄호일 경우 ==> 여는 괄호가 나올때까지 연산자를 모두 pop
            if infix[i] == ")":
                while stack:
                    char = stack.pop()
                    if char == "(":
                        break
                    postfix += char
            # 괄호가 아닐 경우 => 자기 자신이 스택안에 있는 것보다 우선순위가 높아질 때까지 pop
            else:
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                # 이제 내 우선순위가 높거나 스택 안에 아무것도 남지 않았다 => 그냥 push
                stack.append(infix[i])
    while stack:
        # 남은 연산자는 수식 뒤에 다 붙인다.
        postfix += stack.pop()
    return postfix


def get_result(postfix):
    stack = []

    for c in postfix:
        if "0" <= c <= "9":
            stack.append(int(C))
        else:
            right = stack.pop()
            left = stack.pop()

            if c == "+":
                result = left + right
            elif c == "*":
                result = left * right
            elif c == "/":
                result = int(left / right)
            elif c == "-":
                result = left - right

            stack.append(result)

    return stack.pop()


T = 10
for tc in range(1, T + 1):
    n = int(input())
    exp = input()

    # 중위표기식 => 후위표기식
    postfix = get_postfix(exp, n)
    # 후위표기식의 결과 계싼
    answer = get_result(postfix)

    print(f"#{tc} {answer}")
