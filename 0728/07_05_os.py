from faker import Faker

class Pairprogramming:

    # 1. 인자로 학생들의 이름으로 이루어진 리스트를 받아서 인스턴스 변수에 할당한다.
    def __init__(self, students):
        self.students = students

students = []

# 학생 리스트 만들기
fake = Faker("ko_KR")

for i in range(11):
    students.append(fake.name())

print(students)

pair1 = Pairprogramming(students)
print(pair1.students)