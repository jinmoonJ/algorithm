
def fn_d(n): # n은 입력으로 들어오는 숫자, 결과로 각 자릿수를 더하고, 자기 자신을 더해서 반환
    # 91 = 9 + 1 + 91 = 101
    # n 을 그대로 숫자로 쓰는 방법
    # n 을 10으로 나누고 몫을 가져와서 사용
    # 91을 10으로 나누면 몫이 9
    # 1은 10으로 나누면 나머지가 1


    # n 을 문자열로 바꿔서 쓰는 방법
    number = str(n) # 입력받은 숫자를 문자열로 바꿈 *************************
    # 문자열로 바꾸면 각 인덱스 위치에 있는 철자가 바로 자리수가 된다.
    # 앞에서 부터 하나씩 뗴와서 숫자로 다시 바꾼 다음 더해주면 된다.
    # number 91234
    # i -> "9", "1", "2", "3", "4" 
    for i in number: # i는 문자열에서 때어낸 철자 하나(숫자로 바꾸면 자릿수)
        n += int(i)
    return n

number_set = set(range(1,10001)) # 1부터 10000까지 함수를 이용해서 수를 만든다
gen_set = set() # 함수를 이용해서 만든 수를 저장할 세트
for i in range(1, 10001):
    gen_set.add(fn_d(i)) # 수를 만들어서 저장한다.

self_set = set() # 셀프 넘버를 저장할 세트

self_set = number_set - gen_set # 차집합을 이용해서 빼주면 만들수 없는 숫자들만 남게된다.

def is_selfnumber(n): # n 이라는 수가 selfnumber인가?
    return n in self_set
    

print(fn_d(n))

