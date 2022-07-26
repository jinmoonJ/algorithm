fruits = "apple, rottenBanana, apple, RoTTenorange,Orange"

# 문자열을 split() 함수를 통해 쪼개서 리스트로 만들어 준다.

fruit_list = fruits.split(",") # , 기준으로 자른다

# 신선한 과일만 담을 주머니(리스트) 생성

fresh_list = []

# 반복문을 사용해서 리스트 안의 썩은 과일을 새걸로 만든다음 신선한 과일 주머니로 옮긴다.
# 썩은 과일이 아닐 경우 신선한 과일 주머니로 그대로 옮겨도 된다.

string1 = "RoTTenorange"

string2 = "rottenorange" # 문자열을 모두 소문자로 바꿔주는 함수

for fruit in fruit_list:
    if "rotten" in fruit.lower(): # fruit : 과일 주머니에 들어있는 과일, 소문자로 모두바꿔준 결과 : fruit.lower()
        # 썩은 과일이다. --> 신선한 과일로 바꿔서 새 주머니로 옮긴다
        fresh_list.append(fruit.lower().replace("rotten",""))
        # replace("바꿀 문자열", "변경후 문자열")
    else:
        # 썩은 과일이 아니다 --> 그대로 새 주머니에 옮긴다
        fresh_list.append(fruit.lower())

print(fresh_list)