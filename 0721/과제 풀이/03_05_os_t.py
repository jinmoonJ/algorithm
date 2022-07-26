# 소금물 농도

salt = 9 # 소금의 양
water = 0 # 소금물의 양

count = 0 # 현재 내가 입력한 소금물의 갯수
while count < 5:
    command = input("농도를 입력(Done 입력시 종료) : ")
    if command == "Done":
        break # 반복문을 즉시 종료

    # 여기는 Done 을 입력하지 않았따 --> command에 농도가 들어있다.
    density = int(command) # 농도
    brine = int(input("소금물 입력 : ")) # 소금물

    # 지금까지 입력받은 소금물의 소금양을 누적시킨다.
    salt += density * brine
    # 지금까지 입력받은 소금물의 총합
    water += brine

    # 입력을 하나 받았으니 count 증가
    count += 1

# 혼합물의 농도와 총량을 출력해달라
# :.2f --> 소수점 2번째 자리까지 출력
# f 스트링에서 소수점 정하는 방법은 ":.2"
salt /= 100
print(f"혼합물의 농도는 {salt/water:.2f}, 양은 {water} 입니다.")
density = salt/water
brine
print("혼합물의 농도는 {:.2f}, 양은{}".format(density, water))