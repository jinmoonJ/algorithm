# 소금물 농도

salt = 0
water = 0

count = 0
salt,water=[],[]  #소금의 양과 소금물의 양을 받기 위한 리스트
while count < 5:
    N = input("소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ")
    if N =='Done':
        break
    else:
        a,b = N[:N.find("%")],N[N.find("%")+1:N.find("g")]  #a=%앞의 숫자(소금의 농도), b=g앞의 숫자(소금물의 양)
        salt.append(float(a)/100*float(b))  #소금의 양(a/100에 b를 곱한 것)을 salt에 추가.
        water.append(float(b))
    count +=1
print(str(round(sum(salt)*100/sum(water),2))+"%",str(round(sum(water),2))+"g")