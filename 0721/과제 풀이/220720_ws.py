# 1. 세로로 출력하기
a = int(input())

for i in range(1,a+1):
    print(i)

# 2. 가로로 출력하기
a = int(input())

for i in range(1,a+1):
    print(i, end='')

# 3. 거꾸로 세로로 출력하기
a = int(input())

for i in range(a, 0, -1):
    print(i)

# 4. 거꾸로 출력해 보아요(SWEA #1545)
a = int(input())

for i in range(a, 0, -1):
    print(i, end='')

# 5. N줄 덧셈(2025)
n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i

print(sum)

# 6. 삼각형 출력하기
n = int(input())
for i in range(1, n+1):
    print("*"*i)

# 7. 중간값 찾기
numbers = [
85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
n = numbers
n.sort()
middle = 0
mid = 0

if len(n) % 2 ==0:
    mid = len(n)//2
    middle=(n[mid-1]+n[mid]/2)
else:
    mid = len(n)//2
    middle = n[mid]

print(middle)

