# 1.숫자의 입력과 출력
a = int(input()) # input()함수는 입력한 값을 모두 문자열로 처리하기때문에 -> 숫자로 바꿔줘야함
b = int(input())

sum = (a + b)

print(sum)

# 2. Dictionary활용하여 평균 구하기
menu = {"김치찜": 7000, "돼지국밥": 6500, "피자": 12000}

avg = sum(menu.values()) / len(menu)
print(int(avg))

## 2. 교수님 풀이(반복문 x)
menu = {"김치찜": 7000, "돼지국밥": 6500, "피자": 12000}

avg_menu = (menu["김치찜"] + menu["돼지국밥"] + menu["피자"]) / 3

print(sum(menu.valuse()) / len(menu.keys()))