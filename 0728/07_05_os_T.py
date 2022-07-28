from faker import Faker
import random
import copy

class Pairprogramming:

    # 1. 인자로 학생들의 이름으로 이루어진 리스트를 받아서 인스턴스 변수에 할당한다.
    def __init__(self, students):
        self.students = students

    def pick(self, n):
        result = set() # 결과로 반환할 랜덤으로 뽑은 학생 세트(중복 불가)

        while len(result) < n: # result의 원소가 n보다 작을때 까지 반복한다 # 내가 뽑기 원하는 학생수가 될때까지 계속 세트에서 뽑아서 넣기
            result.add(random.choice(self.students))

        return list(result)  # return result ==> return list(result) --- result 를 list로 반환
        '''
        for i in range(n):
            result.append(random.choice(self.students))
        '''

    def match_pair(self):
        result = [] # 결과로 반환할 리스트
        # 학생 리스트를 복사해서 (깊은복사)
        # 뽑아서 짝을 지어준 학생은 리스트에서 제거
        # 그 다음에 다시 짝을 지어줄 학생을 뽑아서 페어링을 해주면 된다.
        # [1,2,3,4,5]
        # [1,2,3]
        # [4,5]

        if len(self.students) < 2:
            return None
        
        # 학생들의 수가 홀수인 경우 미리 3명을 뽑아서 조를 만들어 준다.
        if len(self.students) % 2 == 1:
            random_pick = self.pick(3)
            # 뽑은 세명은 짝짓기가 완료 되었으니까 리스트에서 제거 해준다(다음에 또 뽑지 않기 위해서)
            for student in random_pick:
                self.students.remove(student)
            # 결과로 반환할 리스트에 뽑아온 3명 리스트를 추가
            result.append(random_pick)

        # 나머지 인원에 대해서 페어링을 진행
        # 남은 사람이 없을떄까지 반복한다.
        while len(self.students) > 0:
            random_pick = self.pick(2) # 2명 뽑아온다
            for student in random_pick: # 뽑아온 두명은 다음에 다시 뽑지않ㄱ ㅣ위해 리스트에서 제거
                self.students.remove(student)
            result.append(random_pick) # 뽑아온 2명을 리스트에 추가

        # 반복문이 끝나면 남은 학생이 없다.
        return result
        

students = []

# 학생 리스트 만들기
fake = Faker("ko_KR")

for i in range(11):
    students.append(fake.name())

print(students)

pair1 = Pairprogramming(students)
print(pair1.students)

print(pair1.pick(6))

print(pair1.match_pair())