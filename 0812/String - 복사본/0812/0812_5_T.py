def itoa(a):
    i = 10
    s = "" # 숫자를 문자열로 바꾼 결과

    while a > 0:
        mod = a % i #
        s += chr(ord("0") + mod)
        a //= 10
    return s[::-1]

a = 1234
b = itoa(a)
print(b)
print(type(a))
print(type(b))