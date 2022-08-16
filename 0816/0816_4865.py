# SWEA 4865 글자수
T = int(input())

for tc in range(1, T + 1):
    str1 = set(input())  # 중복 제거하고 set에 넣기
    str2 = input()

    dict = {}

    for i in str1:  # 중복을 제거한 str1의 문자열에 맞게 0을 넣어서 dict 초기화
        dict[i] = 0

    for j in str2:  # str2를 돌면서
        if j in str1:  # str2의 j가 str1에 들어있다면
            dict[j] += 1  # j의 값에 1을 추가해준다

    answer = 0
    for b in dict.values():  # 위에서 생성한 dict의 값을 돌면서
        if b > answer:  # b값이 answer 보다 크다면
            answer = b  # answer는 b가 된다
    print(f"#{tc} {answer}")  # 가장 높은 값을 출력
