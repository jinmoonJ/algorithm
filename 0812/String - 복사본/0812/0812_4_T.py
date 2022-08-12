# 문자열에 부등호 사용시 문자의 ASCII 값을 비교
def my_strcmp(s1,s2):
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

print(my_strcmp("123", "123"))
print(my_strcmp("123", "122"))
print(my_strcmp("123", "124"))
print(my_strcmp("a", "A")) # 97, 95