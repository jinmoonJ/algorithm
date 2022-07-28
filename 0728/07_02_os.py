from faker import Faker
import random

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




students = []

# 학생 리스트 만들기
fake = Faker("fr_FR")

for i in range(11):
    students.append(fake.name())

print(students)

pair1 = Pairprogramming(students)
print(pair1.students)

print(pair1.pick(6))