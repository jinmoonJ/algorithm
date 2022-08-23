# SWEA 4874 Forth
T = int(input())
for tc in range(1, T + 1):
    postfix = input().split()
    S = []
    for i in postfix:
        if i == ".":
            if len(S) == 1:
                print(f"#{tc} {S[0]}")
                break
            else:
                print(f"#{tc} error")
                break

        elif i in "+*-/":
            if len(S) >= 2:
                b = S.pop()
                a = S.pop()
                if i == '+':
                    S.append(a + b)
                elif i == "*":
                    S.append(a * b)
                elif i == "-":
                    S.append(a - b)
                elif i == "/":
                    S.append(a // b)
            else:
                print(f"#{tc} error")
                break
        else:
            S.append(int(i))
