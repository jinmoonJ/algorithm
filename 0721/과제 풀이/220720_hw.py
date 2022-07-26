# 1. Built-in 함수
enumerate(), str(), join(), split(), zip(), abs(), all(), bool()

# 2. 홀수만 담기
a = list(range(1,51,2))
print(a)

# 3. 반복문으로 네모 출력
n = 5
m = 9

for i in range(m):
    for j in range(n):
        print("*", end = "")
    print()

# 4. 조건 표현식
temp = 36.5
a = "입실 불가"  if temp >= 37.5 else "입실 가능"

# 5. 정중앙 문자
def get_middle_char(str):
    return str[(len(str)-1)//2:len(str)//2+1]

print(get_middle_char("ssafy"))
print(get_middle_char("coding"))
