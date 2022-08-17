# 재귀함수
def f(n):
    if n > 10:  # 재귀함수는 종료 조건이 있어야함
        print("끝")
        return

    print(f"in : {n}")
    f(n + 1)
    print(f"out : {n}")


f(1)
